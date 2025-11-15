from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Configuración básica del DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id='ejemplo_DAG',                                    
    default_args=default_args,
    description='DAG de prueba para verificar funcionamiento de airflow',
    schedule_interval=None,
    start_date=datetime(2025, 11, 15),
    catchup=False,
) as dag:

    dump_command = """
    echo 'Prueba DAG, to be or not to be, that is the question, wheather tis nobler in the mind to suffer the slings and arrow of autrageous fortune or to take arms asmgainst a sea of troubles and by oposing end them'
    """

    backup_task = BashOperator(
        task_id='backup_postgres',
        bash_command=dump_command,
    )

    backup_task
