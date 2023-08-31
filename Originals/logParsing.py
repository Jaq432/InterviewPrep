# The goal was to get different information about a log file which contained 500
# entries which look like the one below
# 
# Assignment Details
# Objective 1. get a list of each IP address and the number of times they appear in the logs
# Objective 2. list out the top 5 occurred IP addresses
# Objective 3. get a list of the number of successful HTTP hits in each hour

# Example format
# $remote_addr - $remote_user - [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"
# Example log entry
# 93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"

import random

logstringArray = []
httpResonseList = [100,200,300,400,500]

#logstring = '93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"'

# Generate 500 items into the array
for x in range(500):
    # Generate random values for the array
    generatedFirstIp = str(192)
    generatedSecondIp = str(168)
    generatedThirdIp = str(42)
    generatedFourthIp = str(random.randint(1,254))
    generatedDay = str(random.randint(0,31))
    generatedHour = str(random.randint(0,24))
    generatedMinute = str(random.randint(0,60))
    generatedSecond = str(random.randint(0,60))
    generatedProductNumber = str(random.randint(1,9))
    generatedHttpResponse = str(random.choice(httpResonseList))

    # Add all of the generated rows into the array 
    logstringArray.append(generatedFirstIp+"."+generatedSecondIp+"."+generatedThirdIp+"."+generatedFourthIp+" - - ["+generatedDay+"/May/2015:"+generatedHour+":"+generatedMinute+":"+generatedSecond+' +0000] "GET /downloads/product_'+generatedProductNumber+' HTTP/1.1" '+generatedHttpResponse+' 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"')

ipAddressCountingList = {}
successfulHttpPerHour = {}

for logstring in logstringArray:

    # Get all of the data from the log
    ipAddress = logstring[:logstring.find(" ")]
    day = logstring[logstring.find('['):logstring.find('/')]
    month = logstring.split('/')[1]
    year = logstring.split('/')[2][:logstring.split('/')[2].find(':')]
    hour = logstring.split(':')[1]
    minute = logstring.split(':')[2]
    second = logstring.split(':')[3][:logstring.split(':')[3].find(' ')]
    command = logstring.split('"')[1]
    httpResponse = logstring.split(" ")[8]
    operatingSystem = logstring.split('"')[5]

    # Objective 1
    if ipAddress in ipAddressCountingList:
        ipAddressCountingList[ipAddress] += 1
    else:
        ipAddressCountingList[ipAddress] = 1

    # Objective 3
    if int(hour) in successfulHttpPerHour:
        if httpResponse == str(200):
            successfulHttpPerHour[int(hour)] += 1
    else:
        successfulHttpPerHour[int(hour)] = 1

#print(successfulHttpPerHour)

#quit()
    
# Sort the IP address count list
ipAddressCountingList = sorted(ipAddressCountingList.items(), key=lambda x:x[1])

# Objective 2 Proof
print("Pos 1 IP address in logs " + str(ipAddressCountingList[-1]))
print("Pos 2 IP address in logs " + str(ipAddressCountingList[-2]))
print("Pos 3 IP address in logs " + str(ipAddressCountingList[-3]))
print("Pos 4 IP address in logs " + str(ipAddressCountingList[-4]))
print("Pos 5 IP address in logs " + str(ipAddressCountingList[-5]))

# Objective 3 Proof
successfulHttpPerHour = dict(sorted(successfulHttpPerHour.items()))
print("Below are the hour and successful http response count in that hour.")
for hour in successfulHttpPerHour:
    print(str(hour) + "," + str(successfulHttpPerHour[int(hour)]))