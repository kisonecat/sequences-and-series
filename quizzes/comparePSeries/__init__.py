from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'reciprocal-n-log-n'
    forum = 10119
    title = 'compare a series to a p-series'

    def good_enough(self):
        for i in range(self.initial,self.initial + 100):
            if self.term_x(x=i) <= 0:
                return False

        if self.denominator_term == x**self.denominator_power:
            return False

        if self.numerator_term == x**self.numerator_power:
            return False

        return True

    def perturb(self):
        x = var('x')
        self.x = var('x')

        #(x^n - lower)/(x^m + lower) < (x^n - lower) / (x^m) < x^n / x^m
        #for n,m half integers

        if randint(0,1) == 0:
            self.goal_power = [1, 0.5][randint(0,1)]
            the_sign = -1
        else:
            self.goal_power = [1.5, 2, 3, 4][randint(0,3)]
            the_sign = 1
            
        self.numerator_power = 0.5 * randint(1,6)
        self.denominator_power = self.goal_power + self.numerator_power

        self.numerator_term = x**self.numerator_power
        self.denominator_term = x**self.denominator_power
        
        if self.numerator_power - 1 >= 0:
            self.numerator_term = self.numerator_term - the_sign * randint(1,5) * (x**randint(0,floor(self.numerator_power - 1)))

        if self.denominator_power - 1 >= 0:
            self.denominator_term = self.denominator_term + the_sign * randint(1,5) * (x**randint(0,floor(self.denominator_power - 1)))

        self.term_x = (self.numerator_term / self.denominator_term)
        self.term = (self.numerator_term / self.denominator_term )(x = self.variable)

        minimal_initial = 0
        try:
            minimal_initial = max(minimal_initial,find_root(self.numerator_term,0.5,100))
        except RuntimeError:
            print 'Numerator not zero'

        try:
            minimal_initial = max(minimal_initial,find_root(self.denominator_term,0.5,100))
        except RuntimeError:
            print 'Denominator not zero'

        self.initial = randint(ceil(minimal_initial) + 1,ceil(minimal_initial) + 5)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
        if self.answer() == 'The series diverges.':
            return [('The series converges.',r'Note that in this case the series is basically \(\sum ' + latex(1/(self.variable ** self.goal_power)) + '\).')]
        else:
            return [('The series diverges.',r'Note that in this case the series is basically \(\sum ' + latex(1/(self.variable ** self.goal_power)) + '\).')]

    def verify(self):
        try:
            if sum(self.term, self.variable, self.initial, oo).is_infinity():
                assert( self.answer() == 'The series diverges.' )
            else:
                assert( self.answer() == 'The series converges.' )
        except ValueError:
            assert( self.answer() == 'The series diverges.' )
    
    def answer(self):
        if self.goal_power > 1:
            return 'The series converges.'
        if self.goal_power <= 1:
            return 'The series diverges.'

        return 'I am not sure about the convergence of this series.'
