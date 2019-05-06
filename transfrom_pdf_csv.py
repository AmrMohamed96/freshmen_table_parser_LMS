import cv2
import numpy as np
from PIL import Image
import os
import os
import img2pdf
from fpdf import FPDF
import camelot
from PIL import Image
from tabula import read_pdf
from tabula import convert_into


im1 = Image.open("image.jpg")

im_list = [im1]

pdf1_filename = "tester1222.pdf"

im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)

df = read_pdf("tester1222.pdf")
convert_into("tester1222.pdf","tester1222.csv",output_format="csv")