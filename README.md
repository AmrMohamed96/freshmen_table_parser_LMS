# FRESHMEN TABLE ANALYZER PROJECT
A desktop application that takes any freshmen timetable as an input and provides the user with his individual section's timetable, away from any hassle and extra unnecessary information

## Getting Started
### Prequisites
You need to install some dependencies before using this project in your virtual environment.
Use the following command from the terminal in your virtual-env to install the dependecies
```
pip install -r requirements.txt
```
This installs the following:
- opencv-python
- numpy
- matplotlib
- camelot-py[cv]
- PyQt5
- imutils
- pdf2image
- Pillow
- pytesseract
- XlsxWriter

You will also need to install:
- ghostscript

For Linux:
```
sudo apt install ghostscript
```

### Installing and Running
Clone this image and open ***main_prog.py*** and run it. This will start the GUI of the application.

## Team Members
- Amr Mohamed Refaat
- Ahmed Ali Emam
- Mohammed Ali Maher
- Omar Salah Hassan
- Nabil Mostafa

## Project Code Concept and Flow 
The project is made modular so that editing parts of the algorithms does not affect the other scripts functionality.

### Image Scanning
The script named ***scan.py*** is used to convert a photo into a document like image.
This part uses the following algorithms
1. Edge Detection
    - Using Canny Edge Detector to convert the image into a binary image with only paper edges visible.

2. Contour Detection
    - Contours are detected, then we find the largest contour and consider this the "screen" that we are looking for.

3. Four Point Transformation
    - A four point algorithm is used that detects the four corner points, calculates warping needed and warps the image to get a top-down bird-eye view of that "screen".

4. Binarization and Adaptive Thresholding
    - Adaptive Thresholding is used to give the image that black and white look. This is the most suitable especially considering bimodal images.

### PDF Coversion
Converting the image created in the previous step into a searchable PDF

### Tabular Data Extraction
The script name ***tabular_extract.py*** is used to extract data from the tables and it the exports the results to an excel file.
Note that the script also returns the extracted table for a desired section number in a list of strings, to be processed by later parts of the script

### Main Program
The main program script ***main_gui.py*** runs the GUI and it views the extracted data for the specific section.

## Known Issues
- Extracted image can not be useful if the resolution is low.
- OCR is having some issues translating images into text

## Built By
- PyCharm (IDE)
- Qt Designer (for GUI)

