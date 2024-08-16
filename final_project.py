class doctor:
    def __init__(self, id, name, specilist, timing, qualification, roomNb):
        self.id = id
        self.name = name
        self.specilist = specilist
        self.timing = timing
        self.qualification = qualification
        self.roomNb = roomNb


    @staticmethod
    def formatDrInfo(doctor):
        return doctor.id +"_"+ doctor.name+"_"+ doctor.specilist+"_"+ doctor.timing+"_"+ doctor.qualification+"_"+ doctor.roomNb+"\n"
    

    @staticmethod
    def enterDrInfo():
        id = input("Input Dr. ID")
        n = input("Input Dr. Name")
        s = input("Input Dr. Specialty")
        t = input("Input Dr. Time")
        q = input("Input Dr. Qualification")
        rn = input("Input Dr. Room number")
        return doctor(id,n,s,t,q,rn)

    

    @staticmethod
    def readDoctorsFile():
        doctors = []
        #Open the doctor file
        f_obj = open('files/doctors.txt', 'r')
        line = f_obj.readline()

        while line != '':
            if line != 'id_name_specilist_timing_qualification_roomNb\n':
                #fill doctors into a list
                tlist = line.rstrip().split("_")
                d = doctor(tlist[0], tlist[1], tlist[2], tlist[3], tlist[4], tlist[5])
                doctors.append(d)
            line = f_obj.readline()
        f_obj.close()
        return(doctors)


    @staticmethod
    def searchDoctorByName():
        doctors = doctor.readDoctorsFile()
        i = input("Enter the doctor Name: ")
        for d in doctors:
            if d.name == i:
                return d
        return ''


    @staticmethod
    def displayDoctorInfo(doctor):
        print(f"ID: {doctor.id}")
        print(f"Name: {doctor.name}")
        print(f"Specialization: {doctor.specilist}")
        print(f"Working Time: {doctor.timing}")
        print(f"Qualification: {doctor.qualification}")
        print(f"Room Number: {doctor.roomNb}")


    @staticmethod
    def editDoctorInfo():
        id = input("Enter Dr. ID")
        doctors = doctor.readDoctorsFile()
        for d in doctors:
            if d.id == id:
                n = input("Input Dr. Name")
                s = input("Input Dr. Specialty")
                t = input("Input Dr. Time")
                q = input("Input Dr. Qualification")
                rn = input("Input Dr. Room number")
                for i in range(len(doctors)):
                    if doctors[i].id == id:
                        doctors[i].name = n
                        doctors[i].specilist = s
                        doctors[i].timing = t
                        doctors[i].qualification = q
                        doctors[i].roomNb = rn
                doctor.writeListOfDoctorsToFile(doctors)
        else:
            print("Dr. not found")


    @staticmethod
    def displayDoctorsList():
        doctors = doctor.readDoctorsFile()
        for d in doctors:
            doctor.displayDoctorInfo(d)


    @staticmethod
    def searchDoctorById():
        doctors = doctor.readDoctorsFile()
        i = input("Enter the doctor ID: ")
        for d in doctors:
            if d.id == i:
                return d
        return ''
         

    @staticmethod
    def writeListOfDoctorsToFile(doctors):
        f_obj = open('files/doctors.txt', 'w')
        for d in doctors:
            f_obj.write(doctor.formatDrInfo(d))
        f_obj.close()


    @staticmethod
    def addDrToFile(doctor):
        doctors = doctor.readDoctorsFile()
        doctors.append(doctor)
        doctor.writeListOfDoctorsToFile(doctors)
        


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
        f_obj = open('files/facilities.txt', 'r')
        line = f_obj.readline()

        while line != '':
            if line != 'Hospital  Facility are:\n':
                f = facility(line)
                facilities.append(f)
            line = f_obj.readline()
        f_obj.close()
        return(facilities)



class laboratory:
    def __init__(self, labName, cost):
        self.labName = labName
        self.cost = cost

    @staticmethod
    def addLabToFile(laboratory):
        laboratories = laboratory.readLaboratoriesFile()
        laboratories.append(laboratory)
        laboratory.writeListOfLabsToFile(laboratories)

    @staticmethod
    def writeListOfLabsToFile(laboratories):
        f_obj = open('files/laboratories.txt', 'w')
        for l in laboratories:
            f_obj.write(laboratory.formatLabInfo(l))
        f_obj.close()

    @staticmethod
    def displayLabsList():
        labs = laboratory.readLaboratoriesFile()
        for l in labs:
            print(l.labName + "\t\t" + l.cost)

    @staticmethod
    def formatLabInfo(laboratory):
        return laboratory.labName +"_"+ laboratory.cost+"_"+ "\n"
    
    @staticmethod
    def enterLaboratoryInfo():
        n = input("Input Lab name")
        c = input("Input Lab cost")
        return laboratory(n,c)
       
    @staticmethod
    def readLaboratoriesFile():
        laboratories = []
        f_obj = open('files/laboratories.txt', 'r')
        line = f_obj.readline()

        while line != '':
            if line != 'Laboratory_Cost\n':
                tlist = line.rstrip().split("_")
                l = laboratory(tlist[0], tlist[1])
                laboratories.append(l)
            line = f_obj.readline()
        f_obj.close()
        return(laboratories)
    


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



def DisplayMenu():
    while True:
        print("\nWelcome to Alberta Hospital (AH) Management system\nSelect from the following options, or select 0 to stop: ")
        print("1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients\n0 - Exit program\n")
        
        choice = int(input("Enter your selection: "))
        
        match choice:
            case 1:
                doctorMenu()
            case 2:
                facilityMenu()
            case 3:
                laboratoryMenu()
            case 4:
                patientMenu()
            case 0:
                print("Goodbye!")
                return
            case _:
                print("Invalid Selection. Please enter 1-4 or 0 to exit.")

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
                    print("No Id match")
                else:
                    doctor.displayDoctorInfo(d)
            case 3:
                d = doctor.searchDoctorByName()
                if d == '':
                    print("No Name match")
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
    while True:
        print("\nFacilities Menu:")
        print("1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n")

        fchoice = int(input("Enter your selection: "))
        
        match fchoice:
            case 1:
                facility.displayFacilities()
            case 2:
                facility.addFacility()
            case 3:
                DisplayMenu()
                return
            case _:
                print("Invalid selection. Please enter a number 1-3 for your selection.")

def laboratoryMenu():
    while True:
        print("\nLaboratories Menu:")
        print("1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n")

        lchoice = int(input("Enter your selection: "))
        
        match lchoice:
            case 1:
                laboratory.displayLabsList()
            case 2:
                l = laboratory.enterLaboratoryInfo()
                laboratory.addLabToFile(l)
            case 3:
                DisplayMenu()
                return
            case _:
                print("Invalid selection. Please enter a number 1-3 for your selection.")

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
                    print("No Id match")
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