from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import psycopg2
import clickhouse_driver

# Define default arguments for the DAG
default_args = {
    'owner': 'pg_to_ch_data_transfer',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'pg_to_ch_data_transfer',
    default_args=default_args,
    schedule_interval=timedelta(hours=1),
    catchup=False,  
)

# Define a Python function to transfer data from PostgreSQL to ClickHouse
def transfer_data_pg_to_ch():
    # PostgreSQL connection
    pg_conn = psycopg2.connect(
        host="your_pg_host",
        database="your_pg_database",
        user="your_pg_user",
        password="your_pg_password"
    )

    # ClickHouse connection
    ch_conn = clickhouse_driver.Client("your_ch_host")

    # Here you can use SQL to copy data from PostgreSQL to ClickHouse
    pg_cursor = pg_conn.cursor()
    pg_cursor.execute("SELECT * FROM your_pg_table")
    data = pg_cursor.fetchall()
    



    ch_conn.execute(
        "
        CREATE TABLE IF NOT EXISTS tetuan_city_power_consumption
            (
                date_time DateTime DEFAULT now(),
                temperature Float32,
                humidity Float32,
                wind_speed Float32,
                general_diffuse_flows Float32,
                diffuse_flows Float32,
                zone_1_power_consumption Float32,
                zone_2_power_consumption Float32,
                zone_3_power_consumption Float32
            ) 
            ENGINE = ReplacingMergeTree()
            ORDER BY date_time
            PRIMARY KEY date_time
        "
        )

    ch_conn.execute(
        "INSERT INTO tetuan_city_power_consumption (date_time, temperature,humidity,wind_speed, general_diffuse_flows, diffuse_flows, zone_1_power_consumption, zone_2_power_consumption, zone_3_power_consumption) VALUES", data
    )

    # Close connections
    pg_conn.close()
    ch_conn.disconnect()

# Define a PythonOperator to run the data transfer function
transfer_task = PythonOperator(
    task_id='transfer_data_task',
    python_callable=transfer_data_pg_to_ch,
    provide_context=True,
    dag=dag,
)

# Set task dependencies
transfer_task

if __name__ == "__main__":
    dag.cli()


