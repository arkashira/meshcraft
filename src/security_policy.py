import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class PolicyStatus(Enum):
    COMPLIANT = 1
    NON_COMPLIANT = 2

@dataclass
class SecurityPolicy:
    name: str
    rules: List[str]

@dataclass
class ComplianceReport:
    policy_name: str
    status: PolicyStatus
    details: str

class SecurityPolicyEnforcer:
    def __init__(self, policies: List[SecurityPolicy]):
        self.policies = policies

    def enforce_policies(self, identity_provider_data: dict) -> List[ComplianceReport]:
        reports = []
        for policy in self.policies:
            compliant = self.check_compliance(policy, identity_provider_data)
            status = PolicyStatus.COMPLIANT if compliant else PolicyStatus.NON_COMPLIANT
            details = f"Policy {policy.name} is {'compliant' if compliant else 'non-compliant'}"
            reports.append(ComplianceReport(policy.name, status, details))
        return reports

    def check_compliance(self, policy: SecurityPolicy, identity_provider_data: dict) -> bool:
        # Simplified example: check if all rules are present in the identity provider data
        return all(rule in identity_provider_data for rule in policy.rules)

    def generate_compliance_report(self, reports: List[ComplianceReport]) -> str:
        report_data = {"reports": [{"policy_name": report.policy_name, "status": report.status.name, "details": report.details} for report in reports]}
        return json.dumps(report_data, indent=4)
