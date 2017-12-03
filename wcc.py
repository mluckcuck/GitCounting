import git, os, shutil, subprocess, time
from git import Repo

print("+++ Begin +++")

DIR_NAME = "thesis-temp"
REMOTE_URL = "https://ml881:Mercian1588@bitbucket.org/ml881/thesis.git"
FILENAME = "thesis.tex"


def makeNewDir(name):
	print("+++ Making Directory", name ,"+++")
	
	if os.path.isdir(DIR_NAME):
		shutil.rmtree(DIR_NAME)
		
	os.mkdir(DIR_NAME)

	 
def wordCount():
	""" Counts the words in the file given by FILENAME"""
	# Runs the included pearl script to count the words
	rootDir = DIR_NAME + "/Big T/"
	fileAddress = rootDir + FILENAME
	pipe = subprocess.run(["perl", "texcount/texcount.pl" , "-total" , "-merge" ,  "-out=count.txt", "-dir=" + rootDir ,fileAddress])

	
	# Parse output
	file = open("count.txt")
	contents = file.read().splitlines()

	for c in contents:
		if c.startswith("Words in text:"):
			split = c.split(": ")
			return split[1]
	

#makeNewDir(DIR_NAME)

#r = git.Repo.clone_from(REMOTE_URL, DIR_NAME)

wc = wordCount()

## Next, get the date and commit message from this  commit

repo = Repo(DIR_NAME)

headcommit = repo.head.commit

name = headcommit.message


time.asctime(time.gmtime(headcommit.committed_date))
commitTime = time.strftime("%a, %d %b %Y %H:%M", time.gmtime(headcommit.committed_date))



## Bank this along with the wordCount

print(wc)
print(name)

print(commitTime)

## Go back one commit and do again



## list(repo.iter_commits('master', max_count=50))

print ("+++ DONE +++")
