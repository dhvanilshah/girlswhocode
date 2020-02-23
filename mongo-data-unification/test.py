#!/usr/bin/env python
import os
import pandas as pd
import pymongo
import json

# Database configuration
mng_client = pymongo.MongoClient('localhost', 27017)
mng_db = mng_client['gwc'] # Making a database called 'gwc'
collection_name = 'all-students' # Making a collection called for all students
db_cm = mng_db[collection_name]

# Import all students from the "
def import_content(filepath):
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    print(data_json)
    # db_cm.remove()
    db_cm.insert_many(data_json)

if __name__ == "__main__":
  filepath = '../girlswhocode/dataset/college.csv'  #pass csv file path
  import_content(filepath)