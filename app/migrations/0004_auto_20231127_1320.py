# Generated by Django 2.2.3 on 2023-11-27 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20230412_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(3, 'STUDENT'), (2, 'STAFF'), (1, 'HOD')], default=1, max_length=50),
        ),
    ]
