# Generated by Django 3.2 on 2022-07-26 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('discussion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='user.customuser')),
                ('discussion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='discussion.discussion')),
                ('likes', models.ManyToManyField(related_name='likes', to='user.CustomUser')),
            ],
        ),
    ]
