# Generated by Django 4.2.2 on 2023-08-02 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('positionSalary', models.CharField(max_length=255)),
                ('positionLocation', models.CharField(max_length=255)),
                ('companyName', models.CharField(max_length=255)),
                ('companyLocation', models.CharField(max_length=255)),
                ('companyEmail', models.EmailField(max_length=254)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='job.category')),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-createdAt',),
            },
        ),
    ]