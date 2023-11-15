# Generated by Django 4.2.7 on 2023-11-14 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group_lavazem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(default='honda.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(default='honda.png', upload_to='')),
                ('price', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lavazem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('color', models.CharField(max_length=255)),
                ('price', models.BigIntegerField()),
                ('lavazem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='honda.group_lavazem')),
            ],
        ),
        migrations.AddField(
            model_name='group_lavazem',
            name='motor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='honda.motor'),
        ),
    ]