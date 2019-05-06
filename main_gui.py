"""
Main GUI Menu

Function:
        This python file contains the main gui
        menu. This is the default menu
        in which the user loads file and enters
        his section number.
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from table_gui import Ui_Dialog

# some global variables that we use and pass
# to the next window
image_path = ''
pdf_path = ''
section_number = 2
save_bool = 1
img_state = 1


class Ui_MainWindow(object):
	# function that opens the next window
	def openWindow(self):
		global img_state, section_number

		# here we check that nothing will throw an error in the next window
		# and pass a list that contains all the required variables for the
		# program to function.
		if section_number == '':
			print("No Section Number Entered.")
			return
		else:
			section_number = int(section_number)

		if image_path == '':
			img_state = 0
			if pdf_path == '':
				print("No image or pdf file selected.")
				return

		if pdf_path == '':
			print("No pdf file selected.")
			return

		if section_number <= 0:
			print("Invalid Section Number.")
			return

		passed_list = [image_path, pdf_path, section_number, save_bool, img_state]
		self.window = QtWidgets.QDialog()
		self.ui= Ui_Dialog()
		self.ui.setupUi(self.window, passed_list)
		self.window.show()

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(624, 678)
		MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(120, 30, 381, 151))
		self.label.setObjectName("label")

		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(120, 210, 381, 91))
		self.label_2.setObjectName("label_2")

		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(160, 350, 301, 61))
		self.label_3.setObjectName("label_3")

		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(160, 429, 301, 81))
		self.label_4.setObjectName("label_4")

		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(160, 520, 301, 71))
		self.label_5.setObjectName("label_5")

		self.useimage = QtWidgets.QPushButton(self.centralwidget)
		self.useimage.setGeometry(QtCore.QRect(160, 350, 301, 61))

		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

		self.useimage.setPalette(palette)
		self.useimage.setText("")
		self.useimage.setFlat(True)
		self.useimage.setObjectName("useimage")

		self.usepdf = QtWidgets.QPushButton(self.centralwidget)
		self.usepdf.setGeometry(QtCore.QRect(160, 440, 301, 61))

		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
		self.usepdf.setPalette(palette)
		self.usepdf.setText("")
		self.usepdf.setFlat(True)
		self.usepdf.setObjectName("usepdf")

		self.exitt = QtWidgets.QPushButton(self.centralwidget)
		self.exitt.setEnabled(True)
		self.exitt.setGeometry(QtCore.QRect(160, 524, 301, 61))

		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
		self.exitt.setPalette(palette)
		self.exitt.setText("")
		self.exitt.setCheckable(False)
		self.exitt.setAutoDefault(False)
		self.exitt.setDefault(False)
		self.exitt.setFlat(True)
		self.exitt.setObjectName("exitt")

		self.entersection = QtWidgets.QLineEdit(self.centralwidget)
		self.entersection.setGeometry(QtCore.QRect(160, 250, 311, 31))
		self.entersection.setObjectName("entersection")

		self.Enter = QtWidgets.QPushButton(self.centralwidget)
		self.Enter.setGeometry(QtCore.QRect(220, 290, 200, 35))

		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
		brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
		brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
		brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
		brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
		brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
		brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
		brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
		brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
		brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
		brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
		brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
		brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
		brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
		brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
		brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)

		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
		self.Enter.setPalette(palette)
		self.Enter.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.Enter.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
		self.Enter.setFlat(False)
		self.Enter.setObjectName("Enter")

		self.label.raise_()
		self.label_2.raise_()
		self.label_3.raise_()
		self.label_4.raise_()
		self.label_5.raise_()

		self.exitt.raise_()
		self.usepdf.raise_()
		self.useimage.raise_()
		self.entersection.raise_()
		self.Enter.raise_()

		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 26))
		self.menubar.setObjectName("menubar")

		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		# open window to choose png image from computer when USE IMAGE button is pressed
		self.useimage.clicked.connect(self.loadImage)

		# open window to choose pdf file from computer when USE IMAGE button is pressed
		self.usepdf.clicked.connect(self.loadpdf)

		# exit program when EXIT button is pressed
		self.exitt.clicked.connect(self.exitapp)

		# enter section number
		self.Enter.clicked.connect(self.yoursection)

		# open the table when Enter button is pressed
		self.Enter.clicked.connect(self.openWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Table Analyzer"))
		self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"PNG/Main-Menu_03.png\"/></p></body></html>"))
		self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"PNG/Main-Menu_06.png\"/></p></body></html>"))
		self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"PNG/Main-Menu_09.png\"/></p></body></html>"))
		self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"PNG/Main-Menu_12.png\"/></p></body></html>"))
		self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"PNG/Main-Menu_15.png\"/></p></body></html>"))
		self.Enter.setText(_translate("MainWindow", "Get My Table"))

	# exit button method
	def exitapp(self):
		sys.exit(app.exec_())

	# load png image method
	def loadImage(self):
		global image_path
		image_path, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select Image","","*.jpg")

	# load pdf file method
	def loadpdf(self):
		global pdf_path
		pdf_path, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select pdf","","*.pdf")

	# section number entry for user
	def yoursection(self):
		global section_number
		section_number = self.entersection.text()


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
