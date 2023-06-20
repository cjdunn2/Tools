import csv
import os.path
import pandas as pd
import numpy as np
import data_generate as dg

#Helper functions

#parsing a csv file into a list of touples
def parse_csv(filename):
    with open(filename, 'r') as f:
        print('Parsing file: ' + filename)
        reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        next(reader)    
        listForReturn = [[float(x) for x in row] for row in reader]
        f.close()
        return listForReturn
    

def all_time_parse(filename):
    with open(filename, 'r') as f:
        print('Parsing file: ' + filename)
        reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        next(reader)    
        #this needs list both ints and strings
        listForReturn = [[float(x[0]), float(x[1]), list(x[2])] for x in reader]
        # listForReturn = [[float(x) for x in row] for row in reader]
        f.close()
        return listForReturn

#this is gonna take a list of [cost, listOfConfigurations] and turn it into a csv formatted index, cost, listOfConfigrations    
def all_time_write(list):
    if os.path.exists('all_time.csv'):
        os.remove('all_time.csv')
        print('all_time.csv deleted')
    with open('all_time.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['index', 'cost', 'listOfConfigurations'])
        for i in range(len(list)):
            writer.writerow([list[i][0], list[i][1], list[i][2]])
        f.close()
        
if __name__ == '__main__':
    #create a fake all_time_vms file basically a list of lists of vm configurations
    '''COMMENTED OUT AFTER BASE CREATION'''
    # if os.path.exists('all_time.csv'):
    #     os.remove('all_time.csv')
    #     print('all_time.csv deleted')
    # fake_list = []
    # for i in range(10):
    #     fake_list.append([i, 1000000000, [i, i, i, i]])
    # all_time_write(fake_list)
    
                
