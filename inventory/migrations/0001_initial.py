# Generated by Django 3.1.5 on 2021-01-11 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=17)),
                ('scalable', models.BooleanField(default=False)),
                ('taxable', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.item')),
                ('plu', models.IntegerField(unique=True)),
                ('variety', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=30, null=True)),
                ('botanical', models.CharField(max_length=100, null=True)),
            ],
            bases=('inventory.item',),
        ),
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.item')),
                ('upc', models.CharField(max_length=30, unique=True)),
                ('vendor', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='inventory.vendor')),
            ],
            bases=('inventory.item',),
        ),
    ]
