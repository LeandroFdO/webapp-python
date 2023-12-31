# Generated by Django 4.2.7 on 2023-11-07 03:40

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('webapp_python', '0003_delete_produtos'),
    ]

    operations = [
        migrations.CreateModel(
            name='produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=4, default=Decimal('0.00'), max_digits=20)),
                ('tipo', models.CharField(max_length=200)),
                ('fornecedor', models.CharField(max_length=200)),
                ('quantidade', models.IntegerField(default=0)),
            ],
        ),
    ]
