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
* git
* matplotlib

## To Do

* Script to install dependancies
* Generalise to count other document types
  - Other text documents
  - Lines of Code
