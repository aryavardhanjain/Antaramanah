# Generated by Django 4.2.7 on 2023-11-20 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0002_alter_therapist_therapist_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='therapist',
            name='therapist_id',
        ),
    ]
