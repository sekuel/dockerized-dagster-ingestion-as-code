# Dagster Ingestion as Code - Dockerized

## Running on local
1. Make sure you have Docker installed
2. Run Airbyte
3. Run the dagster project:
    ```
    make compose-up
    ```
4. Run @op `airbyte_check_diff` to prints out differences between the current state of the Airbyte instance and the desired state specified in the reconciler.
5. Run @op `airbyte_apply_diff` to apply the changes.
6. Hot reload the dagster definitions via UI to get the latest assets. Read more at: https://github.com/dagster-io/dagster/discussions/14709.
7. To shut down the project:
    ```
    make compose-down
    ```
