import pytest

from shop import api, service


def test_total_sums_price_times_quantity():
    assert service.order_total({"tshirt": 2, "mug": 1}) == 5248


@pytest.mark.parametrize(
    "items, error",
    [({}, "order is empty"), ({"mug": 0}, "quantity"), ({"hat": 1}, "unknown product")],
)
def test_total_rejects_bad_orders(items, error):
    with pytest.raises(ValueError, match=error):
        service.order_total(items)


def test_checkout_ok():
    assert api.checkout({"items": {"poster": 3}}) == {"status": 200, "total_cents": 2397}


def test_checkout_bad_request():
    assert api.checkout({})["status"] == 400
    assert api.checkout({"items": {"hat": 1}})["error"] == "unknown product: hat"
