# Generated by Django 2.2 on 2019-10-05 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ticker",
            fields=[
                ("table", models.CharField(choices=[("SF1", "SF1")], max_length=3)),
                ("permaticker", models.IntegerField(primary_key=True, serialize=False)),
                ("ticker", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=100)),
                ("exchange", models.CharField(max_length=100)),
                (
                    "isdelisted",
                    models.CharField(choices=[("N", "No"), ("Y", "Yes")], max_length=1),
                ),
                ("category", models.CharField(max_length=100)),
                ("cusips", models.CharField(max_length=100)),
                ("siccode", models.CharField(max_length=100)),
                ("sicsector", models.CharField(max_length=100)),
                ("sicindustry", models.CharField(max_length=100)),
                ("famasector", models.CharField(max_length=100)),
                ("famaindustry", models.CharField(max_length=100)),
                ("sector", models.CharField(max_length=100)),
                ("industry", models.CharField(max_length=100)),
                ("scalemarketcap", models.CharField(max_length=100)),
                ("scalerevenue", models.CharField(max_length=100)),
                ("relatedtickers", models.CharField(max_length=100)),
                ("currency", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("lastupdated", models.CharField(max_length=100)),
                ("firstadded", models.CharField(max_length=100)),
                ("firstpricedate", models.CharField(max_length=100)),
                ("lastpricedate", models.CharField(max_length=100)),
                ("firstquarter", models.CharField(max_length=100)),
                ("lastquarter", models.CharField(max_length=100)),
                ("secfilings", models.CharField(max_length=100)),
                ("companysite", models.CharField(max_length=100)),
            ],
        )
    ]
