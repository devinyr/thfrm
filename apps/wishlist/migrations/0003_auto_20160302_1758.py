# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_item_added_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='username',
            new_name='uname',
        ),
    ]
