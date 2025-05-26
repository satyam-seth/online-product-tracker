import argparse

from .services import (
    create_product,
    get_product_by_id,
    get_product_by_url,
    list_products,
    update_product,
    delete_product,
)


def add_products_subparsers(subparsers: argparse._SubParsersAction):
    # Create
    create = subparsers.add_parser("create", help="Create a new product")
    create.add_argument("--url", required=True)
    create.add_argument("--source_id", required=True, type=int)

    # Get by ID
    get = subparsers.add_parser("get", help="Get product by ID")
    get.add_argument("--id", required=True, type=int)

    # Get by URL
    get_url = subparsers.add_parser("get-by-url", help="Get product by URL")
    get_url.add_argument("--url", required=True)

    # List
    subparsers.add_parser("list", help="List all products")

    # Update
    update = subparsers.add_parser("update", help="Update a product")
    update.add_argument("--id", required=True, type=int)
    update.add_argument("--url")
    update.add_argument("--source_id", type=int)

    # Delete
    delete = subparsers.add_parser("delete", help="Delete a product")
    delete.add_argument("--id", required=True, type=int)


async def handle_products_commands(args):
    if args.command == "create":
        product = await create_product(args.url, args.source_id)
        print("Created:", product)

    elif args.command == "get":
        product = await get_product_by_id(args.id)
        print("Retrieved:", product)

    elif args.command == "get-by-url":
        product = await get_product_by_url(args.url)
        print("Retrieved:", product)

    elif args.command == "list":
        products = await list_products()
        for product in products:
            print(product)

    elif args.command == "update":
        updated = await update_product(args.id, args.url, args.source_id)
        print("Updated:" if updated else "Not found", updated)

    elif args.command == "delete":
        success = await delete_product(args.id)
        print("Deleted:", success)
