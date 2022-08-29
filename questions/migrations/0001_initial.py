# Generated by Django 3.1.4 on 2021-03-16 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.IntegerField()),
                ('option_one', models.CharField(max_length=100)),
                ('option_two', models.CharField(max_length=100)),
                ('option_three', models.CharField(blank=True, max_length=100)),
                ('option_four', models.CharField(blank=True, max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.course')),
            ],
        ),
    ]
