# Generated by Django 2.2.1 on 2020-02-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0012_remove_contactinfo_contact_lg'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='contact_name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='contact名称'),
        ),
    ]