#!/usr/bin/python3

DoctorSpecialities = open("speciality.txt", "r")  # (path, mode)

for doctor in DoctorSpecialities.readlines():
    print(doctor)
DoctorSpecialities.close()
