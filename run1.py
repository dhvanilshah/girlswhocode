import pandas as pd
import pymongo
import glob

# client = pymongo.MongoClient("localhost", 27017)
# db = client.gwc_db
# print(db.name)

path = "dataset"  # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.groupby('PID', as_index=False).app(' '.join).reset_index()

# print(frame.query('PID == 867'))

# single_person = frame.query('PID == 867')

print("Done")

# data = pd.read_csv("girlswhocode/dataset/college.csv")
# print(data.head())
#
# data = data.query('PID < 10')
#
# print(data)

