from django.http import HttpResponseRedirect
from django.shortcuts import render
from hoteladmin.models import *


def customer_checkout(request, customer_id):
    print(request)
    print(customer_id)
    return HttpResponseRedirect('/list/customer/')


def reservation_cancel(request, reservation_id):
    print(request)
    print(reservation_id)
    return HttpResponseRedirect('/list/reservation/')


def employee_dismiss(request, employee_id):
    print(request)
    print(employee_id)
    return HttpResponseRedirect('/list/employee/')

def employee_list(request):
    employees = Employee.objects.raw(raw_query='''SELECT * FROM employee;''')
    return render(
        request,
        template_name="index.html",
        context={
            "employees": employees,
        },
    )

def room_list(request):
    rooms = Room.objects.raw(raw_query='''SELECT * FROM room;''')
    return render(
        request,
        template_name="index.html",
        context={
            "rooms": rooms,
        },
    )

def customer_list(request):
    customers = Customer.objects.raw(raw_query='''SELECT * FROM customer;''')
    return render(
        request,
        template_name="index.html",
        context={
            "customers": customers,
        },
    )

def reservation_list(request):
    reservations = Reservation.objects.raw(raw_query='''SELECT * FROM reservation;''')
    return render(
        request,
        template_name="index.html",
        context={
            "rooms": rooms,
            "reservations": reservations,
            "customers": customers,
            "employees": employees,
        },
    )

def overview(request):
    return render(
        request,
        template_name="index.html",
        context={
            "rooms": rooms,
            "reservations": reservations,
            "customers": customers,
            "employees": employees,
        },
    )
