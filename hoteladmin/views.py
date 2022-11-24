import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import connection

from collections import namedtuple


def namedtuplefetchall(cursor):
    """Return all rows from a cursor as a namedtuple"""
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def customer_checkout(request, customer_id):
    ...
    return HttpResponseRedirect('/list/customer/')


def lineitem_delete(request, bill_id, line_number):
    with connection.cursor() as c:
        c.execute('''
        DELETE FROM line_item WHERE bill_id = %s AND line_number = %s;
        ''', [bill_id, line_number])
    return HttpResponseRedirect(f'/detail/order/{bill_id}')


def reservation_cancel(request, reservation_id):
    with connection.cursor() as c:
        c.execute('''
        DELETE FROM reservation WHERE reservation.reservation_id = %s;
        ''', [reservation_id])
    return HttpResponseRedirect('/list/reservation/')


def employee_dismiss(request, employee_id):
    with connection.cursor() as c:
        c.execute('''
        DELETE FROM employee WHERE employee.cpr_number = %s;
        ''', [employee_id])
    return HttpResponseRedirect('/list/employee/')


def employee_list(request):
    with connection.cursor() as c:
        c.execute('''SELECT * FROM `employee`;''')
        employees = namedtuplefetchall(c)
    return render(
        request,
        template_name="list/employee.html",
        context={
            "employees": employees,
        },
    )


def reservation_list(request):
    if True:  # Today and 4 weeks ahead of time
        today = datetime.date.today()
        week_from_now = today + datetime.timedelta(weeks=4)
    elif False:  # In the midst of a reservation
        today = datetime.date.fromisoformat("2022-12-02")
        week_from_now = today + datetime.timedelta(weeks=4)
    else:  # Show all reservations
        today = datetime.date.fromisoformat("2020-01-01")
        week_from_now = today + datetime.timedelta(weeks=300)

    with connection.cursor() as c:
        c.execute(
            '''
            SELECT reservation.reservation_id, reservation.room_id, reservation.checkin_date, reservation.checkout_date,
            customer.email AS customer_email, 
            room.room_type, 
            ROUND(DATEDIFF(reservation.checkout_date, reservation.checkin_date) * room.price_per_day_pennies / 100, 2) AS reservation_price
            FROM reservation
            INNER JOIN customer
            ON reservation.customer_id = customer.customer_id
            INNER JOIN room
            ON reservation.room_id = room.room_id
            WHERE reservation.checkin_date >= %s AND reservation.checkin_date <= %s
            ORDER BY reservation.checkin_date;
            ''', [today, week_from_now])
        reservations = namedtuplefetchall(c)
    return render(
        request,
        template_name="list/upcoming_reservations.html",
        context={
            "reservations": reservations,
        },
    )


def room_list(request):
    with connection.cursor() as c:
        c.execute('''
           SELECT * FROM room_availability;
        ''', [])
        rooms = namedtuplefetchall(c)
    return render(
        request,
        template_name="list/room.html",
        context={
            "rooms": rooms,
        },
    )


def order_list(request):
    with connection.cursor() as c:
        c.execute('''
           SELECT bill.bill_id, bill.bill_date, bill.customer_id,
            customer.firstname, customer.surname, customer.address,
            line_item.line_number,line_item.product_id, line_item.amount,
            product.name, get_reservation_price.reservation_price,
            CAST(product.sales_price_pennies/100 AS DECIMAL(7,2)) AS sales_price_pennies,
            CAST(line_item.amount * product.sales_price_pennies  / 100 AS DECIMAL(7,2)) AS line_total,
            bill_lineitems_total.lineitems_total,
            (bill_lineitems_total.lineitems_total + get_reservation_price.reservation_price) AS total_price
            FROM bill
            INNER JOIN customer
            ON bill.customer_id = customer.customer_id
            INNER JOIN line_item
            ON bill.bill_id = line_item.bill_id
            INNER JOIN product
            ON line_item.product_id = product.product_id
            INNER JOIN get_reservation_price
            ON get_reservation_price.reservation_id = line_item.reservation_id
            INNER JOIN bill_lineitems_total
            ON bill.bill_id = bill_lineitems_total.bill_id
            GROUP BY bill.bill_id;
        ''', [])
        bills = namedtuplefetchall(c)
    return render(
        request,
        template_name="list/order.html",
        context={
            "bills": bills,
        },
    )


def order_detail(request, order_id):
    with connection.cursor() as c:
        c.execute('''
           SELECT bill.bill_id, bill.bill_date, bill.customer_id,
            customer.firstname, customer.surname, customer.address,
            line_item.line_number,line_item.product_id, line_item.amount,
            product.name,
            CAST(product.sales_price_pennies/100 AS DECIMAL(7,2)) AS sales_price_pennies,
            CAST(line_item.amount * product.sales_price_pennies  / 100 AS DECIMAL(7,2)) AS line_total
            FROM bill
            INNER JOIN customer
            ON bill.customer_id = customer.customer_id
            INNER JOIN line_item
            ON bill.bill_id = line_item.bill_id
            INNER JOIN product
            ON line_item.product_id = product.product_id
            WHERE bill.bill_id = %s
            ORDER BY line_item.line_number;
        ''', [order_id])
        bill = namedtuplefetchall(c)
    return render(
        request,
        template_name="detail/order.html",
        context={
            "bill": bill,
        },
    )


def customer_list(request):
    today = datetime.date.today()
    with connection.cursor() as c:
        # c.execute('''SELECT * FROM `customer`;''')
        c.execute('''
        SELECT customer.customer_id, customer.email, customer.firstname, customer.surname, customer.phone_number,
        reservation.reservation_id, reservation.room_id, reservation.checkin_date, reservation.checkout_date
        FROM customer
        INNER JOIN reservation
        ON reservation.customer_id = customer.customer_id
        WHERE (reservation.checkin_date <= %s AND reservation.checkout_date >= %s) 
        ORDER BY reservation.checkin_date;
        ''', [today, today])
        customers = namedtuplefetchall(c)
    return render(
        request,
        template_name="list/current_guests.html",
        context={
            "customers": customers,
        },
    )


def overview(request):
    return render(
        request,
        template_name="frontpage.html",
    )
