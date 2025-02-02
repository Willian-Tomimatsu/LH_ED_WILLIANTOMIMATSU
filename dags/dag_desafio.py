import os
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

#basedir = os.path.abspath(os.path.dirname(__file__))

with DAG(
    dag_id="desafio_indicium",
    start_date=datetime(2025, 1, 2),
    schedule="@daily",
    catchup=False,
) as dag:
    
    #Extrair dados
    extract = BashOperator(
        task_id="extract",
        bash_command="""cd /home/willian/Project
        source venv/bin/activate
        cd desafio_indicium/
        pwd
        source <(python generate_execution_date.py)
        source <(python generate_dynamic_path.py csv order_details)
        meltano run tap-csv-order_details_initial target-csv
        source <(python generate_dynamic_path.py postgres categories)
        meltano run tap-postgres-categories target-csv
        source <(python generate_dynamic_path.py postgres products)
        meltano run tap-postgres-products target-csv
        source <(python generate_dynamic_path.py postgres suppliers)
        meltano run tap-postgres-suppliers target-csv
        source <(python generate_dynamic_path.py postgres orders)
        meltano run tap-postgres-orders target-csv
        source <(python generate_dynamic_path.py postgres customers)
        meltano run tap-postgres-customers target-csv
        source <(python generate_dynamic_path.py postgres customer_customer_demo)
        meltano run tap-postgres-customer_customer_demo target-csv
        source <(python generate_dynamic_path.py postgres customer_demographics)
        meltano run tap-postgres-customer_demographics target-csv
        source <(python generate_dynamic_path.py postgres employees)
        meltano run tap-postgres-employees target-csv
        source <(python generate_dynamic_path.py postgres employee_territories)
        meltano run tap-postgres-employee_territories target-csv
        source <(python generate_dynamic_path.py postgres territories)
        meltano run tap-postgres-territories target-csv
        source <(python generate_dynamic_path.py postgres region)
        meltano run tap-postgres-region target-csv
        source <(python generate_dynamic_path.py postgres shippers)
        meltano run tap-postgres-shippers target-csv
        source <(python generate_dynamic_path.py postgres us_states)
        meltano run tap-postgres-us_states target-csv
        """,
    )
    

    # Carregar dados
    load = BashOperator(
        task_id="load",
        bash_command="""cd /home/willian/Project
        source venv/bin/activate
        cd desafio_indicium/
        pwd
        source <(python generate_execution_date.py)
        echo $EXECUTION_DATE
        meltano run load_to_northwind_final_db
        """,
    )

    # Consulta
    query = BashOperator(
        task_id="query",
        bash_command="""cd /home/willian/Project
        source venv/bin/activate
        cd desafio_indicium/
        meltano run tap-postgres-final target-csv-final
        python combine_csv.py
        """,
    )

extract >> load >> query
