from dagster import Definitions, EnvVar   #load_assets_from_modules
from dagster_snowflake import SnowflakeResource

from .assets import create_database, aggregate_braze_user_events, sf_table_statistics  # noqa: TID252

#all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=[create_database, aggregate_braze_user_events, sf_table_statistics],
    resources={
        "snowflake": SnowflakeResource(
            account=EnvVar("SNOWFLAKE_ACCOUNT"),
            user=EnvVar("SNOWFLAKE_USER"),
            password=EnvVar("SNOWFLAKE_PASSWORD"),
            database="FLOWERS",
            schema="IRIS",
            warehouse="JING_TEST_WH", 
            ROLE="JING_TEST_ROLE"
        )
    },
)
