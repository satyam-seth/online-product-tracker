import argparse
import asyncio
from tracker.actions import history, show, track
from tracker.storage.products.cli import (
    add_products_subparsers,
    handle_products_commands,
)
from tracker.storage.sources.cli import add_sources_subparsers, handle_sources_commands
from tracker.storage.snapshots.cli import (
    add_snapshots_subparsers,
    handle_snapshots_commands,
)


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

    # Group for products CRUD commands
    products_parser = subparsers.add_parser(
        "products",
        help="Product Services Commands",
    )
    products_subparsers = products_parser.add_subparsers(dest="command", required=True)
    add_products_subparsers(products_subparsers)

    # Group for snapshots CRUD commands
    snapshots_parser = subparsers.add_parser(
        "snapshots",
        help="Product Snapshot Services Commands",
    )
    snapshots_subparsers = snapshots_parser.add_subparsers(
        dest="command", required=True
    )
    add_snapshots_subparsers(snapshots_subparsers)

    args = parser.parse_args()

    # Handle monitor commands
    if args.command_group == "monitor":
        if args.command == "track":
            await track(args.url)
            return
        if args.command == "history":
            await history(args.url)
            return
        if args.command == "show":
            await show(args.url)
            return

    # Handle sources commands
    if args.command_group == "sources":
        await handle_sources_commands(args)

    # Handle products commands
    if args.command_group == "products":
        await handle_products_commands(args)

    # Handle snapshots commands
    if args.command_group == "snapshots":
        await handle_snapshots_commands(args)


if __name__ == "__main__":
    asyncio.run(async_main())
