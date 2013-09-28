from questions import *

class Question(RandomizedQuestion):
    module = __file__
    title = 'evaluate a geometric series with rational ratio'
    def perturb(self):
        denominator = randint(2,10)
        numerator = randint(1,denominator - 1)
        sign = 2*randint(0,1) - 1
        self.ratio = Rational((sign * numerator, denominator))
        self.initial = randint(0,5)

    def __init__(self):
        self.perturb()
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        super(Question, self).__init__()

    def verify(self):
        return sum(self.ratio ** self.variable, self.variable, self.initial, oo) == self.answer()

    def answer(self):
        return (self.ratio ** self.initial) / (1 - self.ratio)
