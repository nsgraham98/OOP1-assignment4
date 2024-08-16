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
        file = open("facilities.txt", "r")
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

    # Writes the facilities list to facilities.txt
    @staticmethod
    def writeListOfFacilitiesToFile(full_fac_list):
        file = open("facilities.txt", "w")
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
        f_obj = open('laboratories.txt', 'r')
        line = f_obj.readline()

        while line != '':
            lab_data = line.rstrip().split('_')
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
        file = open('laboratories.txt', 'w')
        for lab_obj in new_lab_list:
            file.write(Laboratory.formatLabInfo(lab_obj))

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
    def enterPatientInfo(): #returns inputted info as a patient's object
        patient_obj = Patient(int(input("Enter the patient's ID: ")), input("Enter the patient's name: "), input("Enter the patient's disease: "), input("Enter the patient's gender: "), int(input("Enter the patient's age: ")))
        Patient.addPatientToFile(patient_obj)

    # readPatientsFile 
    # Reads from “patients.txt” file and fills the patient's objects in a list
    @staticmethod
    def readPatientsFile(): #returns list of all Patient_objects in patients.txt
        full_patient_list = []
        file = open("patients.txt", "r")
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
        pid = int(input("Enter the patient's ID: "))
        full_patient_list = Patient.readPatientsFile()
        for patient_obj in full_patient_list:
            if patient_obj != "":
                if pid == patient_obj._pid:
                    Patient.displayPatientInfo(patient_obj)
            else:
                print("Can't find the patient with the same ID on the system")

    # displayPatientInfo 
    # Displays patient's information on different lines, as a list
    @staticmethod
    def displayPatientInfo(patient_obj): #requires list of 1 patient
        Patient.patientHeader()
        temp_list = patient_obj._patient_info
        print(f'{temp_list[0]:<10}{temp_list[1]:<20}{temp_list[2]:<20}{temp_list[3]:<20}{temp_list[4]}')

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

    # displayPatientsList 
    # Displays all the Patients’ information, read from the file, as a report/table
    @staticmethod
    def displayPatientList():
        full_patient_list = Patient.readPatientsFile()
        Patient.patientHeader()
        for patient_obj in full_patient_list:
            temp_list = patient_obj._patient_info
            print(f'{temp_list[0]:<10}{temp_list[1]:<20}{temp_list[2]:<20}{temp_list[3]:<20}{temp_list[4]:<20}')

    # writeListOfPatientsToFile 
    # Writes the list of Patients to the patients.txt file after formatting it correctly
    @staticmethod
    def writeListOfPatientsToFile(full_patient_list): #requires list of all patients
        patient_list = full_patient_list

        file = open("patients.txt", "w")
        file.write(f"id_Name_Disease_Gender_Age\n")
        for patient_obj in patient_list:
            file.write(f'{Patient.formatPatientInfo(patient_obj)}\n')
        
        file.close()

    # addPatientToFile 
    # Writes Patients to the patients.txt file after formatting it correctly
    @staticmethod
    def addPatientToFile(patient_obj): #requires 1 Patient_object
        patient = patient_obj

        file = open("patients.txt", "a")
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
    while True:
        print("\nDoctors Menu:")
        print("1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n")

        drchoice = int(input("Enter your selection: "))
        
        match drchoice:
            case 1:
                doctor.displayDoctorsList()
            case 2:
                d = doctor.searchDoctorById()
                if d == '':
                    print("Can't find the doctor with the same ID on the system")
                else:
                    doctor.displayDoctorInfo(d)
            case 3:
                d = doctor.searchDoctorByName()
                if d == '':
                    print("Can't find the doctor with the same name on the system")
                else:
                    doctor.displayDoctorInfo(d)
            case 4:
                d = doctor.enterDrInfo()
                doctor.addDrToFile(d)
            case 5:
                doctor.editDoctorInfo()
            case 6:
                DisplayMenu()
                return
            case _:
                print("Invalid selection. Please enter a number 1-6 for your selection.")

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