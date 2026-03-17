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

def copy():
    ## Copy source if destination hasn't exist yet
    if not os.path.exists(destination):
        shutil.copytree(source, destination)

    ## Get the directory for DICOM file
    dicDir = os.path.join(source, "DICOM")

    for (root, dirs, files) in os.walk(dicDir):
        print(f"Directory Path: {root}")
        print(f"Directory Names: {dirs}")
        print(f"File Names: {files}")

    # for file in files:
    #     fullDir = os.path.join(dicDir, file)

    #     if not os.path.isfile(fullDir):
    #         print(f"{fullDir} is not a valid path!")
    #         continue

    #     ds = pydicom.dcmread(fullDir);
        
    #     for elem in ds:
    #         if elem.keyword in anonymizeKeyword:
    #             elem.value = ""
    #     ds.remove_private_tags()

    #     outputPath = os.path.join(dicDir, f"{file}.dcm")
    #     ds.save_as(outputPath, enforce_file_format=True)

def main():
    x = input("Enter source file: ")
    print("SOURCE: ", x)

copy();