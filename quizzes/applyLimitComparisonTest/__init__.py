from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'limit-comparison-test'
    forum = 10144
    title = 'apply the limit comparison test to analyze convergence'
    textbook = 'section:limit-comparison-test'

    def perturb(self):
        x = var('x')
        self.x = x
        self.total_power = randint(1,3)
        self.numerator_power = randint(1,3)
        self.denominator_power = self.total_power + self.numerator_power

        self.numerator_term = randint(1,7)*x**self.numerator_power + sum([randint(0,5) * x**i for i in range(1,self.numerator_power)]) + randint(1,8)
        self.numerator_n = self.numerator_term(x=self.variable)
        self.denominator_term = randint(1,7)*x**self.denominator_power + sum([randint(0,5) * x**i for i in range(1,self.denominator_power)]) + randint(1,8)
        self.denominator_n = self.denominator_term(x=self.variable)
        self.term = (self.numerator_term / self.denominator_term)(x = self.variable)
        self.initial = randint(0,5)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
        if self.answer() == 'The series diverges.':
            return [('The series converges.',r'Consider how the largest power in the numerator compares to the largest power in the denominator.')]
        else:
            return [('The series diverges.',r'Consider how the largest power in the numerator compares to the largest power in the denominator.')]

    def verify(self):
        try:
            if sum(self.term, self.variable, self.initial, oo).is_infinity():
                assert( self.answer() == 'The series diverges.' )
            else:
                assert( self.answer() == 'The series converges.' )
        except ValueError:
            assert( self.answer() == 'The series diverges.' )
    
    def answer(self):
        if self.total_power > 1:
            return 'The series converges.'
        else:
            return 'The series diverges.'

