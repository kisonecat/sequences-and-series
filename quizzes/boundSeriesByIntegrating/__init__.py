from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'integral-test'
    forum = 10121
    title = 'bound the value of a series by using the integral test'
    textbook = 'example:approximate-sum-one-over-n-squared'

    def good_enough(self):
        return (self.integral_value != self.initial_value) and (len(self.distractors(0)) >= 2)

    def perturb(self):
        x = var('x')
        self.x = var('x')
        monomials = [a*x + c for a in range(1,5) for c in range(1,5) if gcd(a,c) == 1]
        shuffle(monomials)

        self.term_x = derivative(-1/monomials[0],x)
        self.term = (self.term_x)(x=self.variable)
        self.initial = randint(1,5)

        self.integral_value = integral( self.term_x, x, self.initial, oo )
        self.initial_value = (self.term_x)(x=self.initial)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
        results = []

        results.append(([self.initial_value, self.initial_value + self.integral_value], r'You have exchanged the roles of \(f(' + str(self.initial) + ')\) and the integral.'))

        results.append(([self.integral_value - self.initial_value, self.integral_value], r'You are subtracting \(f(' + str(self.initial) + ')\) when you should be adding it.'))

        results.append((sorted([self.integral_value, self.initial_value]), r'You should add \(f(' + str(self.initial) + ')\) to the value of the integral.'))

        true_value = n(sum(self.term_x, var('x'), self.initial, oo))

        nearby = RR(true_value).nearby_rational(max_denominator=2 * QQ(self.integral_value).denominator())
        results.append((sorted([self.integral_value, nearby]), r'You should add \(f(' + str(self.initial) + ')\) to the value of the integral.'))

        nearby = RR(true_value).nearby_rational(max_denominator=2 * QQ(self.integral_value).denominator())
        results.append((sorted([self.integral_value + self.initial_value, self.integral_value + self.initial_value*2]), r'You should add \(f(' + str(self.initial) + ')\) to the value of the integral.'))

        results = [r for r in results if not ((r[0][0] <= true_value) and (true_value <= r[0][1]))]

        real_results = []
        for r in results:
            if not any([x[0] == r[0] for x in real_results]):
                real_results.append(r)

        return real_results

    def verify(self):
        true_value = n(sum(self.term_x, var('x'), self.initial, oo))
        lhs = self.answer()[0]
        rhs = self.answer()[1]
        assert( lhs <= true_value )
        assert( true_value <= rhs )
    
    def answer(self):
        return [ self.integral_value, self.integral_value + self.initial_value ]
