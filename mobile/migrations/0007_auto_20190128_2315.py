# Generated by Django 2.1.5 on 2019-01-28 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0006_auto_20190126_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operators',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operators', to='mobile.Countries'),
        ),
    ]