# Generated by Django 4.1.7 on 2023-03-25 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_icons_icon_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.icons', verbose_name='Иконка'),
        ),
    ]
