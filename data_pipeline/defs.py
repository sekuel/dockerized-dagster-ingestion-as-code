from dagster import Definitions, OpExecutionContext, op, job, FilesystemIOManager
from dagster_shell import execute_shell_command
from assets.airbyte import airbyte_assets
from assets.dbt import dbt_assets, DBT_PROJECT_PATH, DBT_PROFILES
from dagster_dbt import DbtCliClientResource

resources = {
    "dbt": DbtCliClientResource(
        project_dir=DBT_PROJECT_PATH,
        profiles_dir=DBT_PROFILES,
    )
}

@op
def airbyte_check_diff(context: OpExecutionContext):
    return execute_shell_command("dagster-airbyte check -m assets.airbyte -d .", 
                                 output_logging="STREAM", 
                                 log=context.log,
                                 cwd="/opt/dagster/app")

@op
def airbyte_apply_diff(context: OpExecutionContext):
    return execute_shell_command("dagster-airbyte apply -m assets.airbyte -d .", 
                                 output_logging="STREAM", 
                                 log=context.log,
                                 cwd="/opt/dagster/app")

@job(resource_defs={"io_manager": FilesystemIOManager()})
def airbyte_check():
    airbyte_check_diff()
    airbyte_apply_diff()

defs = Definitions(
    assets = (dbt_assets + [airbyte_assets]),
    jobs=[airbyte_check],
    resources=resources,
)