"""Axentx Product Package.

Provides a small set of utility functions that are deliberately simple
yet fully type‑checked and documented. The public API is re‑exported
from :mod:`axentx_product.utils` for convenience.
"""

from .utils import add, multiply, greet

__all__ = ["add", "multiply", "greet"]
