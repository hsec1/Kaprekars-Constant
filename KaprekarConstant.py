def sortNum(num,sortMethod="asc"):
    rev = False
    if sortMethod == "desc": rev=True
    num = sorted(list(str(num)),key=int,reverse=rev)
    return int("".join(num))

num=input("Enter a 4 digit number. There cannot be three of the same letter the number: ")
startFNum= sortNum(num,"desc")
tmpResult = None
lastResult=None
for i in range(1,150):
    print("{} loops".format(i))
    if tmpResult:
        startFNum = sortNum(tmpResult,"desc")
    ascFnum = sortNum(startFNum)
    print("Start number:{},second number {}. So {}-{}".format(startFNum,ascFnum,startFNum,ascFnum))
    tmpResult = startFNum-ascFnum
    print("Result is {}".format(tmpResult))
    if tmpResult == lastResult:
        print("Kaprekars constant found")
        break
    lastResult = tmpResult
        
