# Generated by Django 4.1.3 on 2022-11-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_date', models.DateField()),
            ],
            options={
                'db_table': 'bill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('credit_card_id', models.AutoField(primary_key=True, serialize=False)),
                ('card_number', models.BigIntegerField()),
                ('cvc_number', models.IntegerField()),
                ('cardholder_name', models.CharField(max_length=128)),
                ('expiry_date', models.DateField()),
            ],
            options={
                'db_table': 'credit_card',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('phone_number', models.IntegerField(unique=True)),
                ('address', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('cpr_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=128)),
                ('firstname', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('bank_account_details', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('bill_id', models.IntegerField(primary_key=True, serialize=False)),
                ('line_number', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
            options={
                'db_table': 'line_item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('zip_code', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=64)),
                ('purchase_price_pennies', models.IntegerField()),
                ('sales_price_pennies', models.IntegerField()),
                ('stock_count', models.IntegerField()),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
            ],
            options={
                'db_table': 'reservation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_type', models.CharField(max_length=64)),
                ('price_per_day_pennies', models.IntegerField()),
            ],
            options={
                'db_table': 'room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('cvr_number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'supplier',
                'managed': False,
            },
        ),
    ]