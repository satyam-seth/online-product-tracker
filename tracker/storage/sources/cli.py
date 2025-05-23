# crud_cli.py
import argparse
from .services import (
    create_source,
    get_source_by_id,
    list_sources,
    update_source,
    delete_source,
)


def add_sources_subparsers(subparsers: argparse._SubParsersAction):
    create_parser = subparsers.add_parser("create", help="Create a new source")
    create_parser.add_argument("--name", required=True)
    create_parser.add_argument("--domain", required=True)
    create_parser.add_argument("--title_selector", required=True)
    create_parser.add_argument("--price_selector", required=True)
    create_parser.add_argument("--rating_selector", required=True)

    get_parser = subparsers.add_parser("get", help="Retrieve a source by ID")
    get_parser.add_argument("id", type=int)

    subparsers.add_parser("list", help="List all sources")

    update_parser = subparsers.add_parser("update", help="Update a source by ID")
    update_parser.add_argument("id", type=int)
    update_parser.add_argument("--name")
    update_parser.add_argument("--domain")
    update_parser.add_argument("--title_selector")
    update_parser.add_argument("--price_selector")
    update_parser.add_argument("--rating_selector")

    delete_parser = subparsers.add_parser("delete", help="Delete a source by ID")
    delete_parser.add_argument("id", type=int)


async def handle_sources_commands(args: argparse.Namespace):
    if args.command == "create":
        source = await create_source(
            name=args.name,
            domain=args.domain,
            title_selector=args.title_selector,
            price_selector=args.price_selector,
            rating_selector=args.rating_selector,
        )
        print("Created:", source)

    elif args.command == "get":
        source = await get_source_by_id(args.id)
        print("Retrieved:", source)

    elif args.command == "list":
        sources = await list_sources()
        for s in sources:
            print(s)

    elif args.command == "update":
        source = await update_source(
            source_id=args.id,
            name=args.name,
            domain=args.domain,
            title_selector=args.title_selector,
            price_selector=args.price_selector,
            rating_selector=args.rating_selector,
        )
        print("Updated:", source)

    elif args.command == "delete":
        success = await delete_source(args.id)
        print("Deleted:", success)
