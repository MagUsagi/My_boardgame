# Generated by Django 4.2.11 on 2024-04-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_rename_recoed_id_record_record_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='record_id',
        ),
        migrations.AddField(
            model_name='record',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
