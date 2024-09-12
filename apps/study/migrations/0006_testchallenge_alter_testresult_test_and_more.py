# Generated by Django 5.1 on 2024-09-11 22:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("study", "0005_useranswer"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestChallenge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_of_questions", models.IntegerField()),
                (
                    "difficulty",
                    models.CharField(
                        choices=[
                            ("easy", "Easy"),
                            ("medium", "Medium"),
                            ("hard", "Hard"),
                        ],
                        max_length=10,
                    ),
                ),
                ("passing_score", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("questions", models.ManyToManyField(to="study.question")),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="study.topic"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="testresult",
            name="test",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="study.testchallenge"
            ),
        ),
        migrations.AlterField(
            model_name="useranswer",
            name="test",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="study.testchallenge"
            ),
        ),
        migrations.DeleteModel(
            name="Test",
        ),
    ]
