# Generated by Django 4.2.3 on 2023-09-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenders', '0012_alter_lenderprofile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='lenderprofile',
            name='zip_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
