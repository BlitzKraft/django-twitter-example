# Generated by Django 3.1.1 on 2020-09-04 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytweet',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tweeter_app.myuser'),
        ),
    ]