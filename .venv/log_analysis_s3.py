#This code downloads a log file present in an s3 bucket and performs log analysysis on it. It uses the boto3 library to interact with AWS S3 service.

from collections import Counter

import boto3
import re


s3=boto3.client('s3')
file_name='log_file.log'
with open(file_name,'wb') as f:
     s3.download_fileobj('demo-bucket-1987687', 'log_file.log', f)#download the log file from s3 bucket and save it locally

error_pattern=re.compile(r'^(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2},\d{3} - ERROR (.+))') #compile a regular expression pattern to search for 'ERROR' in the log file
error_list=[]
with open(file_name,'r') as f: #open the downloaded log file and read it line by line
     for line in f:
           match=error_pattern.search(line) #search for the pattern in each line
           if(match):  
                    timestamp, error_message = match.groups() #if a match is found, extract the timestamp and error message
                    error_list.append(error_message)
error_counter=Counter(error_list)

for error,count in error_counter.items():
      print(f'{error}: {count} occurences') #print the error message and its count




