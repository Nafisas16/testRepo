class Employee:
    """
    Employee Class adalah Class untuk membuat object pegawai.
    """

    raise_amount = 1.10
    employee_id = 10000

    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.payment = pay
        

        self.email = (f'{self.firstname.lower()}.{self.lastname.lower()}@outlook.com')
        Employee.employee_id += 1
        self.id = Employee.employee_id

    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    def apply_raise (self):
        self.payment = int(self.payment * self.raise_amount)
    

emp_1 = Employee('nafis', 'ahmad', 8000000)
emp_2 = Employee('brian', 'latu', 2000000)


print(Employee.__doc__)


print(emp_1.firstname)
print(emp_1.fullname())
print(emp_1.email)
print('ID karyawan saya', emp_1.id)
print('gaji sekarang sebesar', emp_1.payment)
print('rate kenaikan gaji',emp_1.raise_amount)
emp_1.apply_raise()  # agar rumus masuk ke output
print('gaji setelah kenaikan',emp_1.payment)
print(emp_1.__dict__)


print(emp_2.firstname)
print(emp_2.fullname())
print(emp_2.email)
print(emp_2.id)
print('gaji skearang sebesar',emp_2.payment)
# print('kenaikan gaji brian', emp_2.raise_amount)
emp_2.raise_amount = 1.20
print('rate kenaikan gaji', emp_2.raise_amount)
emp_2.apply_raise()
print('gaji sekarang setelah kenaikaan sebesar', emp_2.payment)
print(emp_2.__dict__)



# print(emp_2.firstname)
# print(emp_2.payment)

# print(Employee.__doc__)