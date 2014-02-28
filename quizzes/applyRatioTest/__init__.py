from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'ratio-test-example'
    forum = 10115
    title = 'apply the ratio test on a series involving powers'
    textbook = 'example:n-to-fifth-over-five-to-n'

    def good_enough(self):
        return self.ell != 1

    def perturb(self):
        x = var('x')
        self.x = var('x')

        self.ratio = randint(2,3)
        self.c = randint(2,3)
        monomials = [a*x + c for a in range(1,10) for c in range(0,10) if gcd(a,c) == 1]
        shuffle(monomials)
        self.denominator = self.ratio**( self.c * x + randint(1,5) ) * monomials[0]
        self.denominator_n = self.denominator(x=self.variable)

        if randint(0,1) == 0:
            self.numerator_ratio = randint( self.ratio ** self.c + 1, self.ratio ** self.c + 3 )
        else:
            self.numerator_ratio = randint( 2, self.ratio ** self.c - 1 )

        self.numerator = self.numerator_ratio**x
        self.numerator_n = self.numerator(x=self.variable)

        self.term_x = (self.numerator / self.denominator)
        self.ell = limit( (self.term_x)(x = x+1) / (self.term_x), x=oo )

        self.term = (self.numerator / self.denominator)(x = self.variable)
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

        return 'The ratio test is silent as to whether this series converges or diverges.'
