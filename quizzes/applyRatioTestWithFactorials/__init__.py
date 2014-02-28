from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'ratio-test-statement'
    forum = 10116
    title = 'apply the ratio test on a series involving factorials'

    def good_enough(self):
        return self.ell != 1

    def perturb(self):
        x = var('x')
        self.x = var('x')

        self.factorial_term = factorial(x) * (randint(1,4) * x  + randint(1,4))
        self.factorial_term_n = self.factorial_term(x=self.variable)

        self.ratio = randint(2,6)
        self.power_term = self.ratio**x
        self.power_term_n = self.power_term(x=self.variable)

        if randint(0,1) == 0:
            self.term_x = (self.power_term / self.factorial_term)
        else:
            self.term_x = (self.factorial_term / self.power_term)

        self.term = (self.term_x)(x = self.variable)
        self.ell = limit( (self.term_x)(x = x+1) / (self.term_x), x=oo )
        self.initial = randint(0,9)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
        if self.answer() == 'The series diverges.':
            return [('The series converges.',r'Note that in this case \(L = ' + latex(self.ell) + '\).')]
        else:
            return [('The series diverges.',r'Note that in this case \(L = ' + latex(self.ell) + '\).')]

    def verify(self):
        try:
            if sum(self.term, self.variable, self.initial, oo).is_infinity():
                assert( self.answer() == 'The series diverges.' )
            else:
                assert( self.answer() == 'The series converges.' )
        except ValueError:
            assert( self.answer() == 'The series diverges.' )
    
    def answer(self):
        if self.ell < 1:
            return 'The series converges.'
        if self.ell > 1:
            return 'The series diverges.'
        if self.ell.is_infinity():
            return 'The series diverges.'

        return 'The ratio test is silent as to whether this series converges or diverges.'
