```markdown
# tech-spec.md – MeshCraft v1

## 1. Stack
| Layer | Technology | Version | Rationale |
|-------|------------|---------|-----------|
| **Runtime** | Go (Golang) | 1.22 | High concurrency, static binaries, native support for gRPC & HTTP/2. |
| **Web Framework** | Gin | 1.9 | Minimal overhead, built‑in middleware for logging, recovery, CORS. |
| **Service Mesh SDK** | Linkerd 2.x | 2.13 | Mature, open‑source, Kubernetes‑native, provides `linkerd` CLI and `linkerd` API. |
| **Configuration Store** | etcd | 3.5 | Consistent key‑value store for mesh configs, high availability. |
| **Database** | PostgreSQL | 15 | Relational store for user/organization metadata, audit logs. |
| **Message Bus** | NATS | 2.10 | Lightweight pub/sub for inter‑service communication. |
| **Container Runtime** | Docker | 24 | Standard containerization for CI/CD. |
| **Orchestration** | Kubernetes (EKS / GKE / AKS) | 1.30 | Native deployment, autoscaling, secrets management. |
| **Observability** | OpenTelemetry | 1.28 | Unified tracing, metrics, and logs. |
| **CI/CD** | GitHub Actions | – | Native to repo, free tier for public repos. |
| **Package Manager** | Go Modules | – | Dependency management. |

## 2. Hosting
| Platform | Free‑Tier Availability | Notes |
|----------|------------------------|-------|
| **GitHub Actions** | Yes | For CI/CD pipelines, test, build, and publish Docker images. |
| **Amazon EKS (Fargate)** | $0.10/hr per pod (free tier: 750 hrs/month) | Serverless Kubernetes, no EC2 management. |
| **Google GKE (Autopilot)** | $0.10/hr per pod (free tier: 750 hrs/month) | Serverless, auto‑scaling. |
| **Azure AKS (AKS‑F)** | $0.10/hr per pod (free tier: 750 hrs/month) | Serverless, integrated with Azure AD. |

**Deployment Flow**  
1. Build Docker image in GitHub Actions.  
2. Push to GitHub Container Registry (GHCR).  
3. Deploy to chosen Kubernetes cluster via Helm chart.  
4. Use `linkerd` CLI to inject sidecars automatically.

## 3. Data Model

### 3.1 Tables (PostgreSQL)

| Table | Key Fields | Description |
|-------|------------|-------------|
| `organizations` | `org_id (PK)`, `name`, `created_at`, `updated_at` | Top‑level tenant. |
| `users` | `user_id (PK)`, `org_id (FK)`, `email`, `role`, `created_at` | Authenticated users. |
| `mesh_configs` | `config_id (PK)`, `org_id (FK)`, `name`, `spec (JSONB)`, `created_at`, `updated_at` | Serialized Linkerd config. |
| `audit_logs` | `log_id (PK)`, `user_id (FK)`, `action`, `target`, `timestamp`, `details (JSONB)` | Immutable audit trail. |
| `metrics` | `metric_id (PK)`, `config_id (FK)`, `name`, `value`, `timestamp` | Optional local metrics store (fallback). |

### 3.2 Collections (etcd)

| Key | Value | Purpose |
|-----|-------|---------|
| `/meshcraft/links/{org_id}/{config_id}` | YAML/JSON | Runtime config for Linkerd. |
| `/meshcraft/health/{org_id}` | JSON | Liveness & readiness status. |

## 4. API Surface
| Method | Path | Purpose |
|--------|------|---------|
| `POST /api/v1/organizations` | Create organization |
| `GET /api/v1/organizations/{org_id}` | Retrieve org details |
| `POST /api/v1/users` | Add user to org |
| `GET /api/v1/users/{user_id}` | Get user profile |
| `POST /api/v1/meshes` | Create new mesh config |
| `GET /api/v1/meshes/{config_id}` | Retrieve mesh spec |
| `PUT /api/v1/meshes/{config_id}` | Update mesh spec |
| `DELETE /api/v1/meshes/{config_id}` | Delete mesh |
| `GET /api/v1/meshes/{config_id}/status` | Get runtime status (linkerd health) |
| `POST /api/v1/meshes/{config_id}/deploy` | Trigger sidecar injection & rollout |

All endpoints are RESTful, JSON‑based, and versioned (`/api/v1/`). Pagination is applied to list endpoints (`?page=1&size=50`).

## 5. Security Model
| Layer | Mechanism | Details |
|-------|-----------|---------|
| **Auth** | OAuth2 + OpenID Connect (OIDC) | Integration with Keycloak or Auth0; JWT bearer tokens. |
| **Secrets** | Kubernetes Secrets + Vault | Store API keys, etcd credentials, Linkerd certs. |
| **IAM** | Role‑Based Access Control (RBAC) | `admin`, `operator`, `viewer` roles per org. |
| **Transport** | TLS 1.3 | Mutual TLS for API server and etcd. |
| **Network** | Kubernetes Network Policies | Restrict pod communication to required ports. |
| **Audit** | Immutable audit logs in PostgreSQL | Signed logs, write‑once storage. |

## 6. Observability
| Component | Tool | Exporter | Notes |
|-----------|------|----------|-------|
| **Logs** | Fluent Bit → Loki | Sidecar logs forwarded to Loki. |
| **Metrics** | Prometheus | Exporter on `/metrics` endpoint. |
| **Traces** | OpenTelemetry Collector → Jaeger | Distributed tracing of API calls and sidecar interactions. |
| **Dashboards** | Grafana | Pre‑built dashboards for Linkerd health, MeshCraft usage, and system metrics. |

## 7. Build / CI
| Step | Tool | Description |
|------|------|-------------|
| **Lint** | `golangci-lint` | Static analysis for Go code. |
| **Test** | `go test -cover` | Unit & integration tests. |
| **Build** | `docker buildx` | Multi‑arch Docker image (amd64, arm64). |
| **Publish** | `docker push ghcr.io/arkashira/meshcraft:{{tag}}` | Tagging with semantic version. |
| **Helm Chart** | `helm lint` | Validate Helm chart. |
| **Deploy** | `kubectl apply -f k8s/` | Deploy to test cluster. |
| **Security Scan** | `Trivy` | Container vulnerability scanning. |
| **Release** | GitHub Release | Automated via `semantic-release`. |

All CI steps are defined in `.github/workflows/ci.yml`. The pipeline runs on every push to `main` and on pull requests. The free tier of GitHub Actions provides 2,000 minutes/month for public repos; additional minutes can be requested via a paid plan.

---

**End of tech-spec.md**