# Generated by Django 5.1.1 on 2024-10-01 02:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('data', models.JSONField(blank=True, default=dict)),
                ('urn', models.CharField(help_text='urn:cite2:&lt;site>:dictionaries.atlas_v1', max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Dictionaries',
            },
        ),
        migrations.CreateModel(
            name='DictionaryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headword', models.CharField(db_index=True, max_length=255)),
                ('headword_normalized', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('headword_normalized_stripped', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('data', models.JSONField(blank=True, default=dict)),
                ('idx', models.IntegerField(help_text='0-based index')),
                ('urn', models.CharField(help_text='urn:cite2:&lt;site>:entries.atlas_v1', max_length=255, unique=True)),
                ('dictionary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='dictionaries.dictionary')),
            ],
            options={
                'verbose_name_plural': 'Dictionary Entries',
                'unique_together': {('dictionary', 'idx')},
            },
        ),
    ]