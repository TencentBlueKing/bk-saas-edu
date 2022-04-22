# -*- coding: utf-8 -*-
import os
import json
import codecs

from django.db import migrations
from django.conf import settings

from iam.contrib.iam_migration.migrator import IAMMigrator


def forward_func(apps, schema_editor):

    migrator = IAMMigrator(Migration.migration_json)
    migrator.migrate()


class Migration(migrations.Migration):
    migration_json = "0001_bk_saas_edu_20220321-1505.json"

    dependencies = []

    operations = [
        migrations.RunPython(forward_func)
    ]
