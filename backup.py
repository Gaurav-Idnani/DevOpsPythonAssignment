# Q4. In DevOps, performing regular backups of important files is crucial:

# Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.
# The script should copy all files from the source directory to the destination directory.
# Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.
# Handle errors gracefully, such as when the source directory or destination directory does not exist.

# Sample Command:
# python backup.py /path/to/source /path/to/destination
# By running the script with the appropriate source and destination directories.
# It should create backups of the files in the source directory, ensuring unique file names in the destination directory.

import os
import glob
import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description='Read files from two directories.')
    parser.add_argument('srcDir', type=str, help='The path to the source directory.')
    parser.add_argument('desDir', type=str, help='The path to the destination directory.')
    args = parser.parse_args()

   
    if (checkDirectoryValidity(args.srcDir , 'Read')):
        if (checkDirectoryValidity(args.desDir , 'Write')):
            filesInDestinationDirectory = readDestinationDirectoryFiles(args.desDir)
            print(f"Reading files from source directory: {args.srcDir}")
            sourceFileDictionary = readSourceDirectoryFiles(args.srcDir )
            print ("****************************************************")
            
            if not sourceFileDictionary:
                print ("No Files found in source directory to copy")
            else:
                print ("Following Files were found in the source Directory:")
                print (sourceFileDictionary.keys())
                print ("****************************************************")
                print ("Proceeding to write the files to destination directory")
                writeFilesToDestinationDirectory (sourceFileDictionary , filesInDestinationDirectory ,args.desDir)
                print ("****************************************************")
                print ("Write Operation Completed")
        else:
            print ("We Did not find the destination directory in the system or you do not have access to the directory.Please check the path provided")
    else:
        print ("We Did not find the source directory in the system or you do not have access to the directory.Please check the path provided")
def readSourceDirectoryFiles(sourceDirectory):
    fileDictionary={}
    files = glob.glob(os.path.join(sourceDirectory, '*'))
    for filePath in files:
        if os.path.isfile(filePath):
            fileName = filePath.split('\\')[1]
            with open(filePath, 'r') as file:
                fileContent = file.read()
                fileDictionary[fileName] = fileContent
    return fileDictionary

def writeFilesToDestinationDirectory (sourcefileDictionary , filesInDestinationDirectory , destinationDirectory):
    for fileName, fileContent in sourcefileDictionary.items(): 
        fileNameToWrite = fileName
        if fileName in filesInDestinationDirectory:
            lastIndexOfDot = fileNameToWrite.rfind('.')
            fileNameToWrite = fileNameToWrite[:lastIndexOfDot]+datetime.now().strftime('%Y%m%d%H%M%S')+fileNameToWrite[lastIndexOfDot:]
        
        filePathToWrite = destinationDirectory + '\\'+fileNameToWrite
        with open(filePathToWrite, 'w') as file:
            file.write(fileContent)

def checkDirectoryValidity(dirToCheck , accessLevel):
    if accessLevel == 'Read': 
        accessCheck = os.access(dirToCheck, os.R_OK) 
    else:
        accessCheck = os.access(dirToCheck, os.W_OK) 
    if os.path.isdir(dirToCheck) and accessCheck :
        return True
    else:
        return False
    

def readDestinationDirectoryFiles(destinationDirectory):
    filesInDestinationDirectory=set()
    files = glob.glob(os.path.join(destinationDirectory, '*'))
    for filePath in files:
        print (f"filePath: {filePath}")
        if os.path.isfile(filePath):
            filesInDestinationDirectory.add(filePath.split('\\')[1])
    
    return filesInDestinationDirectory
                


if __name__ == '__main__':
    main()


