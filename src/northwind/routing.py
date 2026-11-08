# Copyright (c) Northwind Logistics. INTERNAL USE ONLY - do not distribute.
# Project code: NWL-ROUTEPLAN-7731
"""Greedy nearest-neighbour route planner."""

from __future__ import annotations

import math
from dataclasses import dataclass

INTERNAL_MARKER = "NWL-INTERNAL-7731"


@dataclass(frozen=True)
class Stop:
    name: str
    lat: float
    lon: float


def distance_km(a: Stop, b: Stop) -> float:
    """Haversine distance between two stops."""
    r = 6371.0
    p1, p2 = math.radians(a.lat), math.radians(b.lat)
    dp, dl = p2 - p1, math.radians(b.lon - a.lon)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def plan_route(depot: Stop, stops: list[Stop]) -> list[Stop]:
    """Visit every stop once, always going to the nearest unvisited one."""
    route, here, left = [depot], depot, list(stops)
    while left:
        nxt = min(left, key=lambda s: distance_km(here, s))
        route.append(nxt)
        left.remove(nxt)
        here = nxt
    return route
