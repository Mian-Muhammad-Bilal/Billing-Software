from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QCheckBox, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QCheckBox, QFrame, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys


class BillingSoftware(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mian Cooling Center - Billing Software")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout(self.central_widget)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        # Shop Name
        shop_name_label = QLabel("Mian Cooling Center")
        font = QFont("Helvetica [Cronyx]", 16)
        font.setBold(True)
        shop_name_label.setFont(font)
        self.central_layout.addWidget(
            shop_name_label, alignment=Qt.AlignCenter)

        # Contact Information
        contact_label = QLabel("Contact Information:", self)
        contact_label.setFont(QFont("Helvetica [Cronyx]", 12))
        contact_label.setUnderline(True)
        self.central_layout.addWidget(contact_label, alignment=Qt.AlignCenter)

        phone_label = QLabel("Phone: +123 456 7890", self)
        self.central_layout.addWidget(phone_label, alignment=Qt.AlignCenter)

        email_label = QLabel("Email: info@miancoolingcenter.com", self)
        self.central_layout.addWidget(email_label, alignment=Qt.AlignCenter)

        # Separator Line
        separator_line = QFrame(self)
        separator_line.setFrameShape(QFrame.HLine)
        separator_line.setFrameShadow(QFrame.Sunken)
        self.central_layout.addWidget(separator_line)

        # Compressor Section
        compressor_layout = QHBoxLayout()
        compressor_label = QLabel("Compressor:", self)
        compressor_options = ["Select Compressor",
                              "National", "Denfast", "Espra", "Embraco"]
        self.compressor_combo = QComboBox(self)
        self.compressor_combo.addItems(compressor_options)

        compressor_layout.addWidget(compressor_label)
        compressor_layout.addWidget(self.compressor_combo)
        self.central_layout.addLayout(compressor_layout)

        # Model No and Description (Optional)
        model_layout = QHBoxLayout()
        model_label = QLabel("Model No:", self)
        self.model_entry = QLineEdit(self)

        model_layout.addWidget(model_label)
        model_layout.addWidget(self.model_entry)
        self.central_layout.addLayout(model_layout)

        # Gas Charge Section
        gas_layout = QHBoxLayout()
        gas_label = QLabel("Gas Charge:", self)
        self.gas_entry = QLineEdit(self)

        gas_layout.addWidget(gas_label)
        gas_layout.addWidget(self.gas_entry)
        self.central_layout.addLayout(gas_layout)

        # Freezer Section
        freezer_layout = QHBoxLayout()
        freezer_label = QLabel("Freezer Work:", self)
        self.freezer_checkbox = QCheckBox("Include Freezer Work", self)

        freezer_layout.addWidget(freezer_label)
        freezer_layout.addWidget(self.freezer_checkbox)
        self.central_layout.addLayout(freezer_layout)

        # Condenser Section
        condenser_layout = QHBoxLayout()
        condenser_label = QLabel("Condenser:", self)
        self.condenser_entry = QLineEdit(self)

        condenser_layout.addWidget(condenser_label)
        condenser_layout.addWidget(self.condenser_entry)
        self.central_layout.addLayout(condenser_layout)

        # Filter Section
        filter_layout = QHBoxLayout()
        filter_label = QLabel("Filter:", self)
        self.filter_entry = QLineEdit(self)

        filter_layout.addWidget(filter_label)
        filter_layout.addWidget(self.filter_entry)
        self.central_layout.addLayout(filter_layout)

        # Evaporator Section
        evaporator_layout = QHBoxLayout()
        evaporator_label = QLabel("Evaporator:", self)
        self.evaporator_entry = QLineEdit(self)

        evaporator_layout.addWidget(evaporator_label)
        evaporator_layout.addWidget(self.evaporator_entry)
        self.central_layout.addLayout(evaporator_layout)

        # Button to Calculate Total
        calculate_button = QPushButton("Calculate Total", self)
        calculate_button.setStyleSheet(
            "background-color: #4CAF50; color: white;")
        calculate_button.clicked.connect(self.calculate_total)
        self.central_layout.addWidget(
            calculate_button, alignment=Qt.AlignCenter)

    def calculate_total(self):
        # Add your logic for calculating the total amount based on selected options
        # This function will be called when the user clicks the "Calculate Total" button
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = BillingSoftware()
    main_window.show()
    sys.exit(app.exec_())
