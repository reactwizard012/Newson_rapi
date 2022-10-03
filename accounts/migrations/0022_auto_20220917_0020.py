# Generated by Django 3.2 on 2022-09-16 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_linkedinaccount_blacklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proxy',
            name='credential',
        ),
        migrations.AddField(
            model_name='proxy',
            name='password',
            field=models.CharField(default='test', max_length=700),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proxy',
            name='username',
            field=models.CharField(default='test', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='linkedinaccount',
            name='proxy',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='linkedin_proxy', to='accounts.proxy'),
        ),
        migrations.DeleteModel(
            name='ProxyCredential',
        ),
    ]
