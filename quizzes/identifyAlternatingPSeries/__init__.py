from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'alternating-series-test'
    forum = 10145
    title = 'identify an alternating p-series'

    def good_enough(self):
        # do not want to test on harmonic series
        return self.p != 1

    def perturb(self):
        x = var('x')
        self.x = var('x')

        self.p = randint(50,150) / 100.0
        if randint(0,2) == 0:
            self.p = -self.p

        #d = randint(2,8)
        #nn = randint(0,d-1)
        #self.p = Rational('1') + Rational(str(nn) + '/' + str(d)) * ((-1)**randint(0,1))
        #self.p = n(self.p,digits=2)
        
        self.term_x = randint(2,7) / (randint(2,7) * (x ** self.p))
        self.term = ((-1)**x * self.term_x)(x = self.variable)
        self.initial = randint(1,5)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
        if self.answer() == 'The series diverges.':
            return [('The series converges absolutely.',r'But this is basically an alternating p-series with \(p = ' + latex(self.p) + '\).'),
                    ('The series converges conditionally.',r'But this is basically an alternating p-series with \(p = ' + latex(self.p) + '\).')]

        if self.answer() == 'The series converges absolutely.':
            return [('The series diverges.',r'But this is basically an alternating p-series with \(p = ' + latex(self.p) + '\).'),
                    ('The series converges conditionally.',r'But this is basically an alternating p-series with \(p = ' + latex(self.p) + '\).')]

        if self.answer() == 'The series converges conditionally.':
            return [('The series converges absolutely.',r'But this is basically an alternating p-series with \(p = ' + latex(self.p) + '\).'),
                    ('The series diverges.',r'But this is basically an alternating p-series with \(p = ' + latex(self.p) + '\).')]

    def verify(self):
        try:
            if sum(self.term, self.variable, self.initial, oo).is_infinity():
                assert( self.answer() == 'The series diverges.' )
            else:
                assert( self.answer() == 'The series converges.' )
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
