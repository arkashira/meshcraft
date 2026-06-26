import json
from dataclasses import dataclass
from typing import List

@dataclass
class Policy:
    name: str
    rules: List[str]

class ControlPlane:
    def __init__(self):
        self.policies = []
        self.clusters = []

    def define_policy(self, policy: Policy):
        self.policies.append(policy)

    def add_cluster(self, cluster_name: str):
        self.clusters.append(cluster_name)

    def propagate_policies(self):
        for cluster in self.clusters:
            print(f"Propagating policies to cluster {cluster}")
            for policy in self.policies:
                print(f"Applying policy {policy.name} to cluster {cluster}")

    def validate_policy(self, policy: Policy):
        if not policy.name or not policy.rules:
            raise ValueError("Policy must have a name and rules")
        return True

    def enforce_policy(self, policy: Policy, cluster_name: str):
        if cluster_name not in self.clusters:
            raise ValueError("Cluster not found")
        print(f"Enforcing policy {policy.name} on cluster {cluster_name}")

    def report_errors(self):
        print("No errors reported")

def main():
    control_plane = ControlPlane()
    policy = Policy("test_policy", ["rule1", "rule2"])
    control_plane.define_policy(policy)
    control_plane.add_cluster("test_cluster")
    control_plane.propagate_policies()
    control_plane.validate_policy(policy)
    control_plane.enforce_policy(policy, "test_cluster")
    control_plane.report_errors()

if __name__ == "__main__":
    main()
