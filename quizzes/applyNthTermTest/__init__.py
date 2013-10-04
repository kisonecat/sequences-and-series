from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'nth-term-test'
    forum = 10086
    title = 'apply the limit test for divergence'
    def good_enough(self):
        bad_points = [QQ(e.rhs()) for e in solve(self.denominator==0,x)]
        if any([p.is_integral() for p in bad_points]):
            return False

        return self.term.numerator().degree(self.variable) == 2 and self.term.denominator().degree(self.variable) == 2

    def perturb(self):
        x = var('x')
        monomials = [a*((-1)**b)*x + c for a in range(1,10) for b in range(0,2) for c in range(0,10) if gcd(a,c) == 1]
        shuffle(monomials)
        self.numerator = monomials[0] * monomials[1]
        self.denominator = monomials[2] * monomials[3]
        self.term = (self.numerator / self.denominator)(x=self.variable)
        self.the_limit = limit((self.numerator / self.denominator), x=oo)
        self.initial = randint(0,5)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
        if self.answer() == 'The series diverges.':
            return [('The series converges.',r'You should consider the limit of \(' + latex(self.term) + r'\).')]
        else:
            return [('The series diverges.',r'You should consider the limit of \(' + latex(self.term) + r'\).')]

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

