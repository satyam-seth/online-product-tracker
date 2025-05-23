import argparse
import asyncio
from tracker.fetcher import fetch_product_details
from tracker.db import init_db, save_product_data, get_product_history
from tracker.storage.sources.cli import add_sources_subparsers, handle_sources_commands


async def track(url):
    try:
        product = await fetch_product_details(url)
        save_product_data(product)
        print("\nProduct data saved successfully.\n", product)
    except ValueError as e:
        print("Failed to fetch product details:", e)


def history(url):
    data = get_product_history(url)
    if not data:
        print("No history found for this URL.")
        return
    print("\nPrice History:\n", data)


async def show(url):
    try:
        product = await fetch_product_details(url)
        print("\nProduct Info:")
        for key, value in product.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print("Failed to fetch product details:", e)


async def async_main():
    parser = argparse.ArgumentParser(description="Online Product Tracker CLI")
    subparsers = parser.add_subparsers(dest="command_group", required=True)

    # Group for monitor commands "track", "history", "show"
    sync_parser = subparsers.add_parser("monitor", help="Product Monitor Commands")
    sync_subparsers = sync_parser.add_subparsers(dest="command", required=True)

    for cmd in ["track", "history", "show"]:
        sp = sync_subparsers.add_parser(cmd)
        sp.add_argument("--url", required=True, help="Product URL")

    # Group for sources CRUD commands
    sources_parser = subparsers.add_parser(
        "sources",
        help="Product Sources Services Commands",
    )
    sources_subparsers = sources_parser.add_subparsers(dest="command", required=True)
    add_sources_subparsers(sources_subparsers)

    args = parser.parse_args()

    # Handle monitor commands
    if args.command_group == "monitor":
        if args.command == "track":
            await track(args.url)
            return
        if args.command == "history":
            history(args.url)
            return
        if args.command == "show":
            await show(args.url)
            return

    # Handle sources commands
    if args.command_group == "sources":
        await handle_sources_commands(args)


if __name__ == "__main__":
    # TODO: remove it
    init_db()
    asyncio.run(async_main())
