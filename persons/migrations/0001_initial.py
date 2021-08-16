# Generated by Django 3.2.6 on 2021-08-16 19:59

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import persons.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='نام کاربری')),
                ('first_name', models.CharField(blank=True, max_length=200, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=200, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator], verbose_name='ایمیل')),
                ('national_code', models.CharField(db_index=True, max_length=10, unique=True, validators=[django.core.validators.RegexValidator(regex='^([0-9]){10}$')], verbose_name='کد ملی')),
                ('mobile_number', models.CharField(db_index=True, max_length=11, unique=True, validators=[django.core.validators.RegexValidator(regex='09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}')], verbose_name='موبایل')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='آدرس')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='توضیحات')),
                ('email_confirm', models.BooleanField(default=False, verbose_name='تاییدیه ایمیل')),
                ('mobile_confirm', models.BooleanField(default=False, verbose_name='تایدیه شماره همراه')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_admin', models.BooleanField(default=False, verbose_name='مدیر')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=persons.models.get_person_avatar_path, verbose_name='تصویر پروفایل')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ثبت نام')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان آپدیت')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
    ]
