# Security Policy Enforcer

A Python project that enforces predefined security policies and generates compliance reports.

## Usage

1. Create a `SecurityPolicy` object with a name and a list of rules.
2. Create a `SecurityPolicyEnforcer` object with a list of `SecurityPolicy` objects.
3. Call the `enforce_policies` method with identity provider data to generate compliance reports.
4. Call the `generate_compliance_report` method to generate a JSON report.

## Testing

Run `pytest` to execute the tests.
