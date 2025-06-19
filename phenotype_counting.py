import pandas as pd
import os
import numpy as np
import re
import argparse


def parse():

    parser=argparse.ArgumentParser()

    parser.add_argument("-i", "--INPUT", help="directory path to a folder with input data", required=True)
    parser.add_argument("-o", "--OUTPUT", help="directory path to an output file or a folder where the output file will be created", required=True)
    
    args=parser.parse_args()
    
    return args


def main():

    arguments=parse() # parsing arguments
    input=arguments.INPUT # input directory
    output=arguments.OUTPUT # output directory
    
    result={} # result matrix 

    for filename in os.listdir(input): # list of files in the folder
        if re.match(r".*_properties_.*.tsv.gz", filename):   # filtering files to open
            
            file_path=os.path.join(input, filename)
            data=pd.read_csv(file_path,  compression='gzip', sep='\t')
            
            filter_data=data[data['in.ROI.tumor_tissue']==True] # filtering: only columns in ROI
            phenotype_counts=filter_data['phenotype'].value_counts() # counting phenotypes
            
            patient_ID=(re.search(r"[^-]*-[^-]*-[^-]*-", filename).group(0)[:-1]) # the first occurrence of three '-' it's patient's ID
            result[patient_ID]=phenotype_counts # adding new column (patient) to result matrix

    df=pd.DataFrame(result).fillna(0).astype(int).T # changing NaNs to 0, giving type Int to the values, transposing
    df.index.name = 'patient' # assigning name to the first column

    if os.path.isdir(output): # if output argument is a path not a file
        output=os.path.join(output, "phenotype_counting_result.tsv") # default resullt file name

    df.to_csv(output, sep="\t") # result file


if __name__=='__main__':
    main()