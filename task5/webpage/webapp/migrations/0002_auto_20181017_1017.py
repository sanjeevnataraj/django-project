# Generated by Django 2.1 on 2018-10-17 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admission',
            new_name='Admissions',
        ),
        migrations.RenameModel(
            old_name='Alumini',
            new_name='Aluminis',
        ),
        migrations.RenameModel(
            old_name='Approval',
            new_name='Approvals',
        ),
        migrations.RenameModel(
            old_name='CollegeDetail',
            new_name='CollegeDetails',
        ),
        migrations.RenameModel(
            old_name='Facility',
            new_name='Facilites',
        ),
    ]