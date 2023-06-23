import csv
import os.path
import pandas as pd
import numpy as np
import data_generate as dg

king = 0
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
        print('Parsing file ALL TIMME: ' + filename)
        reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        next(reader)    
        #this needs list both ints and strings
        listForReturn = [[float(x[0]), float(x[1]), list(x[2]), list(x[3])] for x in reader]
        # listForReturn = [[float(x) for x in row] for row in reader]
        f.close()
        return listForReturn

#this is gonna take a list of ([cost, listOfConfigurations]) and turn it into a csv formatted index, cost, listOfConfigrations    
def all_time_write(my_list):
    if os.path.exists('all_time.csv'):
        os.remove('all_time.csv')
        print('all_time.csv deleted')
    '''    
    #this is writing a weird csv, it is writing the list of configurations as a string with like a billion commas
    #I want it to write it as a string with all the numbers just apended together without a space or comma
    #I think I can do this by just making the list a string and then writing it
    # with open('all_time.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['index', 'cost', 'listOfConfigurations'])
    #     for i in range(len(list)):
    #         # listToStr = ' '.join([str(elem) for elem in list])
    #         writer.writerow([list[i][0], list[i][1], (' '.join([str(elem) for elem in list[i][2]])), (' '.join([str(elem) for elem in list[i][3]]))])
    #     f.close()
    
        #basiclaly this is gonna test stupid shit
    list = [0,1,1,1,3,5]
    listToStr = ' '.join([str(elem) for elem in list])
    apple = "String"
    digit = 4
    
    #create a csv that will store those valies
    pd.DataFrame({'id': apple, 'number': digit, 'list': listToStr}, index=[0]).to_csv('Test.csv', index=False)

    '''
    
    # #use pandas to write the csv
    # #I need to insert list[0] into 'index', and so on
    # #make a dataframe with columns inex, cost, listOFConfigurations
    # df = pd.DataFrame(columns=["index", 'cost', 'listOfConfigurations'])
    # for i in range(len(my_list)):
    #     # print('This is list of i',list[i])
    #     temp_df = pd.DataFrame('index': my_list[i], 'cost': my_list[0])
        
        
    #     #append to dataframe
    
    #TODO THIS THIS THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        
#The above method is writing it wrong


#I need to write a method that will parse the current csv of vms, and then upgrade the configurations 
#of the vms by one configuration and then write it back to the csv and return it as the parsed?
#its gonnna take an iterator to see how many times it has been called and then it will return the new vms
#accordingly to scale up the vms
def upgraded_vm_creation():
    #open the vms csv and parse it
    vms = parse_csv('FUCK YOU CJ')
    recursive_flag = 1
    flag = 1
    #create a local dictionary of the vm configurations by the class structure
    vm_config_dict = {}    
    config1 = [8, 2, 0.096, 0, 1]
    config2 = [16, 4, 0.192, 0, 2]
    config3 = [32, 8, 0.384, 0, 3]
    config4 = [64, 16, 0.768, 0, 4]
    config5 = [128, 32, 1.536, 0, 5]
    config6 = [192, 48, 2.304, 0, 6]
    config7 = [256, 64, 3.072, 0, 7]
    config8 = [384, 96, 4.608, 0, 8]
    
    vm_config_dict[1] = config1
    vm_config_dict[2] = config2
    vm_config_dict[3] = config3
    vm_config_dict[4] = config4
    vm_config_dict[5] = config5
    vm_config_dict[6] = config6
    vm_config_dict[7] = config7
    vm_config_dict[8] = config8
    
    for vm in vms:
        #get the current configuration number then update that vm to the next configuration
        current_config = vm[4]
        #if the current configuration is 8, then just keep it at 8
        if current_config == 8:
            #loop to see if they are already all 8's
            #if they are then just return the vms as all 8's
            if all(vm[4] == 8 for vm in vms):
                return vms, flag
            if all(vm[4] == 2 for vm in vms):
                return vms, flag
        else:
            vm[0] = vm_config_dict[current_config + 1][0]
            vm[1] = vm_config_dict[current_config + 1][1]
            vm[2] = vm_config_dict[current_config + 1][2]
            vm[3] = vm_config_dict[current_config + 1][3]
            vm[4] = vm_config_dict[current_config + 1][4]
            
    #dont write them to the csv just return the list of vms
    return vms, 0
        
def test_boy():
    
    #basiclaly this is gonna test stupid shit
    list = [0,1,1,1,3,5]
    listToStr = ' '.join([str(elem) for elem in list])
    apple = "String"
    digit = 4
    
    #create a csv that will store those valies
    pd.DataFrame({'id': apple, 'number': digit, 'list': listToStr}, index=[0]).to_csv('Test.csv', index=False)
    


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
    
    test_boy()
    
                
