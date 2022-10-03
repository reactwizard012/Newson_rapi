# Generated by Django 3.2 on 2022-04-30 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_label_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProspectLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.label')),
                ('prospect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.prospect')),
            ],
            options={
                'unique_together': {('prospect', 'label')},
            },
        ),
    ]
