# Generated by Django 4.0.4 on 2022-05-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_alter_candidate_language_alter_candidate_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Хобби')),
            ],
            options={
                'verbose_name': 'Хобби',
                'verbose_name_plural': 'Хобби',
                'db_table': 'Хобби',
            },
        ),
        migrations.AddField(
            model_name='candidate',
            name='hobby',
            field=models.ManyToManyField(blank=True, null=True, to='candidates.hobby', verbose_name='Навык'),
        ),
    ]