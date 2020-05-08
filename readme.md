# Git Counting

A tool for graphing the word counts of a `.tex` document stored in a git repository.

Git Counting:
* Clones a git repo
* For each commit in the repo
 - Finds a given (tex) file
 - Runs texcount on it (pearl script from http://app.uio.no/ifi/texcount/)
 - Gets result and logs it with commit message and date
* Plots the date vs the word count
 - Every 10th data point includes its commit message

## Depends on

* Pearl
* Python3
* Pip (for the below)
* GitPython
 - pip3 install gitpython
* matplotlib
 - pip3 install -U matplotlib

## Usage

``python3 gitCounting.py --url <The URL of your repository> --file <File name you wish to word count>``

The parameter for ``--url`` should be the url you'd use to clone the repository, and ``--file`` should be the 'main' tex file of your document.

## To Do

* Script to install dependancies
* Make program clean up (after counting or on command, or both?)
* Generalise to count other document types
  - Other text documents
  - Lines of Code
