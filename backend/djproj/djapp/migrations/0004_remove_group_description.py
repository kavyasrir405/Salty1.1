# Generated by Django 4.0.3 on 2025-03-07 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0003_alter_group_group_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
    ]
