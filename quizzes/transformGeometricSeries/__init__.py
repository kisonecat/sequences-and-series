from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'transform-geometric-series'
    forum = 10159
    title = 'transform a geometric series to find a power series representation'
    textbook = 'example:formula-for-log-three-halves'

    def good_enough(self):
        self.verify()
        return True

    def perturb(self):
        x = var('x')
        self.x = x

        self.the_coefficient = randint(1,4)
        self.the_power = randint(1,4)
        self.the_variable = (self.the_coefficient*x)**self.the_power
        self.the_first_function = 1/(1-self.the_variable)
        self.the_function = expand(derivative(self.the_first_function,x))

        nn = var('n')
        self.nn = nn
        self.the_term = nn*self.the_power * self.the_coefficient**(nn*self.the_power) * x**(nn*self.the_power-1)

        c = prod([e for e in (self.the_term).operands() if e.is_numeric()])
        self.c = c

        self.the_first_function = self.the_first_function / c
        self.the_function = self.the_function / c
        self.the_term = self.the_term / c

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','n','m','m','m','m','m','k','k','k','k']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def verify(self):
        assert( sum(self.answer(),self.nn,1,oo) == self.the_function )
        return True

    def answer(self):
        return self.the_term
