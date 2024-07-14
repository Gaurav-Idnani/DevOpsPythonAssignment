# Q3. In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.
# ●  The program should read a configuration file (you can provide them with a sample configuration file).
# ●  It should extract specific key-value pairs from the configuration file.
# ●  The program should store the extracted information in a data structure (e.g., dictionary or list).
# ●  It should handle errors gracefully in case the configuration file is not found or cannot be read.
# ●  Finally save the output file data as JSON data in the database.
# ●  Create a GET request to fetch this information.

# Sample Configuration file: 

# [Database]
# host = localhost
# port = 3306
# username = admin
# password = secret

# [Server]

# address = 192.168.0.1
# port = 8080

# Sample Output: 
# Configuration File Parser Results:
# Database:

# - host: localhost
# - port: 3306
# - username: admin
# - password: secret

# Server:

# - address: 192.168.0.1
# - port: 8080 


from flask import Flask,jsonify
import re
import json
app = Flask(__name__)

@app.route('/')
def baseRoute():
    print ("Configuration Management automater is now active")

@app.route('/generateConfigReport', methods=['GET'])
def configFileParse():
    metaPattern = r'^\[.*\]$'
    dataPattern = r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.*)\s*$'
    listOfConfigs = []
    individualConfig={}
    try:
        with open('sampleConfigFile.txt', 'r') as fileObject:
            for line in fileObject:
                if re.match(metaPattern, line):
                    print ("meta pattern matched")
                    if (individualConfig != {}):
                        listOfConfigs.append(individualConfig)
                    individualConfig={}
                    individualConfig={"configName":line[1:-2]}
                elif re.match(dataPattern , line):
                    print ("data pattern matched")
                    propertyName = line.split('=')[0].strip()
                    propertyValue = line.split('=')[1].strip()
                    individualConfig[propertyName] = propertyValue
    except Exception as ex:
        return "We ran into an error while reading the file and parsing the data."
    print ("listOfConfigs:")
    listOfConfigs.append(individualConfig)
    print (listOfConfigs)
    with open('configReportFile.txt', 'w') as fileObj:
        fileObj.write ("Configuration File Parser Results:\n")
        json.dump(listOfConfigs,fileObj)
    
    returnStr=''
    for config in listOfConfigs:
        for key in config:
            if key == "configName":
                returnStr+= (config[key]+":<br/>")
            else:
                returnStr+= ("- "+key+": "+config[key]+"<br/>")    
    
    return returnStr
    

   

app.run()