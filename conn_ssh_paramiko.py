from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import paramiko

# Define la función que ejecutará la tarea SSH
def execute_ssh_command():
    # Configura los detalles de la conexión SSH
    ssh_host = 'tu_servidor_ssh'
    ssh_port = 22
    ssh_username = 'tu_usuario_ssh'
    ssh_password = 'tu_contraseña_ssh'  # También puedes utilizar claves SSH

    # Crea una instancia de SSHClient
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conéctate al servidor SSH
        ssh_client.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)

        # Ejecuta un comando SSH
        ssh_command = 'ls -l'
        stdin, stdout, stderr = ssh_client.exec_command(ssh_command)

        # Lee la salida del comando
        command_output = stdout.read()
        print("Comando SSH ejecutado exitosamente:")
        print(command_output.decode('utf-8'))

    except Exception as e:
        print(f"Error al ejecutar el comando SSH: {str(e)}")
    finally:
        # Cierra la conexión SSH
        ssh_client.close()

# Define el DAG de Airflow
dag = DAG('ejemplo_ssh_dag', description='Ejemplo de tarea SSH en Airflow', schedule_interval=None)

# Define la tarea que ejecutará la conexión SSH
ssh_task = PythonOperator(
    task_id='tarea_ssh',
    python_callable=execute_ssh_command,
    dag=dag,
)

# Define las dependencias entre las tareas (si es necesario)
# other_task >> ssh_task

if __name__ == "__main__":
    dag.cli()
