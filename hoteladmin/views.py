from django.http import HttpResponseRedirect
from django.shortcuts import render
from hoteladmin.models import *
from django.db import connection


def customer_checkout(request, customer_id):
    # Customer.objects.raw('DELETE FROM customer WHERE customer_id=1;')
    #Customer.objects.get(customer_id=customer_id)
    print(request)
    print(customer_id)
    return HttpResponseRedirect('/list/customer/')


def reservation_cancel(request, reservation_id):
    Reservation.objects.raw()
    print(request)
    print(reservation_id)
    return HttpResponseRedirect('/list/reservation/')


def employee_dismiss(request, employee_id):
    Employee.objects.raw()
    print(request)
    print(employee_id)
    return HttpResponseRedirect('/list/employee/')


def employee_list(request):
    employees = Employee.objects.raw(raw_query='''SELECT * FROM employee;''')
    return render(
        request,
        template_name="list/employee.html",
        context={
            "employees": employees,
        },
    )


def reservation_list(request):
    reservations = Reservation.objects.raw(raw_query='''SELECT * FROM reservation;''')
    return render(
        request,
        template_name="list/reservation.html",
        context={
            "reservations": reservations,
        },
    )


def room_list(request):
    rooms = Room.objects.raw(raw_query='''SELECT * FROM room;''')
    return render(
        request,
        template_name="list/room.html",
        context={
            "rooms": rooms,
        },
    )


def customer_list(request):
    customers = Customer.objects.raw(raw_query='''SELECT * FROM customer;''')
    return render(
        request,
        template_name="list/customer.html",
        context={
            "customers": customers,
        },
    )


def overview(request):
    return render(
        request,
        template_name="frontpage.html",
        context={
            # "rooms": rooms,
            # "reservations": reservations,
            # "customers": customers,
            # "employees": employees,
        },
    )
