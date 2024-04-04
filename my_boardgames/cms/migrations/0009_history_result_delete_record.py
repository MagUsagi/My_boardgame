# Generated by Django 4.2.11 on 2024-04-04 16:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_record_winner'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('duaration', models.CharField(max_length=50)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.game')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=100)),
                ('score', models.IntegerField(blank=True, default=None, null=True)),
                ('winner', models.BooleanField()),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.history')),
            ],
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]