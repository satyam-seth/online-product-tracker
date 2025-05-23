# Online Product Tracker

Tool for managing product sources and tracking product URLs asynchronously with a database.

## Features

- Track product URLs (`track`, `history`, `show`)
- CRUD operations on product sources (`create`, `get`, `list`, `update`, `delete`)
- Async database interactions using SQLAlchemy with async sessions
- Modular CLI built using Python's standard `argparse` and `asyncio`

## Setup

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

- [DB Setup](./tracker/README.md)

- Run project with uv

  ```bash
  uv run cli.py --help
  ```

## Usage

Run the CLI with Python:

```bash
python cli.py <command> [options]
```

### Commands

#### Monitor Product

- **track**

  Track a product by URL

  ```bash
  python cli.py track --url "https://example.com/product/123"
  ```

- **history**

  Show tracking history for a product URL

  ```bash
  python cli.py history --url "https://example.com/product/123"
  ```

- **show**

  Show product details for a URL

  ```bash
  python cli.py show --url "https://example.com/product/123"
  ```

---

#### CRUD operations for product Sources

- **create**

  Create a new source

  ```bash
  python cli.py sources create \
  --name EXAMPLE_IN \
  --domain "www.example.in" \
  --title_selector "#title" \
  --price_selector "#price" \
  --rating_selector "#rating"
  ```

- **get**

  Retrieve a source by ID

  ```bash
  python cli.py get 1
  ```

- **list**

  List all sources

  ```bash
  python cli.py list
  ```

- **update**

  Update an existing source by ID

  ```bash
  python cli.py update 1 --domain "www.newdomain.com"
  ```

- **delete**

  Delete a source by ID

  ```bash
  python cli.py delete 1
  ```
