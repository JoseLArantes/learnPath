import json
from django.core.management.base import BaseCommand
from apps.study.models import Topic, Question, Answer

class Command(BaseCommand):
    help = 'Import questions from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        json_file = options['json_file']
        
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        for item in data:
            topic, _ = Topic.objects.get_or_create(name=item['topic'])
            question = Question.objects.create(
                topic=topic,
                text=item['question'],
                difficulty=item['difficulty']
            )
            for answer in item['answers']:
                Answer.objects.create(
                    question=question,
                    text=answer['text'],
                    is_correct=answer['is_correct']
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully imported questions'))
