# Generated by Django 5.1.1 on 2024-10-29 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('texts', '0002_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='NamedEntityCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('data', models.JSONField(blank=True, default=dict)),
                ('urn', models.CharField(help_text='urn:cite2:<site>:named_entity_collection.atlas_v1', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NamedEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('kind', models.CharField(choices=[('person', 'Person'), ('place', 'Place')], max_length=6)),
                ('url', models.URLField()),
                ('data', models.JSONField(blank=True, default=dict)),
                ('idx', models.IntegerField(blank=True, help_text='0-based index', null=True)),
                ('urn', models.CharField(max_length=255, unique=True)),
                ('tokens', models.ManyToManyField(related_name='named_entities', to='texts.token')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='named_entities.namedentitycollection')),
            ],
        ),
    ]
