""" wccPlot Plots the given data using matplotlib """

import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
import json


def loadFromFile(fileName):

    print("Load from", fileName)
    jsonFile = open(fileName, "r")
    print(jsonFile)

    jsonData = json.load(jsonFile)

    dataTuple = (jsonData["commitDates"], jsonData["wordCounts"], jsonData["commitMsgs"])

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

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot_date(dateList, data[1], "o-", xdate=True)
    #annotate every thenth point with it's commit message
    for x, y, label in zip(dateList, data[1], data[2][0:len(data[2]):10]):
        ax.annotate(label, xy=(x, y), textcoords='data')

    plt.xlabel('Date')
    plt.ylabel('Word Count')
    plt.title("Thesis Word Count")
    plt.show()
