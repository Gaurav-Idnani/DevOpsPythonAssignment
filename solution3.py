from flask import Flask,jsonify
import re
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
        for config in listOfConfigs:
            for key in config:
                if key == "configName":
                    fileObj.write (config[key]+":\n")
                else:
                    fileObj.write ("- "+key+": "+config[key]+"\n")    
    
    return jsonify(listOfConfigs)
    

   

app.run()