# Generated by Django 3.2.5 on 2021-10-26 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20211026_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Friday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Monday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Saturday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Sunday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Thursday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Tuesday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Wednesday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='question3',
        ),
        migrations.AddField(
            model_name='profile',
            name='answer1',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='answer2',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='question1',
            field=models.CharField(choices=[('a', '学院はどこですか？'), ('b', '部活サークルは？'), ('c', '出身県は？'), ('d', '出身高校は？'), ('e', '興味のある分野は？'), ('f', '将来の夢はなんですか？')], max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='question2',
            field=models.CharField(choices=[('a', '学院はどこですか？'), ('b', '部活サークルは？'), ('c', '出身県は？'), ('d', '出身高校は？'), ('e', '興味のある分野は？'), ('f', '将来の夢はなんですか？')], max_length=150),
        ),
        migrations.DeleteModel(
            name='Question_Answer',
        ),
    ]
