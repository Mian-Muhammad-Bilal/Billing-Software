from tkinter import messagebox
# import win32ui
# import win32print
# import tkinter as tk
import tkinter as tk
# import win32print
# import win32ui
# import win32con
# from tkinter import messagebox


def calculate_total():
    # Add your logic for calculating the total amount based on selected options
    # This function will be called when the user clicks the "Calculate Total" button
    pass


# Create the main application window
root = tk.Tk()
root.title("Mian Cooling Center - Billing Software")
root.geometry("800x600")
root.configure(bg="#F0F0F0")  # Set the background color


def calculate_total():
    # Add your logic for calculating the total amount based on selected options
    # This function will be called when the user clicks the "Calculate Total" button
    pass


# def print_receipt():
#     # Get data from the entries and other widgets
#     compressor_value = compressor_var.get()
#     model_value = model_entry.get()
#     gas_value = gas_entry.get()
#     freezer_checked = freezer_checkbox.instate(['selected'])
#     condenser_value = condenser_entry.get()
#     filter_value = filter_entry.get()
#     evaporator_value = evaporator_entry.get()

#     # Create a string with the receipt information
#     receipt_info = f"Compressor: {compressor_value}\nModel No: {model_value}\nGas Charge: {gas_value}\n" \
#         f"Freezer Work: {'Yes' if freezer_checked else 'No'}\nCondenser: {condenser_value}\n" \
#         f"Filter: {filter_value}\nEvaporator: {evaporator_value}"

#     try:
#         # Open a printer dialog and print the receipt
#         hprinter = win32print.OpenPrinter(win32print.GetDefaultPrinter())
#         hdc = win32ui.CreateDC()
#         hdc.CreatePrinterDC(hprinter)

#         hdc.StartDoc(receipt_info)
#         hdc.StartPage()

#         # Set the font and print the receipt
#         hdc.SetMapMode(win32con.MM_TWIPS)
#         hdc.SetTextAlign(win32con.TA_LEFT | win32con.TA_TOP)
#         hdc.TextOut(1440, 1440, receipt_info)

#         hdc.EndPage()
#         hdc.EndDoc()
#         hdc.DeleteDC()
#         # win32print.ClosePrinter(hprinter)

#         messagebox.showinfo("Print Success", "Receipt printed successfully!")

#     except Exception as e:
#         messagebox.showerror(
#             "Print Error", f"Error occurred while printing: {str(e)}")


# Run the application
# root.mainloop()


# Add Shop Logo
# Update the path to your logo file
# logo_img = tk.PhotoImage(file="path/to/your/logo.png")
# logo_label = tk.Label(root, image=logo_img, bg="#F0F0F0")
# logo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Add Shop Name
shop_name_label = tk.Label(root, text="Mian Cooling Center", font=(
    "Helvetica", 16, "bold"), bg="#F0F0F0")
shop_name_label.grid(row=1, column=0, columnspan=2, pady=5)

# Add Contact Information
contact_label = tk.Label(root, text="Contact Information:", font=(
    "Helvetica", 12, "underline"), bg="#F0F0F0")
contact_label.grid(row=2, column=0, columnspan=2, pady=5)

phone_label = tk.Label(root, text="Phone: +123 456 7890", bg="#F0F0F0")
phone_label.grid(row=3, column=0, columnspan=2, pady=2)

email_label = tk.Label(
    root, text="Email: info@miancoolingcenter.com", bg="#F0F0F0")
email_label.grid(row=4, column=0, columnspan=2, pady=2)

# Separator Line
separator = tk.Frame(root, height=2, width=800, bg="black")
separator.grid(row=5, column=0, columnspan=2, pady=10)

# Compressor Section
compressor_label = tk.Label(root, text="Compressor:", bg="#F0F0F0")
compressor_label.grid(row=6, column=0, padx=10, pady=10)

compressor_options = ["Select Compressor",
                      "National", "Denfast", "Espra", "Embraco"]
compressor_var = tk.StringVar(root)
compressor_var.set(compressor_options[0])

compressor_menu = tk.OptionMenu(root, compressor_var, *compressor_options)
compressor_menu.grid(row=6, column=1, padx=10, pady=10)

# Model No and Description (Optional)
model_label = tk.Label(root, text="Model No:")
model_label.grid(row=7, column=0, padx=10, pady=10)

model_entry = tk.Entry(root)
model_entry.grid(row=7, column=1, padx=10, pady=10)

# Gas Charge Section
gas_label = tk.Label(root, text="Gas Charge:")
gas_label.grid(row=8, column=0, padx=10, pady=10)

gas_entry = tk.Entry(root)
gas_entry.grid(row=8, column=1, padx=10, pady=10)

# Freezer Section
freezer_label = tk.Label(root, text="Freezer Work:")
freezer_label.grid(row=9, column=0, padx=10, pady=10)

freezer_checkbox = tk.Checkbutton(root, text="Include Freezer Work")
freezer_checkbox.grid(row=9, column=1, padx=10, pady=10)

# Condenser Section
condenser_label = tk.Label(root, text="Condenser:")
condenser_label.grid(row=10, column=0, padx=10, pady=10)

condenser_entry = tk.Entry(root)
condenser_entry.grid(row=10, column=1, padx=10, pady=10)

# Filter Section
filter_label = tk.Label(root, text="Filter:")
filter_label.grid(row=11, column=0, padx=10, pady=10)

filter_entry = tk.Entry(root)
filter_entry.grid(row=11, column=1, padx=10, pady=10)

# Evaporator Section
evaporator_label = tk.Label(root, text="Evaporator:")
evaporator_label.grid(row=12, column=0, padx=10, pady=10)

evaporator_entry = tk.Entry(root)
evaporator_entry.grid(row=12, column=1, padx=10, pady=10)

# Button to Calculate Total
calculate_button = tk.Button(
    # Set the background and text color of the button
    root, text="Calculate Total", command=calculate_total, bg="#4CAF50", fg="white")
calculate_button.grid(row=13, column=0, columnspan=2, pady=20)

# Button to Print Receipt
# print_recipe_button = tk.Button(
# root, text="Print", command=print_receipt, bg="#f44336", fg="white")
# print_recipe_button.grid(row=13, column=2, pady=20)
# Run the application
root.mainloop()
