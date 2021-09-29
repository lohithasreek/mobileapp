# Generated by Django 3.2.5 on 2021-09-29 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Email', models.EmailField(default='@gmail.com', max_length=254)),
                ('Brand', models.CharField(default='Mi11x', max_length=100)),
                ('Color', models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Silver', 'Silver')], max_length=100)),
                ('Contact', models.IntegerField()),
                ('Ordered_Date', models.DateTimeField(auto_now=True, null=True)),
                ('Price', models.IntegerField()),
            ],
        ),
    ]