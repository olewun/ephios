# Generated by Django 3.1.2 on 2020-10-14 14:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_management", "0003_userprofile_calendar_token_squashed_0008_auto_20200925_1640"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qualification",
            name="included_qualifications",
            field=models.ManyToManyField(
                blank=True, related_name="included_by", to="user_management.Qualification"
            ),
        ),
        migrations.AlterField(
            model_name="qualificationgrant",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="qualification_grants",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user profile",
            ),
        ),
    ]