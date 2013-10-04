from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'harmonic-series'
    forum = 10087
    title = 'analyze series similar to the harmonic series'
    def good_enough(self):
        return True

    def perturb(self):
        x = var('x')
        good_pairs = [(a,b) for a in range(2,9) for b in range(2,9) if gcd(a,b) == 1]
        shuffle(good_pairs)
        a = good_pairs[0][0]
        b = good_pairs[0][1]
        self.term_numerator = a
        self.term_denominator = b*(x + randint(2,7))
        self.term = (self.term_numerator / self.term_denominator)(x = self.variable)

        self.term_numerator = self.term.numerator()
        self.term_denominator = self.term.denominator()
        self.initial = randint(0,5)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
        if self.answer() == 'The series diverges.':
            return [('The series converges.',r'Recall that the harmonic series diverges.')]
        else:
            return [('The series diverges.',r'Recall that the harmonic series diverges.')]

    def verify(self):
        try:
            if sum(self.term, self.variable, self.initial, oo).is_infinity():
                assert( self.answer() == 'The series diverges.' )
            else:
                assert( self.answer() == 'The series converges.' )
        except ValueError:
            assert( self.answer() == 'The series diverges.' )
    
    def answer(self):
        return 'The series diverges.'

