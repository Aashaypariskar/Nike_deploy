# Generated by Django 5.1.1 on 2024-11-12 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('SNEAKERS', 'sneakers'), ('FOOTBALL SHOES', 'football shoes'), ('RUNNING SHOES', 'running shoes')], max_length=20)),
                ('small_description', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('original_price', models.IntegerField()),
                ('discounted_price', models.IntegerField()),
                ('pets_image', models.ImageField(upload_to='pet_images')),
            ],
        ),
        migrations.DeleteModel(
            name='Marvel',
        ),
    ]
