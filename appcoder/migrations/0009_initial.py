# Generated by Django 4.0.3 on 2022-03-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appcoder', '0008_delete_asignatura_delete_extasis_delete_mago_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('clase', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Extasis',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('fecha_entregado', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Mago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('casa', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('materia', models.CharField(max_length=60)),
            ],
        ),
    ]
