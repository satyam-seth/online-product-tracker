import argparse
from tracker.fetcher import fetch_product_details

def show(url):
    try:
        product = fetch_product_details(url)
        print("\nProduct Info:")
        for key, value in product.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print("Failed to fetch product details:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Online Product Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    for cmd in ["show"]:
        sp = subparsers.add_parser(cmd)
        sp.add_argument("--url", required=True, help="Product URL")

    args = parser.parse_args()

    if args.command == "show":
        show(args.url)
    else:
        parser.print_help()
