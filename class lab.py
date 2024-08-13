class Laboratory:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def formatLabInfo(self):
        return f"{self.name}_{self.cost}"

    def enterLaboratoryInfo(self):
        self.name = input("Enter Laboratory Name: ")
        self.cost = input("Enter Laboratory Cost: ")

    def addLabToFile(self):
        self.enterLaboratoryInfo()
        with open("laboratories.txt", "a") as file:
            file.write(self.formatLabInfo() + "\n")

    def displayLabsList(self):
        with open("laboratories.txt", "r") as file:
            for line in file:
                print(line.strip())

    def writeListOfLabsToFile(self, labs):
        with open("laboratories.txt", "w") as file:
            for lab in labs:
                file.write("_".join(lab) + "\n")