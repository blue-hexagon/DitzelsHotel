from django.db import models


class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    bill_date = models.DateField()
    customer = models.ForeignKey('Customer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill'

    def __str__(self) -> str:
        return str(self.bill_id)


class CreditCard(models.Model):
    credit_card_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING)
    card_number = models.BigIntegerField()
    cvc_number = models.IntegerField()
    cardholder_name = models.CharField(max_length=128)
    expiry_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'credit_card'

    def __str__(self) -> str:
        return self.cardholder_name


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    firstname = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone_number = models.IntegerField(unique=True)
    address = models.CharField(max_length=255)
    zip_code = models.ForeignKey('Location', models.DO_NOTHING, db_column='zip_code', blank=True, null=True)
    country = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self) -> str:
        return self.firstname + " " + self.surname


class Employee(models.Model):
    cpr_number = models.CharField(primary_key=True, max_length=10)
    email = models.CharField(max_length=128)
    firstname = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    zip_code = models.ForeignKey('Location', models.DO_NOTHING, db_column='zip_code')
    bank_account_details = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'employee'

    def __str__(self) -> str:
        return self.firstname + " " + self.surname


class LineItem(models.Model):
    bill_id = models.IntegerField(primary_key=True)
    line_number = models.IntegerField()
    product = models.ForeignKey('Product', models.DO_NOTHING)
    amount = models.IntegerField()
    reservation = models.ForeignKey('Reservation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'line_item'
        unique_together = (('bill_id', 'line_number'),)

    def __str__(self) -> str:
        return f"{self.bill_id}-{self.line_number}"


class Location(models.Model):
    zip_code = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'location'

    def __str__(self) -> str:
        return str(self.zip_code)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    cvr_number = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='cvr_number')
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
    purchase_price_pennies = models.IntegerField()
    sales_price_pennies = models.IntegerField()
    stock_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product'

    def __str__(self) -> str:
        return str(self.product_id)


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    room = models.ForeignKey('Room', models.DO_NOTHING)
    checkin_date = models.DateField()
    checkout_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'reservation'

    def __str__(self) -> str:
        return str(self.reservation_id)


class Room(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=64)
    price_per_day_pennies = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room'

    def __str__(self) -> str:
        return str(self.room_id)


class Supplier(models.Model):
    cvr_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone_number = models.IntegerField()
    zip_code = models.ForeignKey(Location, models.DO_NOTHING, db_column='zip_code')
    address = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'supplier'

    def __str__(self) -> str:
        return str(self.cvr_number)
