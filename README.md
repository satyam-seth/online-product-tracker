# Online Product Tracker

Tool for managing product sources and tracking product URLs asynchronously with a database.

## Features

- Track product URLs (`track`, `history`, `show`)
- CRUD operations on product sources (`create`, `get`, `list`, `update`, `delete`)
- CRUD operations on product (`create`, `get`, `get-by-url`, `list`, `update`, `delete`)
- CRUD operations on product (`create`, `get`, `list`, `list-by-product`, `update`, `delete`)
- Async database interactions using SQLAlchemy with async sessions
- Modular CLI built using Python's standard `argparse` and `asyncio`

## Setup

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

- [DB Setup](./DB.md)

## API

- [Run API Server](./API.md)

## CLI

- [Run CLI](./CLI.md)
