import time
import wccRepo
import wccCount
import wccPlot
import json
#import argparse

startTime = time.time()
print("+++ Begin +++")

#parser = argparse.ArgumentParser()
#parser.add_argument("--url", help="The URL of your repository")
#parser.add_argument("--file", help="File name you wish to word count")
#args = parser.parse_args()

#urlArg = args.url
#searchName = ''
#if args.searchName:
#     searchName = args.searchName


DIR_NAME = ".thesis-temp"
REMOTE_URL = "https://ml881:Mercian1588@bitbucket.org/ml881/thesis.git"
FILENAME = "thesis.tex"
TEMP_FILE = ".count.txt"
DATA_FILE = FILENAME + "-data.json"

wccRepo.makeNewDir(DIR_NAME)
wccRepo.cloneRepo(REMOTE_URL, DIR_NAME)

dataList = wccCount.buildDataList(DIR_NAME, FILENAME, TEMP_FILE)
jsonDataFile = open(DATA_FILE, "w")
json.dump(dataList, jsonDataFile)
print(jsonDataFile)
jsonDataFile.close()
completeTime = round(time.time() - startTime, 2)
print ("+++ DONE (" + str(completeTime) + " seconds) +++")
wccPlot.plotData(DATA_FILE)
