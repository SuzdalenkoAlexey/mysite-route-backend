# Generated by Django 4.2.3 on 2023-07-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_rename_order_collectionlines_by_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='uid',
            field=models.CharField(max_length=77, null=True, unique=True),
        ),
    ]