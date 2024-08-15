class laboratory:
    def __init__(self, labName, cost):
        self.labName = labName
        self.cost = cost

    @staticmethod
    def addLabToFile(laboratory):
        laboratories = laboratory.readLaboratoriesFile()
        laboratories.append(laboratory)
        laboratory.writeListOfLabsToFile(laboratories)

    @staticmethod
    def writeListOfLabsToFile(laboratories):
        f_obj = open('files/laboratories.txt', 'w')
        for l in laboratories:
            f_obj.write(laboratory.formatLabInfo(l))
        f_obj.close()

    @staticmethod
    def displayLabsList():
        labs = laboratory.readLaboratoriesFile()
        for l in labs:
            print(l.labName + "\t\t" + l.cost)

    @staticmethod
    def formatLabInfo(laboratory):
        return laboratory.labName +"_"+ laboratory.cost+"_"+ "\n"
    
    @staticmethod
    def enterLaboratoryInfo():
        n = input("Input Lab name")
        c = input("Input Lab cost")
        return laboratory(n,c)
       
    @staticmethod
    def readLaboratoriesFile():
        laboratories = []
        #Open the labratory file
        f_obj = open('files/laboratories.txt', 'r')
        line = f_obj.readline()

        while line != '':
            if line != 'Laboratory_Cost\n':
                #fill laboratories into a list
                tlist = line.rstrip().split("_")
                l = laboratory(tlist[0], tlist[1])
                laboratories.append(l)
            line = f_obj.readline()
        f_obj.close()
        return(laboratories)
    
    
#1 display doctors list
laboratory.displayLabsList()

#4 add dr
'''d = laboratory.enterLaboratoryInfo()
laboratory.addLabToFile(d)
laboratory.displayLabsList()'''




