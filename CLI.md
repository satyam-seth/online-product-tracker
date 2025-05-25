- Run cli with uv

  ```bash
  uv run -m app.cli <command> [options]
  ```

- Run the CLI with Python:

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

---

#### CRUD operations for **Products**

- **create**

  Create a new product.

  ```bash
  python cli.py products create \
  --url "https://www.example.in/product/123" \
  --source_id 1
  ```

- **get**

  Retrieve a product by ID.

  ```bash
  python cli.py products get --id 1
  ```

- **get by url**

  Retrieve a product by URL.

  ```bash
  python cli.py products get --url-by-url "https://www.example.in/product/123"
  ```

- **list**

  List all products.

  ```bash
  python cli.py products list
  ```

- **update**

  Update an existing product.

  ```bash
  python cli.py products update \
  --id 1 \
  --url "https://www.example.in/product/updated-url"
  ```

- **delete**

  Delete a product by ID.

  ```bash
  python cli.py products delete --id 1
  ```

---

#### CRUD operations for **Product Snapshots**

- **create**

  Create a new snapshot for a product.

  ```bash
  python cli.py snapshots create \
  --product_id 1 \
  --title "Example Product" \
  --rating 4.5 \
  --amount 499.99 \
  --currency "INR"
  ```

- **get**

  Retrieve a snapshot by ID.

  ```bash
  python cli.py snapshots get --id 1
  ```

- **list**

  List all snapshots.

  ```bash
  python cli.py snapshots list
  ```

- **list by product id**

  List all snapshots for a product ID.

  ```bash
  python cli.py snapshots list-by-product --product_id 1
  ```

- **update**

  Update a snapshot by ID.

  ```bash
  python cli.py snapshots update \
  --id 1 \
  --rating 4.8
  ```

- **delete**

  Delete a snapshot by ID.

  ```bash
  python cli.py snapshots delete --id 1
  ```
