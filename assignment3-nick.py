class Doctor:

    def __init__(self, id=0, name="", specialization="", working_time="", qualification="", room_number=0):
        self._id = id
        self._name = name
        self._specialization = specialization
        self._working_time = working_time
        self._qualification = qualification
        self._room_number = room_number
        self._doc_info = [id, name, specialization, working_time, qualification, room_number]

    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_specialization(self):
        return self._specialization
    def get_working_time(self):
        return self._working_time
    def get_qualification(self):
        return self._qualification
    def get_room_number(self):
        return self._room_number
    def get_doc_info(self):
        return self._doc_info
    
    def set_id(self, id):
        self._id = id
    def set_name(self, name):
        self._name = name
    def set_specialization(self, specialization):
        self._specialization = specialization
    def set_working_time(self, working_time):
        self._working_time = working_time
    def set_qualification(self, qualification):
        self._qualification = qualification
    def set_room_number(self, room_number):
        self._room_number = room_number

    def set_doc_info(self, id, name, specialization, working_time, qualification, room_number):
        self._doc_info = [id, name, specialization, working_time, qualification, room_number]
        

        # formatDrInfo
        # Formats each doctor’s information (properties) in the same format used in the .txt file (i.e., has underscores between values)
    @staticmethod
    def formatDrInfo(doc_obj): #requires 1 doctor_object
        temp_list = doc_obj._doc_info
        temp_list[0] = str(temp_list[0])
        temp_list[5] = str(temp_list[5])
        separ = "_"
        formatted_dr_string = separ.join(temp_list)
        return formatted_dr_string

    # enterDrInfo
    # Asks the user to enter doctor properties (listed in the Properties point)
    @staticmethod
    def enterDrInfo(): #returns inputted info as a doctor object
        doc_obj = Doctor(int(input("Enter the doctor's ID: ")), input("Enter the doctor's name: "), input("Enter the doctor's specility: "), input("Enter the doctor's timing (e.g., 7am-10pm): "), input("Enter the doctor's qualification: "), int(input("Enter the doctor's room number: ")))
        Doctor.addDrToFile(doc_obj)

    # readDoctorsFile 
    # Reads from “doctors.txt” file and fills the doctor objects in a list
    @staticmethod
    def readDoctorsFile(): #returns list of all doctor_objects in doctors.txt
        full_doc_list = []
        file = open("files/doctors.txt", "r")
        file.readline()
        line = file.readline().rstrip("\n")

        while line != "":
            doc_list = line.split("_")
            doc_obj = Doctor(int(doc_list[0]),doc_list[1],doc_list[2],doc_list[3],doc_list[4],int(doc_list[5]),)
            full_doc_list.append(doc_obj)
            line = file.readline()

        file.close()
        return full_doc_list

    # searchDoctorById 
    # Searches whether the doctor is in the list of doctors/file using the doctor ID that the user enters
    @staticmethod
    def searchDoctorById():
        id = int(input("Enter the doctor ID: "))
        full_doc_list = Doctor.readDoctorsFile()
        for doc_obj in full_doc_list:
            if doc_obj != "":
                if id == doc_obj._id:
                    Doctor.displayDoctorInfo(doc_obj)
            else:
                print("Can't find the doctor with the same ID on the system")

    # searchDoctorByName 
    # Searches whether the doctor is in the list of doctors/file using the doctor name that the user enters
    @staticmethod
    def searchDoctorByName():
        name = input("Enter the doctor name: ")
        full_doc_list = Doctor.readDoctorsFile()
        for doc_obj in full_doc_list:
            if doc_obj != "":
                if name == doc_obj._id:
                    Doctor.displayDoctorInfo(doc_obj)
            else:
                print("Can't find the doctor with the same name on the system")

    # displayDoctorInfo 
    # Displays doctor information on different lines, as a list
    @staticmethod
    def displayDoctorInfo(doc_obj): #requires list of 1 doc
        Doctor.doctorHeader()
        temp_list = doc_obj._doc_info
        print(f'{temp_list[0]:<10}{temp_list[1]:<20}{temp_list[2]:<20}{temp_list[3]:<20}{temp_list[4]:<20}{temp_list[5]}')

    # doctorHeader
    # prints a header to be used when displaying doctor info
    @staticmethod
    def doctorHeader():
        print(f'\n{"ID":<10}{"Name":<20}{"Speciality":<20}{"Timing":<20}{"Qualification":<20}Room Number')
        print(f'{"=" * 101}\n')

    # editDoctorInfo 
    # Asks the user to enter the ID of the doctor to change their information, and then the user can enter the new doctor information
    @staticmethod
    def editDoctorInfo(): #returns list of all doctors
        id = int(input("Please enter the ID of the doctor that you want to edit their information: "))
        full_doc_list = Doctor.readDoctorsFile()
        for doc_obj in full_doc_list:
            if doc_obj != "":
                if doc_obj._id == id:
                    doc_obj._name = input("Enter new name: ")
                    doc_obj._specialization = input("Enter new Specilist in: ")
                    doc_obj._working_time = input("Enter new Timing: ")
                    doc_obj._qualification = input("Enter new Qualification: ")
                    doc_obj._room_number = int(input("Enter new Room number: "))
                    doc_obj.set_doc_info(doc_obj._id, doc_obj._name, doc_obj._specialization, doc_obj._working_time, doc_obj._qualification, doc_obj._room_number)
            else:
                print("Doctor ID not found. ")
        Doctor.writeListOfDoctorsToFile(full_doc_list)

    # displayDoctorsList 
    # Displays all the doctors’ information, read from the file, as a report/table
    @staticmethod
    def displayDoctorList():
        full_doc_list = Doctor.readDoctorsFile()
        Doctor.doctorHeader()
        for doc_obj in full_doc_list:
            temp_list = doc_obj._doc_info
            print(f'{temp_list[0]:<10}{temp_list[1]:<20}{temp_list[2]:<20}{temp_list[3]:<20}{temp_list[4]:<20}{temp_list[5]}')

    # writeListOfDoctorsToFile 
    # Writes the list of doctors to the doctors.txt file after formatting it correctly
    @staticmethod
    def writeListOfDoctorsToFile(full_doc_list): #requires list of all docs
        doc_list = full_doc_list

        file = open("files/doctors.txt", "w")
        file.write(f"id_name_specialist_timing_qualification_roomNb\n")
        for doc_obj in doc_list:
            file.write(f'{Doctor.formatDrInfo(doc_obj)}\n')
        
        file.close()

    # addDrToFile 
    # Writes doctors to the doctors.txt file after formatting it correctly
    @staticmethod
    def addDrToFile(doc_obj): #requires 1 doctor_object
        doc = doc_obj

        file = open("files/doctors.txt", "a")
        file.write(f'{Doctor.formatDrInfo(doc)}\n')
        file.close()

