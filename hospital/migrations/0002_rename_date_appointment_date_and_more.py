# Generated by Django 5.0.6 on 2024-06-21 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='Time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Special',
            new_name='special',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Name',
            new_name='name',
        ),
    ]
