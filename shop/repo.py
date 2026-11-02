"""Storage layer. The only module that knows how data is kept."""

PRODUCTS = {"tshirt": 1999, "mug": 1250, "poster": 799}  # price in cents


def get_price(sku: str) -> int:
    if sku not in PRODUCTS:
        raise ValueError(f"unknown product: {sku}")
    return PRODUCTS[sku]
