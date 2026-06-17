# Roadmap – meshcraft

**Project**: meshcraft – a scalable and efficient service‑mesh management solution  
**Repository**: `arkashira/meshcraft`  
**Target Release**: Q4 2026 (MVP)  
**Audience**: Developers, DevOps teams, Platform Engineers

---

## 1. Vision & Success Criteria

| Metric | Target |
|--------|--------|
| **Adoption** | 100+ installations in production by end‑Q1 2027 |
| **Performance** | 99.9 % uptime, < 50 ms latency for mesh‑control API |
| **Security** | Zero critical CVEs in first 12 months |
| **Revenue** | $200k ARR from enterprise subscriptions |

---

## 2. MVP (Must‑Have for Launch) – Q4 2026

| Feature | Description | Owner | Status |
|---------|-------------|-------|--------|
| **Core Mesh Controller** | Deployable controller that manages Envoy sidecars, configures routing, retries, and observability. | Core Team | ✅ |
| **CLI & Web UI** | `meshcraft` CLI for bootstrap, status, and diagnostics; lightweight web UI for visual mesh health. | UI/UX | ✅ |
| **Self‑Healing & Auto‑Scaling** | Auto‑detect pod failures, restart sidecars, and scale Envoy replicas based on traffic. | Ops | ✅ |
| **Metrics & Tracing** | Export Prometheus metrics and OpenTelemetry traces to any backend. | Observability | ✅ |
| **Secure Mesh** | Mutual TLS, JWT auth, and role‑based access control for mesh resources. | Security | ✅ |
| **Documentation & Quickstart** | Full README, Helm chart, and example manifests. | Docs | ✅ |
| **CI/CD Pipeline** | GitHub Actions for linting, unit tests, integration tests, and image publishing. | DevOps | ✅ |
| **Compliance** | Open-source license (Apache‑2.0) and minimal data retention. | Legal | ✅ |

> **MVP‑Critical**: Core Mesh Controller, CLI/Web UI, Self‑Healing, Metrics, Secure Mesh, Documentation, CI/CD, Compliance.

---

## 3. Phase V1 – Q1 2027

| Theme | Deliverables | Owner |
|-------|--------------|-------|
| **Observability Deep‑Dive** | Advanced dashboards, anomaly detection, alerting via Prometheus Alertmanager. | Observability |
| **Policy Engine** | Fine‑grained traffic policies (rate‑limit, circuit‑breaker, canary). | Policy |
| **Multi‑Cluster Support** | Federation across up to 5 clusters, shared control plane. | Ops |
| **Marketplace Integration** | Publish meshcraft as a Helm chart and Operator on Artifact Hub. | Ops |
| **Developer Experience** | SDKs (Go, Python) for programmatic mesh manipulation. | SDK |
| **Performance Optimizations** | Reduce control‑plane CPU usage by 30 %. | Performance |

---

## 4. Phase V2 – Q3 2027

| Theme | Deliverables | Owner |
|-------|--------------|-------|
| **AI‑Driven Optimization** | Auto‑tune routing and resource allocation using ML models trained on internal telemetry. | AI/ML |
| **Zero‑Trust Enhancements** | Integrate with external IAM (OPA, Auth0) and provide policy-as-code. | Security |
| **Hybrid‑Cloud & Edge** | Support for on‑prem, public cloud, and edge nodes with minimal footprint. | Cloud |
| **Enterprise Features** | SSO, audit logs, role‑based access control, and subscription tiers. | Enterprise |
| **Marketplace Expansion** | Partnerships with major cloud providers for pre‑configured meshcraft bundles. | Partnerships |
| **Community & Ecosystem** | Open‑source plugins, community governance, and contribution guidelines. | Community |

---

## 5. Release Cadence

| Cycle | Duration | Focus |
|-------|----------|-------|
| **Sprint** | 2 weeks | Incremental feature development, bug fixes |
| **Release** | 6 weeks | Feature freeze, QA, documentation, and deployment |
| **Hotfix** | As needed | Critical security or stability issues |

---

## 6. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Complexity of multi‑cluster federation** | High | Start with single‑cluster MVP, incremental federation |
| **Security compliance** | High | Adopt OWASP Top 10, regular penetration tests |
| **ML model drift** | Medium | Continuous monitoring, retraining pipeline |
| **Community adoption** | Medium | Early evangelism, open‑source contributions |

---

## 7. Key Milestones

| Date | Milestone | Notes |
|------|-----------|-------|
| **2026‑10‑01** | MVP Alpha | Internal demo |
| **2026‑11‑15** | MVP Beta | External beta testing |
| **2026‑12‑31** | MVP Launch | Public release |
| **2027‑04‑30** | V1 Release | Multi‑cluster, policy engine |
| **2027‑10‑31** | V2 Release | AI‑driven optimization, enterprise tier |

---

## 8. Dependencies

- **Infrastructure**: Kubernetes 1.28+, Envoy 1.20+
- **Third‑Party**: Prometheus, Grafana, OpenTelemetry Collector
- **Internal**: Axentx shared BRAIN (pgvector) for telemetry data

---

## 9. Governance

- **Roadmap Review**: Quarterly with product, engineering, and sales
- **Feature Prioritization**: Based on validated customer pain points and revenue potential
- **Documentation**: Updated with every release; hosted on GitHub Pages

---

**Prepared by:**  
Senior Product & Engineering Lead – meshcraft  
`arkashira/meshcraft` | 2026‑06‑17
