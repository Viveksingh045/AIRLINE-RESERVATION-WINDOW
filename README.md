# AIRLINE-RESERVATION-WINDOW


This project is a Python-based console application that simulates an airline reservation system. It provides functionalities for customer registration, ticket pricing, and displaying customer data.

## Features

- **Customer Registration**: Registers customers with their name, address, journey date, source, and destination.
- **Ticket Pricing**: Calculates ticket costs based on class type and extra luggage charges.
- **Customer Bill Viewing**: Displays specific customer details and their bill.
- **All Customers Overview**: Displays all registered customer details.

## Requirements

To run this project, you need:

- Python 3.x
- MySQL database
- MySQL Connector for Python

## Database Setup

1. The program creates a database named `vivekproject` if it does not exist.
2. It sets up two tables:
   - `pdata`: Stores customer details (Customer Number, Name, Address, Journey Date, Source, Destination).
   - `tkt`: Stores ticket information (Customer Number, Ticket Total, Luggage Total, Grand Total).

## How to Run

1. Install required dependencies:
   ```bash
   pip install mysql-connector-python
   ```

2. Set up a MySQL server and ensure it is running.

3. Modify the database connection details in the script:
   ```python
   mydb = mysql.connect(host="localhost", user="root", passwd="sql1234")
   ```
   Replace `host`, `user`, and `passwd` with your MySQL server's credentials.

4. Run the script:
   ```bash
   python air_test.py
   ```

## Usage

Upon running, the program will present a menu with the following options:

1. **Enter Customer Data**: Register a new customer.
2. **Ticket Amount**: Calculate the ticket price for a customer.
3. **Display Customer Details**: View specific customer details and their bill.
4. **Display All Details**: View all registered customer details.
5. **Exit**: Close the application.

## Example

```text
-------------------------------------------------------------------------
Enter 1: To enter customer data.
Enter 2: For ticket amount.
Enter 3: Display customer-specific details.
Enter 4: Display all details.
Enter 5: Exit.
-------------------------------------------------------------------------
Enter your choice: 1
-------------------------------------------------------------------------
Enter name: John Doe
Enter address: 123 Main Street
Enter date of journey (YYYY-MM-DD): 2024-12-20
Enter source: New York
Enter destination: Los Angeles
-------------------------------------------------------------------------
Customer is Successfully Registered with ID: 789456
```

## Notes

- Ensure that the MySQL server credentials in the script match your setup.
- The script uses random numbers for customer IDs; ensure no conflicts arise if used in a production environment.

## License

This project is open-source and available for modification and distribution under the MIT License.
