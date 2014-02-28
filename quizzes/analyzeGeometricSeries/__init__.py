from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'geometric-series'
    forum = 10084
    title = 'analyze the convergence of a geometric series'
    textbook = 'section:geometric-series'

    def good_enough(self):
        return self.ratio != 1

    def perturb(self):
        self.telescope = randint(1,5)/(randint(1,5) * var('x') + randint(1,5))
        self.ratio = RR(random()*4 - 2).nearby_rational(max_denominator=12)
        self.term = randint(1,9)*((-1)**randint(0,1)) * (self.ratio**self.variable)
        self.initial = randint(0,5)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
        if self.answer() == 'The series diverges.':
            return [('The series converges.',r'Note that the common ratio in this geometric series is \(' + latex(self.ratio) + r'\), which is larger than \(1\) in absolute value.')]
        else:
            return [('The series diverges.',r'Note that the common ratio in this geometric series is \(' + latex(self.ratio) + r'\), which is between \(-1\) and \(1\).')]

    def verify(self):
        try:
            if sum(self.term, self.variable, self.initial, oo).is_infinity():
                assert( self.answer() == 'The series diverges.' )
            else:
                assert( self.answer() == 'The series converges.' )
        except ValueError:
            assert( self.answer() == 'The series diverges.' )
    
    def answer(self):
        if abs(self.ratio) < 1:
            return 'The series converges.'
        else:
            return 'The series diverges.'

