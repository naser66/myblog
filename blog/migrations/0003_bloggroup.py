# Generated by Django 5.0 on 2024-02-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_datetime_edite_post_datetime_edit'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
