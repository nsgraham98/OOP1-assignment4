class Facility:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name


    # Adds and writes the facility name to the file    
    @staticmethod      
    def addFacility(): #returns full list of all fac_objects (with the new one)
        fac_obj = Facility(input("Enter new facility name: "))
        full_fac_list = Facility.readFacilitiesFile()
        full_fac_list.append(fac_obj)

        Facility.writeListOfFacilitiesToFile(full_fac_list)

    @staticmethod
    def readFacilitiesFile(): #returns full list of all fac_objects
        full_fac_list = []
        file = open("files/facilities.txt", "r")
        file.readline()
        line = file.readline().rstrip()

        while line != "":
            fac_obj = Facility(line.rstrip())
            full_fac_list.append(fac_obj)
            line = file.readline()

        file.close()
        return full_fac_list

    # Displays the list of facilities
    @staticmethod
    def displayFacilies():
        full_fac_list = Facility.readFacilitiesFile()
        print("The Hospital Facilities are:\n")
        for fac_obj in full_fac_list:
            name = fac_obj._name
            print(f'{name}\n')

    # Writes the facilities list to facilities.txt
    @staticmethod
    def writeListOfFacilitiesToFile(full_fac_list):
        file = open("files/facilities.txt", "w")
        file.write(f"Hospital  Facility are:\n")
        for fac_obj in full_fac_list:
            file.write(f'{fac_obj._name}\n')
        
        file.close()
