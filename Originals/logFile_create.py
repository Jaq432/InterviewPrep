import random

logstringArray = []
httpResonseList = [100,200,300,400,500]

# Generate 500 items into the array
for x in range(500):
    # Generate random values for the array
    generatedFirstIp = str(192)
    generatedSecondIp = str(168)
    generatedThirdIp = str(42)
    generatedFourthIp = str(random.randint(1,254))
    #generatedDay = str(random.randint(0,31))
    generatedDay = 12
    generatedHour = str(random.randint(0,24))
    generatedMinute = str(random.randint(0,60))
    generatedSecond = str(random.randint(0,60))
    generatedProductNumber = str(random.randint(1,9))
    generatedHttpResponse = str(random.choice(httpResonseList))

    # Add all of the generated rows into the array 
    logstringArray.append(generatedFirstIp+"."+generatedSecondIp+"."+generatedThirdIp+"."+generatedFourthIp+" - - ["+generatedDay+"/May/2015:"+generatedHour+":"+generatedMinute+":"+generatedSecond+' +0000] "GET /downloads/product_'+generatedProductNumber+' HTTP/1.1" '+generatedHttpResponse+' 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"'+"\n")

with open("./logFile_test.txt", "w") as logFile:
    for log in logstringArray:
        logFile.write(str(log))
