# Generated by Django 4.1.2 on 2022-10-21 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(choices=[('yellow', 'yellow'), ('blue', 'blue'), ('gray', 'gray')], max_length=20)),
                ('model', models.CharField(choices=[('hatch', 'hatch'), ('sedan', 'sedan'), ('convertible', 'convertible')], max_length=20)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='api.person')),
            ],
        ),
    ]