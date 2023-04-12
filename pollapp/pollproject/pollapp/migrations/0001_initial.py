# Generated by Django 3.2 on 2022-06-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PollModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('op1', models.CharField(max_length=30)),
                ('op2', models.CharField(max_length=30)),
                ('op3', models.CharField(max_length=30)),
                ('op1c', models.IntegerField(default=0)),
            ],
        ),
    ]
