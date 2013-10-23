from questions import *

class Question(RandomizedQuestion):
    module = __file__
#    video = ''
    forum = 0
    title = 'multiply two power series'

    def good_enough(self):
        return True

    def perturb(self):
        x = var('x')
        self.x = x
        nn = var('n')
        self.nn = nn

        self.term_a = (randint(1,5) * nn + randint(1,5)) * x**nn
        self.term_b = (randint(1,5) * nn + randint(1,5)) * x**nn

        self.sum_a = sum([self.term_a(n=i) for i in range(0,5)])
        self.sum_b = sum([self.term_b(n=i) for i in range(0,5)])
        self.the_answer = (self.sum_a * self.sum_b).polynomial(QQ).truncate(4)

    def __init__(self):
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
        results = []

        for i in range(1,count+1):
            wrong_answer = self.the_answer + i*(x**2) * (-1)**(randint(0,1)) + randint(0,8)*(x**3) * (-1)**(randint(0,1)) + randint(0,8)*(x**4) * (-1)**(randint(0,1))
            wrong_answer = wrong_answer.polynomial(QQ).truncate(4)
            results.append((r'\(' + join((latex(wrong_answer).split('+'))[::-1],'+') + r'+ \cdots \)','Focus on the \(x^2\) term, since that is the first to differ among the choices.'))

        return results

    def verify(self):
        return True

    def answer(self):
        return r'\(' + join((latex(self.the_answer).split('+'))[::-1],'+') + r'+ \cdots \)'
