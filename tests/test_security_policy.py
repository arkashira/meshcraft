from security_policy import SecurityPolicy, SecurityPolicyEnforcer, ComplianceReport, PolicyStatus

def test_enforce_policies_compliant():
    policy = SecurityPolicy("test_policy", ["rule1", "rule2"])
    enforcer = SecurityPolicyEnforcer([policy])
    identity_provider_data = {"rule1": True, "rule2": True}
    reports = enforcer.enforce_policies(identity_provider_data)
    assert len(reports) == 1
    assert reports[0].status == PolicyStatus.COMPLIANT

def test_enforce_policies_non_compliant():
    policy = SecurityPolicy("test_policy", ["rule1", "rule2"])
    enforcer = SecurityPolicyEnforcer([policy])
    identity_provider_data = {"rule1": True}
    reports = enforcer.enforce_policies(identity_provider_data)
    assert len(reports) == 1
    assert reports[0].status == PolicyStatus.NON_COMPLIANT

def test_generate_compliance_report():
    policy = SecurityPolicy("test_policy", ["rule1", "rule2"])
    enforcer = SecurityPolicyEnforcer([policy])
    identity_provider_data = {"rule1": True, "rule2": True}
    reports = enforcer.enforce_policies(identity_provider_data)
    report = enforcer.generate_compliance_report(reports)
    assert "COMPLIANT" in report

def test_check_compliance():
    policy = SecurityPolicy("test_policy", ["rule1", "rule2"])
    enforcer = SecurityPolicyEnforcer([policy])
    identity_provider_data = {"rule1": True, "rule2": True}
    compliant = enforcer.check_compliance(policy, identity_provider_data)
    assert compliant

def test_check_compliance_non_compliant():
    policy = SecurityPolicy("test_policy", ["rule1", "rule2"])
    enforcer = SecurityPolicyEnforcer([policy])
    identity_provider_data = {"rule1": True}
    compliant = enforcer.check_compliance(policy, identity_provider_data)
    assert not compliant
