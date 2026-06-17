# TECH_SPEC.md – MeshCraft

---

## 1. Overview

**MeshCraft** is a lightweight, cloud‑native service mesh management platform designed for modern micro‑service architectures. It provides:

- **Declarative configuration** via CRDs (Custom Resource Definitions) in Kubernetes.
- **Dynamic traffic routing** (split, mirroring, fault injection).
- **Observability** (metrics, logs, distributed tracing) integrated with Prometheus, Loki, and Jaeger.
- **Policy enforcement** (rate limiting, authentication, authorization) using Envoy filters.
- **Zero‑downtime upgrades** and **self‑healing** through automated health checks.

The platform is built on top of **Istio** and **Envoy**, but abstracts complexity through a unified API and a UI dashboard.

---

## 2. Architecture

```
+----------------------+          +---------------------+
|  Client (CLI/REST)  |<-------->|  MeshCraft API      |
|  Dashboard (React)  |          |  (Go, gRPC)         |
+----------------------+          +---------------------+
          |                                 |
          |                                 |
          v                                 v
+----------------------+          +---------------------+
|  MeshCraft Controller|<-------->|  Kubernetes API     |
|  (Operator, Go)      |          |  (CRDs)             |
+----------------------+          +---------------------+
          |                                 |
          |                                 |
          v                                 v
+----------------------+          +---------------------+
|  Envoy Sidecar       |<-------->|  Istio Pilot        |
|  (per pod)           |          |  (Service Discovery)|
+----------------------+          +---------------------+
          |                                 |
          |                                 |
          v                                 v
+----------------------+          +---------------------+
|  Service Mesh (Envoy)|<-------->|  Service Mesh Core  |
|  (Traffic Routing)   |          |  (Istio Envoy)      |
+----------------------+          +---------------------+
```

### 2.1 Core Components

| Component | Responsibility | Tech |
|-----------|----------------|------|
| **MeshCraft API** | REST/GRPC gateway for CRUD on mesh resources | Go, Gin, gRPC |
| **MeshCraft Operator** | Watches CRDs, reconciles Envoy configs | Go, controller-runtime |
| **Dashboard** | UI for visualizing topology, metrics, policies | React, TypeScript, D3 |
| **CRDs** | Declarative definitions: Mesh, Service, Route, Policy | Kubernetes |
| **Envoy Configurator** | Generates Envoy bootstrap and filter chains | Go, Envoy API |
| **Metrics Collector** | Exposes Prometheus metrics | Go, Prometheus client |
| **Tracing Agent** | Sends traces to Jaeger | Go, OpenTelemetry |

---

## 3. Data Model

### 3.1 CRDs

| CRD | Spec Fields | Status Fields |
|-----|-------------|---------------|
| `Mesh` | `name`, `namespace`, `config` (global Envoy settings) | `phase`, `conditions` |
| `Service` | `name`, `namespace`, `selector`, `port`, `protocol` | `phase`, `conditions` |
| `Route` | `name`, `namespace`, `match`, `route`, `retry`, `timeout` | `phase`, `conditions` |
| `Policy` | `name`, `namespace`, `type` (rate‑limit, auth), `spec` | `phase`, `conditions` |

### 3.2 Internal State

- **Cache**: In‑memory map of current Envoy configs per pod.
- **Event Bus**: Kafka topic `meshcraft.events` for cross‑component notifications.
- **Audit Log**: JSON entries stored in S3 for compliance.

---

## 4. Key APIs & Interfaces

### 4.1 REST Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET /meshes` | List all meshes |
| `POST /meshes` | Create a new mesh |
| `GET /meshes/{name}` | Retrieve mesh details |
| `PUT /meshes/{name}` | Update mesh |
| `DELETE /meshes/{name}` | Delete mesh |
| `GET /services` | List services in a mesh |
| `POST /services` | Add service |
| `GET /routes` | List routes |
| `POST /routes` | Create route |
| `GET /policies` | List policies |
| `POST /policies` | Create policy |

### 4.2 gRPC Service

```
service MeshCraft {
  rpc CreateMesh(CreateMeshRequest) returns (Mesh);
  rpc UpdateMesh(UpdateMeshRequest) returns (Mesh);
  rpc DeleteMesh(DeleteMeshRequest) returns (google.protobuf.Empty);
  rpc ListServices(ListServicesRequest) returns (ListServicesResponse);
  // ... other RPCs
}
```

### 4.3 Envoy Config API

- **Bootstrap**: `/config/bootstrap`
- **Route**: `/config/route`
- **Filter**: `/config/filter`

These are internal endpoints used by the Operator to push configs to Envoy sidecars via the Envoy Admin API.

---

## 5. Technology Stack

| Layer | Technology | Reason |
|-------|------------|--------|
| **API** | Go (Gin, gRPC) | High performance, static typing |
| **Operator** | Go (controller-runtime) | Native Kubernetes operator |
| **UI** | React, TypeScript, D3 | Interactive topology visualization |
| **Data Store** | PostgreSQL (for audit logs) | ACID compliance |
| **Messaging** | Kafka | Event‑driven architecture |
| **Observability** | Prometheus, Loki, Jaeger | Standard OpenTelemetry stack |
| **CI/CD** | GitHub Actions, Helm | Automated releases |
| **Container Runtime** | Docker, containerd | OCI compliance |
| **Deployment** | Helm charts, Kustomize | Reproducible installs |

---

## 6. Dependencies

| Dependency | Version | Notes |
|------------|---------|-------|
| Kubernetes API | v1.30 | Operator uses controller-runtime v0.15 |
| Istio | v1.18 | MeshCraft relies on Pilot for service discovery |
| Envoy | v1.27 | Sidecar injection via Istio |
| Prometheus | v2.52 | Metrics scraping |
| Loki | v3.1 | Log aggregation |
| Jaeger | v1.48 | Distributed tracing |
| Go | 1.22 | Language |
| Helm | 3.15 | Packaging |
| Kafka | 3.6 | Event bus |
| PostgreSQL | 16 | Audit logs |

All dependencies are pinned in `go.mod` and Helm `requirements.yaml`.

---

## 7. Deployment

### 7.1 Prerequisites

- Kubernetes cluster v1.24+ with RBAC enabled.
- Istio installed (control plane + sidecar injector).
- Prometheus, Loki, Jaeger deployed.
- Kafka cluster accessible from the cluster.
- PostgreSQL instance for audit logs.

### 7.2 Helm Chart

```bash
helm repo add meshcraft https://charts.meshcraft.io
helm install meshcraft meshcraft/meshcraft \
  --namespace meshcraft-system \
  --create-namespace \
  --set kafka.bootstrapServers=broker:9092 \
  --set postgres.host=postgres:5432 \
  --set postgres.user=meshcraft \
  --set postgres.password=secret
```

### 7.3 Operator Lifecycle

1. **CRD Installation** – `kubectl apply -f crds/`
2. **Operator Deployment** – Helm chart deploys a Deployment with `meshcraft-operator` container.
3. **Sidecar Injection** – Istio auto‑injects Envoy sidecar into all pods in namespaces labeled `meshcraft.io/managed=true`.
4. **Configuration Push** – Operator watches CRDs, generates Envoy configs, pushes via Envoy Admin API.
5. **Observability** – Metrics exposed on `/metrics`; logs forwarded to Loki; traces to Jaeger.

### 7.4 Scaling

- Operator runs as a single replica (high‑availability via leader election).
- API service can be scaled horizontally behind a LoadBalancer.
- Kafka and PostgreSQL are external services; scale per cluster capacity.

---

## 8. Security

- **RBAC**: API server enforces fine‑grained permissions via Kubernetes RBAC.
- **Transport**: All API traffic uses TLS; Envoy sidecars terminate TLS.
- **Secrets**: Stored in Kubernetes Secrets; accessed via Vault integration.
- **Audit**: Every CRUD operation logged to PostgreSQL and S3.

---

## 9. Testing & Validation

| Test | Tool | Frequency |
|------|------|-----------|
| Unit | Go test | CI |
| Integration | KinD + Helm | CI |
| E2E | Cypress (UI) | CI |
| Load | k6 | Monthly |
| Security | Trivy, kube-hunter | Quarterly |

All tests are run via GitHub Actions and results are stored in the `meshcraft-ci` bucket.

---

## 10. Roadmap Highlights

| Phase | Feature | Target |
|-------|---------|--------|
| 1 | **Zero‑downtime upgrades** for Envoy sidecars | Q3 2026 |
| 2 | **Service Mesh Federation** across clusters | Q1 2027 |
| 3 | **AI‑driven traffic routing** (predictive) | Q4 2027 |
| 4 | **Marketplace for reusable policies** | Q2 2028 |

---

## 11. Contact & Governance

- **Lead Engineer**: Jane Doe (jane@axentx.com)
- **Repository**: `arkashira/meshcraft`
- **Issue Tracker**: GitHub Issues
- **Slack Channel**: `#meshcraft-dev`

---
