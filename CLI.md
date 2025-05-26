- Run cli with uv

  ```bash
  uv run -m app.cli <command> [options]
  ```

- Run the CLI with Python:

  ```bash
  python -m app.cli <command> [options]
  ```

### Commands

#### Monitor Product

- **track**

  Track a product by URL

  ```bash
  python -m app.cli track --url "https://example.com/product/123"
  ```

- **history**

  Show tracking history for a product URL

  ```bash
  python -m app.cli history --url "https://example.com/product/123"
  ```

- **show**

  Show product details for a URL

  ```bash
  python -m app.cli show --url "https://example.com/product/123"
  ```

---

#### CRUD operations for product Sources

- **create**

  Create a new source

  ```bash
  python -m app.cli sources create \
  --name EXAMPLE_IN \
  --domain "www.example.in" \
  --title_selector "#title" \
  --price_selector "#price" \
  --rating_selector "#rating"
  ```

- **get**

  Retrieve a source by ID

  ```bash
  python -m app.cli get 1
  ```

- **list**

  List all sources

  ```bash
  python -m app.cli list
  ```

- **update**

  Update an existing source by ID

  ```bash
  python -m app.cli update 1 --domain "www.newdomain.com"
  ```

- **delete**

  Delete a source by ID

  ```bash
  python -m app.cli delete 1
  ```

---

#### CRUD operations for **Products**

- **create**

  Create a new product.

  ```bash
  python -m app.cli products create \
  --url "https://www.example.in/product/123" \
  --source_id 1
  ```

- **get**

  Retrieve a product by ID.

  ```bash
  python -m app.cli products get --id 1
  ```

- **get by url**

  Retrieve a product by URL.

  ```bash
  python -m app.cli products get --url-by-url "https://www.example.in/product/123"
  ```

- **list**

  List all products.

  ```bash
  python -m app.cli products list
  ```

- **update**

  Update an existing product.

  ```bash
  python -m app.cli products update \
  --id 1 \
  --url "https://www.example.in/product/updated-url"
  ```

- **delete**

  Delete a product by ID.

  ```bash
  python -m app.cli products delete --id 1
  ```

---

#### CRUD operations for **Product Snapshots**

- **create**

  Create a new snapshot for a product.

  ```bash
  python -m app.cli snapshots create \
  --product_id 1 \
  --title "Example Product" \
  --rating 4.5 \
  --amount 499.99 \
  --currency "INR"
  ```

- **get**

  Retrieve a snapshot by ID.

  ```bash
  python -m app.cli snapshots get --id 1
  ```

- **list**

  List all snapshots.

  ```bash
  python -m app.cli snapshots list
  ```

- **list by product id**

  List all snapshots for a product ID.

  ```bash
  python -m app.cli snapshots list-by-product --product_id 1
  ```

- **update**

  Update a snapshot by ID.

  ```bash
  python -m app.cli snapshots update \
  --id 1 \
  --rating 4.8
  ```

- **delete**

  Delete a snapshot by ID.

  ```bash
  python -m app.cli snapshots delete --id 1
  ```
