# DICOM Dataset Anonymization Script

## Purpose
This Python script anonymizes selected metadata fields from a DICOM dataset exported from medical imaging systems (e.g., hospital CD exports). The script processes all DICOM files within the dataset and removes or clears identifiable patient information while preserving the image data so that the files remain viewable in standard DICOM viewers.

The script also converts DICOM files to use the `.dcm` extension to ensure compatibility with systems or tools that expect this file format.

Developed as part of an internship project in collaboration with Insight RSA.
---

## Intended Use
This tool was developed as part of a project for **Insight RSA** and is intended primarily for **internal use and demonstration purposes**.

The anonymization implemented in this script is designed to remove commonly identifiable metadata fields so that the dataset can be used for:

- Demonstrations
- Development testing
- Internal showcases

This script is **not intended to serve as a fully compliant medical data anonymization pipeline**.

---

## Important Disclaimer
This project was developed as part of an internship and is shared for demonstration purposes only.  
It is not intended for clinical or production use.

While the script removes commonly identifiable metadata fields, it does not guarantee full compliance with medical data privacy regulations (e.g., HIPAA or equivalent standards).

---

## What the Script Does

The script performs the following steps:

1. Copies the original dataset to a new destination directory.
2. Recursively scans the `DICOM` folder for all DICOM files.
3. Removes selected metadata fields containing identifiable patient or institution information.
4. Removes private DICOM tags.
5. Saves the anonymized files using the `.dcm` file extension.

---

## Limitations

- Only selected metadata fields are anonymized.
- Some identifying information may exist in fields not covered by the script.
- The script does not rebuild or maintain `DICOMDIR`.
- The script does not guarantee compliance with medical data privacy standards.

---

## Requirements

- Python 3.x
- `pydicom`

Install dependencies with:

```bash
pip install pydicom
```

---
## Usage
Run the script and provide the requested directories:

```bash
python anonymizeDCM.py
```

Alternatively, you can also run the .exe file in the `/dist` folder.

Either way, You will be prompted for:
- The source dataset directory
- The destination directory for the anonymized dataset
- The name of the output folder