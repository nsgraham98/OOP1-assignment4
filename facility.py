class facility:
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def addFacility():
        f = input("What facility would you like to add?")
        newf = facility(f)
        facilities = facility.readFacilitiesFile()
        facilities.append(newf)
        facility.writeListOffacilitiesToFile(facilities)
        

    @staticmethod
    def displayFacilities():
        facilities = facility.readFacilitiesFile()
        for f in facilities:
            print(f.name)

    
    @staticmethod
    def writeListOffacilitiesToFile(facilities):
        f_obj = open('files/facilities.txt', 'w')
        f_obj.write("Hospital Facilities are: \n")
        for f in facilities:
            f_obj.write(f.name + "\n")
        f_obj.close()

    @staticmethod
    def readFacilitiesFile():
        facilities = []
        #Open the doctor file
        f_obj = open('files/facilities.txt', 'r')
        line = f_obj.readline()

        while line != '':
            if line != 'Hospital  Facility are:\n':
                #fill doctors into a list
                f = facility(line)
                facilities.append(f)
            line = f_obj.readline()
        f_obj.close()
        return(facilities)
    
#facility.displayFacilities()

facility.addFacility()
facility.displayFacilities()