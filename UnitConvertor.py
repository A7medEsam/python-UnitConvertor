import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QComboBox )
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

#MAIN UNITS AND THEIR CONVERSION RATE -----------------------------------------

Mass = {
    "kilogram" : 1,
    "Gram": 0.001,
    "Tons": 1000,
    "Pounds" : 0.45359
}

MassKeys = []
for key in Mass:
    MassKeys.append(key)

Length = {
    "Meters" : 1,
    "Centimeters": 0.01,
    "kilometers" : 1000,
    "Millimeters" : 0.001
}

LengthKeys = []
for key in Length:
    LengthKeys.append(key)

Temp = {
    "Celsius(C)" : 1,
    "Fahrenheit(F)": -17.22,
}

TempKeys = []
for key in Temp:
    TempKeys.append(key)

#CHOSEN CATEGORY --------------------------------------------------------------

MassChosen = True
LengthChosen = False
TempChosen = False

#MAIN WINDOW CLASS ------------------------------------------------------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,700)
        self.setWindowTitle("Unit Convertor")
        self.initUI()

#INITIALIZING LAYOUT ----------------------------------------------------------

    def initUI(self):
        self.box1 = QWidget(self)
        self.box2 = QWidget(self)
        self.central = QWidget(self)
        self.SideBar = QWidget(self)

# MAINWIDGET --------------------------------------------------------

        self.MainWidgetLayout = QVBoxLayout()
        self.setCentralWidget(self.central)
        self.MainWidgetLayout.addWidget(self.box1)
        self.MainWidgetLayout.addWidget(self.box2)
        self.MainWidgetLayout.addWidget(self.SideBar)
        self.central.setLayout(self.MainWidgetLayout)

#SIDE BAR ---------------------------------------------------------------

        self.SideBar_Layout = QVBoxLayout(self.SideBar)

        self.mass_btn = QPushButton("Mass")
        self.length_btn = QPushButton("Length")
        self.temp_btn = QPushButton("Temperature")

        self.SideBar_Layout.addWidget(self.mass_btn)
        self.SideBar_Layout.addWidget(self.length_btn)
        self.SideBar_Layout.addWidget(self.temp_btn)

#BOX 1 ---------------------------------------------------------------

        self.UnitFrom = QLineEdit(self.box1)
        self.UnitFrom.setValidator(QDoubleValidator())
        self.UnitFrom.textEdited.connect(self.Unit_convert)
        self.UnitChooseFrom = QComboBox(self.box1)
        if MassChosen:
            self.UnitChooseFrom.addItems(MassKeys)
            self.mass_btn.setDisabled(True)
        elif LengthChosen:
            self.UnitChooseFrom.addItems(LengthKeys)
            self.length_btn.setDisabled(True)
        elif TempChosen:
            self.UnitChooseFrom.addItems(TempKeys)
            self.temp_btn.setDisabled(True)
            
        self.box1Layout = QHBoxLayout()
        self.box1Layout.addWidget(self.UnitFrom)
        self.box1Layout.addWidget(self.UnitChooseFrom)
        self.box1.setLayout(self.box1Layout)

#BOX 2 ---------------------------------------------------------------
        self.UnitTo = QLineEdit(self.box2)
        self.UnitTo.setValidator(QDoubleValidator())
        self.UnitChooseTo = QComboBox(self.box2)
        self.UnitChooseTo.addItems(MassKeys)

        self.box2Layout = QHBoxLayout()
        self.box2Layout.addWidget(self.UnitTo)
        self.box2Layout.addWidget(self.UnitChooseTo)
        self.box2.setLayout(self.box2Layout)

#CLICKED BUTTONS ----------------------------------------------------------

        self.mass_btn.clicked.connect(lambda:self.list_update(MassKeys))
        self.length_btn.clicked.connect(lambda:self.list_update(LengthKeys))
        self.temp_btn.clicked.connect(lambda:self.list_update(TempKeys))

#CSS STYLING --------------------------------------------------------------

        self.setStyleSheet("""
        QMainWindow{
        background-color:#EAE2D6;
        }
        QLineEdit{
        background-color : #F7F2EB;
        padding : 10px;
        border : solid 3px green
        }
        QLIneEdit:hover{
        background-color : #8B9A6E;
        }
        QComboBox{
        padding : 10px;
        background-color : #F7F2EB;
        border : solid 0px ;
        }
        QPushButton{
        background-color:#8B9A6E;
        padding : 20px ;
        border-radius: 6px;
        color: white;
        font-size: 15px;
        font-weight: bold;
        }
        QPushButton:hover{
        background-color:#EAE2D6;
        border: 2px solid #8B9A6E;
        }
""")

#UNIT ENABLE FUNCTIONS ----------------------------------------------------

    def list_update(self, keys):
        if "kilogram" in keys:
            self.mass_btn.setDisabled(True)
            self.length_btn.setEnabled(True)
            self.temp_btn.setEnabled(True)
        elif "Meters" in keys:
            self.mass_btn.setEnabled(True)
            self.length_btn.setDisabled(True)
            self.temp_btn.setEnabled(True)
        else:
            self.mass_btn.setEnabled(True)
            self.length_btn.setEnabled(True)
            self.temp_btn.setDisabled(True)

        self.UnitChooseFrom.clear()
        self.UnitChooseTo.clear()
        self.UnitChooseFrom.addItems(keys)
        self.UnitChooseTo.addItems(keys)

#UNIT CONVERSION FUNCTION -------------------------------------------------

    def Unit_convert(self):
        if self.UnitFrom.text():
            ExtractedFromNumber = float(self.UnitFrom.text())
        else:
            return 
        ExtractedFromUnit = self.UnitChooseFrom.currentText()
        ExtractedToUnit = self.UnitChooseTo.currentText()
        if ExtractedFromUnit in Mass and ExtractedToUnit in Mass:
            ConvertFromBaseRate = Mass[ExtractedFromUnit]
            ConvertToBaseRate = Mass[ExtractedToUnit]
        elif ExtractedFromUnit in Length and ExtractedToUnit in Length:
            ConvertFromBaseRate = Length[ExtractedFromUnit]
            ConvertToBaseRate = Length[ExtractedToUnit]  
        elif ExtractedFromUnit == "Celsius(C)" and ExtractedToUnit == "Fahrenheit(F)":
            Result = (9/5 * ExtractedFromNumber) + 32
        elif  ExtractedFromUnit == "Fahrenheit(F)" and ExtractedToUnit == "Celsius(C)":
            Result = 5/9 *(ExtractedFromNumber -32)
        else :
            Result = ExtractedFromNumber

        if ExtractedFromUnit in Temp:
            self.UnitTo.setText(str(Result))
        else:
            NumberInBase = ExtractedFromNumber * ConvertFromBaseRate
            Result = NumberInBase / ConvertToBaseRate
            self.UnitTo.setText(str(Result))


#MAIN FUNCTION ------------------------------------------------------------

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

#DIRECT RUN ------------------------------------------------------------

if __name__ == "__main__":
    main()