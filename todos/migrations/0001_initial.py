# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=256)),
                ('status', models.CharField(default=b'default', max_length=16, choices=[(b'default', b'Default status'), (b'scheduled', b'Scheduled status'), (b'archived', b'archived status')])),
                ('due_at', models.DateTimeField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ToDoItemList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('is_archived', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('owner', models.ForeignKey(related_name='lists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='itemlist',
            field=models.ForeignKey(related_name='todos', blank=True, to='todos.ToDoItemList', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todoitem',
            name='owner',
            field=models.ForeignKey(related_name='todos', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
