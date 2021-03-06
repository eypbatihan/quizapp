# Generated by Django 4.0.3 on 2022-03-12 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='quiz.questions'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='quiz.quiz'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
