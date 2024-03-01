import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QCheckBox, QFrame, QWidget


class BillingSoftware(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mian Cooling Center - Billing Software")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout(self.central_widget)

        self.setup_ui()

    def save_receipt(self):
        # Get data from the entries and other widgets
        customer_name = self.customer_name_entry.text()
        customer_phone = self.customer_phone_entry.text()
        customer_email = self.customer_email_entry.text()

        compressor_value = self.compressor_combo.currentText()
        model_value = self.model_entry.text()
        gas_value = self.gas_entry.text()
        freezer_value = self.freezer_entry.text()  # Updated reference
        condenser_value = self.condenser_entry.text()
        filter_value = self.filter_entry.text()
        evaporator_value = self.evaporator_entry.text()

        # Create a string with the receipt information
        receipt_info = f"Customer Name: {customer_name}\nCustomer Phone: {customer_phone}\nCustomer Email: {customer_email}\n" \
            f"Compressor: {compressor_value}\nModel No: {model_value}\nGas Charge: {gas_value}\n" \
            f"Freezer Work: {freezer_value}\nCondenser: {condenser_value}\n" \
            f"Filter: {filter_value}\nEvaporator: {evaporator_value}"

        # Save the receipt to a file with a timestamp in the filename
        timestamp = QDateTime.currentDateTime().toString("yyyyMMdd_hhmmss")
        filename = f"receipt_{timestamp}.txt"

        try:
            with open(filename, 'w') as file:
                file.write(receipt_info)
            QMessageBox.information(
                self, "Save Success", f"Receipt saved successfully as {filename}")
        except Exception as e:
            QMessageBox.warning(
                self, "Save Error", f"Error occurred while saving receipt: {str(e)}")

    def setup_ui(self):
        layout = QVBoxLayout()
        # Shop Name
        shop_name_label = QLabel("Mian Cooling Center")
        font = QFont("Helvetica [Cronyx]", 20)
        font.setBold(True)
        shop_name_label.setFont(font)
        self.central_layout.addWidget(
            shop_name_label, alignment=Qt.AlignCenter)

        # self.central_layout.addSpacing(10)  # Adjust the value as needed

        # Contact Information
        contact_label = QLabel("Contact Information:", self)
        contact_label.setStyleSheet("text-decoration: underline;")
        self.central_layout.addWidget(contact_label, alignment=Qt.AlignCenter)

        phone_label = QLabel("Phone: +92 300 123456", self)
        self.central_layout.addWidget(phone_label, alignment=Qt.AlignCenter)

        email_label = QLabel("Email: mian_cooling@yahoo.com", self)
        self.central_layout.addWidget(email_label, alignment=Qt.AlignCenter)

   # Customer Information Section
        customer_layout = QVBoxLayout()
        customer_label = QLabel("Customer Information:", self)
        customer_label.setStyleSheet("text-decoration: underline;")
        self.central_layout.addWidget(customer_label, alignment=Qt.AlignCenter)

        customer_name_layout = QHBoxLayout()
        customer_name_label = QLabel("Name:", self)
        self.customer_name_entry = QLineEdit(self)

        customer_name_layout.addWidget(customer_name_label)
        customer_name_layout.addWidget(self.customer_name_entry)
        customer_layout.addLayout(customer_name_layout)

        customer_phone_layout = QHBoxLayout()
        customer_phone_label = QLabel("Phone:", self)
        self.customer_phone_entry = QLineEdit(self)

        customer_phone_layout.addWidget(customer_phone_label)
        customer_phone_layout.addWidget(self.customer_phone_entry)
        customer_layout.addLayout(customer_phone_layout)

        customer_email_layout = QHBoxLayout()
        customer_email_label = QLabel("Email:", self)
        self.customer_email_entry = QLineEdit(self)

        customer_email_layout.addWidget(customer_email_label)
        customer_email_layout.addWidget(self.customer_email_entry)
        customer_layout.addLayout(customer_email_layout)

        self.central_layout.addLayout(customer_layout)

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
        self.freezer_entry = QLineEdit(self)

        freezer_layout.addWidget(freezer_label)
        freezer_layout.addWidget(self.freezer_entry)
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

        # Button to Save Receipt
        save_button = QPushButton("Save Receipt", self)
        save_button.setStyleSheet(
            "background-color: #3498db; color: white;")
        save_button.clicked.connect(self.save_receipt)
        self.central_layout.addWidget(save_button, alignment=Qt.AlignCenter)

    def calculate_total(self):
        # Add your logic for calculating the total amount based on selected options
        # This function will be called when the user clicks the "Calculate Total" button
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = BillingSoftware()
    main_window.show()
    sys.exit(app.exec_())
