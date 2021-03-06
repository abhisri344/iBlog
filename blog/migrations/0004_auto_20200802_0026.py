# Generated by Django 3.0.8 on 2020-08-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='', help_text='Enter your name', max_length=24),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead0',
            field=models.CharField(default='', help_text='Enter content for heading 0', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead1',
            field=models.CharField(default='', help_text='Enter content for heading 1', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead2',
            field=models.CharField(default='', help_text='Enter content for heading 2', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head0',
            field=models.CharField(default='', help_text='Enter heading 0 for blog', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head1',
            field=models.CharField(default='', help_text='Enter heading 1 for blog', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(default='', help_text='Enter heading 2 for blog', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default='', help_text='Enter title of blog', max_length=50),
        ),
    ]
