from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget,QVBoxLayout
from PyQt5.QtCore import Qt
import qtable


class window2_object(QWidget):
    def __init__(self, main: qtable.Window):
        super().__init__()
        self.main = main
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(250, 200, 350, 150)
        self.setWindowTitle("Second Window")
        self.UI()
        self.show()

    def UI(self):
        self.MainDesign()
        self.applyLayout()

    def MainDesign(self):
        # ===== Widget Setup =====
        self.main_layout = QVBoxLayout()
        self.name_text = QtWidgets.QLabel("Item Name: ")
        self.name_input = QtWidgets.QLineEdit()
        self.item_amount = QtWidgets.QLabel("Quantity: ")
        self.item_amount_input = QtWidgets.QLineEdit()
        self.price_per_unit = QtWidgets.QLabel("Price Per Unit: ")
        self.price_per_unit_input = QtWidgets.QLineEdit()
        self.add_item_button = QtWidgets.QPushButton("Add Item")

        # ===== Form Layout =====
        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.addRow(self.name_text, self.name_input)
        self.form_layout.addRow(self.item_amount, self.item_amount_input)
        self.form_layout.addRow(self.price_per_unit, self.price_per_unit_input)
        self.bottom_layout = QtWidgets.QHBoxLayout()
        self.bottom_layout.addWidget(self.add_item_button)

    def applyLayout(self):
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.bottom_layout)
        self.setLayout(self.main_layout)




