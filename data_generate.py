import pandas as pd
import random
import numpy as np
import os.path
import csv

#using class structure im gonna make different configurations of vms
class VM_config:
    def __init__(self, memory: float, cpu: float, cost: float, config_number: float) -> None:
        self.memory = memory
        self.cpu = cpu
        self.cost = cost
        self.config_number = config_number
        self.ratio = memory/cpu
        # self.name = 'm' + str(memory) + 'c' + str(cpu)

#workload class if we were to be able to know such a thing
class Workload_config:
    def __init__(self, memory_cost: float, cpu_cost: float) -> None:
        self.memory_cost = memory_cost
        self.cpu_cost = cpu_cost


#function to generate sets of workloads 100 workloads at random but ascending in size and complexity by set
    #by complexity I mean the ratio of memory to cpu are also ascending
def generate_workloads_by_set(num_workloads: int, set_num: int) -> pd.DataFrame:
    #definte a multiplier for the memory and cpu to ascend each set and keep track of set nummber with i
    #workload size multiplier and workload complexity multiplier
    wsm = 2
    wcm = 2
    for i in range(set_num):
        curr_wsm = i*wsm
        curr_wcm = i*wcm
        #generate the workloads that ascend in size and complexity through multipliers
        ram = np.random.randint(i*curr_wcm, size=num_workloads*curr_wsm)
        cpu = np.random.randint(i*curr_wcm, size=num_workloads*curr_wsm)
        ids = np.arange(num_workloads*curr_wsm)
        
        if os.path.exists('workloads' + str(i) + '.csv'):
            os.remove('workloads' + str(i) + '.csv')
            print('workloads' + str(i) + '.csv deleted')
        
        #write the workloads to a csv
        pd.DataFrame({'id': ids, 'ram': ram, 'cpu': cpu}).to_csv('workloads' + str(i) + '.csv', index=False)
    
    print('Workloads generated!')
                    
    


#Functions to create workloads at random not using the class structure
def generate_workloads(num_workloads: int, rating: int) -> pd.DataFrame:
    ram = np.random.randint(4, size=num_workloads)
    cpu = np.random.randint(4, size=num_workloads)
    ids = np.arange(num_workloads)
    
    return pd.DataFrame({'id': ids, 'ram': ram, 'cpu': cpu})


#Functions to create VMs using the class structure, these wont be random 
#they adhere to AWS EC2 instance types such as the following:
# m5.large, m5.xlarge, m5.2xlarge, m5.4xlarge, m5.8xlarge, m5.12xlarge, m5.16xlarge, m5.24xlarge
#with the following specs:
# m5.large: 2 vCPU, 8 GiB RAM
# m5.xlarge: 4 vCPU, 16 GiB RAM
# m5.2xlarge: 8 vCPU, 32 GiB RAM
# m5.4xlarge: 16 vCPU, 64 GiB RAM
# m5.8xlarge: 32 vCPU, 128 GiB RAM
# m5.12xlarge: 48 vCPU, 192 GiB RAM
# m5.16xlarge: 64 vCPU, 256 GiB RAM
# m5.24xlarge: 96 vCPU, 384 GiB RAM
def random_generate_VMS(vm_count: int) -> pd.DataFrame:
    #create a list of VM configurations
    #Memory, CPU, Cost
    
    configs = []
    config1 = VM_config(8, 2, 0.096, 1)
    config2 = VM_config(16, 4, 0.192, 2)
    config3 = VM_config(32, 8, 0.384, 3)
    config4 = VM_config(64, 16, 0.768, 4)
    config5 = VM_config(128, 32, 1.536, 5)
    config6 = VM_config(192, 48, 2.304, 6)
    config7 = VM_config(256, 64, 3.072, 7)
    config8 = VM_config(384, 96, 4.608, 8)
    
    columns = ['memory', 'cpu', 'cost', 'ratio', 'config_number']
    #create a dataframe from the list of VM configurations
    df = pd.DataFrame(columns=columns, index=None)
    
    if(vm_count == 0):
        for i in range(random.randint(1, 100)):
            # configs.append(random.choice([config1, config2, config3, config4, config5, config6, config7, config8]))
            temp = random.choice([config1, config2, config3, config4, config5, config6, config7, config8])
            df2 = pd.DataFrame({'memory': [temp.memory], 'cpu': [temp.cpu], 'cost': [temp.cost], 'ratio': [temp.ratio], 'config_number': [temp.config_number]})
            df = df.append(df2)
    
    #randomly append configurations to the list for vm_count
    for i in range(vm_count):
        temp = random.choice([config1, config2, config3, config4, config5, config6, config7, config8])
        df2 = pd.DataFrame({'memory': [temp.memory], 'cpu': [temp.cpu], 'cost': [temp.cost], 'ratio': [temp.ratio], 'config_number': [temp.config_number]})
        df = df.append(df2)

    
    
    if os.path.exists('vms.csv'):
        os.remove('vms.csv')
        print('vms.csv deleted')
        
    df.to_csv('vms.csv', index=False)
    
    #return the dataframe
    # return df
    


#this will be the function that will be called the run the data generation
def generate_data(vm_count: int, workload_count: int):
    
    #generate the VMs, if given zero, will generate random amount 0..100
    vms = random_generate_VMS(vm_count)    
    #generate the workloads
    '''COMMENTED OUT BECAUSE WE ARE KEEPING THE WORKLOADS STANDARDIZED FOR NOW'''
    # workloads = generate_workloads_by_set(workload_count, 10)
    


if __name__ == '__main__':
    generate_data(100, 100)
    print('Done?')





