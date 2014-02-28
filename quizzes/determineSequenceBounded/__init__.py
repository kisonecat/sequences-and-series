from questions import *
import re

################################################################
class GenericBoundednessQuestion(RandomizedQuestion):
    module = __file__
    title = 'determine whether a sequence is bounded'
    video = 'sequence-bounded'
    textbook = 'example:sequence-bounded'
    forum = 10057
    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','k']
        sequences = ['a','b','c']
        x = var( variables[randint(0, len(variables)-1)] )
        a_n = var( sequences[randint(0, len(sequences)-1)] )
        self.variable = x
        self.sequence = a_n
        self.term = x
        RandomizedQuestion.__init__(self)

    def text(self):
        term = latex(self.term)
        return "Consider the sequence ${self.sequence}_{{{n}}} = {term}$.  Is the sequence bounded above?  Bounded below?".format(n=self.variable,self=self,term=term)

    def distractors(self, count):
        result = []

        value = limit( self.term, **{str(self.variable): oo} )
        if not (value.is_real() and value.is_infinity() and value.is_positive()):
            result.append('Bounded below, but not bounded above.')
        if not (value.is_real() and value.is_infinity() and value.is_negative()):
            result.append( 'Bounded above, but not bounded below.')
        if not (not value.is_real() and str(value) == 'ind'):
            result.append( 'Bounded above and bounded below.')
        if not (not value.is_real() and str(value) == 'und'):
            result.append( 'Bounded neither above nor below.')

        return result

    def answer(self):
        value = limit( self.term, **{str(self.variable): oo} )
        if value.is_real() and value.is_infinity() and value.is_positive():
            return 'Bounded below, but not bounded above.'
        if value.is_real() and value.is_infinity() and value.is_negative():
            return 'Bounded above, but not bounded below.'
        if not value.is_real() and str(value) == 'ind':
            return 'Bounded above and bounded below.'
        if not value.is_real() and str(value) == 'und':
            return 'Bounded neither above nor below.'
    
class Question(GenericBoundednessQuestion):
    def __init__(self):
        GenericBoundednessQuestion.__init__(self)
        x = self.variable
        # could include something which is bounded both ways, and also x*sin(x)
        self.term = randint(1,5)*((-1)**(randint(0,1)))*x*x + randint(-5,5)*x + randint(-5,5)
