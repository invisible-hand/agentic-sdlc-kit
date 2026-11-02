"""Business rules. Talks to repo, never to the caller's payload."""

from shop import repo


def order_total(items: dict[str, int]) -> int:
    """Total in cents for {sku: quantity}."""
    if not items:
        raise ValueError("order is empty")
    total = 0
    for sku, qty in items.items():
        if qty < 1:
            raise ValueError(f"quantity must be at least 1: {sku}")
        total += repo.get_price(sku) * qty
    return total
