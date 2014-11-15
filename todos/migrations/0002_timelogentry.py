# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeLogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('end_at', models.DateTimeField(null=True, blank=True)),
                ('todoItem', models.ForeignKey(related_name='logs', to='todos.ToDoItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
