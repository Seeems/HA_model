import sqlalchemy
from sqlalchemy.exc import OperationalError
import pandas as pd

import os
import json

# Project loaction for a variable execution location
PROJECT_LOCATION = os.path.dirname(os.path.abspath(__file__))

# load config file
with open(os.path.join(PROJECT_LOCATION, 'config.json'), 'r') as file:
    config = json.load(file)

class Manager():

    def database_modification(data: pd.DataFrame):
        db_url = os.path.join(PROJECT_LOCATION, config['db_url'])
        db = sqlalchemy.create_engine(db_url)

        if not sqlalchemy.database_exists(db.url):
            sqlalchemy.create_database(db.url)
        try:
            sql_update_statement = data
            db.connect()
            db.execute(sql_update_statement)
        except OperationalError:
            # Switch database component of the uri
            meta = sqlalchemy.MetaData(db)
            t1 = sqlalchemy.Table('Table_1', meta,
                                  sqlalchemy.Column('x', sqlalchemy.Integer),
                                  sqlalchemy.Column('name', sqlalchemy.String))

            t1.create()


    def csv_loader(file_name: str, directory_path: str = PROJECT_LOCATION) -> pd.DataFrame:
        """
        Loading data of csv file into a DataFrame.

        input:
        file_name: str -> Name of csv file
        directory_path: str -> Location of directory_path

        output:
        df: DataFrame -> loaded data of csv file
        """
        file_path = os.path.join(file_name, directory_path)
        print(file_path)
        df = pd.read_csv(file_path)

        return df

    # Schreiben von Daten in SQL-Datenbank
    # Laden von Daten aus SQL-Datenbank
