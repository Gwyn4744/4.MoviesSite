# Generated by Django 3.1.1 on 2020-10-08 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('url', models.URLField()),
                ('youtube_id', models.CharField(max_length=256)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.hall')),
            ],
        ),
    ]