# Generated by Django 5.0.1 on 2024-01-22 07:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0005_remove_owner_journey_remove_team_journey_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Owner',
            new_name='Assignee',
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=20)),
                ('counter', models.IntegerField()),
                ('journey', models.ManyToManyField(blank=True, to='products.journey')),
            ],
        ),
        migrations.DeleteModel(
            name='ValueStream',
        ),
    ]
