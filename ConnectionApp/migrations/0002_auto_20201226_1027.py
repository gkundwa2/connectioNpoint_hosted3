# Generated by Django 3.1.4 on 2020-12-26 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConnectionApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='validation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='familyidentity',
            name='familyMembers',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='familyidentity',
            name='firstName',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='familyidentity',
            name='lastName',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='familyidentity',
            name='middleName',
            field=models.CharField(max_length=300),
        ),
    ]
