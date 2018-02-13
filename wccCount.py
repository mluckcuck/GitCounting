""" wccCount Counts the words in a given file in each commit of a given
git repo (remote or local) and outputs the data to a local file
"""
import subprocess
import os
from datetime import date
from git import Repo

def findFileAddress(currentDir, fileName):
    """Finds the full address of the (first) file that has the right name """

    for root, dirs, files in os.walk(currentDir):
        if fileName in files:
            return root, os.path.join(root, fileName)


def wordCount(repoDir, fileName, tempFile):
    """ Counts the words in the file, fileName using the included Pearl script """

    rootDir,fileAddress = findFileAddress(repoDir, fileName)

    subprocess.run(["perl", "texcount/texcount.pl", "-total", "-merge",
                    "-out=" + tempFile, "-dir=" + rootDir, fileAddress])

    # Parse output
    file = open(tempFile)
    contents = file.read().splitlines()

    #Bit of a hack
    for c in contents:
        if c.startswith("Words in text:"):
            split = c.split(": ")
    return int(split[1])


def extractDataFromCommit(repoDir, commit, fileName, tempFile):
    """ Returns the time, message, and word count from the commit """

    print("+++ Extracting Data From Commit +++")

    commitTime = (date.fromtimestamp(commit.committed_date))

    commitMessage = commit.message

    commitWordCount = wordCount(repoDir, fileName, tempFile)

    return (commitTime, commitMessage, commitWordCount)


def buildDataList(repoDir, fileName, tempFile):
    """ Builds a ditionary of three lists: wordCounts, commitDates, and commitMsgs """

    print("+++ Build Data List +++")
    dataLists = {"wordCounts": [], "commitDates": [], "commitMsgs": []}

    repo = Repo(repoDir)
    git = repo.git

    for commit in list(repo.iter_commits('master', max_count=3)):
        git.checkout(commit)
        commitTuple = extractDataFromCommit(repoDir, commit, fileName, tempFile)
        dataLists["commitDates"].append(str(commitTuple[0]))
        dataLists["commitMsgs"].append(commitTuple[1])
        dataLists["wordCounts"].append(commitTuple[2])

        print(commitTuple[0], commitTuple[2])
        print("+++ Next +++")

    #Quick cleanup
    git.checkout(repo.head.commit)
    print(dataLists)
    return dataLists
