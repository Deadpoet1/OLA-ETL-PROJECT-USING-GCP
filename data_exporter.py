import pandas as pd
import pandas_gbq 
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(df1: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    project_id='ola-data-analysis'
    dataset_id='ola-data-analysis.ola'
    table_id = 'ola-data-analysis.ola.ola_data'

    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
        pandas_gbq.to_gbq(df1, table_id, project_id=project_id),
        table_id,
        if_exists='replace',  # Specify resolution policy if table name already exists
    )