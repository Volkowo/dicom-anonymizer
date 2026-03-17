import pydicom
import os
import shutil
from pydicom.uid import generate_uid

# List of "variables" in a DICOM file that should be anonymized
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

def getPaths():
    source = input("Enter the source directory (no need to include the DICOM folder): ")
    parent = input("Enter the parent directory where the anonymized dataset will be saved: ")
    folder = input("Enter the name for the anonymized dataset folder: ")
    destination = os.path.join(parent, folder)

    return source, destination

def copyFiles(sourceDir, destinationDir):
    # Copy source if destination hasn't exist yet
    if not os.path.exists(destinationDir):
        shutil.copytree(sourceDir, destinationDir)
        return True
    # print an error if the destiantion already exists
    else:
        print("Destination folder already exists. Please choose another one.")
        return False

def anonymizeFile(dicomFolderDir):
    for (root, dirs, files) in os.walk(dicomFolderDir):
        for file in files:
            fullDir = os.path.join(root, file)

            # Checks if the directory is valid or not
            try:
                ds = pydicom.dcmread(fullDir)
            except pydicom.errors.InvalidDicomError:
                print(f"{fullDir} is not a valid path!")
                continue
        
            # Anonymizes the value that are in the anonymizeKeyword array
            for elem in ds:
                if elem.keyword in anonymizeKeyword:
                    elem.value = ""

            # Remove any private tags
            ds.remove_private_tags()

            # Separates the file from it's extension (if it exists)
            name, extension = os.path.splitext(file)

            outputPath = os.path.join(root, f"{name}.dcm")
            ds.save_as(outputPath, enforce_file_format=True)
            
            # The original files usually do not have extension in them, so this if statement removes any of the extension-less files.
            if outputPath != fullDir:
                os.remove(fullDir)

def main():
    source, destination = getPaths()
    copied = copyFiles(source, destination)

    if not copied:
        return
    
    # Get the directory for DICOM file
    dicDir = os.path.join(destination, "DICOM")
    anonymizeFile(dicDir)

main();