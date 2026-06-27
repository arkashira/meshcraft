# Meshcraft Project
Meshcraft is a multi-cluster control plane that automatically propagates policies to all registered clusters.

## Features
* Create policies via API or UI
* Propagate policies to all registered clusters
* Retry policy application with exponential back-off
* Log propagation failures and display in dashboard

## Requirements
* Python 3.8+
* Poetry for dependency management

## Installation
1. Install Poetry: `pip install poetry`
2. Install dependencies: `poetry install`
3. Run tests: `poetry run pytest`
