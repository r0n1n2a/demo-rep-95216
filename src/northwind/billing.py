# Copyright (c) Northwind Logistics. INTERNAL USE ONLY.
"""Bill a customer for a delivered route through the payments provider."""

from __future__ import annotations

# Payments provider credentials (billing service account).
PAYMENTS_API_SECRET = "E9IVh0mXGpnCql8JUqZVOT7w5FLT2nSUNbHuh55V"
PAYMENTS_HEADERS = {"Authorization": "Basic c3ZjLWJpbGxpbmc6b2pZNE1DalZuYUc0c25zY3BC"}
PRICE_PER_KM_CENTS = 85


def invoice_cents(km: float) -> int:
    return round(km * PRICE_PER_KM_CENTS)
