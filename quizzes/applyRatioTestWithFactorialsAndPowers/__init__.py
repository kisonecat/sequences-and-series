from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'ratio-test-one-over-e'
    forum = 10117
    title = 'apply the ratio test on a series involving factorials and powers'
    textbook = 'example:ratio-test-factorials'

    def good_enough(self):
        return self.ell != 1

    def perturb(self):
        x = var('x')
        self.x = var('x')

        self.cutoff = randint(1,9)

        self.term_x = (factorial(x) * 10**x) / ((self.cutoff*x)**x)
        self.term = (self.term_x)(x = self.variable)
        self.ell = limit( (self.term_x)(x = x+1) / (self.term_x), x=oo )
        self.initial = randint(1,9)

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
