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
        print(f'\n{"Lab":<20}{"Cost":<}')
        print(f'{"="*25}')
        for lab_obj in full_lab_list:
            print(f'{lab_obj._name:<20}{lab_obj._cost:<}')
        print("\nBack to the previous menu")

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
    print("\nBack to the previous menu")

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

class Patient:

    def __init__(self, pid=0, name="", disease="", gender="", age=0):
        self._pid = pid
        self._name = name
        self._disease = disease
        self._gender = gender
        self._age = age
        self._patient_info = [pid, name, disease, gender, age]

    def get_pid(self):
        return self._pid
    def get_name(self):
        return self._name
    def get_disease(self):
        return self._disease
    def get_gender(self):
        return self._gender
    def get_age(self):
        return self._age
    def get_patient_info(self):
        return self._patient_info
    
    def set_pid(self, pid):
        self._pid = pid
    def set_name(self, name):
        self._name = name
    def set_disease(self, disease):
        self._disease = disease
    def set_gender(self, gender):
        self._gender = gender
    def set_age(self, age):
        self._age = age

    def set_patient_info(self, pid, name, disease, gender, age):
        self._patient_info = [pid, name, disease, gender, age]
        

        # formatPatientInfo
        # Formats each Patient’s information (properties) in the same format used in the .txt file (i.e., has underscores between values)
    @staticmethod
    def formatPatientInfo(patient_obj): #requires 1 Patient_object
        temp_list = patient_obj._patient_info
        temp_list[0] = str(temp_list[0])
        temp_list[4] = str(temp_list[4])
        separ = "_"
        formatted_patient_str = separ.join(temp_list)
        return formatted_patient_str

    # enterPatientInfo
    # Asks the user to enter patient's properties (listed in the Properties point)
    @staticmethod
    def enterPatientInfo(): 
        patient_obj = Patient(int(input("Enter the patient's ID: ")), input("Enter the patient's name: "), input("Enter the patient's disease: "), input("Enter the patient's gender: "), int(input("Enter the patient's age: ")))
        Patient.addPatientToFile(patient_obj)
    print("\nBack to the previous menu")

    # readPatientsFile 
    # Reads from “patients.txt” file and fills the patient's objects in a list
    @staticmethod
    def readPatientsFile(): #returns list of all Patient_objects in patients.txt
        full_patient_list = []
        file = open("files/patients.txt", "r")
        file.readline()
        line = file.readline().rstrip("\n")

        while line != "":
            patient_list = line.split("_")
            patient_obj = Patient(int(patient_list[0]),patient_list[1],patient_list[2],patient_list[3],int(patient_list[4]),)
            full_patient_list.append(patient_obj)
            line = file.readline()

        file.close()
        return full_patient_list

    # searchPatientById 
    # Searches whether the patient's is in the list of Patients/file using the patient's pid that the user enters
    @staticmethod
    def searchPatientById():
        verify = False
        pid = int(input("Enter the patient's ID: "))
        full_patient_list = Patient.readPatientsFile()
        for patient_obj in full_patient_list:
            if patient_obj != "":
                if pid == patient_obj._pid:
                    Patient.displayPatientInfo(patient_obj)
                    verify = True
        if verify == False:
            print("Can't find the patient with the same ID on the system")
        print("\nBack to the previous menu")

    # displayPatientInfo 
    # Displays patient's information on different lines, as a list
    @staticmethod
    def displayPatientInfo(patient_obj): #requires list of 1 patient
        Patient.patientHeader()
        temp_list = patient_obj._patient_info
        print(f'{temp_list[0]:<10}{temp_list[1]:<20}{temp_list[2]:<20}{temp_list[3]:<20}{temp_list[4]}')
        print("\nBack to the previous menu") 

    # patientHeader
    # prints a header to be used when displaying patient's info
    @staticmethod
    def patientHeader():
        print(f'\n{"ID":<10}{"Name":<20}{"Disease":<20}{"Gender":<20}Age')
        print(f'{"=" * 75}')

    # editPatientInfo 
    # Asks the user to enter the pid of the patient's to change their information, and then the user can enter the new patient's information
    @staticmethod
    def editPatientInfo(): #returns list of all Patients
        pid = int(input("Please enter the ID of the patient that you want to edit the information of: "))
        full_patient_list = Patient.readPatientsFile()
        for patient_obj in full_patient_list:
            if patient_obj != "":
                if patient_obj._pid == pid:
                    patient_obj._name = input("Enter new name: ")
                    patient_obj._disease = input("Enter new disease: ")
                    patient_obj._gender = input("Enter new gender: ")
                    patient_obj._age = int(input("Enter new age: "))
                    patient_obj.set_patient_info(patient_obj._pid, patient_obj._name, patient_obj._disease, patient_obj._gender, patient_obj._age)
            else:
                print("Patient pid not found. ")
        Patient.writeListOfPatientsToFile(full_patient_list)
        print("\nBack to the previous menu")

    # displayPatientsList 
    # Displays all the Patients’ information, read from the file, as a report/table
    @staticmethod
    def displayPatientList():
        full_patient_list = Patient.readPatientsFile()
        Patient.patientHeader()
        for patient_obj in full_patient_list:
            temp_list = patient_obj._patient_info
            print(f'{temp_list[0]:<10}{temp_list[1]:<20}{temp_list[2]:<20}{temp_list[3]:<20}{temp_list[4]:<20}')
        print("\nBack to the previous menu")

    # writeListOfPatientsToFile 
    # Writes the list of Patients to the patients.txt file after formatting it correctly
    @staticmethod
    def writeListOfPatientsToFile(full_patient_list): #requires list of all patients
        patient_list = full_patient_list

        file = open("files/patients.txt", "w")
        file.write(f"id_Name_Disease_Gender_Age\n")
        for patient_obj in patient_list:
            file.write(f'{Patient.formatPatientInfo(patient_obj)}\n')
        
        file.close()

    # addPatientToFile 
    # Writes Patients to the patients.txt file after formatting it correctly
    @staticmethod
    def addPatientToFile(patient_obj): #requires 1 Patient_object
        patient = patient_obj

        file = open("files/patients.txt", "a")
        file.write(f'\n{Patient.formatPatientInfo(patient)}')
        file.close()

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
        Laboratory.enterLaboratoryInfo()
        laboratoryMenu()
    elif lab_choice == 3:
        DisplayMenu()
    else:
        print("Invalid selection. Please enter a number 1-3 for your selection.")
        laboratoryMenu()
    
def patientMenu():
    print("\nPatients Menu:")
    print(f"1 - Display Patients list\n2 - Search for Patient by ID\n3 - Add Patient\n4 - Edit Patient info\n5 - Back to the Main Menu\n")
    pat_choice = int(input("Enter your selection: "))
    if pat_choice == 1:
        Patient.displayPatientList()
        patientMenu()
    elif pat_choice == 2:
        Patient.searchPatientById()
        patientMenu()
    elif pat_choice == 3:
        Patient.enterPatientInfo()
        patientMenu()
    elif pat_choice == 4:
        Patient.editPatientInfo()
        patientMenu()
    elif pat_choice == 5:
        DisplayMenu()
    else:
        print("Invalid selection. Please enter a number 1-6 for your selection.")
        patientMenu()

DisplayMenu()
