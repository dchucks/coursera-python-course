import json
import sqlite3
import os
from os import listdir

conn = sqlite3.connect('accidentsdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS AccidentsData;

CREATE TABLE AccidentsData (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    State   TEXT,
    Year   INTEGER,
    Accidents INTEGER,
    Education TEXT
);
''')

filedir = os.path.join(os.path.dirname(__file__), "dataset//accidents-vs-education//2009-2015")
filelist = listdir(filedir)
print("Found following files in specified folder ", filedir, ":", filelist)
totrows = 0

for fname in filelist:
    print("Now inserting data from:", fname)
    if len(fname) > 1:
        education = fname.split(".")[0]
        # print("education", education)

        str_data = open(filedir + "/" + fname).read()
        json_data = json.loads(str_data)

        # Get the listed Years from Fields and add them to our array
        yearlist = []
        for field in json_data['fields']:
            try:
                yearlist.append(int(field['label']))
            except:
                # print("error:", field['label'])
                print("")

        # Parse the accident data
        for accidata in json_data['data']:
            # print(accidata)
            # State | Year | Accidents | Education
            state = accidata[0]
            # print("State:",state)
            cnt = 0
            for data in accidata:
                if cnt > 0 and data != "NA" and data != "NR":
                    accidents = int(data)
                    year = yearlist[cnt - 1]
                    # We will not consider data where education is unknown or accidents were zero
                    if accidents > 0 and education != "Unknown":
                        cur.execute(
                            '''INSERT OR IGNORE INTO AccidentsData (State, Year, Accidents, 
                            Education) VALUES ( ?, ?, ?, ? )''',
                            (state, year, accidents, education))
                        # print("[",cnt,"] Inserted:", state, year, accidents, education)
                        totrows = totrows + 1
                cnt = cnt + 1

conn.commit()
print("Finished inserting", totrows, "rows of data from the json files.")

#Make data corrections
cur.execute("Update AccidentsData set State='Andaman & Nicobar Islands' where state = 'Andaman and Nicobar Islands'")
cur.execute("Update AccidentsData set State='Dadra & Nagar Haveli' where state='Dadra and Nagar Haveli'")
cur.execute("Update AccidentsData set State='Daman & Diu' where state='Daman and Diu'")
conn.commit()
print("Corrected names of 3 states")


