#upcalc-gui.py

'''''''''''''''''''''''''''''''''''''''''''''''''''''
Developed by Juliana Seok (https://github.com/jouleseok)
Start date: August 5, 2025
Purpose: An app for comparing the unit price of grocery store items
    especially when unit conversion is required, e.g:
    $/lb vs $/kg
*** This version is for GUI interface, using PyQt6
'''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys

from PyQt6.QtCore import pyqtSlot, Qt, pyqtSignal

from PyQt6.QtWidgets import(
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTabWidget,
    QPushButton,
    QRadioButton,
    QButtonGroup,
    QLineEdit,
    QLabel,
    QGridLayout
)

# Global constants
ERROR_MSG = "ERROR"
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
DISPLAY_HEIGHT = 35
LABEL_HEIGHT = 35

class UPCalcWindow(QMainWindow):
    """UPCalc's main window (GUI/View)."""

    #class initiator
    def __init__(self):
        super().__init__()
        self.setWindowTitle("jouleseok's Unit Price Comparison App")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.centralWidget = MyTableWidget(self) #parent of all GUI components
        self.setCentralWidget(self.centralWidget)
        self.pushButtonTab1 = self.centralWidget.pushButtonTab1

        self.show()
    
    def setOption1Text(self, text):
         """Set the display's text."""
         self.centralWidget.display1.setText(text)
         self.centralWidget.display1.setFocus() # sets the cursor's focus on the display

    def setOption2Text(self, text):
         """Set the display's text."""
         self.centralWidget.display2.setText(text)
         self.centralWidget.display2.setFocus() # sets the cursor's focus on the display

    def getOption1Text(self):
        """Get Option 1's display text."""
        return self.centralWidget.display1.text()
    
    def getOption2Text(self):
        """Get Option 1's display text."""
        return self.centralWidget.display2.text()
    
    def clearDisplays(self):
        """Clear both displays."""
        self.centralWidget.setOption1Text("")
        self.centralWidget.setOption2Text("")

    def setResultLabelText(self, text):
        self.centralWidget.resultLabel.setText(text)
    
    def getCheckedButton1(self):
        """Get Option 1's units."""
        return self.centralWidget.group1.checkedButton()
    
    def getCheckedButton2(self):
        """Get Option 2's units."""
        return self.centralWidget.group2.checkedButton()

# MyTableWidget class is based on template code from https://pythonspot.com/pyqt5-tabs/
class MyTableWidget(QWidget):

    def _createTab1(self):
        self.tab1.layout = QGridLayout()
        
        # OPTION 1
        self.label1 = QLabel()
        self.label1.setFixedHeight(LABEL_HEIGHT)
        self.label1.setText("Option 1")
        self.tab1.layout.addWidget(self.label1, 0, 0, 1, 4)

        self.display1 = QLineEdit()
        self.display1.setFixedHeight(DISPLAY_HEIGHT)
        self.display1.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.tab1.layout.addWidget(self.display1, 1, 0, 1, 4)

        self.group1 = QButtonGroup()

        rButton1 = QRadioButton("$/g", 1)
        rButton2 = QRadioButton("$/kg", 2)
        rButton3 = QRadioButton("$/oz", 3)
        rButton4 = QRadioButton("$/lb", 4)
        
        self.tab1.layout.addWidget(rButton1, 2, 0)
        self.tab1.layout.addWidget(rButton2, 2, 1)
        self.tab1.layout.addWidget(rButton3, 2, 2)
        self.tab1.layout.addWidget(rButton4, 2, 3)

        self.group1.addButton(rButton1)
        self.group1.addButton(rButton2)
        self.group1.addButton(rButton3)
        self.group1.addButton(rButton4)

        self.gapWidget1 = QWidget()
        self.gapWidget1.setFixedHeight(50)
        self.tab1.layout.addWidget(self.gapWidget1, 3, 0, 1, 4) 
        
        # OPTION 2
        self.label2 = QLabel()
        self.label2.setFixedHeight(LABEL_HEIGHT)
        self.label2.setText("Option 2")
        self.tab1.layout.addWidget(self.label2, 4, 0, 1, 4)

        self.display2 = QLineEdit()
        self.display2.setFixedHeight(DISPLAY_HEIGHT)
        self.display2.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.tab1.layout.addWidget(self.display2, 5, 0, 1, 4)

        self.group2 = QButtonGroup()

        rButton5 = QRadioButton("$/g", 5)
        rButton6 = QRadioButton("$/kg", 6)
        rButton7 = QRadioButton("$/oz", 7)
        rButton8 = QRadioButton("$/lb", 8)
        
        self.tab1.layout.addWidget(rButton5, 6, 0)
        self.tab1.layout.addWidget(rButton6, 6, 1)
        self.tab1.layout.addWidget(rButton7, 6, 2)
        self.tab1.layout.addWidget(rButton8, 6, 3)

        self.group2.addButton(rButton5)
        self.group2.addButton(rButton6)
        self.group2.addButton(rButton7)
        self.group2.addButton(rButton8)

        self.gapWidget2 = QWidget()
        self.gapWidget2.setFixedHeight(50)
        self.tab1.layout.addWidget(self.gapWidget2, 7, 0, 1, 4)

        self.pushButtonTab1 = QPushButton("Compare")
        self.tab1.layout.addWidget(self.pushButtonTab1, 8, 0, 1, 2)

        self.resultLabel = QLabel()
        self.resultLabel.setText("Result placeholder.")  
        self.tab1.layout.addWidget(self.resultLabel, 8, 2, 1, 2)

        self.tab1.setLayout(self.tab1.layout)

    def _createTab2(self):
        self.tab2.layout = QVBoxLayout()
        self.pushButtonTab2 = QPushButton("Tab2 Placeholder")
        self.tab2.layout.addWidget(self.pushButtonTab2)
        self.tab2.setLayout(self.tab2.layout)

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        #Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        #Add tabs
        self.tabs.addTab(self.tab1, "Price per Weight/Mass")
        self.tabs.addTab(self.tab2, "Price per Quantity")

        self._createTab1()
        self._createTab2()

        #Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

def compareOptions(option1, unit1, option2, unit2):
    """Compare unit prices (Model)."""
    # convert units to $/g
    # check input validity

class UpCalc:
    """UpCalc's controller class."""

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()
    
    def _connectSignalsAndSlots(self):
        self._view.centralWidget.pushButtonTab1.clicked.connect(self.onPushButtonTab1Click)

    def onPushButtonTab1Click(self):
        option1 = self._view.getOption1Text()
        option2 = self._view.getOption2Text()
        unit1 = self._view.getCheckedButton1()
        unit2 = self._view.getCheckedButton2()

        print(f"Option1 Text: {option1} Option2 Text: {option2}")

        if option1 == "" or option2 == "":
            resultMessage = "One or more fields blank."    
        elif unit1 == None or unit2 == None:
            resultMessage = "Oops! You forgot units."
        else:
            resultMessage = "All fields complete, well done!"
            compareOptions(option1, unit1, option2, unit2)


        self._view.setResultLabelText(resultMessage)
        
    

def main():
    """UPCalc's main function."""

    QApplication.setStyle('Fusion')
    upcalcApp = QApplication([])

    upcalcWindow = UPCalcWindow()

    ctrl = UpCalc(model=compareOptions, view=upcalcWindow)

    sys.exit(upcalcApp.exec())

if __name__ == "__main__":
    main()