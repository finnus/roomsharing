# Generated by Django 3.0.12 on 2021-04-18 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rs_organizations', '0002_auto_20210418_1725'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='rooms_of_organizationaladdress', related_query_name='room_of_organizationaladdress', to='rs_organizations.OrganizationalAddress'),
            preserve_default=False,
        ),
    ]