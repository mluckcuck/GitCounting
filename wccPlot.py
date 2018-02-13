""" wccPlot Plots the given data using matplotlib """

import matplotlib
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
from ast import literal_eval as make_tuple
import json
import time


def loadFromFile(fileName):

    print("Load from", fileName)
    jsonFile = open(fileName, "r")
    print(jsonFile)

    jsonData = json.load(jsonFile)

    dataTuple = (jsonData["commitDates"], jsonData["wordCounts"])

    return dataTuple


def plotData(fileName):

    data = loadFromFile(fileName)

    dateStrings = data[0]
    dateList = []

    for d in dateStrings:

        dList = d.split("-")

        dtObj = datetime(int(dList[0]), int(dList[1]), int(dList[2]))

        dateList.append(dtObj)

    dateList = matplotlib.dates.date2num(dateList)

    plt.plot_date(dateList, data[1], "o-", xdate=True)
    plt.xlabel('Date')
    plt.ylabel('Word Count')
    plt.title("Thesis Word Count")
    plt.show()
