# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='fulll_name',
        ),
        migrations.AddField(
            model_name='signup',
            name='full_name',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
