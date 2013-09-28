from questions import *
import re

class Question(RandomizedQuestion):
    module = __file__
    title = 'compute limit of a sequence presented as a formula'
    video = 'sequence-limit'
    forum = 10054
    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','k']
        sequences = ['a','b','c']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.sequence = sequences[randint(0, len(sequences)-1)]
        x = var('x')
        
        denominator = ((x + randint(1,5)) * (x + randint(1,5))).expand()
        self.formula = (randint(-5,5) * x * x + randint(-5,5) * x + randint(-5,5))/denominator
        self.formula_latex = latex(self.formula(x=self.variable))
        self.sequence_limit = limit(self.formula,x=oo)

        super(Question, self).__init__()

    def good_enough(self):
        negative_roots = all([s.rhs().is_negative() for s in solve(self.formula.denominator()==0,x)])
        return (not self.sequence_limit.is_infinity()) and (self.formula(x=100) != self.formula(x=1000)) and negative_roots

    def verify(self):
        p2 = self.initial_0
        p1 = self.initial_1
        for i in range(2,self.goal_index):
            x = self.formula(p_1=p1, p_2=p2)
            p2 = p1
            p1 = x
        return p1 == self.answer()

    def answer(self):
        return self.sequence_limit
