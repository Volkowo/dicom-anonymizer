import pydicom
import os
import shutil
from pydicom.uid import generate_uid

anonymizeKeyword = [
    "PatientName",
    "PatientID",
    "PatientBirthDate",
    "PatientSex",
    "PatientAge",
    "PatientWeight",
    "InstitutionName",
    "InstitutionAddress",
    "ReferringPhysicianName",
    "OperatorsName",
    "StationName",
    "DeviceSerialNumber",
    "AccessionNumber",
    "StudyID",
    "StudyDate",
    "SeriesDate",
    "AcquisitionDate",
    "StudyTime",
    "SeriesTime",
    "AcquisitionTime",
    "StudyDescription",
    "SeriesDescription",
    "ProtocolName",
    "PerformedProcedureStepID",
    "PerformedProcedureStepDescription",
]

fileInput = r"D:\VIDEO PROJECT CUS SIZE BIG\MRI - HG\DICOM"

## Get the number of .dcm files inside the DICOM folder
files = os.listdir(fileInput)

for file in files:
    print(file)

# for number in range(len(files)):
#     fullDir = os.path.join(fileInput, number)


# print(len(files))


# ds = pydicom.dcmread(input)

# # print(ds)

# for elem in ds:
#     if elem.keyword in anonymizeKeyword:
#         print("BEFORE ANON:", elem.keyword, "=", elem.value)
#         elem.value = ""
#         print("AFTER ANON:", elem.keyword, "=", elem.value)
# print(ds.PatientID)
# print(ds.PatientBirthDate)