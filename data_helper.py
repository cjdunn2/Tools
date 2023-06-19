import csv
import os.path
import pandas as pd
import numpy as np

#Helper functions

#parsing a csv file into a list of touples
def parse_csv(filename):
    with open(filename, 'r') as f:
        print('Parsing file: ' + filename)
        reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        next(reader)    
        listForReturn = [[int(x) for x in row] for row in reader]
        f.close()
        return listForReturn
    

