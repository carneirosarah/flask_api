import logging
import pandas as pd
from api import db, Organization, User
import psycopg2

class DataHandler():

    def __init__(self, input_folder, files) -> None:

        self.input_folder = input_folder
        
        self.data = self.__read_data(files)

        for key, value in self.data.items():
            print(key, value)

        DataHandler.__create_database()
        self.__insert_data()

    # read data from csv files
    def __read_data(self, files):

        try:

            data = {}

            for file in files:

                data[file] = pd.read_csv(self.input_folder + '/' + file, header=0).to_dict('records')

            return data

        except Exception as e:

            logging.error("DataHandler - read data: " +  str(e.__class__) + " :" + str(e))
            raise Exception("DataHandler - read data: " +  str(e.__class__) + " :" + str(e))
    
    # create database
    @staticmethod
    def __create_database():

        try:
        
            db.drop_all()
            db.create_all()

        except Exception as e:

            logging.error("DataHandler - create database: " +  str(e.__class__) + " :" + str(e))
            raise Exception("DataHandler - create database: " +  str(e.__class__) + " :" + str(e))

    # insert data into database
    def __insert_data(self):

        try:

            organizations = []
            users = []
            
            for file, data in self.data.items():

                if file == 'organization.csv':

                    for row in data:
                        
                        organizations.append(Organization(row['name']))

                elif file ==  'user.csv':

                    for row in data:

                        users.append(User(row['email'], row['first_name'], row['last_name'], row['organization_id']))
            
            db.session.add_all(organizations)
            db.session.add_all(users)

            db.session.commit()

        except Exception as e:

            logging.error("DataHandler - insert data: " +  str(e.__class__) + " :" + str(e))
            raise Exception("DataHandler - insert data: " +  str(e.__class__) + " :" + str(e))


    