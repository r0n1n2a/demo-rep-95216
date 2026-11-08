from northwind.routing import Stop, plan_route


def test_plan_visits_every_stop_once() -> None:
    depot = Stop("depot", 51.5, -0.1)
    stops = [Stop("a", 51.6, -0.1), Stop("b", 51.4, -0.2), Stop("c", 51.55, -0.05)]
    route = plan_route(depot, stops)
    assert route[0] == depot
    assert sorted(s.name for s in route[1:]) == ["a", "b", "c"]
