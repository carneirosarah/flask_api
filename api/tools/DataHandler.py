import logging
import pandas as pd

class DataHandler():

    def __init__(self, input_folder, files) -> None:

        self.input_folder = input_folder
        
        # read data from csv files
        self.data = self.__read_data(files)

        for key, value in self.data.items():
            print(key, value)

    # read data from csv files
    def __read_data(self, files):

        try:

            data = {}

            for file in files:

                data[file] = pd.read_csv(self.input_folder + '/' + file, header=0, index_col=0)

            return data

        except Exception as e:

            logging.error("DataHandler - read data: " +  e.__class__ + " :" + str(e))
            raise Exception("DataHandler - read data: " +  e.__class__ + " :" + str(e))

if __name__ == '__main__':

    data_handler = DataHandler('/home/sarah/Documentos/proto_challenge/flask_api/api/data', ['organization.csv', 'user.csv'])