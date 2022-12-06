import yaml
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

class DatabaseConnector():
    def read_db_creds(self):
        '''
        Reads the credentials of the RDS database from the locally stored YAML file
        '''
        with open("rds_db_creds.yaml", "r") as stream:
            try:
                return(yaml.safe_load(stream))
            except yaml.YAMLError as exc:
                return(exc)
        
    def init_db_engine(self):
        '''
        Takes Database credentials and creates an SqlAlchemy Engine to the database
        '''
        creds = self.read_db_creds()
        engine_url = URL.create('postgresql',creds['RDS_USER'],creds['RDS_PASSWORD'],creds['RDS_HOST'],creds['RDS_PORT'],creds['RDS_DATABASE'])
        engine = create_engine(engine_url)
        return engine

    def upload_to_db(self):
        pass


if __name__ == '__main__':
    Db_connector = DatabaseConnector()
    print(Db_connector.init_db_engine())