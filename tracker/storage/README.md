1. Initializing alembic

   ```sh
   alembic init -t async alembic
   ```

2. Generate migration for sources model (Optional)

   ```sh
   alembic revision --autogenerate -m "Create Sources Table"
   ```

   ```sh
   alembic revision --autogenerate -m "Add created_on and updated_on columns in Sources Table"
   ```

3. Apply migration

   ```sh
   alembic upgrade head
   ```
