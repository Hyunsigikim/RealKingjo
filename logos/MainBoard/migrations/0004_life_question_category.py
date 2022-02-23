# Generated by Django 4.0.2 on 2022-02-21 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FreeBoard', '0004_alter_comment_answer_alter_comment_question'),
        ('MainBoard', '0003_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='life_question',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_life_question', to='FreeBoard.category'),
            preserve_default=False,
        ),
    ]
