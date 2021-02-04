from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import window2
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Vertical Box layout")
        self.setGeometry(150, 150, 400, 400)
        self.UI_setup()
        self.show()


    def UI_setup(self):
        self.createLayout()
        self.AddEntryFunc()

    def AddEntryFunc(self):
        self.button1.clicked.connect(self.launch_second_window)

    def createLayout(self):
        self.main_layout = QVBoxLayout()
        self.bottom_layout = QHBoxLayout()
        self.fill_form_box = QAbstractSpinBox()
        self.main_layout.addLayout(self.bottom_layout)
        self.table_widget = QTableWidget()
        self.button1 = QPushButton("Add Item")
        self.bottom_layout.addWidget(self.table_widget)
        self.bottom_layout.addWidget(self.button1)
        self.setLayout(self.main_layout)


        # ==== Table Methods ====
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(4)
        self.table_widget.setColumnWidth(0, 150)
        self.table_widget.setFixedWidth(624)
        # self.table_widget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_widget.setHorizontalHeaderItem(0, QTableWidgetItem("Item"))
        self.table_widget.setHorizontalHeaderItem(1, QTableWidgetItem("Price Per Unit"))
        self.table_widget.setHorizontalHeaderItem(2, QTableWidgetItem("Quantity"))
        self.table_widget.setHorizontalHeaderItem(3, QTableWidgetItem("Item Total"))
        print(self.table_widget.verticalHeader().width())
        self.table_widget.verticalHeader().hide()
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers) #Switch Off edits
        # self.table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def print_length(self):
        print(self.table_widget.rowCount())

    def launch_second_window(self):
        try:
            self.cw = window2.window2_object(self)
        except Exception as e:
            print(e)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()

