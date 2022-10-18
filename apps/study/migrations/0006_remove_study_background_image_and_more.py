# Generated by Django 4.1.1 on 2022-10-07 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_remove_about_background_en_and_more'),
        ('study', '0005_alter_universityimages_university'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='background_image',
        ),
        migrations.RemoveField(
            model_name='studyblog',
            name='background',
        ),
        migrations.AddField(
            model_name='study',
            name='background',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.background'),
        ),
        migrations.AddField(
            model_name='study',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='study.category'),
        ),
        migrations.AddField(
            model_name='studyblog',
            name='background_image',
            field=models.ImageField(null=True, upload_to='study/base/'),
        ),
        migrations.AlterField(
            model_name='study',
            name='image',
            field=models.ImageField(null=True, upload_to='study/base/'),
        ),
    ]