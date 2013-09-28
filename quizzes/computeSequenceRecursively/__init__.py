from questions import *
import re

class Question(RandomizedQuestion):
    module = __file__
    title = 'compute terms of a sequence presented as a recursive formula'
    video = 'recursive-sequence'
    forum = 10052
    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','k']
        sequences = ['a','b','c']
        x = var( variables[randint(0, len(variables)-1)] )
        self.variable = x
        self.sequence = sequences[randint(0, len(sequences)-1)]

        self.initial_0 = randint(-5,5)
        self.initial_1 = randint(-5,5)

        self.previous_1 = var( 'p_1' )
        self.previous_2 = var( 'p_2' )

        self.formula = 0
        while (not re.search( 'p_\{1\}', str(latex(self.formula)) )) or (not re.search( 'p_\{2\}', str(latex(self.formula)) )):
            self.formula = randint(-2,3)*self.previous_1 + randint(-1,1)*self.previous_1*self.previous_2 + randint(-2,3)*self.previous_2
            print latex(self.formula)
        
        self.formula_latex = self.sequence + '_' + str(x) + ' = ' + latex(self.formula).replace( 'p_{1}', '{' + self.sequence + '_{' + str(x) + '-1}}' ).replace( 'p_{2}', '{' + self.sequence + '_{' + str(x) + '-2}}' )

        self.terms = [self.initial_0, self.initial_1]
        for i in range(2,10):
            self.terms = self.terms + [self.formula(p_1=self.terms[i-1], p_2=self.terms[i-2])]

        self.goal_index = randint(4,6)

        super(Question, self).__init__()

    def verify(self):
        p2 = self.initial_0
        p1 = self.initial_1
        for i in range(2,self.goal_index):
            x = self.formula(p_1=p1, p_2=p2)
            p2 = p1
            p1 = x
        return p1 == self.answer()

    def answer(self):
        return self.terms[self.goal_index]
