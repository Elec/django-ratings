# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
    ]
