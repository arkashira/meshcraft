import pytest
from meshcraft import ControlPlane, Policy

def test_define_policy():
    control_plane = ControlPlane()
    policy = Policy("test_policy", ["rule1", "rule2"])
    control_plane.define_policy(policy)
    assert len(control_plane.policies) == 1
    assert control_plane.policies[0].name == "test_policy"

def test_add_cluster():
    control_plane = ControlPlane()
    control_plane.add_cluster("test_cluster")
    assert len(control_plane.clusters) == 1
    assert control_plane.clusters[0] == "test_cluster"

def test_propagate_policies():
    control_plane = ControlPlane()
    policy = Policy("test_policy", ["rule1", "rule2"])
    control_plane.define_policy(policy)
    control_plane.add_cluster("test_cluster")
    control_plane.propagate_policies()
    # No assertions, just checking it runs without errors

def test_validate_policy():
    control_plane = ControlPlane()
    policy = Policy("test_policy", ["rule1", "rule2"])
    assert control_plane.validate_policy(policy) is True

def test_validate_policy_empty():
    control_plane = ControlPlane()
    policy = Policy("", [])
    with pytest.raises(ValueError):
        control_plane.validate_policy(policy)

def test_enforce_policy():
    control_plane = ControlPlane()
    policy = Policy("test_policy", ["rule1", "rule2"])
    control_plane.add_cluster("test_cluster")
    control_plane.enforce_policy(policy, "test_cluster")
    # No assertions, just checking it runs without errors

def test_enforce_policy_cluster_not_found():
    control_plane = ControlPlane()
    policy = Policy("test_policy", ["rule1", "rule2"])
    with pytest.raises(ValueError):
        control_plane.enforce_policy(policy, "non_existent_cluster")

def test_report_errors():
    control_plane = ControlPlane()
    control_plane.report_errors()
    # No assertions, just checking it runs without errors
