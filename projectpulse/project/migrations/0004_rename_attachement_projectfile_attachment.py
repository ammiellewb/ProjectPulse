# Generated by Django 5.0.4 on 2024-05-03 13:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0003_projectfile_project"),
    ]

    operations = [
        migrations.RenameField(
            model_name="projectfile",
            old_name="attachement",
            new_name="attachment",
        ),
    ]