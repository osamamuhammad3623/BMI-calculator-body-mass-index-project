import sys
from os import path
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5.uic import loadUiType

FORM_CLASS,_ = loadUiType(path.join(path.dirname("__file__"),"main.ui"))


class my_form(QMainWindow,FORM_CLASS):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.calculate_btn.clicked.connect(self.calculate_bmi)
        self.clear_btn.clicked.connect(self.clear_all)
        self.show()
        
    def calculate_bmi(self):
        try:  #in case if unvalid numbers
            height = int(self.height_input.text())
            weight = int(self.weight_input.text())
        except:
            self.some_error()
        else:
            try: #in case of division by zero
                bmi_float = (weight / ((height/100) **2))
            except:
                self.some_error()
            else:
                bmi = round(bmi_float, 2)
                self.bmi_result.setText(str(bmi))
                   
                if bmi < 18.5:
                    self.state.setText("You are underweight!")
                elif bmi >= 18.5 and bmi <= 25 :
                    self.state.setText("You are in an optimalweight state!")
                elif bmi > 25 :
                    self.state.setText("You are overweight!")
    
    def clear_all(self):
        self.height_input.clear()
        self.weight_input.clear()
        self.bmi_result.setText(" ")
        self.state.setText(" ")
    
    def some_error(self):
        self.state.setText("Enter valid numbers!")
        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = my_form()
    window.show()
    sys.exit(application.exec_())
    
#osama_muhammad
