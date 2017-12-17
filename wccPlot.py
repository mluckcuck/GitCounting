""" wccPlot Plots the given data using matplotlib """

import matplotlib
import matplotlib.pyplot as plt
from datetime import date
import json


def loadFromFile(dataFile):

    print("Load from", dataFile)
    jsonFile = open(dataFile, "r")
    print(jsonFile)
    jsonData = json.load(jsonFile)

    dataTuple = (jsonData["commitDates"], jsonData["wordCounts"])

    return dataTuple


def plotData(dataFile):

    data = loadFromFile(dataFile)

    dateStrings = data[0]
    dateList = []

    for d in dateStrings:
        dateList.append(date.fromtimestamp(d))

    dateList = matplotlib.dates.date2num(dateList)

    plt.plot_date(dateList, data[1], "o-", xdate=True)
    plt.xlabel('Date')
    plt.ylabel('Word Count')
    plt.title("Thesis Word Count")
    plt.show()
