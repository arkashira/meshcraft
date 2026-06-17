# REQUIREMENTS.md

## Project Overview
**Project Name:** *meshcraft*  
**Repository:** `arkashira/meshcraft`  
**Purpose:** Provide a scalable, efficient, and developer‑friendly service‑mesh management platform that simplifies deployment, observability, and policy enforcement across Kubernetes clusters.

---

## 1. Functional Requirements

| ID | Description | Acceptance Criteria |
|----|-------------|---------------------|
| **FR‑1** | **Cluster Discovery** | Meshcraft must automatically discover all Kubernetes clusters registered in the organization’s registry (via kubeconfig or cloud‑provider APIs). |
| **FR‑2** | **Service Registration** | Meshcraft must expose an API to register services, including metadata (name, namespace, labels, annotations). |
| **FR‑3** | **Traffic Routing** | Meshcraft must allow users to define routing rules (e.g., canary, blue/green) via a declarative YAML/JSON API. |
| **FR‑4** | **Policy Enforcement** | Meshcraft must support RBAC and network policies, enforce them at runtime, and provide audit logs. |
| **FR‑5** | **Observability Dashboard** | Meshcraft must provide a web UI that visualizes traffic metrics, latency, error rates, and policy violations. |
| **FR‑6** | **Auto‑Scaling** | Meshcraft must automatically scale sidecar proxies based on CPU/memory thresholds and traffic patterns. |
| **FR‑7** | **Multi‑Cluster Federation** | Meshcraft must enable traffic routing across clusters with minimal latency and consistent policy enforcement. |
| **FR‑8** | **API Gateway Integration** | Meshcraft must expose an API gateway endpoint that can be used by external services to route traffic into the mesh. |
| **FR‑9** | **Configuration Versioning** | Meshcraft must maintain a versioned history of all configuration changes and allow rollback. |
| **FR‑10** | **CLI Tool** | Provide a `meshcraft` CLI that supports CRUD operations for all resources and can be scripted. |
| **FR‑11** | **Health Checks** | Meshcraft must expose `/healthz` and `/readyz` endpoints for Kubernetes liveness and readiness probes. |
| **FR‑12** | **Self‑Healing** | Meshcraft must detect and recover from failed sidecar proxies or control‑plane pods automatically. |
| **FR‑13** | **Documentation** | All APIs and CLI commands must have auto‑generated, up‑to‑date docs (OpenAPI, Markdown). |
| **FR‑14** | **Extensibility** | Meshcraft must expose a plugin system for custom metrics, authentication, or routing logic. |

---

## 2. Non‑Functional Requirements

| ID | Category | Requirement | Acceptance Criteria |
|----|----------|-------------|---------------------|
| **NFR‑1** | **Performance** | Latency added by Meshcraft must be < 5 ms for 95 % of requests. | Benchmark with `wrk` against a 1 kB payload; 95 % percentile < 5 ms. |
| **NFR‑2** | **Throughput** | Meshcraft must handle ≥ 10 k req/s per cluster without degradation. | Load test with `k6`; sustained throughput ≥ 10 k req/s. |
| **NFR‑3** | **Scalability** | Meshcraft control plane must horizontally scale to support 10,000 services across 100 clusters. | Stress test with simulated 10k services; no memory or CPU > 80 %. |
| **NFR‑4** | **Reliability** | 99.9 % uptime for control plane; 99.5 % for data plane. | Simulate 30 min outage; recovery time < 30 s. |
| **NFR‑5** | **Security** | All APIs must use TLS 1.2+; secrets stored encrypted at rest. | Pen‑test; verify no plaintext secrets in etcd. |
| **NFR‑6** | **Compliance** | Meshcraft must support GDPR data‑subject request handling (data erasure). | Provide API to delete service data; audit log shows deletion. |
| **NFR‑7** | **Observability** | Logs must be structured JSON, include trace IDs, and be exportable to Loki/Prometheus. | Verify log format via `jq`; export to Loki works. |
| **NFR‑8** | **Maintainability** | Codebase must have > 80 % unit test coverage and CI pipeline that runs tests on every PR. | Coverage report > 80 %; CI passes. |
| **NFR‑9** | **Usability** | CLI must provide `--help` and auto‑completion for Bash/Zsh. | `meshcraft --help` shows all commands; completion scripts work. |
| **NFR‑10** | **Documentation** | All public APIs documented in OpenAPI 3.0 and auto‑generated docs. | Swagger UI renders correctly; docs match code. |

---

## 3. Constraints

| ID | Constraint | Rationale |
|----|------------|-----------|
| **C‑1** | Must run on Kubernetes 1.28+ | Future‑proofing and compatibility. |
| **C‑2** | Must use Go 1.22+ for control plane | Aligns with existing Axentx stack. |
| **C‑3** | Must integrate with existing Axentx BRAIN (pgvector) for policy lookup | Reuse shared knowledge base. |
| **C‑4** | Must not duplicate existing product “iceoryx2” | Avoid portfolio overlap. |
| **C‑5** | Must be open‑source under Apache‑2.0 | Aligns with repository license. |
| **C‑6** | Must support multi‑cloud (AWS, GCP, Azure) out of the box | Target market. |

---

## 4. Assumptions

| ID | Assumption | Impact |
|----|------------|--------|
| **A‑1** | Users have access to a Kubernetes cluster with sufficient RBAC permissions. | Control plane can install sidecars. |
| **A‑2** | Network connectivity between clusters is available via VPN or inter‑connect. | Multi‑cluster federation works. |
| **A‑3** | Metrics and logs can be collected via Prometheus and Loki. | Observability stack integration. |
| **A‑4** | Users will provide TLS certificates or use cert‑manager. | Security compliance. |
| **A‑5** | Axentx’s BRAIN will expose a gRPC service for policy queries. | Policy enforcement integration. |

---

## 5. Deliverables

1. **Control Plane** – Go microservice with REST/GRPC APIs.  
2. **Sidecar Proxy** – Envoy‑based proxy with custom filters.  
3. **CLI** – `meshcraft` command line tool.  
4. **Web UI** – React/Vue dashboard for observability.  
5. **Documentation** – OpenAPI spec, Markdown docs, auto‑generated CLI help.  
6. **CI/CD Pipeline** – GitHub Actions with lint, test, build, and container push.  
7. **Test Suite** – Unit, integration, and performance tests.  

---

## 6. Acceptance Checklist

- [ ] All functional requirements implemented and unit‑tested.  
- [ ] Performance benchmarks meet NFR‑1 & NFR‑2.  
- [ ] Security audit passes (TLS, secrets, RBAC).  
- [ ] Documentation fully auto‑generated and published.  
- [ ] CI pipeline passes on every PR.  
- [ ] No overlapping features with existing “iceoryx2” product.  

---
