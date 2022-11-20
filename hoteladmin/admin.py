import datetime

from django.contrib import admin
from django.db.models import Sum
from django.utils.html import format_html

from .models import *


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("zip_code", "city_name")
    ordering = ("zip_code",)
    search_fields = ("city_name__contains",)


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ("bill_id", "bill_date", "customer", "line_items", "price_for_products", "price_for_room", "price_total")
    ordering = ("-bill_date",)

    def line_items(self, bill: Bill):
        result = LineItem.objects.filter(bill_id=bill.bill_id).count()
        return result

    def price_for_products(self, bill: Bill):
        products_cost = LineItem.objects.filter(bill_id=bill.bill_id).aggregate(Sum('product__sales_price_pennies'))['product__sales_price_pennies__sum']
        if products_cost is None:
            return f"0 kr"
        else:
            return f"{products_cost // 100} kr"

    def price_for_room(self, bill: Bill):
        hotel_stay_cost = Reservation.objects.filter(customer=bill.customer)[0].room.price_per_day_pennies // 100
        return f"{hotel_stay_cost} kr"

    def price_total(self, bill: Bill):
        products_cost = LineItem.objects.filter(bill_id=bill.bill_id).aggregate(Sum('product__sales_price_pennies'))['product__sales_price_pennies__sum']
        hotel_stay_cost = Reservation.objects.filter(customer=bill.customer)[0].room.price_per_day_pennies // 100
        if products_cost is None:
            return f"{hotel_stay_cost} kr"
        else:
            return f"{products_cost // 100 + hotel_stay_cost} kr"


@admin.register(LineItem)
class Admin(admin.ModelAdmin):
    list_display = ("line_number","bill_id", "product_name", "amount", "reservation")
    # "line_number", "product",
    ordering = ("-bill_id",)
    #TODO: Add  URL link to a product and return the name of the product
    # Fix not being able to edit
    # def product(self, lineitem: LineItem):
    #     return self.name
    def product_name(self, lineitem: LineItem):
        return Product.objects.filter(product_id=lineitem.product.product_id)[0].name


@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ("credit_card_id", "customer", "card_number", "cvc_number", "cardholder_name", "expiry_date")
    ordering = ("expiry_date",)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_id", "email", "firstname", "surname", "phone_number", "address", "zip_code", "country", "credit_card")
    ordering = ("zip_code",)
    list_filter = ("country",)

    def credit_card(self, customer: Customer):
        cardholder_identifier = CreditCard.objects.get(customer_id=customer.customer_id).cardholder_name
        return format_html(f'<a href="../creditcard/{customer.customer_id}/change">{cardholder_identifier}</a>')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("cpr_number", "email", "firstname", "surname", "phone_number", "address", "zip_code", "bank_account_details")
    ordering = ("cpr_number",)


@admin.register(Product)
class Admin(admin.ModelAdmin):
    list_display = ("product_id", "cvr_number", "supplier", "name", "type", "purchase_price", "sales_price", "stock_count")
    ordering = ("stock_count",)

    # purchase_price_pennies, sales_price_pennies

    def supplier(self, product):
        return Supplier.objects.filter(cvr_number=product.cvr_number_id)[0].name

    def purchase_price(self, product):
        result = Product.objects.filter(product_id=product.product_id)[0].purchase_price_pennies / 100
        return str(result) + " kr"

    def sales_price(self, product):
        result = Product.objects.filter(product_id=product.product_id)[0].sales_price_pennies / 100
        return str(result) + " kr"


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("reservation_id", "customer", "room", "checkin_date", "checkout_date", "days_staying")
    ordering = ("-reservation_id",)

    def days_staying(self, reservation):
        checkin = Reservation.objects.get(reservation_id=reservation.reservation_id).checkin_date
        checkout = Reservation.objects.get(reservation_id=reservation.reservation_id).checkout_date
        return (checkout - checkin).days


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("room_id", "room_type", "price_per_day")
    ordering = ("price_per_day_pennies",)

    def price_per_day(self, room):
        result = Room.objects.filter(room_id=room.room_id)[0].price_per_day_pennies // 100
        return str(result) + " kr"


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("cvr_number", "name", "email", "phone_number", "zip_code", "address")
    ordering = ("zip_code",)
