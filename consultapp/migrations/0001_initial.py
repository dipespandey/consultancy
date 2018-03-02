# Generated by Django 2.0.2 on 2018-03-02 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
