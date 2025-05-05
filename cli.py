import argparse
from tracker.fetcher import fetch_product_details
from tracker.storage import init_db, save_product_data


def track(url):
    try:
        product = fetch_product_details(url)
        save_product_data(product)
        print("Product data saved successfully.\n", product)
    except ValueError as e:
        print("Failed to fetch product details:", e)


def show(url):
    try:
        product = fetch_product_details(url)
        print("\nProduct Info:")
        for key, value in product.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print("Failed to fetch product details:", e)


if __name__ == "__main__":
    init_db()
    parser = argparse.ArgumentParser(description="Online Product Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    for cmd in ["track", "show"]:
        sp = subparsers.add_parser(cmd)
        sp.add_argument("--url", required=True, help="Product URL")

    args = parser.parse_args()

    if args.command == "track":
        track(args.url)
    elif args.command == "show":
        show(args.url)
    else:
        parser.print_help()
