# Generated by Django 3.1.2 on 2020-11-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_tipsdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipsOnModal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='TipsDB',
        ),
    ]