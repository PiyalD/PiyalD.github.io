from django.db import models


class Employee(models.Model):
    e_id = models.IntegerField("Employee ID")
    e_fname = models.CharField("First Name", max_length=250)
    e_mname = models.CharField("Middle Name", max_length=250, default=None)
    e_lname = models.CharField("Last Name", max_length=250)
    e_age = models.IntegerField("Age")
    e_phone = models.IntegerField("Phone")
    e_email = models.CharField("Email", max_length=250)
    e_CTC_Year = models.IntegerField("CTC p.a")

    def __str__(self):
        return "First Name : " + str(self.e_fname) + "\nMiddle Name : " + str(
            self.e_mname) + "\nLast Name : " + str(self.e_lname) + "\nAge : " + str(
            self.e_age) + "\nPhone : " + str(self.e_phone) + "\nEmail : " + str(self.e_email)


class MonthlySalaryDetail(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_month = models.CharField("Salary Month", max_length=15)
    salary_year = models.IntegerField("Salary Year")
    no_of_days = models.IntegerField("No. of working days")
    no_of_days_worked = models.IntegerField("No. of days worked")
    other_allowances = models.FloatField("Other Allowances")
    other_deductions = models.FloatField("Other Deductions")

    def salary_calculation(self):

        # Earning Summary
        self.CTC_Year = self.emp.e_CTC_Year
        self.CTC_Monthly = int(self.CTC_Year) // 12
        self.basic_salary = self.CTC_Monthly
        self.da_salary = self.basic_salary * 0.20
        self.hra_salary = self.basic_salary * 0.50
        self.ca_salary = 800
        self.total_earning = self.basic_salary + self.hra_salary + self.da_salary + self.ca_salary + self.other_allowances
        st = "*************************************************************************"
        st = st + "\nSALARY STRUCTURE for the Month : " + str(self.salary_month) + " and Year : " + str(
            self.salary_year) + " for Employee :\n" + str(
            self.emp)
        st = st + "\n\nSALARY STATEMENT :\nCTC per year : Rs. " + str(self.CTC_Year)
        st = st + "\nCTC per month : Rs. " + str(self.CTC_Monthly)
        st = st + "\n\nEARNINGS : \nBasic : Rs. " + str(self.basic_salary)
        st = st + "\nDearness Allowance(DA) : Rs. " + str(self.da_salary)
        st = st + "\nHouse Rent Allowance(HRA) : Rs. " + str(self.hra_salary)
        st = st + "\nConveyance Allowance(CA) : Rs. " + str(self.ca_salary)
        st = st + "\nOther Allowance : Rs. " + str(self.other_allowances)
        st = st + "\nTotal Earning : Rs. " + str(self.total_earning)

        # Deduction Summary
        self.pf_salary = (self.basic_salary + self.da_salary) * 0.12
        self.pt_salary = self.total_earning * 0.005
        if self.CTC_Year <= 250000:
            self.tds_salary = 0.00
        elif 250000 < self.CTC_Year < 500000:
            self.tds_salary = (self.CTC_Year * 0.05) // 12
        elif 500000 < self.CTC_Year < 1000000:
            self.tds_salary = 12500 + ((self.CTC_Year * 0.20) // 12)
        elif self.CTC_Year >= 1000000:
            self.tds_salary = 112500 + ((self.CTC_Year * 0.30) // 12)
        self.total_deductions = self.pf_salary + self.pt_salary + self.tds_salary
        self.total = self.total_earning - self.total_deductions
        st = st + "\n\nDEDUCTIONS : \nProvident Fund(PF) : Rs. " + str(self.pf_salary)
        st = st + "\nProfessional Tax(PT) : Rs. " + str(self.pt_salary)
        st = st + "\nTax Deducted at Source(TDS) : Rs. " + str(self.tds_salary)
        st = st + "\nOther Deductions : Rs. " + str(self.other_deductions)
        st = st + "\nTotal Deductions : Rs. " + str(self.total_deductions)
        st = st + "\nTotal Take-away Salary : Rs. " + str(self.total)

        # Leave Summary for x in Leave.objects.all(): if x.salary_month == self.salary_month and x.salary_year ==
        # self.salary_year and x.emp.e_id == self.emp.e_id:

        # self.no_of_days = x.no_of_days
        self.no_of_days_leave = self.no_of_days - self.no_of_days_worked
        # break
        self.amount_to_deduct_for_leave = (self.total // self.no_of_days) * self.no_of_days_leave
        st = st + "\n\nLEAVE DETAILS : \nNumber of working days : " + str(self.no_of_days)
        st = st + "\nNumber of days leave : " + str(self.no_of_days_leave)
        st = st + "\nAmount to be deducted : Rs. " + str(self.amount_to_deduct_for_leave)
        self.nettotal = self.total - self.amount_to_deduct_for_leave
        st = st + "\nNet Take-away Salary : Rs. " + str(self.nettotal)
        st = st + "\n\n*************************************************************************"
        self.statement = st
        return "Salary Calculated. Here are the details : "
