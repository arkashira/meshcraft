# STORIES.md

## Product: **meshcraft**  
*A scalable and efficient service mesh management solution for developers and organizations.*

---

## Epic 1 – Core Mesh Management

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 1 | **As a developer, I want to deploy a service mesh with a single CLI command, so that I can quickly bootstrap my micro‑service architecture.** | • `meshcraft init <cluster>` creates a default mesh config.<br>• CLI outputs a success message and a link to the dashboard.<br>• Deployment is idempotent – running again does not duplicate resources. |
| 2 | **As an ops engineer, I want to view the health of all mesh components in a single dashboard, so that I can detect failures early.** | • Dashboard lists all pods, sidecars, and control plane components.<br>• Each item shows status (Ready/NotReady) and latency metrics.<br>• Clicking an item opens detailed logs. |
| 3 | **As a security officer, I want to enforce mutual TLS across all services, so that data in transit is encrypted.** | • Mesh automatically generates and rotates certificates.<br>• All traffic between services is encrypted by default.<br>• A CLI flag `--mtls=false` disables it for legacy services. |
| 4 | **As a developer, I want to add a new service to the mesh with minimal configuration, so that I can focus on business logic.** | • `meshcraft add-service <name> --image <url>` creates a deployment, service, and sidecar injection.<br>• The new service is immediately reachable via the mesh’s internal DNS. |
| 5 | **As a system admin, I want to scale the mesh control plane automatically, so that it can handle traffic spikes.** | • Horizontal Pod Autoscaler (HPA) is applied to control plane pods.<br>• Scaling thresholds are configurable via `meshcraft set-hpa`. |

---

## Epic 2 – Traffic Management & Observability

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 6 | **As a developer, I want to route traffic to multiple versions of a service, so that I can perform canary releases.** | • `meshcraft route <svc> --version <v> --weight <pct>` updates Istio VirtualService.<br>• Traffic distribution matches the specified weights within ±1%. |
| 7 | **As a QA engineer, I want to inject faults into the mesh, so that I can test resilience.** | • `meshcraft fault <svc> --type <latency|abort> --value <ms|code>` applies a fault injection policy.<br>• Faults are visible in the dashboard and can be removed with `meshcraft remove-fault`. |
| 8 | **As a data scientist, I want to export request traces to an external analytics platform, so that I can perform deep performance analysis.** | • Traces are sent to a configurable collector (e.g., Jaeger, Zipkin).<br>• Export can be toggled with `meshcraft export-traces --enable`. |
| 9 | **As a developer, I want to set rate limits per service, so that I can protect downstream APIs.** | • `meshcraft ratelimit <svc> --requests <n> --per <s>` creates a DestinationRule.<br>• Exceeding the limit returns HTTP 429. |
| 10 | **As a DevOps engineer, I want to view real‑time latency histograms, so that I can spot performance regressions.** | • Dashboard shows latency percentiles (p50, p90, p99) per service.<br>• Data is refreshed every 5 seconds. |

---

## Epic 3 – Security & Compliance

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 11 | **As a compliance officer, I want to enforce IP whitelisting for inbound traffic, so that only approved networks can reach the mesh.** | • `meshcraft ip-whitelist <svc> --cidr <range>` creates a NetworkPolicy.<br>• Traffic from non‑whitelisted IPs is dropped. |
| 12 | **As a security analyst, I want to audit all configuration changes, so that I can maintain an audit trail.** | • Every CLI command logs to a central audit log.<br>• Logs include timestamp, user, command, and affected resources. |
| 13 | **As a developer, I want to enable automatic certificate renewal, so that I don’t have to manage TLS manually.** | • Certificates are renewed 30 days before expiry.<br>• Renewal is silent and does not disrupt traffic. |

---

## Epic 4 – Integration & Extensibility

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 14 | **As a platform engineer, I want to integrate meshcraft with existing CI/CD pipelines, so that mesh configuration is versioned.** | • `meshcraft export-config --format yaml` outputs a declarative config.<br>• Config can be committed to Git and applied with `meshcraft apply-config`. |
| 15 | **As a developer, I want to write custom plugins in Go, so that I can extend meshcraft’s functionality.** | • Plugin API is documented and available at `pkg/plugin`.<br>• Example plugin compiles and registers with the CLI. |

---

## MVP Release Order

1. **Core Mesh Management** – Deploy, health, TLS, add-service, autoscaling.  
2. **Traffic Management** – Routing, fault injection, tracing, rate limiting, latency dashboards.  
3. **Security & Compliance** – IP whitelisting, audit logs, auto‑renewal.  
4. **Integration & Extensibility** – CI/CD export, plugin framework.

---

### Notes for the Team

- All stories must pass the existing unit test suite and the integration tests against a local minikube cluster.  
- Documentation updates are required for each CLI command; see `docs/cli.md`.  
- The dashboard UI is built with React; story 2 requires a new component `MeshHealth`.  

---
