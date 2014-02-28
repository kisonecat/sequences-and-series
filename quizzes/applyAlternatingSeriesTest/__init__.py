from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'alternating-series-test'
    forum = 10146
    title = 'apply the alternating series test when appropriate'
    textbook = 'thm:alternating-series-test'

    def good_enough(self):
        return True

    def perturb(self):
        x = var('x')
        self.x = var('x')

        self.p = [Rational('1/2'),1,2,3][randint(0,3)]
        print self.p
        if self.p == 2:
            self.term_x = randint(1,5)/(x**2 + randint(1,5) * x + randint(1,5))
        if self.p == 3:
            self.term_x = randint(1,5)/(x**3 + randint(1,5) * x**2 + randint(1,5))
        if self.p == 1:
            if randint(0,1) == 0:
                self.term_x = randint(1,5)/(x + randint(1,3) * log(x))
            else:
                self.term_x = randint(1,5)/(x + randint(1,3) * sqrt(x))
        if self.p == Rational('1/2'):
            if randint(0,1) == 0:
                self.term_x = randint(1,5)/(sqrt(x) + randint(1,3) * sqrt(x))            
            else:
                self.term_x = randint(1,5)/(sqrt(x) + randint(1,3) * log(x))            

        self.term = ((-1)**(x+randint(0,1)) * self.term_x)(x = self.variable)
        self.term_abs = (self.term_x)(x = self.variable)

        self.initial = randint(3,8)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
        response = self.answer()

        if self.answer() == 'The series diverges.':
            return [('The series converges absolutely.',response),
                    ('The series converges conditionally.',response)]

        if self.answer() == 'The series converges absolutely.':
            return [('The series diverges.',response),
                    ('The series converges conditionally.',response)]

        if self.answer() == 'The series converges conditionally.':
            return [('The series converges absolutely.',response),
                    ('The series diverges.',response)]

    def verify(self):
        try:
            if sum(self.term, self.variable, self.initial, oo).is_infinity():
                assert( self.answer() == 'The series diverges.' )
            else:
                try:
                    if sum(abs(self.term), self.variable, self.initial, oo).is_infinity():
                        assert( self.answer() == 'The series converges conditionally.' )
                    else:
                        assert( self.answer() == 'The series converges absolutely.' )
                except ValueError:
                    assert( self.answer() == 'The series converges conditionally.' )
        except ValueError:
            assert( self.answer() == 'The series diverges.' )
    
    def answer(self):
        if self.p > 1:
            return 'The series converges absolutely.'
        if self.p <= 1 and self.p > 0:
            return 'The series converges conditionally.'
        if self.p <= 0:
            return 'The series diverges.'

        return 'I am not sure about the convergence of this series.'
