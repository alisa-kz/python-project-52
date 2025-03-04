# Generated by Django 5.1.6 on 2025-03-04 14:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labels", "0001_initial"),
        ("statuses", "0003_alter_status_name"),
        ("tasks", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="labels",
            field=models.ManyToManyField(to="labels.label"),
        ),
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.TextField(verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="task",
            name="executor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="executor",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Исполнитель",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="statuses.status",
                verbose_name="Статус",
            ),
        ),
    ]
