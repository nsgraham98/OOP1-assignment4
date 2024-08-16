class Laboratory:
    def __init__(self, name, cost):
        self._name = name
        self._cost = cost
    
    def get_name(self):
        return self._name
    def get_cost(self):
        return self._cost
    
    def set_name(self, name):
        self._name = name
    def set_cost(self, cost):
        self._cost = cost

    #Adds and writes the lab name to the file in the format of the data that is in the file
    @staticmethod
    def addLabToFile(lab_obj): #requires a single lab_object
        file = open("files/laboratories.txt", "a")
        file.write(f'\n{Laboratory.formatLabInfo(lab_obj)}')
        file.close()

    #  Writes the list of labs into the file laboratories.txt
    @staticmethod
    def writeListOfLabsToFile(full_lab_list): #requires the full list of all lab_objects
        file = open("files/laboratories.txt", "w")
        file.write(f"Laboratory_Cost\n")
        for lab_obj in full_lab_list:
            file.write(f'{Laboratory.formatLabInfo(lab_obj)}\n')
        file.close()
    
    # Displays the list of laboratories
    def displayLabsList():
        full_lab_list = Laboratory.readLaboratoriesFile()
        print(f'{"Lab":<20}{"Cost":<}\n')
        for lab_obj in full_lab_list:
            print(f'{lab_obj._name:<20}{lab_obj._cost:<}\n')

    # Formats the Laboratory object similar to the laboratories.txt file
    @staticmethod
    def formatLabInfo(lab_obj): #requires a single lab_object, returns formatted string of said lab_object
        temp_list = [lab_obj._name, lab_obj._cost]
        temp_list[1] = str(temp_list[1])
        separ = "_"
        formatted_lab_string = separ.join(temp_list)
        return formatted_lab_string
    
    # enterLaboratoryInfo Asks the user to enter lab name and cost and forms a Laboratory object
    @staticmethod
    def enterLaboratoryInfo():
        lab_obj = Laboratory(input("Enter new Lab name: "), int(input("Enter the cost of the new Lab: $")))
        Laboratory.addLabToFile(lab_obj)

    # Reads the laboratories.txt file and fills its contents in a list of Laboratory objects
    @staticmethod
    def readLaboratoriesFile(): #returns full list of all lab_objects
        full_lab_list = []
        file = open("files/laboratories.txt", "r")
        file.readline()
        line = file.readline().rstrip()

        while line != "":
            lab_list = line.split("_")
            lab_obj = Laboratory(lab_list[0],int(lab_list[1]))
            full_lab_list.append(lab_obj)
            line = file.readline().rstrip()

        file.close()
        return full_lab_list
