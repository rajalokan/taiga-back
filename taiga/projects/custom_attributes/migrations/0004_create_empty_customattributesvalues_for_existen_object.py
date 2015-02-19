# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_empty_user_story_custom_attrributes_values(apps, schema_editor):
    cav_model = apps.get_model("custom_attributes", "UserStoryCustomAttributesValues")
    obj_model = apps.get_model("userstories", "UserStory")
    db_alias = schema_editor.connection.alias

    for user_story in obj_model.objects.using(db_alias).all():
        cav_model.objects.using(db_alias).get_or_create(user_story=user_story,
                                                        defaults={"attributes_values":{}})

def create_empty_task_custom_attrributes_values(apps, schema_editor):
    cav_model = apps.get_model("custom_attributes", "TaskCustomAttributesValues")
    obj_model = apps.get_model("tasks", "Task")
    db_alias = schema_editor.connection.alias

    for task in obj_model.objects.using(db_alias).all():
        cav_model.objects.using(db_alias).get_or_create(task=task,
                                                        defaults={"attributes_values":{}})

def create_empty_issues_custom_attrributes_values(apps, schema_editor):
    cav_model = apps.get_model("custom_attributes", "IssueCustomAttributesValues")
    obj_model = apps.get_model("issues", "Issue")
    db_alias = schema_editor.connection.alias

    for issue in obj_model.objects.using(db_alias).all():
        cav_model.objects.using(db_alias).get_or_create(issue=issue,
                                                        defaults={"attributes_values":{}})


class Migration(migrations.Migration):

    dependencies = [
        ('custom_attributes', '0003_triggers_on_delete_customattribute'),
    ]

    operations = [
        migrations.RunPython(create_empty_user_story_custom_attrributes_values),
        migrations.RunPython(create_empty_task_custom_attrributes_values),
        migrations.RunPython(create_empty_issues_custom_attrributes_values),
    ]
