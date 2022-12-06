from database_utils import DatabaseConnector
from sqlalchemy import create_engine, MetaData, Table
import pandas as pd

class DataExtractor():
    def list_db_tables(self):
        '''
        Returns list of tables in database engine
        '''
        engine = DatabaseConnector().init_db_engine()
        return(engine.table_names())
    
    def extract_rds_table(self,table_name):
        engine = DatabaseConnector().init_db_engine()
        df = pd.read_sql_table(table_name, engine, index_col='index')
        return df


if __name__ == '__main__':
    print('Tables in Database:',DataExtractor().list_db_tables())
    print(DataExtractor().extract_rds_table('orders_table').head())