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

source = r"D:\VIDEO PROJECT CUS SIZE BIG\MRI - HG"
destination = r"D:\VIDEO PROJECT CUS SIZE BIG\MRI - HG_ANON"

## Copy source if destination hasn't exist yet
if not os.path.exists(destination):
    shutil.copytree(source, destination)

## Get the directory for DICOM file
dicDir = os.path.join(destination, "DICOM")

## Get the files that's inside the dicDir file
files = os.listdir(dicDir)

for file in files:
    fullDir = os.path.join(dicDir, file)

    if not os.path.isfile(fullDir):
        print(f"{fullDir} is not a valid path!")
        continue

    ds = pydicom.dcmread(fullDir);
    
    for elem in ds:
        if elem.keyword in anonymizeKeyword:
            elem.value = ""
    ds.remove_private_tags()

    outputPath = os.path.join(dicDir, f"{file}.dcm")
    ds.save_as(outputPath, enforce_file_format=True)