import os
import json

import sqlalchemy
from sqlalchemy.exc import OperationalError
import sqlalchemy_utils
import pandas as pd

import setup_logger

# --------- GLOBAL VARIABLES ----------------
# Project loaction for a variable execution location
PROJECT_LOCATION = os.path.dirname(os.path.abspath(__file__))

# --------- GLOBAL SETTINGS  ----------------
# load config file
with open(os.path.join(PROJECT_LOCATION, 'config.json'), 'r') as file:
    config = json.load(file)


# Class Manager for whole data management. CSV and Database operations
class Manager(object):
    """
    Data Manager class for data management and operations.
    Loading CSV files as DataFrames.
    Creating, loading and modifying database (sqlite)

    Classes:
        Manager

    Functions:
        initialize_database()
        database_modification(data: pd.DataFrame, table_no: int)
        csv_loader(self, file_name: str, directory_path: str = PROJECT_LOCATION) -> pd.DataFrame

    Misc variables:
        PROJECT_LOCATION
    """
    def __init__(self):
        self.config = config
        self.db_url = 'sqlite:///{}'.format(
            os.path.join(os.path.dirname(__file__),
                         config['SQLALCHEMY_DATABASE_URI']))
        self.logger = setup_logger.setup('data_manager')
        self.db = sqlalchemy.create_engine(self.db_url, echo=True)

        self.initialize_database()
        return

    def initialize_database(self, file_name: str, directory_path: str = PROJECT_LOCATION):

        self.logger.info("Initializing database. Checking if database exists.")

        if not sqlalchemy_utils.database_exists(self.db.url):
            self.logger.warning("No database found. Creating new Database.")
            sqlalchemy_utils.create_database(self.db.url)


            file_path = os.path.join(file_name, directory_path)
            df = pd.read_csv(file_path)


        else:
            self.logger.info("Database already exists")
            #if tables not existing

    def database_modification(self, data: pd.DataFrame, table_no: int):
        """
        Checks if table already exists and fill in the tables

        :param table_no: Number of exercise table
        :param data: Data for database
        :return: none

        """
        if table_no == 1:
            table1_df = self.csv_loader('table1.csv')
            table1_df.to_sql(data)
            try:
                sql_update_statement = data
                self.db.connect()
                self.db.execute(sql_update_statement)
            except OperationalError:
                # Switch database component of the uri
                self.logger.warning('No table 1 available. New table will be created.')
                meta = sqlalchemy.MetaData(self.db)
        elif table_no == 2:

        elif table_no == 3:

        else:
            print("Table number not in range (1 - 3)")

    # Laden von Daten aus SQL-Datenbank
