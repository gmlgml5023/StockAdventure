# Generated by Django 4.2.16 on 2024-11-23 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investment_style', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StyleQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, verbose_name='질문')),
            ],
        ),
        migrations.CreateModel(
            name='StyleChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200, verbose_name='선택항목')),
                ('style_points', models.IntegerField(default=0, verbose_name='스타일 점수')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='investment_style.stylequestion')),
            ],
        ),
    ]