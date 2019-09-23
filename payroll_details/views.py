from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Employee, MonthlySalaryDetail
from payroll_details.forms import SalaryMonthYear, SalaryMail


def index(request):
    all_employees = Employee.objects.all()
    template = loader.get_template('payroll_details/index.html')
    context = {'all_employees': all_employees}
    return HttpResponse(template.render(context, request))


def salary(request, emp_id):
    st = ""
    for x in MonthlySalaryDetail.objects.all():
        if int(x.emp.e_id) == int(emp_id):
            st += str(x.salary_calculation())
    if st == "":
        return HttpResponse("<h3>No Salary records found. Please add the necessary details. "
                            "<a href='../admin/payroll_details/monthlysalarydetail/'>Click "
                            "Here</a></h3><a href='../'>Go Back</a>")
    return HttpResponse("<p>" + st + "</p>")


def sal(request, emp_id):
    for x in Employee.objects.all():
        if int(x.e_id) == int(emp_id):
            employee = x

    if request.method == "POST":
        # Get the posted form
        salaryform = SalaryMonthYear(request.POST)
    else:
        salaryform = SalaryMonthYear()

    salitem = ''
    for x in MonthlySalaryDetail.objects.all():
        if x.emp.e_id == employee.e_id and salaryform.data['year'] == str(x.salary_year) and salaryform.data[
            'month'] == x.salary_month:
            salitem = x
            break

    return render(request, 'payroll_details/SalaryEmployee.html',
                  {"salaryform": salaryform, "salitem": salitem, "employee": employee})


def sal_mail(request, emp_id):
    if request.method == "POST":
        # Get the posted form
        form = SalaryMail(request.POST)
    else:
        form = SalaryMail()

    subject = "Payslip for the month : "+form.data['month']+" and year : "+form.data['year']
    message = form.data['msg']
    from_email = settings.EMAIL_HOST_USER
    to_list = [form.data['mailid'], settings.EMAIL_HOST_USER]
    send_mail(subject, message, from_email, to_list, fail_silently=True)

    return render(request, 'payroll_details/SalaryEmployeeMailSuccess.html',
                  {"form": form})


def salary_details(request, emp_id):
    for x in Employee.objects.all():
        if int(x.e_id) == int(emp_id):
            employee = x
    years = []
    months = []
    for x in MonthlySalaryDetail.objects.all():
        if x.emp == employee:
            if x.salary_month not in months:
                months.append(x.salary_month)
            if x.salary_year not in years:
                years.append(x.salary_year)
    context = {'employee': employee,
               'months': months,
               'years': years}
    return render(request, 'payroll_details/SalaryDetails.html', context)


def emp_details(request, emp_id):
    for x in Employee.objects.all():
        if int(x.e_id) == int(emp_id):
            employee = x
    context = {'employee': employee}
    return render(request, 'payroll_details/EmployeeDetails.html', context)
