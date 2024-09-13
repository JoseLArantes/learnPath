# Generated by Django 5.1 on 2024-09-13 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("study", "0006_testchallenge_alter_testresult_test_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Test",
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
                ("number_of_questions", models.PositiveIntegerField()),
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
                ("passing_score", models.PositiveIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
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
                on_delete=django.db.models.deletion.CASCADE, to="study.test"
            ),
        ),
        migrations.AlterField(
            model_name="useranswer",
            name="test",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="study.test"
            ),
        ),
        migrations.DeleteModel(
            name="TestChallenge",
        ),
    ]
