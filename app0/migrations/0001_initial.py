# Generated by Django 4.0.4 on 2022-06-20 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=50)),
                ('bpub_date', models.DateField()),
                ('bread', models.IntegerField()),
                ('bcomnt', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
