import time
import gitCountingRepo
import gitCountingCount
import gitCountingPlot
import json
import argparse

startTime = time.time()
print("+++ Begin +++")

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="The URL of your repository")
parser.add_argument("--file", help="File name you wish to word count")
#Disabled
#parser.add_argument("--annotate", help="Flag; if presenet, then display the commit message of every 10th commit", action='store_true')
args = parser.parse_args()

REMOTE_URL = args.url
FILENAME = args.file
ANNOTATE = False # args.annotate


#REMOTE_URL = "https://ml881:Mercian1588@bitbucket.org/ml881/thesis.git"
#FILENAME = "thesis.tex"
DIR_NAME = "."+FILENAME+"-temp"
TEMP_FILE = ".count.txt"
DATA_FILE = FILENAME + "-data.json"

gitCountingRepo.makeNewDir(DIR_NAME)
gitCountingRepo.cloneRepo(REMOTE_URL, DIR_NAME)

dataList = gitCountingCount.buildDataList(DIR_NAME, FILENAME, TEMP_FILE)
jsonDataFile = open(DATA_FILE, "w")
json.dump(dataList, jsonDataFile)

jsonDataFile.close()
completeTime = round(time.time() - startTime, 2)
print ("+++ DONE (" + str(completeTime) + " seconds) +++")
gitCountingPlot.plotData(DATA_FILE, FILENAME, ANNOTATE)
