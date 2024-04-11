import subprocess
import getpass
from fpdf import FPDF
import re


# Global variable to store the destination address
target = ""
subnet=""
rangip=""
dns=""

# --------------------------IP addr validation -----------------------------
def validate_ipv4(address):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return bool(pattern.match(address))

# Function to save the scanning report
def save_report(output):
    save_choice = input("Do you want to save the scanning report? (yes/no): ")
    if save_choice.lower() in ("yes", "y"):
        save_format = input("Choose the format to save the report (1.pdf or 2.txt): ")
        if save_format.lower() in ("pdf", "1"):
            save_to_pdf(output)
        elif save_format.lower() in ("txt", "2"):
            save_to_txt(output)
        else:
            print("Invalid format choice. Report not saved.")
    else:
        print("Scanning report not saved.")

# Function to save the report as PDF
def save_to_pdf(output):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, output)
    pdf_file_name = input("Enter the name for PDF file (without extension): ")
    pdf_file_path = f"{pdf_file_name}.pdf"
    pdf.output(pdf_file_path)
    print(f"PDF report saved as {pdf_file_path}")

# Function to save the report as TXT
def save_to_txt(output):
    txt_file_name = input("Enter the name for TXT file (without extension): ")
    txt_file_path = f"{txt_file_name}.txt"
    with open(txt_file_path, "w") as txt_file:
        txt_file.write(output)
    print(f"TXT report saved as {txt_file_path}")

# Function to run a command and handle the output
def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        output = output.decode('utf-8')
        print(output)
        save_report(output)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output.decode('utf-8')}")

# Function to perform ping sweep
def ping_sweep():
    subnet= input("Enter target subnet 18/24/64: ")
    try:
        
        command = f" nmap -sP {target}/{subnet}"
        run_command(command)
    except Exception as e:
        print(f"Error: {str(e)}")

# Function to perform port scanning
def port_scan():
    try:
        command = f" nmap {target}"
        run_command(command)
    except Exception as e:
        print(f"Error: {str(e)}")

# Function to authenticate users
def authenticate():
    # Hardcoded username and password (replace with your authentication mechanism)
    correct_username = "a"
    correct_password = "a"

    # Ask for username and password
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    # Check if the entered credentials are correct
    if username == correct_username and password == correct_password:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed. Please try again.")
        return False

# Function to handle Nmap options
def nmap_options():
    while True:
        print("\nChoose an option:")
        print("1. Port Scan")
        print("2. Ping Sweep")
        print("3. Display System Info")
        print("4. Back to Tools list")

        choice = input("Enter your choice: ")

        if choice == '1':
            port_scan()
        elif choice == '2':
            ping_sweep()
        elif choice == '3':
            print("Display System Info functionality not implemented.")
        elif choice == '4':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# Main function
def main():
    global target
    authenticated = False
    while not authenticated:
        authenticated = authenticate()
    while True:
        target = input("Enter target IP : ")
        if validate_ipv4(target):
            break
        else:
            print("Invalid IPv4 address format. Please enter a valid IPv4 address.")



    while True:
        print("\nSelect tool to explore:")
        print("1. Nmap")
        print("2. Tshark")
        print("3. Nmap")
        print("4. Tshark")
        print("5. Exit")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            nmap_options()
        elif choice == '2':
            print("Nikito functionality not implemented.")
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

if __name__ == "__main__":
    main()
