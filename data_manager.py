import os
import json

import sqlalchemy
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

    def initialize_database(self, directory_path: str = PROJECT_LOCATION):

        self.logger.info("Initializing database. Checking if database exists.")

        # Getting all CSV filenames of file directory
        files_path = os.path.join(directory_path, 'files/')
        file_list = [f for f in os.listdir(files_path) if os.path.isfile(os.path.join(files_path, f))]

        if not sqlalchemy_utils.database_exists(self.db.url):
            self.logger.warning("No database found. Creating new Database...")
            sqlalchemy_utils.create_database(self.db.url)

        # get all csv
        for file_name in file_list:
            file_path = os.path.join(files_path, file_name)
            table_df = pd.read_csv(file_path)

            # check if filename contains a number
            if any(char.isdigit() for char in file_name):

                # Get Table number for table name
                for number in file_name:
                    if number.isdigit():
                        i = number

                # check if table exists
                if not self.db.dialect.has_table(self.db.connect(), f'table{i}'):

                    # create table 1 with data of csv
                    table_df.to_sql(f'table{i}',
                                    self.db,
                                    if_exists='replace',
                                    index=True)
                    self.logger.info(f'table {i} creation successfully!')

                else:
                    self.logger.info(f'table {i} already exists!')

            else:
                print("Table number not in range (1 - 3)")

    def database_modification(self, table_no: int):
        """
        Checks if table already exists and fill in the tables

        :param table_no: Number of exercise table
        :param data: Data for database
        :return: none

        """

    # Laden von Daten aus SQL-Datenbank
