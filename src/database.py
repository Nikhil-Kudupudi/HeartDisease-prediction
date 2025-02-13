from mysql import connector
from src.exception import CustomException
from src.logger import logging
import sys
import os
from dotenv import load_dotenv
load_dotenv()
DB_NAME=os.getenv('DB_NAME')

class DBConn:
    def __init__(self):
        try:
            self.db=connector.connect(
                user="root",
                password="root",
                host="localhost",
                port="3306",
                database=DB_NAME
            )
            self.cursor=None
        except Exception as e:
            raise CustomException(e, sys)
    def getConnection(self):
        try:
            return self.db
        except Exception as e:
            raise CustomException(e, sys)            
    def createDB(self):
        try:
            self.cursor=self.db.cursor()
            self.cursor.execute(
f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'"
)
        except Exception as e:
            raise CustomException(e, sys)
if __name__=="__main__":
    db=DBConn()
