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
        print(f"Patient ID: {patient.pid}")
        print(f"Name: {patient.name}")
        print(f"Disease: {patient.disease}")
        print(f"Gender: {patient.gender}")
        print(f"Age: {patient.age}")
        
    @staticmethod
    def editPatientInfo():
        id = input("Enter patient ID")
        patients = patient.readPatientsFile()
        for p in patients:
            if p.pid == id:
                n = input("Input patient Name")
                d = input("Input patient disease")
                g = input("Input patient gender")
                a = input("Input patient age")
                for i in range(len(patients)):
                    if patients[i].pid == id:
                        patients[i].name = n
                        patients[i].disease = d
                        patients[i].gender = g
                        patients[i].age = a
                patient.writeListOfPatientsToFile(patients)
        else:
            print("Patient not found")

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

#1 display patient list
patient.displayPatientsList()

#2 search for patient by id
'''p = patient.searchPatientById()
if p == '':
    print("No Id match")
else:
    patient.displayPatientInfo(p)'''


#4 add patient
'''p = patient.enterPatientInfo()
patient.addPatientToFile(p)
patient.displayPatientsList()'''

#5 edit patient
'''patient.editPatientInfo()
patient.displayPatientsList()'''
