import numpy as np
import cv2 as cv
import utils
from table import Table
import xlsxwriter
from scan import scan_img
"""
Main Program Code

Function:
        This python script has the core algorithm.
        It uses the prepared scan.py method to get the 
        table from a photographed table.
        It then runs a series of processes to detect table
        edges, cells, boundaries and text.
"""

def conversion_algorithm(path):
    # scanning the image, applying perspective warping
    # and adaptive thresholding
    filtered, warped = scan_img(path)

    # line isolation
    SCALE = 23

    # isolate horizontal and vertical lines using morphological operations
    horizontal = filtered.copy()
    vertical = filtered.copy()

    horizontal_size = int(horizontal.shape[1] / SCALE)
    horizontal_structure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))
    utils.isolate_lines(horizontal, horizontal_structure)

    vertical_size = int(vertical.shape[0] / SCALE)
    vertical_structure = cv.getStructuringElement(cv.MORPH_RECT, (1, vertical_size))
    utils.isolate_lines(vertical, vertical_structure)

    # TABLE EXTRACTION
    # create an image mask with just the horizontal
    # and vertical lines in the image. Then find
    # all contours in the mask.
    mask = horizontal + vertical
    cv.imwrite("processing_data/detected_lines.jpg", mask)
    (contours, _) = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # find intersections between the lines
    # to determine if the intersections are table joints.
    intersections = cv.bitwise_and(horizontal, vertical)

    # get tables from the images
    tables = [] # list of tables
    for i in range(len(contours)):
        # verify that region of interest is a table
        (rect, table_joints) = utils.verify_table(contours[i], intersections)
        if rect == None or table_joints == None:
            continue

        # create a new instance of a table
        table = Table(rect[0], rect[1], rect[2], rect[3])

        # get an n-dimensional array of the coordinates of the table joints
        joint_coords = []
        for i in range(len(table_joints)):
            joint_coords.append(table_joints[i][0][0])
        joint_coords = np.asarray(joint_coords)

        # returns indices of coordinates in sorted order
        # sorts based on parameters (aka keys) starting from the last parameter, then second-to-last, etc
        sorted_indices = np.lexsort((joint_coords[:, 0], joint_coords[:, 1]))
        joint_coords = joint_coords[sorted_indices]

        # store joint coordinates in the table instance
        table.set_joints(joint_coords)

        tables.append(table)

        cv.rectangle(warped, (table.x, table.y), (table.x + table.w, table.y + table.h), (0, 255, 0), 1, 8, 0)
        cv.imwrite("processing_data/table_boundaries.jpg", warped)

    # # OCR AND WRITING TEXT TO EXCEL
    # out = "bin/"
    # table_name = "table.jpg"
    # psm = 6
    # oem = 3
    # mult = 3
    #
    # utils.mkdir(out)
    # utils.mkdir("bin/table/")
    #
    # utils.mkdir("excel/")
    # workbook = xlsxwriter.Workbook('excel/tables.xlsx')
    #
    # for table in tables:
    #     worksheet = workbook.add_worksheet()
    #
    #     table_entries = table.get_table_entries()
    #
    #     table_roi = image[table.y:table.y + table.h, table.x:table.x + table.w]
    #     table_roi = cv.resize(table_roi, (table.w * mult, table.h * mult))
    #
    #     cv.imwrite(out + table_name, table_roi)
    #
    #     num_img = 0
    #     for i in range(len(table_entries)):
    #         row = table_entries[i]
    #         for j in range(len(row)):
    #             entry = row[j]
    #             entry_roi = table_roi[entry[1] * mult: (entry[1] + entry[3]) * mult, entry[0] * mult:(entry[0] + entry[2]) * mult]
    #
    #             fname = out + "table/cell" + str(num_img) + ".jpg"
    #             cv.imwrite(fname, entry_roi)
    #
    #             fname = utils.run_textcleaner(fname, num_img)
    #             text = utils.run_tesseract(fname, num_img, psm, oem)
    #
    #             num_img += 1
    #
    #             worksheet.write(i, j, text)
    #
    # workbook.close()


if __name__ == '__main__':
    conversion_algorithm('resources/input/test_img.jpg')