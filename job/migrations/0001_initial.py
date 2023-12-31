# Generated by Django 4.2.5 on 2023-10-29 15:20

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields
import etc.file_uploader


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to=etc.file_uploader.category_logo_uploader)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=etc.file_uploader.company_image_uploader)),
                ('subtitle', models.TextField(max_length=1000)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('location', django_countries.fields.CountryField(max_length=2)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('salary_start', models.IntegerField(blank=True, null=True)),
                ('salary_end', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(max_length=15000)),
                ('vacancy', models.IntegerField()),
                ('job_type', models.CharField(choices=[('FullTime', 'FullTime'), ('PartTime', 'PartTime'), ('Remote', 'Remote'), ('Freelance', 'Freelance'), ('UnDefined', 'UnDefined')], default='UnDefined', max_length=10)),
                ('experience', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
