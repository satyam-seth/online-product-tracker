import argparse

from .schemas import SourceCreate, SourceUpdate
from .services import (
    create_source,
    get_source_by_id,
    get_source_by_domain,
    list_sources,
    update_source,
    delete_source,
)


def add_sources_subparsers(subparsers: argparse._SubParsersAction):
    # Create
    create_parser = subparsers.add_parser("create", help="Create a new source")
    create_parser.add_argument("--name", required=True)
    create_parser.add_argument("--domain", required=True)
    create_parser.add_argument("--title_selector", required=True)
    create_parser.add_argument("--price_selector", required=True)
    create_parser.add_argument("--rating_selector", required=True)

    # Get by ID
    get_parser = subparsers.add_parser("get", help="Retrieve a source by ID")
    get_parser.add_argument("id", type=int)

    # Get by Domain
    get_domain = subparsers.add_parser("get-by-domain", help="Get source by Domain")
    get_domain.add_argument("--domain", required=True)

    # List
    subparsers.add_parser("list", help="List all sources")

    # Update
    update_parser = subparsers.add_parser("update", help="Update a source by ID")
    update_parser.add_argument("id", type=int)
    update_parser.add_argument("--name")
    update_parser.add_argument("--domain")
    update_parser.add_argument("--title_selector")
    update_parser.add_argument("--price_selector")
    update_parser.add_argument("--rating_selector")

    # Delete
    delete_parser = subparsers.add_parser("delete", help="Delete a source by ID")
    delete_parser.add_argument("id", type=int)


async def handle_sources_commands(args: argparse.Namespace):
    if args.command == "create":
        new_source = SourceCreate(
            name=args.name,
            domain=args.domain,
            title_selector=args.title_selector,
            price_selector=args.price_selector,
            rating_selector=args.rating_selector,
        )
        source = await create_source(new_source)
        print("Created:", source)

    elif args.command == "get":
        source = await get_source_by_id(args.id)
        print("Retrieved:", source)

    elif args.command == "get-by-domain":
        product = await get_source_by_domain(args.domain)
        print("Retrieved:", product)

    elif args.command == "list":
        sources = await list_sources()
        for source in sources:
            print(source)

    elif args.command == "update":
        source = await update_source(
            source_id=args.id,
            updated_source=SourceUpdate(
                name=args.name,
                domain=args.domain,
                title_selector=args.title_selector,
                price_selector=args.price_selector,
                rating_selector=args.rating_selector,
            ),
        )
        print("Updated:", source)

    elif args.command == "delete":
        success = await delete_source(args.id)
        print("Deleted:", success)
