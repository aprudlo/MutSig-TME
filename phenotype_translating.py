import pandas as pd
import os
import numpy as np
import re
import argparse


def parse():

    parser=argparse.ArgumentParser()

    parser.add_argument("-i", "--INPUT", help="directory path to a file with input data", required=True)
    parser.add_argument("-o", "--OUTPUT", help="directory path to an output file or a folder where the output file will be created", required=True)
    parser.add_argument("-d", "--DICTIONARY", help="directory path to a phenotype dictionary file", required=True)
    
    args=parser.parse_args()
    
    return args

def main():

    arguments=parse() # parsing arguments
    path_file=arguments.INPUT # input directory
    output=arguments.OUTPUT # output directory
    path_dictionary=arguments.DICTIONARY # dictionary directory

    data=pd.read_csv(path_file, sep='\t') # data from phenotype_counting
    dict=pd.read_csv(path_dictionary) # phenotype dictionary

    keys=dict['phenotype'] # available phenotypes in the dictionary
    values=(dict['celltype']) # available cell types in the dictionary

    dictionary={} # python dictionary for translating
    for i in range (len(keys)):
        dictionary[keys[i]]=values[i]


    sample=keys[0] # example phenotype pattern in dictionary
    slices=re.split(r'[+-]', sample[:-1]) # components of keys in dictionary


    for phenotype in data.columns[1:]: 
        real_phenotype=''
        order=[]

        for slice in slices: # finding the order of each key component in the data
            slice_span=re.search(slice, phenotype)
            order.append(slice_span.span())

        for pair in order: # creating real phenotypes from the order of each component
            real_phenotype+=phenotype[pair[0]:(pair[1]+1)]
        data.rename(columns={phenotype:real_phenotype}, inplace=True)

    
    data.rename(columns=dictionary, inplace=True) # translating the phenotypes
    data=data.T.groupby(level=0, sort=False).sum().T # grouping columns with the same name

    if os.path.isdir(output): # if output argument is a path not a file
        output=os.path.join(output, "phenotype_translating_result.tsv") # default resullt file name

    data.to_csv(output, sep="\t") # result file   


if __name__=='__main__':
    main()