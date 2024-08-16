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
        
#1 display doctors list
'''doctor.displayDoctorsList()'''

#2 search for doctor by id
'''d = doctor.searchDoctorById()
if d == '':
    print("No Id match")
else:
    doctor.displayDoctorInfo(d)'''

#3 search doctor by name
'''d = doctor.searchDoctorByName()
if d == '':
    print("No Name match")
else:
    doctor.displayDoctorInfo(d)'''

#4 add dr
'''d = doctor.enterDrInfo()
doctor.addDrToFile(d)
doctor.displayDoctorsList()'''

#5 edit dr
'''doctor.editDoctorInfo()
doctor.displayDoctorsList()'''
