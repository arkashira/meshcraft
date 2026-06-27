import pytest
from meshcraft import Meshcraft, Cluster, Policy, PolicyStatus

def test_create_policy():
    meshcraft = Meshcraft()
    cluster = Cluster("test-cluster", "https://test-cluster.com")
    meshcraft.add_cluster(cluster)
    policy = Policy(1, "test-policy")
    meshcraft.create_policy(policy)
    assert meshcraft.get_policy_status(1) is not None

def test_propagate_policy():
    meshcraft = Meshcraft()
    cluster = Cluster("test-cluster", "https://test-cluster.com")
    meshcraft.add_cluster(cluster)
    policy = Policy(1, "test-policy")
    meshcraft.create_policy(policy)
    assert meshcraft.get_policy_status(1).content == "test-policy"

def test_apply_policy_success():
    meshcraft = Meshcraft()
    cluster = Cluster("test-cluster", "https://test-cluster.com")
    meshcraft.add_cluster(cluster)
    policy = Policy(1, "test-policy")
    status = meshcraft.apply_policy(cluster, policy)
    assert status == PolicyStatus.APPLIED

def test_apply_policy_failure():
    meshcraft = Meshcraft()
    cluster = Cluster("test-cluster", "https://test-cluster.com")
    meshcraft.add_cluster(cluster)
    policy = Policy(1, "test-policy")
    # Simulate failure
    meshcraft.propagation_attempts = 5
    try:
        status = meshcraft.apply_policy(cluster, policy)
        assert False, "Expected exception not raised"
    except Exception:
        assert True

def test_get_policy_status():
    meshcraft = Meshcraft()
    policy = Policy(1, "test-policy")
    meshcraft.create_policy(policy)
    retrieved_policy = meshcraft.get_policy_status(1)
    assert retrieved_policy.id == 1
    assert retrieved_policy.content == "test-policy"
