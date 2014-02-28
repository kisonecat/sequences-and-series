from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'comparison-test'
    forum = 10088
    title = 'apply the comparison test to analyze convergence'
    textbook = 'section:comparison-test'

    def good_enough(self):
        for i in range(self.cutoff,30):
            if self.numerator(x=i) >= 2**i:
                return False

        return True

    def perturb(self):
        x = var('x')
        self.numerator = randint(1,7)*x*x + randint(0,7)*x + randint(2,8)
        self.numerator_n = self.numerator(x=self.variable)
        self.ratio = randint(3,9)
        self.denominator = self.ratio**x
        self.denominator_n = self.denominator(x=self.variable)
        self.cutoff = ceil(find_root(2**x - self.numerator, 0, 10))
        self.term = (self.numerator / self.denominator)(x = self.variable)
        self.initial = randint(0,5)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
        if self.answer() == 'The series diverges.':
            return [('The series converges.',r'You could compare the given series to a geometric series.')]
        else:
            return [('The series diverges.',r'You could compare the given series to a geometric series.')]

    def verify(self):
        try:
            if sum(self.term, self.variable, self.initial, oo).is_infinity():
                assert( self.answer() == 'The series diverges.' )
            else:
                assert( self.answer() == 'The series converges.' )
        except ValueError:
            assert( self.answer() == 'The series diverges.' )
    
    def answer(self):
        return 'The series converges.'

