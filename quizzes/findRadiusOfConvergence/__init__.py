from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'radius-of-convergence'
    forum = 10157
    title = 'find the radius of convergence of a power series'
    textbook = 'definition:radius-of-convergence'

    def good_enough(self):
        if self.term_coeff_x(x=1) == 0:
            return False

        if self.term_coeff_x.numerator().operator() != operator.add and self.term_coeff_x.denominator().operator() != operator.add:
            return False

        return True

    def perturb(self):
        x = var('x')
        self.x = x

        self.the_power = randint(2,8)
        self.term_coeff_x = (x * randint(1,5) * randint(0,1)  + randint(1,5) * randint(0,1)) / ((self.the_power**x) + randint(1,5) * x * randint(0,1) + randint(1,5) * randint(0,1))
        if self.term_coeff_x.numerator()(x=1) != 0:
            if randint(0,1) == 0:
                self.term_coeff_x = QQ(1) / self.term_coeff_x
            self.radius_of_convergence = QQ(1) / limit(self.term_coeff_x(x=x+1) / self.term_coeff_x,x=oo)

        self.term_coeff = (self.term_coeff_x)(x=self.variable)
        self.term = self.term_coeff * x**self.variable
        self.initial = randint(1,5)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','n','m','m','m','m','m','k','k','k','k']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def verify(self):
        assert( self.radius_of_convergence == QQ(1) / abs(limit(simplify((self.term_coeff_x(x=var('x')+1)) / (self.term_coeff_x(x=var('x')))),x=oo)) )
        return True

    def answer(self):
        return self.radius_of_convergence
        
