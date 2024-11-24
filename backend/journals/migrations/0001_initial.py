# Generated by Django 4.2.16 on 2024-11-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=20)),
                ('transaction_date', models.DateField()),
                ('buysell', models.CharField(choices=[('매수', '매수'), ('매도', '매도')], max_length=2)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('reason', models.TextField()),
                ('feedback', models.TextField()),
            ],
        ),
    ]
