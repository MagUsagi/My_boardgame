# Generated by Django 4.2.11 on 2024-04-04 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_player_record_remove_result_history_delete_history_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='recoed_id',
            new_name='record_id',
        ),
    ]
