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
        print("\nBack to the previous menu")

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
        verify = False
        id = int(input("Enter the doctor ID: "))
        full_doc_list = Doctor.readDoctorsFile()
        for doc_obj in full_doc_list:
            if doc_obj != "":
                if id == doc_obj._id:
                    Doctor.displayDoctorInfo(doc_obj)
                    verify = True
        if verify == False:
                print("Can't find the doctor with the same ID on the system")
        print("\nBack to the previous menu")

    # searchDoctorByName 
    # Searches whether the doctor is in the list of doctors/file using the doctor name that the user enters
    @staticmethod
    def searchDoctorByName():
        verify = False
        name = input("Enter the doctor name: ")
        full_doc_list = Doctor.readDoctorsFile()
        for doc_obj in full_doc_list:
            if doc_obj != "":
                if name == doc_obj._name:
                    Doctor.displayDoctorInfo(doc_obj)
                    verify = True
        if verify == False:
            print("Can't find the doctor with the same name on the system")
        print("\nBack to the previous menu")

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
        print(f'{"=" * 101}')

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
        print("\nBack to the previous menu")

    # displayDoctorsList 
    # Displays all the doctors’ information, read from the file, as a report/table
    @staticmethod
    def displayDoctorList():
        full_doc_list = Doctor.readDoctorsFile()
        Doctor.doctorHeader()
        for doc_obj in full_doc_list:
            temp_list = doc_obj._doc_info
            print(f'{temp_list[0]:<10}{temp_list[1]:<20}{temp_list[2]:<20}{temp_list[3]:<20}{temp_list[4]:<20}{temp_list[5]}')
        print("\nBack to the previous menu")

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
        file.write(f'\n{Doctor.formatDrInfo(doc)}')
        file.close()

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
        print("\nBack to the previous menu")       

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
        print("\nThe Hospital Facilities are:")
        print(f'{"="*28}')
        for fac_obj in full_fac_list:
            name = fac_obj._name
            print(f'{name}')
        print("\nBack to the previous menu")

    # Writes the facilities list to facilities.txt
    @staticmethod
    def writeListOfFacilitiesToFile(full_fac_list):
        file = open("files/facilities.txt", "w")
        file.write(f"Hospital  Facility are:\n")
        for fac_obj in full_fac_list:
            file.write(f'{fac_obj._name}\n')
        
        file.close()

class Laboratory:
    def __init__(self, name, cost):
        self._name = name
        self._cost = cost
    @staticmethod
    def readLabFile():

        full_lab_list = []
        f_obj = open('files/laboratories.txt', 'r')
        line = f_obj.readline()

        while line != '':
            lab_data = line.rstrip().split('_')
            #lab = (lab_data[0], lab_data[1])
            lab = Laboratory(lab_data[0], str(lab_data[1]))
            full_lab_list.append(lab)
            line = f_obj.readline().rstrip()
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
        file = open('files/laboratories.txt', 'w')
        for lab_obj in new_lab_list:
            file.write(Laboratory.formatLabInfo(lab_obj))

class patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age


    @staticmethod
    def formatPatientInfo(patient):
        return patient.pid +"_"+ patient.name+"_"+ patient.disease+"_"+ patient.gender+"_"+ patient.age+"_"+ "\n"
    

    @staticmethod
    def enterPatientInfo():
        pid = input("Enter Patient ID: ")
        n = input("Enter Name: ")
        d = input("Enter Disease: ")
        g = input("Enter Gender: ")
        a = input("Enter Age: ")
        return patient(pid,n,d,g,a)


    @staticmethod
    def readPatientsFile():
        patients = []
        #Open the patient file
        f_obj = open('files/patients.txt', 'r')
        line = f_obj.readline()

        while line != '':
            if line != 'id_Name_Disease_Gender_Age\n':
                #fill patients into a list
                tlist = line.rstrip().split("_")
                p = patient(tlist[0], tlist[1], tlist[2], tlist[3], tlist[4])
                patients.append(p)
            line = f_obj.readline()
        f_obj.close()
        return(patients)

    
    @staticmethod
    def searchPatientById():
        patients = patient.readPatientsFile()
        i = input("Enter the patient ID: ")
        for p in patients:
            if p.pid == i:
                return p
        return ''

    @staticmethod
    def displayPatientInfo(patient):
        print(f"{patient.pid:<10}{patient.name:>20}{patient.disease:>20}{patient.gender:>20}{patient.age:>20}")
        
    @staticmethod
    def editPatientInfo():
        id = input("Enter patient ID")
        patients = patient.readPatientsFile()
        for p in patients:
            if p.pid == id:
                n = input("Enter Patient Name")
                d = input("Enter Patient disease")
                g = input("Enter Patient gender")
                a = input("Enter Patient age")
                for i in range(len(patients)):
                    if patients[i].pid == id:
                        patients[i].name = n
                        patients[i].disease = d
                        patients[i].gender = g
                        patients[i].age = a
                patient.writeListOfPatientsToFile(patients)

    @staticmethod
    def displayPatientsList():
        patients = patient.readPatientsFile()
        for p in patients:
            patient.displayPatientInfo(p)

    @staticmethod
    def writeListOfPatientsToFile(patients):
        f_obj = open('files/patients.txt', 'w')
        for p in patients:
            f_obj.write(patient.formatPatientInfo(p))
        f_obj.close()

    @staticmethod
    def addPatientToFile(patient):
        patients = patient.readPatientsFile()
        patients.append(patient)
        patient.writeListOfPatientsToFile(patients)

def DisplayMenu():

    print("\nWelcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop: ")
    print(f"1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients\n0 - Exit program\n")

    choice = int(input("Enter your selection: "))
    if choice == 1:
        doctorMenu()
    elif choice == 2:
        facilityMenu()
    elif choice == 3:
        laboratoryMenu()
    elif choice == 4:
        patientMenu()
    elif choice == 0:
        print("Goodbye!")
    else:
        print("Invalid Selection. Please enter 1-6 or 0 to exit.")
        DisplayMenu()
    
def doctorMenu():
    print("\nDoctors Menu:")
    print(f"1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n")
    doc_choice = int(input("Enter your selection: "))
    if doc_choice == 1:
        Doctor.displayDoctorList()
        doctorMenu()
    elif doc_choice == 2:
        Doctor.searchDoctorById()
        doctorMenu()
    elif doc_choice == 3:
        Doctor.searchDoctorByName()
        doctorMenu()
    elif doc_choice == 4:
        Doctor.enterDrInfo()
        doctorMenu()
    elif doc_choice == 5:
        Doctor.editDoctorInfo()
        doctorMenu()
    elif doc_choice == 6:
        DisplayMenu()
    else:
        print("Invalid selection. Please enter a number 1-6 for your selection.")
        doctorMenu()

def facilityMenu():
    print("\nFacilities Menu:")
    print(f"1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n")
    fac_choice = int(input("Enter your selection: "))
    if fac_choice == 1:
        Facility.displayFacilies()
        facilityMenu()
    elif fac_choice == 2:
        Facility.addFacility()
        facilityMenu()
    elif fac_choice == 3:
        DisplayMenu()
    else:
        print("Invalid selection. Please enter a number 1-3 for your selection.")
        facilityMenu()

def laboratoryMenu():
    print("\nLaboratories Menu:")
    print(f"1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n")
    lab_choice = int(input("Enter your selection: "))
    if lab_choice == 1:
        Laboratory.displayLabsList()
        laboratoryMenu()
    elif lab_choice == 2:
        Laboratory.addLabToFile()
        laboratoryMenu()
    elif lab_choice == 3:
        DisplayMenu()
    else:
        print("Invalid selection. Please enter a number 1-3 for your selection.")
        laboratoryMenu()
    
def patientMenu():
    while True:
        print("\nPatients Menu:")
        print("1 - Display Patients list\n2 - Search for Patient by ID\n3 - Add Patient\n4 - Edit Patient info\n5 - Back to the Main Menu\n")

        pchoice = int(input("Enter your selection: "))
        
        match pchoice:
            case 1:
                patient.displayPatientsList()
            case 2:
                p = patient.searchPatientById()
                if p == '':
                    print("Can't find the Patient with the same id on the system")
                else:
                    patient.displayPatientInfo(p)
            case 3:
                p = patient.enterPatientInfo()
                patient.addPatientToFile(p)
            case 4:
                patient.editPatientInfo()
            case 5:
                DisplayMenu()
                return
            case _:
                print("Invalid selection. Please enter a number 1-5 for your selection.")
DisplayMenu()
