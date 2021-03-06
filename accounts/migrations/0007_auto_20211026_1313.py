# Generated by Django 3.2.5 on 2021-10-26 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20211019_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(choices=[('a', '学院はどこですか？'), ('b', '部活サークルは？'), ('c', '出身県は？'), ('d', '出身高校は？'), ('e', '興味のある分野は？'), ('f', '将来の夢はなんですか？')], max_length=150)),
                ('question2', models.CharField(choices=[('a', '学院はどこですか？'), ('b', '部活サークルは？'), ('c', '出身県は？'), ('d', '出身高校は？'), ('e', '興味のある分野は？'), ('f', '将来の夢はなんですか？')], max_length=150)),
                ('answer1', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('answer2', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('student', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='student',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
