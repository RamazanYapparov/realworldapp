# Generated by Django 4.0.6 on 2022-07-07 15:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='firstname',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex='[a-zA-Z]+')]),
        ),
        migrations.AlterField(
            model_name='actor',
            name='lastname',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex='[a-zA-Z]+')]),
        ),
        migrations.AlterField(
            model_name='character',
            name='firstname',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex='[a-zA-Z]+')]),
        ),
        migrations.AlterField(
            model_name='character',
            name='lastname',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex='[a-zA-Z]+')]),
        ),
        migrations.AlterField(
            model_name='director',
            name='firstname',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex='[a-zA-Z]+')]),
        ),
        migrations.AlterField(
            model_name='director',
            name='lastname',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex='[a-zA-Z]+')]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex='[a-zA-Z]+')]),
        ),
    ]
