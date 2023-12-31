FROM python:3.11.1

# Checkout and install dagster libraries needed to run the gRPC server
# exposing your repository to dagit and dagster-daemon, and to load the DagsterInstance

RUN pip install \
    dagster \
    dagster-postgres \
    dagster-docker \
    dagster-airbyte \
    dagster-dbt \
    dagster-managed-elements \
    dagster-shell \
    dbt-core \
    dbt-postgres

# Add repository code

WORKDIR /opt/dagster/app

COPY ./data_pipeline /opt/dagster/app

# Run dagster gRPC server on port 4000

EXPOSE 4000

# CMD allows this to be overridden from run launchers or executors that want
# to run other commands against your repository
CMD ["dagster", "code-server", "start", "-h", "0.0.0.0", "-p", "4000", "-f", "defs.py"]
