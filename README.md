# online-product-tracker

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

- [DB Setup](./tracker/storage/README.md)

- Run project with uv

  ```bash
  uv run cli.py --help
  ```

- Show current product info

  ```bash
  uv run cli.py show --url "<product_url>"
  ```

- Show fetch and store product info into database table

  ```bash
  uv run cli.py track --url "<product_url>"
  ```

- Get history of product from database table
  ```bash
  uv run cli.py history --url "<product_url>"
  ```
