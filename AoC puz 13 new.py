with open("AoC puz 13 input.txt", "r") as f:
    rawData = f.read().replace('\n', ',')
splitData = list(rawData.split(','))

currentTime = int(splitData.pop(0))

def filterTimes(intervals):
    waitTimes = {}
    for interval in intervals:
        if interval != 'x':
            nextBus = int(timeStamp / int(interval))+int(interval) 
            waitTime = nextBus - currentTime
            waitTimes[waitTime] = interval
    waitList = list(waitTimes.keys())
    minimumWait = min(waitList)
    rightBus = int(waitTimes.get(minimumWait))
    answer = rightBus * minimumWait
    print (answer)
    
filterTimes(SplitData)

