# Generated by Django 3.2 on 2021-04-27 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0006_remove_attachment_added_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='analyzed',
            new_name='checked',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='analyzed_date',
            new_name='checked_date',
        ),
    ]
