# Generated by Django 3.2.10 on 2024-01-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jornadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('j1', models.IntegerField(default=0)),
                ('j2', models.IntegerField(default=0)),
                ('j3', models.IntegerField(default=0)),
                ('j4', models.IntegerField(default=0)),
                ('j5', models.IntegerField(default=0)),
                ('j6', models.IntegerField(default=0)),
                ('j7', models.IntegerField(default=0)),
                ('j8', models.IntegerField(default=0)),
                ('j9', models.IntegerField(default=0)),
                ('j10', models.IntegerField(default=0)),
                ('j11', models.IntegerField(default=0)),
                ('j12', models.IntegerField(default=0)),
                ('j13', models.IntegerField(default=0)),
                ('j14', models.IntegerField(default=0)),
                ('j15', models.IntegerField(default=0)),
                ('j16', models.IntegerField(default=0)),
                ('j17', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Jornada',
                'verbose_name_plural': 'Jornadas',
            },
        ),
    ]
