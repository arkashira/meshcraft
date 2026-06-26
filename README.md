# Meshcraft

A unified control plane for defining and enforcing policies across multiple clusters.

## Usage

1. Create a `ControlPlane` instance.
2. Define a policy using the `Policy` dataclass.
3. Add a cluster to the control plane.
4. Propagate policies to all clusters.
5. Validate and enforce policies on each cluster.

## Testing

Run `pytest` to execute the tests.
