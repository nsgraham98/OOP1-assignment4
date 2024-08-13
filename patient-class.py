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
        print(f'{"=" * 101}')

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
