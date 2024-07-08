# Generated by Django 5.0.6 on 2024-07-04 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_otherservice_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=100)),
                ('medical_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.service')),
                ('other_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.otherservice')),
            ],
        ),
    ]