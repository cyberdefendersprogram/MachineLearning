"""
Created on Mon Jul 30 15:39:02 2018

@author: Cyber Defenders - Team Aladdin
"""


import json
import csv
import os


# Define feature header
result = [['FileName', 'SectionAlignment', 'FileAlignment', 'SizeOfHeaders', 'TimeDateStamp', 'ImageBase', 'SizeOfImage', 'SizeOfHeaders', 'DllCharacteristics', 'Characteristics', 'HighEntropy', 'LowEntropy', 'TotalSuspiciousSections', 'TotalNonSuspiciousSections']]

# Define standard sections
standardSection = ['.text', '.rdata', '.data', '.rsrc']

# This function is to check if an element exist in a list
def checkExist(listSection, ele):
    for item in listSection:
        if item == ele:
            return True
    return False
# Define the path of the folder which contain json files
path = 'zeus'


for filename in os.listdir(path):
    file = open("./"+path+"/"+filename, 'r') 
    
    for line in file:
        j = json.loads(line)
        
        # HighEntropy and LowEntropy Extraction
        highEntropy = 0
        lowEntropy = 0
        highest = 0
        lowest = 8
        for item in j['PE Sections']:
            if item['Entropy'] < lowest:
                lowest = item['Entropy']
            if item['Entropy'] > highest:
                highest = item['Entropy']

        if highest > 7:
            highEntropy = 1
        if lowest < 1:
            lowEntropy = 1

        # TotalSuspiciousSections and TotalNonSuspiciousSections extraction
        numberSuspicious = 0
        numberNonSuspicious = 0
        for item in j['PE Sections']:
            if checkExist(standardSection, item['Name']['Value']):
                numberNonSuspicious += 1
            else:
                numberSuspicious += 1

    
        #SectionAlignment Extraction
        sectionAlignment = j['OPTIONAL_HEADER']['SectionAlignment']['Value']
        
        #FileAlignment Extraction
        fileAlignment = j['OPTIONAL_HEADER']['FileAlignment']['Value']
        
        # SizeOfHeaders Extraction
        sizeOfHeader = j['OPTIONAL_HEADER']['SizeOfHeaders']['Value']
        
        timeStamp = j['FILE_HEADER']['TimeDateStamp']['Value']
        
        # ImageBase Extraction
        imageBase = j['OPTIONAL_HEADER']['ImageBase']['Value']
        
        # SizeOfImage Extraction
        sizeOfImage = j['OPTIONAL_HEADER']['SizeOfImage']['Value']
        
        #SizeOfHeaders Extraction
        sizeOfHeaders = j['OPTIONAL_HEADER']['SizeOfHeaders']['Value']
        
        #DllCharacteristics Extraction
        dllCharacteristics = j['OPTIONAL_HEADER']['DllCharacteristics']['Value']
        
        # Characteristics Extraction
        characteristics = j['FILE_HEADER']['Characteristics']['Value']
        
        row = [filename, sectionAlignment, fileAlignment, sizeOfHeader, timeStamp, imageBase, sizeOfImage, sizeOfHeaders, dllCharacteristics, characteristics, highEntropy, lowEntropy, numberSuspicious, numberNonSuspicious]
        # print(row)
        result.append(row)
    
with open('Zeus.csv', 'w+', newline='') as f:
    thewriter = csv.writer(f)
    
    thewriter.writerows(result)
    
    
    
        
    
    
