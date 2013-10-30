from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'interval-of-convergence'
    forum = 10156
    title = 'find the interval of convergence of a power series'

    def good_enough(self):
        return True

    def perturb(self):
        x = var('x')
        self.x = x

        possible_rationals = flatten([[QQ(p)/QQ(q) for p in range(1,q) if gcd(p,q) == 1] for q in range(2,10)])
        shuffle(possible_rationals)
        self.r = possible_rationals[0] * ((-1)**(randint(0,1)))
        self.common_ratio = self.r
        self.constant_factor = possible_rationals[1] 
        self.term_coeff_x = self.constant_factor * (self.r**x) / x
        self.term_coeff = (self.term_coeff_x)(x=self.variable)
        self.term = self.term_coeff * x**self.variable
        self.initial = randint(1,5)
        self.answer_interval = self.answer().replace( 'E', 'e' )


    def __init__(self):
        variables = ['n','n','n','n','n','n','n','n','m','m','m','m','m','k','k','k','k']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def verify(self):
        return True

    def possible_answer(self, left_open, right_open):
        result = r'Exactly when \(x\) is in the interval \('
        if left_open:
            result = result + r'\left('
        else:
            result = result + r'\left['

        result = result + latex(-1/abs(self.r))

        result = result + ','

        result = result + latex(1/abs(self.r))

        if right_open:
            result = result + r'\right)'
        else:
            result = result + r'\right]'
            
        result = result + r'\)'
        return result
        
    def distractors(self,count):
        results = []

        results.append((self.possible_answer( self.r > 0, self.r < 0 ),
                        'The series converges conditionally at the other endpoint.'))

        results.append((self.possible_answer( self.r < 0, self.r < 0 ),
                        'The series converges conditionally at exactly one endpoint.'))

        results.append((self.possible_answer( self.r > 0, self.r > 0 ),
                        'The series converges conditionally at exactly one endpoint.'))

        return results

    def answer(self):
        return self.possible_answer( self.r < 0, self.r > 0 )
        
