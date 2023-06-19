#library imports
import pandas as pd
import random
import numpy as np
import csv
import time
import os.path

#file imports
import data_helper as dh
import data_generate as dg
#function imports

#global variables

#class definitions

#sorting methods

#learning methods



#main
if __name__ == '__main__':
    
    #generate data
    # dg.generate_data(1000, 1000)
    
    #read data
    vms = dh.parse_csv('vms.csv')
    workloads = dh.parse_csv('workloads.csv')
    
    """I think the expirement should do the following:
    
        1. Have multiple workload csv files labeled csv1..csv10 that are static sorta standardized
            A. These workloads will be ascending in size and complexity
        2. I run the expiremtn of sorting these workloads against the random vm configurations
        3. I use memoization to store the results of the sorting optimizing for cost seeing which set of vm configurations are best for each workload 
        *If I can keep VM configuration stack that is best for each csv of workloads and then run the expirement again and again I will eventually have a set of VM configurations that are best for each workload
        4. I then run the expirement again but this time I use the memoization to optimize for time
        5. I then run the expirement again but this time I use the memoization to optimize for both time and cost
        
        **This will allow the expirement to eventually be run with real workload numbers and specific confgiurations used by a company and then optimize for cost, time, or both
        
        """
    
    
    
    print('Hey there!')
      