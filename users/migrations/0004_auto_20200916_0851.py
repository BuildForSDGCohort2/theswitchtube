# Generated by Django 3.1 on 2020-09-16 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_profilepic_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepic',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='profilepic',
            name='bio',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profilepic',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
