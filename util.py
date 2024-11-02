import psycopg2
from psycopg2 import Error
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_db(username, password, host, port, database):
    try:
        # Connect to the database with the provided credentials
        connection = psycopg2.connect(user=username,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        cursor = connection.cursor()
        logging.info("Connected to the database successfully.")
        return cursor, connection
    except (Exception, Error) as error:
        logging.error("Error while connecting to PostgreSQL: %s", error)
        raise

def disconnect_from_db(connection, cursor):
    try:
        if connection:
            cursor.close()
            connection.close()
            logging.info("PostgreSQL connection closed successfully.")
        else:
            logging.warning("No active connection to close.")
    except Exception as error:
        logging.error("Error while closing the connection: %s", error)
        raise

def run_and_fetch_sql(cursor, sql_string=""):
    try:
        cursor.execute(sql_string)
        record = cursor.fetchall()
        logging.info("SQL query executed and fetched results successfully.")
        return record
    except (Exception, Error) as error:
        logging.error("Error executing SQL command: %s", error)
        raise

def run_sql(cursor, sql_string=""):
    try:
        cursor.execute(sql_string)
        logging.info("SQL command executed successfully.")
    except (Exception, Error) as error:
        logging.error("Error executing SQL command: %s", error)
        raise

