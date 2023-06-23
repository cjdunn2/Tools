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

#TODO
#Make a new set of workloads that doesnt include zeros but does include floats and shit
#The algorithm is not going through on 9/10 runs but works perfect for one run wtf


#sorting methods
def allocate_1(vms, workloads):
    vm_config_list = []
    #make a list of the vm configurations from the list
    for i in range(len(vms)):
        vm_config_list.append(vms[i][4])
    #start timer
    sTime = time.time()
    #sort the vms by cost from least to greatest
    vms.sort(key=lambda x: x[2])
    #it would be interesting to see how this would work if we sorted by ratio * cost
    # vms.sort(key=lambda x: x.ratio*x.cost)
    #this will be like results, this is where memiozation will come in
    allocation = []
    #Initialize the cost to zero
    total_cost = 0
    #missed workloads
    missed = []
    #iterate through the workloads
    for workload in workloads:
        #Find the least expensive vm that can handle the workload
        best_vm = None
        for vm in vms:
            if vm[0] >= workload[1] and vm[1] >= workload[2]:
                if best_vm is None or vm[3] < best_vm[3]:
                    best_vm = vm
        # If a suitable vm is found, allocate the workload to it
        #best_vm if not none is suitable vm for workload based on the logic above
        if best_vm is not None:
            #make copy so we can find it later
            copy = best_vm
            #dictionary of workloads id = best vm id, make better data to figure this out
            allocation.append((best_vm[4]))
            total_cost += best_vm[3]
            # Decrement the vm's resources
            #cpu, memory, cost, ratio, config_number
            best_vm = (best_vm[0] - workload[1], best_vm[1] - workload[2], best_vm[2], best_vm[3], best_vm[4])
            #this line is wrong below
            # vms[vms.index((best_vm[0], best_vm[1] + workload[1], best_vm[2] + workload[2], best_vm[3]))] = best_vm
            #take the index of the copy and replace it with the new best vm
            vms[vms.index(copy)] = best_vm
        #if no suitable vm is found, return an error
        else:
            missed.append(workload[0])
    # Return the allocation and the total cost
    #this will return a dictionary of workload id = vm id
    #i want it to return a dictionary of vm id = workload id
    #but maybe I should do that in the frontend
    eTime = time.time()
    fTime = eTime - sTime
    # allocation = {v: k for k, v in allocation.items()}
    # return allocation, total_cost, fTime, missed
    if len(missed) > 0:
        #if we missed any we need to create a more expensive set of vms and run the algorithm again on this workload
        #then it will continue, this might happena few times, but it will eventually get all the workloads
        upgraded_vms = dh.upgraded_vm_creation()
        
        if upgraded_vms[1] == 0:
            allocate_1(upgraded_vms[0], workloads)
        else:
            print('Missing this many: ' + str(len(missed)))
            print('THis is TOTAL COST',total_cost, allocation)
            return total_cost, allocation, vm_config_list
        # print('Missing Workloads: ', missed)
        # print('Missing this many: ' + str(len(missed)))
        # print('This is TOTAL COST',total_cost, allocation)
        # return total_cost, allocation, vm_config_list  
    else:
        print('This is TOTAL COST',total_cost, allocation)
        return total_cost, allocation, vm_config_list

        
#learning methods
def learning():
    #opening the all time vm configuration file and parsing it
    # all_time = open('all_time_vms.csv', 'w')
    all_time_parsed = []

    # if os.path.exists('all_time.csv'):
    #     os.remove('all_time.csv')
    #     for i in range(10):
    #         all_time_parsed.append([10, 1000000000, [1, 1, 1, 1]])
    #     dh.all_time_write(all_time_parsed)
    
    #now we are actually implementing this so we need to parse the all time csv
    #then use it and potentially update it later.
    if os.path.exists('all_time.csv'):
        all_time_parsed = dh.all_time_parse('all_time.csv') 
    else: 
        for i in range(10):
            all_time_parsed.append([10, 1000000000, [1, 1, 1, 1]])
        dh.all_time_write(all_time_parsed)
    
    # print(all_time_parsed, 'This is the orginal all time parsed')
    #result list of tuples to see performance by worklaod set [cost, list_of_configaration]
    results = []

    #read data
    # vms = dh.parse_csv('vms.csv')
    # print('This is vms ', vms)
    for i in range(10):
        #read data in the loop so we can change the workloads and not have to worry about it
        #close and open the file each time so that the virtual machines are for sure resetting
        print('This is i', i)
        vms = dh.parse_csv('vms.csv')
        workload = dh.parse_csv('workloads' + str(i) + '.csv')
        cResult = allocate_1(vms, workload)
        results.append(cResult)
    for i in range(len(results)):
        if results[i][0] != 0:
            #can test here if the results are better than the all time results
            if results[i][0] < all_time_parsed[i][1]:
                all_time_parsed[i][1] = results[i][0]
                all_time_parsed[i][2] = results[i][1]
                all_time_parsed[i][3] = results[i][2]
        else: 
            continue
    #write the all time results back to a csv
    dh.all_time_write(all_time_parsed)
    
    
                          
    #This should return a list of tuples of the form (total_cost, fTime)
    # print(all_time_parsed[0], sep='\n')
    # print(all_time_parsed[1], sep='\n')
    # print(all_time_parsed[2], sep='\n')
    # print(all_time_parsed[3], sep='\n')





#main
if __name__ == '__main__':
    
    learning()
    
    #now I need to memoize the results of the sorting methods and only ever keep them if they are better than the all time resutls
    #I could give a score to the run using some sort of metrics and then compare the score with the all time score. 
    #If the score is better than the all time score then I keep the results and replace the all time score with the new score
    
    #how do I score the results?
    #time  shouldnt matter, thats an algorithm metric not a virtual machine metric
    #cost is the only metric that matters
    
    """I think the expirement should do the following:
    
        1. Have multiple workload csv files labeled csv1..csv10 that are static sorta standardized
            A. These workloads will be ascending in size and complexity
        2. I run the expiremtn of sorting these workloads against the random vm configurations
        3. I use memoization to store the results of the sorting optimizing for cost seeing which vm configurations are best for each workload set
            A. We will compare the resutls of the random vm configurations to the memoized results if better ew will replace the currently memoized results with the new results
        *If I can keep VM configuration stack that is best for each csv of workloads and then run the expirement again and again I will eventually have a set of VM configurations that are best for each workload
        4. I then run the expirement again but this time I use the memoization to optimize for time
        5. I then run the expirement again but this time I use the memoization to optimize for both time and cost
        
        **This will allow the expirement to eventually be run with real workload numbers and specific confgiurations used by a company and then optimize for cost, time, or both
        
        """
    
    
    
      