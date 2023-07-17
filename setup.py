from setuptools import find_packages, setup

setup(
    name="data_pipeline",
    packages=find_packages(exclude=["data_pipeline_tests"]),
    install_requires=[
        "dagster",
        "dagster-graphql",
        "dagster-postgres",
        "dagster-docker",
        "dagster-airbyte",
        "dagster-dbt",
        "dagster-duckdb",
        "dagster-duckdb-pandas",
        "dagster-managed-elements",
        "dagster-shell",
        "dbt-core",
        "dbt-postgres",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
