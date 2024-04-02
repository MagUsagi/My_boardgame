# Generated by Django 4.2.11 on 2024-04-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_history_alter_game_image_result_history_game_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='game_id',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='history_id',
            new_name='history',
        ),
        migrations.AlterField(
            model_name='result',
            name='score',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
