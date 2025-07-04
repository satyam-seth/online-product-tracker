from .products import create_product, get_product_by_url
from .snapshots import (
    create_snapshot,
    list_snapshots_for_product,
)
from .fetcher import fetch_product_details


async def track(url):
    try:
        product = await fetch_product_details(url)

        # fetch product data if found then do nothing else store product
        saved_product = await get_product_by_url(url)

        if saved_product is None:
            saved_product = await create_product(url, product.source)

        # save snapshot
        await create_snapshot(
            saved_product.id,
            product.title,
            product.rating,
            product.amount,
            product.currency,
        )

        # save_product_data(product)
        print("\nProduct data saved successfully.\n", product)
    except ValueError as e:
        print("Failed to fetch product details:", e)


async def history(url):
    product = await get_product_by_url(url)

    if not product:
        print("No history found for this URL.")
        return

    snapshots = await list_snapshots_for_product(product.id)
    print("\nPrice History:\n", snapshots)


async def show(url):
    try:
        product = await fetch_product_details(url)
        print("\nProduct Info:")
        for key, value in product.model_dump().items():
            print(f"{key}: {value}")
    except ValueError as e:
        print("Failed to fetch product details:", e)
