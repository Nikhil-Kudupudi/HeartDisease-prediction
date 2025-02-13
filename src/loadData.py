import pandas as pd
from src.exception import CustomException
from src.logger import logging
import sys
import os
from dotenv import load_dotenv
from src.database import DBConn
load_dotenv()

FOLDER_PATH= os.path.join(os.getcwd(),os.getenv('DATASET_FOLDER'))

class LoadDataset:
    def __init__(self):
        dbconn=DBConn()
        self.conn=dbconn.getConnection()
        self.cursor=self.conn.cursor()

    def loadFromCSV(self,table_name, csv_file_name):
        try:
            query= f"""
        LOAD DATA INFILE '{FOLDER_PATH}/{csv_file_name}'
        INTO TABLE {table_name}
        FIELDS  TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;
        """
            self.cursor.execute(query)
        except Exception as e:
            raise CustomException(e,sys)
        
    def execute_query(self,query):
        try:
            if "delete" not  in query.lower():
                result=self.cursor.execute(query)
                logging.INFO("Query executed successfully")
                return result
            else:
                logging.INFO("DELETE query tried to be executed ")
                raise CustomException("DELETE Query is NOT ALLOWED",sys)
        except Exception as e:
            raise CustomException(e, sys)
        

    def getTableNames(self,dir):
        try:
            files=os.listdir(dir)
            tableNames=[]
            for fileName in files:
                name, extension=fileName.split(".")
                tableNames.append((name,fileName))
            return tableNames
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    dataset=LoadDataset()
    try:
        tableNames=dataset.getTableNames(FOLDER_PATH)
        for name,fileName in tableNames:
            print(name,fileName)
            dataset.createTabletoDB(name,fileName)
            logging.INFO("All tables are created successfully")
    except Exception as e:
        raise CustomException(e,sys)