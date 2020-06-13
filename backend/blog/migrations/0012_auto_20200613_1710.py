# Generated by Django 3.0.7 on 2020-06-13 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200613_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('world', 'World'), ('environment', 'Environment'), ('technology', 'Technology'), ('design', 'Design'), ('culture', 'Culture'), ('business', 'Business'), ('politics', 'Politics'), ('opinion', 'Opinion'), ('science', 'Science'), ('health', 'Health'), ('style', 'Style'), ('travel', 'Travel')], default='world', max_length=50),
        ),
    ]
