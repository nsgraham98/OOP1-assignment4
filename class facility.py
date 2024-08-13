class Facility:
    def __init__(self, name):
        self.name = name

    def addFacility(self):
        self.name = input("Enter Facility Name: ")
        with open("facilities.txt", "a") as file:
            file.write(self.name + "\n")

    def displayFacilities(self):
        with open("facilities.txt", "r") as file:
            for line in file:
                print(line.strip())

    def writeListOfFacilitiesToFile(self, facilities):
        with open("facilities.txt", "w") as file:
            for facility in facilities:
                file.write(facility + "\n")