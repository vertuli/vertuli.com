# Generated by Django 2.2 on 2019-10-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("equities", "0009_auto_20191005_2304")]

    operations = [
        migrations.AlterField(
            model_name="ticker", name="isdelisted", field=models.CharField(max_length=1)
        ),
        migrations.AlterField(
            model_name="ticker", name="table", field=models.CharField(max_length=10)
        ),
    ]
