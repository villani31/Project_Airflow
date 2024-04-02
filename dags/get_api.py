from airflow.decorators import task, dag
from datetime import datetime
from include.main import Status_Api, Carrega_Dados, Envia_DB_Sql, Gera_Parquet

@dag(dag_id="get_api",
     description="pipeline_para_coletar_dados_covid19",
     start_date=datetime(2024,4,1),
     schedule="*/30 * * * *",
     catchup=False)

def get_api():

    @task(task_id="task_Status_Api")
    def task_Status_Api():
        return Status_Api()

    @task(task_id="task_Carrega_Dados")
    def task_Carrega_Dados():
        return Carrega_Dados(0,25)

    @task(task_id="task_Envia_DB_Sql")
    def task_Envia_DB_Sql(df):
        return Envia_DB_Sql(df)

    @task(task_id="task_Gera_Parquet")
    def task_Gera_Parquet():
        return Gera_Parquet()

    t1 = task_Status_Api()
    t2 = task_Carrega_Dados()
    t3 = task_Envia_DB_Sql(t2)
    t4 = task_Gera_Parquet()

    t1 >> t2 >> t3 >> t4

#
get_api()