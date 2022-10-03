# Generated by Django 3.2 on 2022-04-15 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhiteLabel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=600, unique=True)),
                ('domain', models.URLField()),
                ('primary_color', models.CharField(max_length=7)),
                ('theme_color', models.CharField(max_length=7)),
                ('logo', models.ImageField(upload_to='whitelabels/logos/')),
                ('favicon', models.ImageField(upload_to='whitelabels/favicons/')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
    ]
