import random
import json

from .multiple_choice import display_quiz_mc
from .dynamic import display_questions_dynamic
def display_quiz (question, answers=[],  randomize=True, multiple=False, 
                  question_background=""):
    if type(question)==dict:
        if 'type' not in question.keys() or \
           question['type']=='multiple_choice':
            if question_background=="":
                question_background="#6F78FF"
            #print(question_background)
            display_quiz_mc(question['question'], question['answers'],
                            multiple=False, randomize=randomize,
                            question_background=question_background)
        elif question['type']=='many_choice':
            if question_background=="":
                question_background="#FEB44A"
            display_quiz_mc(question['question'], question['answers'],
                            multiple=True, randomize=randomize,
                            question_background=question_background)
        else:
            print("Question type", question['type']," not supported yet")
    else:
        if question_background=="":
            question_background="#6F78FF"
        display_quiz_mc(question, answers,
                        multiple=multiple, randomize=randomize,
                        question_background=question_background)



def display_multiple (ref, num=1_000_000, shuffle_questions=False,
                      shuffle_answers=True, static=False):

    if static:
        questions=[]
        with open(ref, 'r') as infile:
            questions=json.load(infile)
  
            if  num < len(questions):
                questions=random.sample(questions, num)
            elif shuffle_questions:
                random.shuffle(questions)

            for question in questions:
                display_quiz (question)

    else:
        display_questions_dynamic(ref, num, shuffle_questions, shuffle_answers)

