from .multiple_choice import display_quiz_mc
def display_quiz (question, answers=[], multiple=False, randomize=True,
                          question_background="#6F78FF"):
    if type(question)==dict:
        if 'type' not in question.keys() or \
           question['type']=='multiple_choice':
            display_quiz_mc(question['question'], question['answers'],
                            multiple=multiple, randomize=randomize,
                            question_background=question_background)
        else:
            print("Question type", question['type']," not supported yet")
    else:
        display_quiz_mc(question, answers,
                        multiple=multiple, randomize=randomize,
                        question_background=question_background)



