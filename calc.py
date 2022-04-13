    # C:\\Users\\pauli\\Desktop\\"+local
def openFile():
        #The local of the file is the desktop
        local = input("Name of the file:")
        file = open(local)
        mathThings(file)

        #Check if the local is correct
        control = input("The file is correct? Y/N")
        if control == "Y" or control == "y":
            mathThings(file)
        else: openFile()


def mathThings(file):
    #method that makes all the math things
        errorcount = 0
        filter = []
        content = file.read().split()

        for var in content:
            try:
                converted = int(var)
                if converted < 30:
                    filter.append(converted)
                else: errorcount += 1
            except:
                errorcount += 1

        if len(filter) == 0:
            print("Error")


        print(str(len(content)) + " numbers was computed")
        for num in range(30):
            print("The number "+str(num) + " appears: " + str(filter.count(num)))
        
            
openFile()

