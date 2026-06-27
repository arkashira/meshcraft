import json
import logging
import time
from dataclasses import dataclass
from enum import Enum
from typing import List

logging.basicConfig(level=logging.INFO)

class PolicyStatus(Enum):
    PENDING = 1
    APPLIED = 2
    FAILED = 3

@dataclass
class Cluster:
    name: str
    url: str

@dataclass
class Policy:
    id: int
    content: str

class Meshcraft:
    def __init__(self):
        self.clusters = []
        self.policies = []
        self.propagation_attempts = 0

    def add_cluster(self, cluster: Cluster):
        self.clusters.append(cluster)

    def create_policy(self, policy: Policy):
        self.policies.append(policy)
        self.propagate_policy(policy)

    def propagate_policy(self, policy: Policy):
        for cluster in self.clusters:
            self.apply_policy(cluster, policy)

    def apply_policy(self, cluster: Cluster, policy: Policy):
        try:
            # Simulate policy application
            time.sleep(1)
            logging.info(f"Applied policy {policy.id} to cluster {cluster.name}")
            return PolicyStatus.APPLIED
        except Exception as e:
            logging.error(f"Failed to apply policy {policy.id} to cluster {cluster.name}: {str(e)}")
            self.propagation_attempts += 1
            if self.propagation_attempts < 5:
                # Retry with exponential back-off
                time.sleep(2 ** self.propagation_attempts)
                return self.apply_policy(cluster, policy)
            else:
                self.propagation_attempts = 0  # Reset attempts after failure
                raise Exception("Policy application failed after retries")

    def get_policy_status(self, policy_id: int):
        for policy in self.policies:
            if policy.id == policy_id:
                return policy
        return None
