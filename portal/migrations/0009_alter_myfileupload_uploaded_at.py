# Generated by Django 3.2.15 on 2022-09-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_alter_myfileupload_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myfileupload',
            name='uploaded_at',
            field=models.DateField(blank=True, null=True, verbose_name='Upload Date(mm/dd/yyyy)'),
        ),
    ]
