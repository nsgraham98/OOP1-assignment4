class Laboratory:
    def __init__(self, name, cost):
        self._name = name
        self._cost = cost
    
    #def get_name(self):
        #return self._name
    #def get_cost(self):
        #return self._cost
    
    #def set_name(self, name):
        #self._name = name
    #def set_cost(self, cost):
        #self._cost = cost

    @staticmethod
    def readLabFile():

        full_lab_list = []
        f_obj = open('laboratories.txt', 'r')
        line = f_obj.readline()

        while line != '':
            lab_data = line.rstrip().split('_')
            #lab = (lab_data[0], lab_data[1])
            lab = Laboratory(lab_data[0], str(lab_data[1]))
            full_lab_list.append(lab)
            line = f_obj.readline().rstrip()


        #with open('laboratories.txt', 'r') as file:
            #full_lab_list = []
           # for lines in file:
             #   lines = file.readlines()
          #      for line in lines:
          #          lab_data = line.strip().split('_')
          #          lab_name, lab_cost = (lab_data[0], lab_data[1])
           #         lab = Laboratory(lab_name, lab_cost)
           #         full_lab_list.append(lab)

        #file = open("laboratories.txt", "r")
        #line = file.readline().rstrip()

        #while line != "":
            #lab_list = line.split("_")
            #lab_obj = Laboratory(lab_list[0],int(lab_list[1]))
            #full_lab_list.append(lab_obj)
            #line = file.readline().rstrip()

        f_obj.close()
        return full_lab_list

    @staticmethod
    def formatLabInfo(lab_obj):
        temp_list = [lab_obj._name, lab_obj._cost]
        temp_list[1] = str(temp_list[1])
        separ = "_"
        formatted_lab_string = separ.join(temp_list)
        return formatted_lab_string + '\n'

    @staticmethod
    def displayLabsList():
        full_lab_list = Laboratory.readLabFile()
        for lab_obj in full_lab_list:
            print(f"{lab_obj._name:<20}{lab_obj._cost:<}")


    @staticmethod
    def addLabToFile():
        new_lab_list = []
        lab_obj = Laboratory.enterLaboratoryInfo()
        new_lab_list = Laboratory.readLabFile()
        new_lab_list.append(lab_obj)
        Laboratory.WriteListOfLabsToFile(new_lab_list)

    @staticmethod
    def enterLaboratoryInfo():
        lab_obj = Laboratory(input("Enter new Lab name: "), int(input("Enter the cost of the new Lab: $")))
        return lab_obj

    @staticmethod
    def WriteListOfLabsToFile(new_lab_list):
        file = open('laboratories.txt', 'w')
        for lab_obj in new_lab_list:
            file.write(Laboratory.formatLabInfo(lab_obj))
            

class Doctor:

    def __init__(self, id=0, name="", specialization="", working_time="", qualification="", room_number=0):
        self._id = id
        self._name = name
        self._specialization = specialization
        self._working_time = working_time
        self._qualification = qualification
        self._room_number = room_number
        self._doc_info = [id, name, specialization, working_time, qualification, room_number]

    @staticmethod
    def readDocFile():
        full_doc_list = []
        f_obj = open('doctors.txt', 'r')
        line = f_obj.readline()

        while line != '':
            doc_data = line.rstrip().split('_')
            docs = Doctor(str(doc_data[0]), doc_data[1], doc_data[2], doc_data[3], doc_data[4], doc_data[5])
            full_doc_list.append(docs)
            line = f_obj.readline().rstrip()

        f_obj.close()
        return full_doc_list

    @staticmethod
    def enterDocInfo():
        doc_obj = Doctor(int(input("Enter the doctor's ID: ")), input("Enter the doctor's name: "), input("Enter the doctor's specility: "), input("Enter the doctor's timing (e.g., 7am-10pm): "), input("Enter the doctor's qualification: "), int(input("Enter the doctor's room number: ")))
        return doc_obj

    @staticmethod
    def formatDocInfo(doc_obj):
        temp_list = doc_obj._doc_info
        temp_list[0] = str(temp_list[0])
        temp_list[5] = str(temp_list[5])
        separ = "_"
        formatted_doc_string = separ.join(temp_list)
        return formatted_doc_string + '\n'

    @staticmethod
    def displayDocList():
        full_doc_list = Doctor.readDocFile()
        for doc_obj in full_doc_list:
            Doctor.displayDocInfo(doc_obj)

    @staticmethod
    def displayDocInfo(doc_obj):
        temp_list = doc_obj._doc_info
        print(f'{temp_list[0]:<10}{temp_list[1]:<20}{temp_list[2]:<20}{temp_list[3]:<20}{temp_list[4]:<20}{temp_list[5]}')


    @staticmethod
    def writeListOfDoctorsToFile(new_doc_list):
        file = open('doctors.txt', 'w')
        for doc_obj in new_doc_list:
            file.write(Doctor.formatDocInfo(doc_obj))

    @staticmethod
    def addDocToFile():
        new_doc_list = []
        doc_obj = Doctor.enterDocInfo()
        new_doc_list = Doctor.readDocFile()
        new_doc_list.append(doc_obj)
        Doctor.writeListOfDoctorsToFile(new_doc_list)

    @staticmethod
    def searchDocById():
        doc_list = Doctor.readDocFile()
        id = input("Enter the doctors ID: ")
        for doc_obj in doc_list:
            if doc_obj._id == id:
                Doctor.displayDocInfo(doc_obj)
            else:
                print("Doctor does not exist")

    @staticmethod
    def searchDocByName():
        doc_list = Doctor.readDocFile()
        name = input("Enter the doctors name: ")
        for doc_obj in doc_list:
            if doc_obj._name == name:
                Doctor.displayDocInfo(doc_obj)
            else:
                print("Doctor does not exist")

    @staticmethod
    def editDocInfo():
        doctors = Doctor.readDocFile()
        id = input("Enter doctors ID: ")
        for d in doctors:
            if d._id == id:
                n = input("Input Dr. Name:")
                s = input("Input Dr. Specialty:")
                t = input("Input Dr. Time:")
                q = input("Input Dr. Qualification:")
                rn = input("Input Dr. Room number:")
                for i in range(len(doctors)):
                    if doctors[i]._id == id:
                        doctors[i]._name = n
                        doctors[i]._specialization = s
                        doctors[i]._working_time = t
                        doctors[i]._qualification = q
                        doctors[i]._room_number = rn
                Doctor.writeListOfDoctorsToFile(doctors)
        else:
            print("Dr. not found")
        
Doctor.editDocInfo()

Doctor.displayDocList()










