# -*- coding: utf-8 -*-
"""pythonproject(assia)ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ot5miNBN5vI5Vq5ylX1d0rn0UwwbGiyi
"""

import json

class Employee:

  def __init__(self , ID , Name, Position , Salary , Email):
    self.ID = ID
    self.Name = Name
    self.Position = Position
    self.Salary = Salary
    self.Email = Email

  def display_employee(self):
       return {
            "ID": self.ID,
            "Name": self.Name,
            "Position": self.Position,
            "Salary": self.Salary,
            "Email": self.Email
        }

class EmployeeManager:

  def __init__(self):
    self.employees = {}

  def add_employee(self):
    ID = input("Enter the employee ID: ")
    if ID in self.employees:
        print("This employee already exists.")
        return
    else:
        Name = input("Enter the employee name: ")
        Position = input("Enter the employee's position: ")
        Salary = input("Enter the employee's salary: ")
        Email = input("Enter the employee's email: ")
        employee = Employee(ID, Name, Position, Salary, Email)
        self.employees[ID] = employee
        print("Employee's data added successfully.")
        print("Data of employee you have been added:", employee.display_employee())
        self.savingdatatojso()

  def List_All_Employees(self):
      if not self.employees:
            print("No employees found!")
            return
      print("Information of employees:")
      for emp in self.employees.values():
            print(emp.display_employee())

  def Updating_an_employeedata(self,ID, Name=None, Position=None, Salary=None, Email=None):
     if ID in self.employees:
        new_employee = self.employees[ID]
        if Name:
            new_employee.Name = Name
        if Position:
            new_employee.Position = Position
        if Salary:
            new_employee.Salary = Salary
        print("Employee's data updated successfully.")
        print("Data of employee you have updated:",new_employee.display_employee())
        self.savingdatatojso()
     else:
        print("This employee can't be found!")

  def deleting_an_employeedata(self,ID):
     if ID in self.employees:
        deleted_an_employee = self.employees.pop(ID)
        print("Employee's data deleted successfully!")
        print("Data of employee you have deleted:",deleted_an_employee.display_employee())
        self.savingdatatojso()
     else:
        print("This employee can't be found!")

  def Searching_for_anemployee(self,ID):
    if ID in self.employees:
      search = self.employees[ID]
      print("The employee you are searching for:",search.display_employee())
    else:
      print("This employee cant be found!")

  def savingdatatojso(self):
    try:
      Employees_data = [emp.display_employee() for emp in self.employees.values()]
      with open('Employees.json', 'w') as json_file:
         json.dump(Employees_data, json_file, indent=4)

    except:
       print("There's an issue")

obj = EmployeeManager()
print("processes:\n","1-Add an employee.\n",
      "2-List all employees.\n","3-Update an employee data.\n",
      "4-searching for an employee.\n","5-Deleting an employee.\n","6-Stop.")

while True:
    Number = int(input("What process do you want to do? "))

    if Number == 1:
        obj.add_employee()

    elif Number == 2:
        obj.List_All_Employees()

    elif Number == 3:
        obj_id = input("Enter the employee ID to update: ")
# Leave the input blank if you do not want to update a specific field
        name = input("Enter new employee name: ")
        position = input("Enter new employee's position: ")
        salary = input("Enter new employee's salary: ")
        email = input("Enter new employee's email: ")
        obj.Updating_an_employeedata(obj_id, name, position, salary, email)

    elif Number == 4:
        obj_id = input("Enter the employee ID to search: ")
        obj.Searching_for_anemployee(obj_id)

    elif Number == 5:
        obj_id = input("Enter the employee ID to delete: ")
        obj.deleting_an_employeedata(obj_id)

    else:
        print("thank you.")
        break

