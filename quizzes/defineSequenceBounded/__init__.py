from questions import *

class BoundedAboveQuestion(StaticQuestion):
    module = __file__
    video = 'sequence-bounded'
    forum = 10056
    textbook = 'subsection:boundedness'
    hint_filename = 'bounded-above-hints.html'
    title = 'define what it means for a sequence to be bounded above'
    question = 'To say that the sequence \(a_n\) is "bounded above" is to say what?'
    correct = 'There exists an \(M \in \mathbb{R}\), so that for all \(n \in \mathbb{N}\), we have \(a_n \leq M\).'
    incorrect = []
    incorrect.append(('There exists an \(n \in \mathbb{N}\), so that for all \(M \in \mathbb{R}\), we have \(a_n \leq M\).', 
                      'You have exchanged the roles of \(n\) and \(M\).'))
    incorrect.append(('For all \(M \in \mathbb{R}\), there exists an \(n \in \mathbb{N}\), so that \(a_n \leq M\).',
                      'You have exchanged the "for all" and "there exists."'))
    incorrect.append(('For all \(n \in \mathbb{N}\), there exists an \(M \in \mathbb{R}\), so that \(a_n \leq M\).', 
                      'You have exchanged the "for all" and "there exists" and the roles of \(n\) and \(M\).'))
    incorrect.append(('There exists an \(M \in \mathbb{R}\), so that for all \(n \in \mathbb{N}\), we have \(a_n \geq M\).', 
                      'You have the inequality going in the wrong direction.'))

    incorrect.append(('There exists an \(n \in \mathbb{N}\), so that for all \(M \in \mathbb{R}\), we have \(a_n \geq M\).', 
                      'You have exchanged the roles of \(n\) and \(M\), and you have the inequality in the wrong direction.'))
    incorrect.append(('For all \(M \in \mathbb{R}\), there exists an \(n \in \mathbb{N}\), so that \(a_n \geq M\).',
                      'You have exchanged the "for all" and "there exists" and you have the inequality in the wrong direction.'))
    incorrect.append(('For all \(n \in \mathbb{N}\), there exists an \(M \in \mathbb{R}\), so that \(a_n \geq M\).', 
                      'You have exchanged the "for all" and "there exists" and the roles of \(n\) and \(M\) and you have the inequality in the wrong direction.'))

class BoundedBelowQuestion(StaticQuestion):
    module = __file__
    hint_filename = 'bounded-below-hints.html'
    video = 'sequence-bounded'
    forum = 10056
    textbook = 'subsection:boundedness'
    title = 'define what it means for a sequence to be bounded below'
    question = 'To say that the sequence \(a_n\) is "bounded below" is to say what?'
    correct = 'There exists an \(M \in \mathbb{R}\), so that for all \(n \in \mathbb{N}\), we have \(a_n \geq M\).'
    incorrect = []
    incorrect.append(('There exists an \(n \in \mathbb{N}\), so that for all \(M \in \mathbb{R}\), we have \(a_n \geq M\).', 
                      'You have exchanged the roles of \(n\) and \(M\).'))
    incorrect.append(('For all \(M \in \mathbb{R}\), there exists an \(n \in \mathbb{N}\), so that \(a_n \geq M\).',
                      'You have exchanged the "for all" and "there exists."'))
    incorrect.append(('For all \(n \in \mathbb{N}\), there exists an \(M \in \mathbb{R}\), so that \(a_n \geq M\).', 
                      'You have exchanged the "for all" and "there exists" and the roles of \(n\) and \(M\).'))
    incorrect.append(('There exists an \(M \in \mathbb{R}\), so that for all \(n \in \mathbb{N}\), we have \(a_n \leq M\).', 
                      'You have the inequality going in the wrong direction.'))

    incorrect.append(('There exists an \(n \in \mathbb{N}\), so that for all \(M \in \mathbb{R}\), we have \(a_n \leq M\).', 
                      'You have exchanged the roles of \(n\) and \(M\), and you have the inequality in the wrong direction.'))
    incorrect.append(('For all \(M \in \mathbb{R}\), there exists an \(n \in \mathbb{N}\), so that \(a_n \leq M\).',
                      'You have exchanged the "for all" and "there exists" and you have the inequality in the wrong direction.'))
    incorrect.append(('For all \(n \in \mathbb{N}\), there exists an \(M \in \mathbb{R}\), so that \(a_n \leq M\).', 
                      'You have exchanged the "for all" and "there exists" and the roles of \(n\) and \(M\) and you have the inequality in the wrong direction.'))

class Question(QuestionBag):
    title = 'define what it means for a sequence to be bounded'
    questions = [BoundedBelowQuestion, BoundedAboveQuestion]
