import os
import logging
import psycopg2
from dotenv import load_dotenv

# Chargement des variables d'environnement ===
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Fonction d'exécution du fichier SQL ===
def run_sql_file(filename, cursor):
    logging.info(f"Running {filename}...")
    with open(filename, "r", encoding="utf-8") as file:
        sql = file.read()
        cursor.execute(sql)
    logging.info(f"{filename} executed successfully.")

# Connexion à PostgreSQL et run des pipelines
try:
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    connection.autocommit = True
    cursor = connection.cursor()
    logging.info("Connected to PostgreSQL.")

    run_sql_file("../SQL/create_tables.sql", cursor)
    run_sql_file("../SQL/insert_dimensions.sql", cursor)
    run_sql_file("../SQL/insert_facts.sql", cursor)

    cursor.close()
    connection.close()
    logging.info("Pipeline executed and connection closed.")

except Exception as e:
    logging.error(f"Error during pipeline execution: {e}")
