from dagster_airbyte import load_assets_from_airbyte_instance, AirbyteResource, AirbyteManagedElementReconciler, AirbyteConnection, AirbyteSyncMode
from dagster_airbyte.managed.generated.sources import MysqlSource
from dagster_airbyte.managed.generated.destinations import PostgresDestination

my_airbyte_resource = AirbyteResource(
    host="airbyte-proxy",
    port="8000",
    # If using basic auth
    username="airbyte",
    password="password",
    request_timeout=300
)

airbyte_assets = load_assets_from_airbyte_instance(my_airbyte_resource, key_prefix=["world"])

mysql_source_world = MysqlSource(
    name="mysql-world",
    host="relational.fit.cvut.cz",
    port=3306,
    database="world",
    username="guest",
    password="relational",
    ssl_mode=MysqlSource.Preferred(),
    ssl=False,
    replication_method=MysqlSource.Standard()
)

postgres_destination_world = PostgresDestination(
    name="postgres-world",
    host="localhost",
    port=50005,
    database="dest_postgres",
    schema="public",
    username="postgresuser",
    password="password",
    ssl_mode=PostgresDestination.Disable(),
)

world_connection = AirbyteConnection(
    name="world_connection",
    source=mysql_source_world,
    destination=postgres_destination_world,
    stream_config={"City": AirbyteSyncMode.full_refresh_overwrite(),
                   "Country": AirbyteSyncMode.full_refresh_overwrite(),
                   "CountryLanguage": AirbyteSyncMode.full_refresh_overwrite(),
                   },
    normalize_data=True,
    destination_namespace="public"
)

airbyte_reconciler = AirbyteManagedElementReconciler(
    airbyte=my_airbyte_resource,
    connections=[world_connection]
)

