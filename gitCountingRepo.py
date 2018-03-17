""" wccRepo Downloads a remote git repository and
makes a new directory for it, if required
"""

import git
import os


def makeNewDir(name):
    """ Makes a new directory, if needed """

    print("+++ Making Directory", name, "+++")

    if not os.path.exists(name):

        print("+++ Made It +++")
        os.makedirs(name)
    else:
        print("+++ Dir", name, "Already Exists +++")

        print("+++ Continue +++")


def cloneRepo(remoteUrl, directory):
    """ Clones the git repository from remoteURL into directory"""

    print("+++ Cloning Repository, Please Wait +++")
    assert os.path.exists(directory)

    if not os.path.exists(directory + "/.git"):
        git.Repo.clone_from(remoteUrl, directory)
        print("+++ Repo Cloned +++")
    else:
        print("+++ Repo Exists +++")

        print("+++ Continue +++")
