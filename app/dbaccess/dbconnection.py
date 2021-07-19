from configparser import ConfigParser
import psycopg2


class DBConnection:
    def getDBConnection(self):
        config = ConfigParser()
        config.read('./config.ini')
        configcategory = 'Database'
        try:
            self.connection = psycopg2.connect(user=config.get(configcategory, 'dbuser'),
                                               password=config.get(configcategory, 'dbpassword'),
                                               host=config.get(configcategory, 'host'),
                                               port=config.get(configcategory, 'port'),
                                               database=config.get(configcategory, 'dbname'))

        except(Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            '''if(self.connection):
                self.connection.close()
                print("PostgreSQL connection is closed")'''
            return self.connection
