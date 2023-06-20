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

#sorting methods
def allocate_1(vms, workloads):
    #start timer
    sTime = time.time()
    #sort the vms by cost from least to greatest
    vms.sort(key=lambda x: x.cost)
    #it would be interesting to see how this would work if we sorted by ratio * cost
    # vms.sort(key=lambda x: x.ratio*x.cost)
    #this will be like results, this is where memiozation will come in
    allocation = {}
    #Initialize the cost to zero
    total_cost = 0
    #missed workloads
    missed = []
    #iterate through the workloads
    for workload in workloads:
        #Find the least expensive vm that can handle the workload
        best_vm = None
        for vm in vms:
            if vm[1] >= workload[1] and vm[2] >= workload[2]:
                if best_vm is None or vm[3] < best_vm[3]:
                    best_vm = vm
                # If a suitable vm is found, allocate the workload to it
        if best_vm is not None:
            #make copy so we can find it later
            copy = best_vm
            #dictionary of workloads id = best vm id, make better data to figure this out
            allocation[workload[0]] = best_vm[0]
            total_cost += best_vm[3]
            # Decrement the vm's resources
            best_vm = (best_vm[0], best_vm[1] - workload[1], best_vm[2] - workload[2], best_vm[3])
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
    allocation = {v: k for k, v in allocation.items()}
    return allocation, total_cost, fTime, missed

#KnapSack algorithm
def knapsack_vms(workloads, vms):
    #start timer
    sTime = time.time()
    #missed workloads
    missed = []
    # Create a dictionary to store the cost and resource usage of each vm
    vm_usage = {vm[0]: [vm[3], vm[1], vm[2]] for vm in vms}
    # Create a dictionary to store the vm used for each workload
    workload_vms = {}

    # Sort the vm list by cost in ascending order
    vms_sorted = sorted(vms, key=lambda x: x[3])

    # Iterate through the workloads and assign them to the least expensive vm that has enough resources
    for workload in workloads:
        assigned_vm = None
        for vm in vms_sorted:
            if vm_usage[vm[0]][1] >= workload[1] and vm_usage[vm[0]][2] >= workload[2]:
                assigned_vm = vm[0]
                vm_usage[vm[0]][1] -= workload[1]
                vm_usage[vm[0]][2] -= workload[2]
                break
        if assigned_vm is None:
            missed.append(workload[0])
        workload_vms[workload[0]] = assigned_vm

    # Compute the total cost
    total_cost = sum([vm_usage[vm][0] for vm in vm_usage])
    eTime = time.time()
    fTime = eTime - sTime
    #this returns a dictionary of workload id = vm id, and the total cost
    return workload_vms, total_cost, fTime, missed


        
#learning methods
def learning():
    
    #this is gonna be a learning method that will learn from the results of the sorting methods
    #it will learn the best vm configuration for each workload set
    print('Learning method not yet implemented') 



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
        3. I use memoization to store the results of the sorting optimizing for cost seeing which vm configurations are best for each workload set
            A. We will compare the resutls of the random vm configurations to the memoized results if better ew will replace the currently memoized results with the new results
        *If I can keep VM configuration stack that is best for each csv of workloads and then run the expirement again and again I will eventually have a set of VM configurations that are best for each workload
        4. I then run the expirement again but this time I use the memoization to optimize for time
        5. I then run the expirement again but this time I use the memoization to optimize for both time and cost
        
        **This will allow the expirement to eventually be run with real workload numbers and specific confgiurations used by a company and then optimize for cost, time, or both
        
        """
    
    
    
    print('Hey there!')
      