import argparse

from .services import (
    create_snapshot,
    get_snapshot_by_id,
    list_snapshots,
    list_snapshots_for_product,
    update_snapshot,
    delete_snapshot,
)


def add_snapshots_subparsers(subparsers: argparse._SubParsersAction):
    # Create
    create = subparsers.add_parser("create", help="Create a snapshot for a product")
    create.add_argument("--product_id", type=int, required=True)
    create.add_argument("--title", type=str)
    create.add_argument("--rating", type=float)
    create.add_argument("--amount", type=float)
    create.add_argument("--currency", type=str)

    # Get
    get = subparsers.add_parser("get", help="Get a snapshot by ID")
    get.add_argument("--id", type=int, required=True)

    # List
    list_cmd = subparsers.add_parser("list", help="List all snapshots")

    # List by Product ID
    list_cmd = subparsers.add_parser(
        "list-by-product", help="List all snapshots for a product"
    )
    list_cmd.add_argument("--product_id", type=int, required=True)

    # Update
    update = subparsers.add_parser("update", help="Update a snapshot")
    update.add_argument("--id", type=int, required=True)
    update.add_argument("--title", type=str)
    update.add_argument("--rating", type=float)
    update.add_argument("--amount", type=float)
    update.add_argument("--currency", type=str)

    # Delete
    delete = subparsers.add_parser("delete", help="Delete a snapshot")
    delete.add_argument("--id", type=int, required=True)


async def handle_snapshots_commands(args):
    if args.command == "create":
        snapshot = await create_snapshot(
            product_id=args.product_id,
            title=args.title,
            rating=args.rating,
            amount=args.amount,
            currency=args.currency,
        )
        print("Created:", snapshot)

    elif args.command == "get":
        snapshot = await get_snapshot_by_id(args.id)
        print("Retrieved:", snapshot)

    elif args.command == "list":
        snapshots = await list_snapshots()
        for snapshot in snapshots:
            print(snapshot)

    elif args.command == "list-by-product":
        snapshots = await list_snapshots_for_product(args.product_id)
        for snapshot in snapshots:
            print(snapshot)

    elif args.command == "update":
        snapshot = await update_snapshot(
            snapshot_id=args.id,
            title=args.title,
            rating=args.rating,
            amount=args.amount,
            currency=args.currency,
        )
        print("Updated:", snapshot)

    elif args.command == "delete":
        success = await delete_snapshot(args.id)
        print("Deleted:", success)
