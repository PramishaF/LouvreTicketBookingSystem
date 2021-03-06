# Generated by Django 3.2.8 on 2021-10-27 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registeron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('City', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('Username', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('Date', models.DateField()),
                ('Tickets', models.IntegerField()),
                ('City', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
            ],
        ),
    ]
