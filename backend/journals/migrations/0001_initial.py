# Generated by Django 4.2.16 on 2024-11-25 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
