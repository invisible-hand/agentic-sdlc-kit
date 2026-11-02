"""Entry point. Translates a request into a service call. Never touches repo directly."""

from shop import service


def checkout(payload: dict) -> dict:
    try:
        return {"status": 200, "total_cents": service.order_total(payload["items"])}
    except KeyError:
        return {"status": 400, "error": "missing field: items"}
    except ValueError as e:
        return {"status": 400, "error": str(e)}
