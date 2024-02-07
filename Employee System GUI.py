from tkinter import *

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def get_position(self):
        return self.position

    def get_salary(self):
        return self.salary

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_position(self, position):
        self.position = position

    def set_salary(self, salary):
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: ({self.age}), Position: {self.position}, Salary: {self.salary} $"





class EmployeeManagerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Employee Manager")

        # create input field
        self.name_label = Label(master, text="Name:")
        self.name_entry = Entry(master)
        self.age_label = Label(master, text="Age:")
        self.age_entry = Entry(master)
        self.position_label = Label(master, text="Position:")
        self.position_entry = Entry(master)
        self.salary_label = Label(master, text="Salary:")
        self.salary_entry = Entry(master)

        # create buttons
        self.add_button = Button(master, text="Add Employee",  command=self.add_employee)
        self.print_button = Button(master, text="Print Employees", command=self.print_employees)
        self.delete_button = Button(master, text="Delete Employee", command=self.delete_employee)
        self.update_button = Button(master, text="Update Salary",command=self.update_salary)
        self.quit_button = Button(master, text="Quit", command=master.quit)

        # create employee listbox & layout widgets
        self.employee_listbox1 = Listbox(master,width=50)
        self.employee_listbox1.grid(row=7, column=0)
        self.employee_listbox2 = Listbox(master,width=50)
        self.employee_listbox2.grid(row=7, column=1)



        # create input lists layout widgets
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.age_label.grid(row=1, column=0)
        self.age_entry.grid(row=1, column=1)
        self.position_label.grid(row=2, column=0)
        self.position_entry.grid(row=2, column=1)
        self.salary_label.grid(row=3, column=0)
        self.salary_entry.grid(row=3, column=1)



        # create Button layout widgets
        self.add_button.grid(row=4, column=0)
        self.print_button.grid(row=4, column=1)
        self.delete_button.grid(row=5, column=0)
        self.update_button.grid(row=5, column=1)
        self.quit_button.grid(row=6, column=0, columnspan=2)

        # initialize employees list
        self.employees = []




    def add_employee(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        position = self.position_entry.get()
        salary = int(self.salary_entry.get())
        employee = Employee(name, age, position, salary)
        self.employees.append(employee)
        self.employee_listbox1.insert(END, str(employee))



    def print_employees(self):

        self.employee_listbox2.delete(0, END)
        for employee in self.employees:
          self.employee_listbox2.insert(END, str(employee))



    def delete_employee(self):
        selection = self.employee_listbox1.curselection()
        if len(selection) == 1:
            del self.employees[selection[0]]
            self.employee_listbox1.delete(selection[0])





    def update_salary(self):
        selection = self.employee_listbox1.curselection()
        if len(selection) == 1:
            employee = self.employees[selection[0]]
            salary = int(self.salary_entry.get())
            employee.set_salary(salary)
            self.employee_listbox1.delete(selection[0])
            self.employee_listbox1.insert(selection[0], str(employee))



m = Tk()
m.geometry('609x300')
app = EmployeeManagerGUI(m)
m.mainloop()
