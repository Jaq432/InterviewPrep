
# 1. get a list of each IP address and the number of times they appear in the logs
# 2. list out the top 5 occurred IP addresses
# 3. get a list of the number of successful HTTP hits in each hour


def logFileLineSplitter(logLine):
    # Look through the log and pull out information
    # List out the attributes we will be stripping from the line
    ipAddress = logLine.split(" ")[0]
    timeStamp = logLine[logLine.find("[")+1:logLine.find("]")]
    httpRequest = logLine.split('"')[1]
    httpResponseCode = logLine.split(" ")[8]
    osOfRequester = logLine.split('"')[-2:]
    arrayOfItems = []
    arrayOfItems.extend([str(ipAddress),
                         str(timeStamp),
                         str(httpRequest),
                         str(httpResponseCode),
                         str(osOfRequester)])
    
    '''
    print(ipAddress)
    print(timeStamp)
    print(httpRequest)
    print(httpResponseCode)
    print(osOfRequester)
    '''
    return arrayOfItems




def main():

    # Make some space :P
    for i in range(25):
        print("*")

    logFileData = []
    with open("./logFile_test.txt", "r") as logFile:
        for line in logFile:
            # 0 - ipAddress
            # 1 - timeStamp
            # 2 - httpRequest
            # 3 - httpResponseCode
            # 4 - osOfRequester
            logFileData.append(logFileLineSplitter(line))

    ipAddressHits = {}

    # Objective 1 
    for log in logFileData:
        # Capture all unique IP addresses and their count
        if log[0] in ipAddressHits:
            ipAddressHits[log[0]] += 1
        else:
            ipAddressHits[log[0]] = 1

    # Objective 2
    # Sort the IP address counts in descending order
    sortedIPAddressHits = sorted(ipAddressHits.items(), key=lambda x:x[1], reverse=True)

    topFiveIPAddresses = {}
    
    for i in range(5):
        formattedIPInfo = str(sortedIPAddressHits[i]).replace("(","").replace("'","").replace(")","").split(",")
        topFiveIPAddresses[formattedIPInfo[0]] = formattedIPInfo[1]

    print(topFiveIPAddresses)
    
    # Objective 3
    '''
    timeStampDay = 
    timeStampMonth
    timeStampYear
    timeStampHour
    timeStampMinute
    timeStampSecond
    for log in logFileData:
    '''

    
main()