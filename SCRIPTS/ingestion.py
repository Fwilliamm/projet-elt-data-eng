import os
import pandas as pd
import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

# Chargement des variables d'environnement
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

# Chargement du fichier CSV
try:
    df = pd.read_csv("../Online_Retail.csv", encoding="ISO-8859-1")
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format="%m/%d/%y %H:%M")
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    logging.info("CSV loaded and cleaned.")
except Exception as e:
    logging.error(f"Failed to load CSV: {e}")
    exit()

# Connexion à PostgreSQL
try:
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    with engine.connect() as conn:
        logging.info("Connected to PostgreSQL.")
except OperationalError as e:
    logging.error(f"Database connection failed: {e}")
    exit()

# Insertion des données dans raw_transactions
try:
    df.to_sql("raw_transactions", con=engine, if_exists="replace", index=False)
    logging.info("Data inserted into raw_transactions.")
except Exception as e:
    logging.error(f"Failed to insert data: {e}")
