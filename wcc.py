import git, os, shutil, subprocess, time
from datetime import date 
from git import Repo
import matplotlib
import matplotlib.pyplot as plt

startTime = time.time()
print("+++ Begin +++")

DIR_NAME = ".thesis-temp"
REMOTE_URL = "https://ml881:Mercian1588@bitbucket.org/ml881/thesis.git"
FILENAME = "thesis.tex"
TEMP_FILE = ".count.txt"



def makeNewDir(name):
	print("+++ Making Directory", name ,"+++")

	if not os.path.exists(name):

		print("+++ Made It +++")
		os.makedirs(name)
	else:
		print("+++ Dir",name,"Already Exists +++" )
		
	print("+++ Continue +++")

	
def cloneRepoInto(directory):

	print("+++ Cloning Repo +++")

	assert os.path.exists(directory)

	if not os.path.exists(directory+"/.git"):
		
		git.Repo.clone_from(REMOTE_URL, directory)
		print("+++ Repo Cloned +++")
	else:
		print("+++ Repo Exists +++")

	print("+++ Continue +++")

	
## THIS IS ONLY CHECKING THE WC OF THE HEAD COMMIT EACH TIME!!!
def wordCount():
	""" Counts the words in the file given by FILENAME"""
	# Runs the included pearl script to count the words
	rootDir = DIR_NAME + "/Big T/"
	fileAddress = rootDir + FILENAME
	pipe = subprocess.run(["perl", "texcount/texcount.pl" , "-total" , "-merge" ,  "-out="+TEMP_FILE, "-dir=" + rootDir ,fileAddress])

	
	# Parse output
	file = open(TEMP_FILE)
	contents = file.read().splitlines()

	for c in contents:
		if c.startswith("Words in text:"):
			split = c.split(": ")
			return split[1]
	


def extractDataFromCommit(commit):

	print("+++ Extracting Data From Commit +++")
	
		
	commitTime = (date.fromtimestamp(commit.committed_date))

	commitMessage = commit.message

	commitWordCount = wordCount()
	
	return (commitTime, commitMessage, commitWordCount)


def buildDataList():

	print("+++ Build Data List +++")
	dataLists = ([],[])

	makeNewDir(DIR_NAME)

	cloneRepoInto(DIR_NAME)
		
	
	repo = Repo(DIR_NAME)
	git = repo.git

	for commit in list(repo.iter_commits('master', max_count=3)):

		
		git.checkout(commit)
		commitTuple = extractDataFromCommit(commit)
		dataLists[0].append(commitTuple[0])
		dataLists[1].append(commitTuple[2])

		print(str(commitTuple[0]) + "  " + commitTuple[2])
		print("+++ Next +++")

	#Quick cleanup
	git.checkout(repo.head.commit)
	return dataLists

def plotData(data):

	
	dates = matplotlib.dates.date2num(data[0])
	
	plt.plot_date(dates,data[1], "o-", xdate=True)
	plt.xlabel('Date')
	plt.ylabel('Word Count')	
	plt.title("Thesis Word Count")
	plt.show()




dataList = buildDataList()


completeTime = round(time.time() - startTime, 2)
print ("+++ DONE (",completeTime," seconds)+++")
plotData(dataList)
