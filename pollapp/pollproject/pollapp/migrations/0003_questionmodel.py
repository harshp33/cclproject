# Generated by Django 3.2 on 2023-03-31 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0002_auto_20220623_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.TextField()),
            ],
        ),
    ]
