# Generated by Django 3.0.7 on 2020-06-19 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200617_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyliving',
            name='other',
            field=models.ManyToManyField(related_name='daily_living_other', to='api.Other'),
        ),
        migrations.AlterField(
            model_name='homeexpense',
            name='other',
            field=models.ManyToManyField(related_name='home_expense_other', to='api.Other'),
        ),
        migrations.AlterField(
            model_name='income',
            name='other',
            field=models.ManyToManyField(related_name='income_other', to='api.Other'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='other',
            field=models.ManyToManyField(related_name='insurance_other', to='api.Other'),
        ),
        migrations.AlterField(
            model_name='saving',
            name='other',
            field=models.ManyToManyField(related_name='saving_other', to='api.Other'),
        ),
    ]
