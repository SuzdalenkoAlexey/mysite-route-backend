# Generated by Django 4.2.3 on 2023-07-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_person_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastvisit',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
