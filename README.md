# Northwind route planner

Route-planning service for Northwind Logistics dispatch. It plans delivery routes with a
nearest-neighbour heuristic and bills customers per delivered route through the payments
provider.

Tickets use the `NWL` prefix. Talk to the dispatch-platform team before changing billing.

Route plans are rebuilt nightly at 02:00 depot time; ask dispatch-platform before changing the schedule.
Depot IDs are four digits; the planner rejects anything else.
