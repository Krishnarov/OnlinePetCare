# Generated by Django 4.2.4 on 2024-12-08 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0005_imageupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardsUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('Description', models.ImageField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
