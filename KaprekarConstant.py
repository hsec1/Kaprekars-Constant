def sortNum(num,sortMethod="asc"):
    rev = False
    if sortMethod == "desc": rev=True
    num = sorted(list(str(num)),key=int,reverse=rev)
    return int("".join(num))
def validateInput():
    while True:
        valid = True
        num=input("Enter a 4 digit number. There cannot be three of the same digits in the number: ")
        if len(num) != 4:
            print("That number is not four digits.  Please enter a number that is four digits")
        else:
            for n in num:
                if num.count(n) > 2:
                    print("That number had at least three of one digit. Please try again.")
                    valid = False
                    break
            if valid:
                return num

while True:
    num=validateInput()
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
    choice = input("Would you like to try again? (Y/N)")
    if choice in ["n","N"]:
        break
