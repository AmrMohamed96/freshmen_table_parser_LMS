import matplotlib.pyplot as plt
from camelot import read_pdf
"""
Tabular Data Extraction

Function:
		Takes a pdf and extracts the tables
		as data frames in python.
		The data can be optionally saved to excel
		or csv format
"""


def extract_table(path, section, save):
	if save == 1:
		tables = read_pdf(path, line_scale=25, copy_text=['h', 'v'], shift_text=['l', 't'])
		whole_table = tables[0].df
		whole_table.to_excel('resources/table_output/extracted.xlsx', sheet_name='Whole Table')

		# debugging lines: used to detect
		# the extracted table lines
		#camelot.plot(tables[0],kind='grid')
		#plt.show()

		# detecting which column to extract based on
		# section number

		# checks if the user input is correct
		if section <= 0:
			print("Invalid Section Number")
			return -1

		if section <= 7:
			section_data = tables[0].df
			section_extract = section_data.loc[2:73, section+2]
			section_extract.to_excel('resources/table_output/sec_' + str(section) + '.xlsx', sheet_name='Sheet1')
			section_data_list = section_extract.values.tolist()
			return section_data_list

		elif section >7:
			section = (section // 7)
			section_data = tables[0].df
			section_extract = section_data.loc[2:73, section+2]
			section_extract.to_excel('resources/table_output/sec_' + str(section) + '.xlsx', sheet_name='Sheet1')
			section_data_list = section_extract.values.tolist()
			return section_data_list

	else:
		tables = read_pdf(path, line_scale=25, copy_text=['h', 'v'], shift_text=['l', 't'])

		# debugging lines: used to detect
		# the extracted table lines
		# camelot.plot(tables[0],kind='grid')
		# plt.show()

		# detecting which column to extract based on
		# section number
		if section <= 7:
			section_data = tables[0].df
			section_extract = section_data.loc[2:73, section + 2]
			section_data_list = section_extract.values.tolist()
			return section_data_list

		elif section > 7:
			section = (section // 7)
			section_data = tables[0].df
			section_extract = section_data.loc[2:73, section + 2]
			section_data_list = section_extract.values.tolist()
			return section_data_list


if __name__ == '__main__':
	extract_table('resources/input/2.pdf', 1, 1)
	print("Done")
