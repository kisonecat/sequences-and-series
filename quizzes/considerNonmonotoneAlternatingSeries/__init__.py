from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'monotone-important-for-ast'
    forum = 10149
    title = 'consider the alternating series test in a nonmonotone situation'

    def good_enough(self):
        if self.p > 1 and self.q <= 1:
            return True

        if self.q > 1 and self.p <= 1:
            return True

        if self.q > 1 and self.q > 1 and self.p != self.q:
            return True

        return False

    def perturb(self):
        x = var('x')
        self.x = var('x')

        self.p = [Rational('1/2'),1,2,3,4][randint(0,4)]
        self.q = [Rational('1/2'),1,2,3,4][randint(0,4)]

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

        self.a_term_x = -1/(x ** self.p)
        self.b_term_x = 1/(x ** self.q)

        if randint(0,1) == 0:
            self.a_term_x = -self.a_term_x
            self.b_term_x = -self.b_term_x

        self.a_term = (self.a_term_x)(x = self.variable)
        self.b_term = (self.b_term_x)(x = self.variable)

        self.a_term = (self.a_term_x)(x = (self.variable+1)/2)
        self.b_term = (self.b_term_x)(x = (self.variable)/2)

        self.initial = randint(1,8)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):

        if self.answer() == 'The series diverges.':
            return [('The series converges.','You may be thinking that the series converges by applying the alternating series test, but the alternating series test assumes that the absolute value of the terms is a monotone sequence, which is not the case here.  In short, the alternating series test does not apply.')]

        if self.answer() == 'The series converges.':
            return [('The series diverges.','You may be thinking that because the alternating series test does not apply, then the series diverges.  But just because a test does not apply does not mean that the test proves divergence.')]

    def verify(self):
        try:
            if sum(self.a_term, self.variable, self.initial, oo).is_infinity() and not sum(self.b_term, self.variable, self.initial, oo).is_infinity():
                assert( self.answer() == 'The series diverges.' )
            if not sum(self.a_term, self.variable, self.initial, oo).is_infinity() and sum(self.b_term, self.variable, self.initial, oo).is_infinity():
                assert( self.answer() == 'The series diverges.' )
            if not sum(self.a_term, self.variable, self.initial, oo).is_infinity() and not sum(self.b_term, self.variable, self.initial, oo).is_infinity():
                assert( self.answer() == 'The series converges.' )
        except ValueError:
            assert( self.answer() == 'The series diverges.' )
    
    def answer(self):
        if self.p > 1 and self.q > 1:
            return 'The series converges.'

        return 'The series diverges.'
