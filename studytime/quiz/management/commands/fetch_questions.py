import random
from django.core.management.base import BaseCommand, CommandError

import requests

from studytime.questions.models import MultipleChoiceQuestion, MultipleChoiceAnswer
from studytime.quiz.models import MultipleChoiceQuiz
from studytime.subjects.models import Subject


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('subject', nargs='+', type=str)

        # Named (optional) arguments
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        base_url = 'https://opentdb.com/api.php?'
        opentdb_subject_map = {
            'science': 17,
            'maths': 19,
            'english': 10,
            'history': 23
        }
        quiz_counter = 0
        for subject in options['subject']:

            if subject not in opentdb_subject_map:
                raise CommandError('Subject must be one of: %s' % opentdb_subject_map.keys())
            url = base_url + 'amount=5&type=multiple&difficulty=easy&category=%s' % opentdb_subject_map[subject]
            self.stdout.write(self.style.SUCCESS('Hitting URL ' + url))
            resp = requests.get(url)
            print(resp.json())
            s_model, created = Subject.objects.get_or_create(name=subject)
            for index, question in enumerate(resp.json()['results']):
                question_cleaned = clean_question(question)
                self.stdout.write(self.style.SUCCESS('Fetched Question "%s"' % question_cleaned))
                if index % 5 == 0:
                    quiz_counter += 1
                z_model, created = MultipleChoiceQuiz.objects.get_or_create(name='opentdb %s' % quiz_counter, subject=s_model)
                q_model, created = MultipleChoiceQuestion.objects.get_or_create(prompt_text=question_cleaned['prompt'], quiz=z_model)
                try:
                    a_model = MultipleChoiceAnswer.objects.get(question=q_model)
                except MultipleChoiceAnswer.DoesNotExist:
                    a_model = MultipleChoiceAnswer(question=q_model, choices=question_cleaned['choices'], answer_array=question_cleaned['answer_array'])
                    a_model.save()
                self.stdout.write(self.style.SUCCESS('Created Model'))


def clean_question(question):
    from pprint import pprint
    pprint(question)
    question_dict = {}
    question_dict['prompt'] = question['question']
    all_answers = question['incorrect_answers']
    all_answers.append(question['correct_answer'])
    random.shuffle(all_answers)
    question_dict['choices'] = all_answers
    for i, choice in enumerate(question_dict['choices']):
        print(i, choice, question['correct_answer'], choice == question['correct_answer'])
        if choice == question['correct_answer']:
            if i == 0:
                question_dict['answer_array'] = ['a']
            elif i == 1:
                question_dict['answer_array'] = ['b']
            elif i == 2:
                question_dict['answer_array'] = ['c']
            elif i == 3:
                question_dict['answer_array'] = ['d']
    pprint(question_dict)
    return question_dict
