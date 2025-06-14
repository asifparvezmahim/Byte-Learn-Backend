# Generated by Django 4.2.21 on 2025-06-08 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_course_module_module_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_no', models.IntegerField()),
                ('video_title', models.TextField(max_length=250)),
                ('video', models.FileField(upload_to='course_video/')),
                ('module', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course_module')),
            ],
        ),
    ]
