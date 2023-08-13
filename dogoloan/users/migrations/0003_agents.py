# Generated by Django 4.2.3 on 2023-08-01 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_phone_number_profile_alternative_mobile_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_location', models.CharField(blank=True, max_length=50, null=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Agent',
                'verbose_name_plural': 'Agents',
            },
        ),
    ]
