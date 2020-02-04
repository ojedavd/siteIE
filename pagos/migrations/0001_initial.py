# Generated by Django 2.0 on 2020-02-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('alumno', models.IntegerField()),
                ('curso', models.CharField(max_length=250)),
                ('curso_id', models.IntegerField()),
                ('cuota_id', models.IntegerField()),
                ('fecha', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(max_length=20)),
                ('sede_id', models.IntegerField()),
                ('tipo', models.CharField(max_length=20)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('user_created', models.CharField(max_length=20)),
                ('user_modified', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'pagos',
                'managed': False,
            },
        ),
    ]
