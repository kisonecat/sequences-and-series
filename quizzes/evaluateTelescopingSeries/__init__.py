from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'telescoping-series'
    forum = 10085
    title = 'evaluate a telescoping series'
    def perturb(self):
        self.telescope = randint(1,5)/(randint(1,5) * var('x') + randint(1,5))
        self.term = (self.telescope - self.telescope(x=x+1)).simplify_rational()(x=self.variable)
        self.initial = randint(0,5)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def verify(self):
        return sum(self.term, self.variable, self.initial, oo) == self.answer()

    def answer(self):
        return self.telescope(x=self.initial)
