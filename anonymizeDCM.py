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

# Prompts the user for the source dataset and the destination folder
def getPaths():
    source = input("Enter the source directory (no need to include the DICOM folder): ")
    parent = input("Enter the parent directory where the anonymized dataset will be saved: ")
    folder = input("Enter the name for the anonymized dataset folder: ")
    destination = os.path.join(parent, folder)

    return source, destination

# Copies the entire dataset from the source directory to the destination directory
def copyFiles(sourceDir, destinationDir):
    sourceDICOM = os.path.join(sourceDir, "DICOM")
    destinationDICOM = os.path.join(destinationDir, "DICOM")

    if not os.path.exists(sourceDICOM):
        print("Source DICOM folder not found.")
        return False

    if os.path.exists(destinationDir):
        print("Destination folder already exists. Please choose another one.")
        return False
    
    print("\nCopying DICOM folder... This may take a while.")
    print("Please do not close this window or interrupt the process.\n")

    os.makedirs(destinationDir)
    shutil.copytree(sourceDICOM, destinationDICOM)
    return True

# Walks through all files inside the DICOM folder and anonymizes metadata
def anonymizeFile(dicomFolderDir):
    for (root, dirs, files) in os.walk(dicomFolderDir):
        for file in files:
            fullDir = os.path.join(root, file)

            # Checks if the directory is valid or not
            try:
                ds = pydicom.dcmread(fullDir)
            except pydicom.errors.InvalidDicomError:
                print(f"{fullDir} is not a valid DICOM file!")
                continue
        
            # Anonymizes the value that are in the anonymizeKeyword array
            for elem in ds:
                if elem.keyword in anonymizeKeyword:
                    elem.value = ""

            # Remove any private tags
            ds.remove_private_tags()

            # Separates the file from it's extension (if it exists)
            name, _ = os.path.splitext(file)

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

    print("DICOM folder copied successfully.")
    print("\nAnonymizing DICOM files... This may take a while.")
    print("Please do not close this window or interrupt the process.\n")

    anonymizeFile(dicDir)

    print("Anonymization complete.")
    print(f"Anonymized files saved in: {destination}")

main();