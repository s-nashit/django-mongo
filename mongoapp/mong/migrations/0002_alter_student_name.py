# Generated by Django 4.1.10 on 2023-08-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mong', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.TextField(),
        ),
    ]
