# Generated by Django 3.2.12 on 2022-06-11 15:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_alter_author_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('a92736c5-48c3-453f-87dd-2302a30b536a'), primary_key=True, serialize=False),
        ),
    ]