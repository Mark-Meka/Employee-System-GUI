# Employee Manager GUI Application

This Python program is a graphical user interface (GUI) application for managing employee information using Tkinter. It allows users to add, view, delete, and update the salary of employees.

## Features

- **Add Employee**: Add a new employee by entering their name, age, position, and salary.
- **Print Employees**: Display a list of all employees in the system.
- **Delete Employee**: Remove an employee from the system by selecting them from the list.
- **Update Salary**: Update the salary of a selected employee.

## Classes

- `Employee`: Represents an employee with attributes for name, age, position, and salary. It includes methods to get and set these attributes.
- `EmployeeManagerGUI`: Manages the GUI components and interactions for the employee management system.

## GUI Components

- **Input Fields**: Text entry fields for entering employee name, age, position, and salary.
- **Buttons**: Buttons for adding an employee, printing employee details, deleting an employee, and updating an employee's salary.
- **List Boxes**: Two list boxes are used to display added employees and print employee details.

## Usage

1. **Run the Program**: Execute the script to launch the GUI application.
2. **Add an Employee**: Fill in the input fields for name, age, position, and salary, and then click the "Add Employee" button.
3. **View Employees**: Click the "Print Employees" button to display the list of all employees in the second list box.
4. **Delete an Employee**: Select an employee from the first list box and click the "Delete Employee" button to remove them from the system.
5. **Update an Employee's Salary**: Select an employee from the first list box, enter the new salary in the salary input field, and click the "Update Salary" button.
6. **Quit**: Click the "Quit" button to exit the application.

## Installation

Ensure you have Python installed on your system. This program requires the Tkinter library, which is included in standard Python installations.

## Running the Program

To run the program, navigate to the directory containing the script and execute it using Python:

```bash
python employee_manager_gui.py

