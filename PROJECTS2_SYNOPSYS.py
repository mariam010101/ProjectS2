class Employee:
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        self.emp_id = emp_id
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_gross_salary(self):
        return self.hourly_rate * self.hours_worked

    def calculate_tax(self, gross_salary):
        if gross_salary <= 1000:
            return gross_salary * 0.10  # 10% tax
        elif gross_salary <= 2000:
            return gross_salary * 0.15  # 15% tax
        else:
            return gross_salary * 0.20  # 20% tax

    def calculate_deductions(self, gross_salary):
       
        health_insurance = 100
        tax = self.calculate_tax(gross_salary)
        return tax + health_insurance

    def calculate_net_salary(self):
        gross = self.calculate_gross_salary()
        deductions = self.calculate_deductions(gross)
        return gross - deductions

    def generate_payslip(self):
        gross = self.calculate_gross_salary()
        tax = self.calculate_tax(gross)
        deductions = self.calculate_deductions(gross)
        net = self.calculate_net_salary()

        print("\n----- PAYSLIP -----")
        print(f"Employee ID   : {self.emp_id}")
        print(f"Name          : {self.name}")
        print(f"Hours Worked  : {self.hours_worked}")
        print(f"Hourly Rate   : ${self.hourly_rate:.2f}")
        print(f"Gross Salary  : ${gross:.2f}")
        print(f"Tax Deducted  : ${tax:.2f}")
        print(f"Other Deductions (Health insurance): ${deductions - tax:.2f}")
        print(f"Net Salary    : ${net:.2f}")
        



if __name__ == "__main__":
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    hourly_rate = float(input("Enter Hourly Rate ($): "))
    hours_worked = float(input("Enter Hours Worked: "))

    employee = Employee(emp_id, name, hourly_rate, hours_worked)
    employee.generate_payslip()
