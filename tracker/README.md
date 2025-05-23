1. Initializing alembic

   ```sh
   alembic init -t async alembic
   ```

2. Generate migration for sources model (Skip if already generated)

   ```sh
   alembic revision --autogenerate -m "Create Sources Table"
   ```

3. Apply migration

   ```sh
   alembic upgrade head
   ```
