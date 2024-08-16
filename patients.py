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