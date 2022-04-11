# importing the required packaged 
import pandas as pd
import numpy as np
import re
import os
import sys
from functools import reduce

#Declared global variables
dir_name = ''
myDict = {}
data_frame = pd.DataFrame()

#This function gets the pathnames to each of the images
def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.
    count = 0
    
    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            count += 1
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            count, file_paths.append(filepath)
    return count, file_paths

#This function parses the path names and extracts the information
def data_to_labels(dir_name):
    counted, file_paths = (get_filepaths(dir_name))
    file_paths_segmented = [f.split('\\') for f in file_paths]
    file_segmented2 = []

    for i, f in enumerate(file_paths_segmented):
        files = []
        for fi in f:
            files.append(fi.replace('_',',').split(','))

        files = reduce(lambda a,b:a+b, files)
        files.insert(0,file_paths[i])
        file_segmented2.append(files)    
        myDict["File " + str(i)] = files
    return myDict

#Main simply stores the information in a CSV. This process will be turned into a seperate function
def main():
    
    #Fill the dir_name string manually to run in notebook
    if(dir_name == ''):
        if(len(sys.argv) != 2):
            print('Please specify a directory or Define "dir_path" in the code')   
        else:
            print(f"Created a CSV file named DataLabels.csv")
            data_frame = (pd.DataFrame.from_dict(data_to_labels(str(sys.argv[1])),orient='columns')).T
            data_frame.columns = ['File Path', 'Data Folder', 'Grid Number', 'Min X', 'Min Y', 'Max X', 'Max Y','Latitude','Longitude','Angle','File Name'] 
            data_frame.to_csv('DataLabels.csv')
    else:
            print(f"Created a CSV file named DataLabels.csv")
            data_frame = (pd.DataFrame.from_dict(data_to_labels(dir_name),orient='columns')).T
            data_frame.columns = ['File Path', 'Data Folder', 'Grid Number', 'Min X', 'Min Y', 'Max X', 'Max Y','Latitude','Longitude','Angle','File Name'] 
            data_frame.to_csv('DataLabels.csv')
    
if __name__=="__main__" :
    main()