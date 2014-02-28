from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'taylor-for-limits'
    forum = 10184
    title = 'evaluate a limit by considering the Taylor series'

    def good_enough(self):
        return True

    def perturb(self):
        x = var('x')
        self.x = x

        self.the_ring = PolynomialRing(QQ,'x')
        self.xx = self.the_ring.gens()[0]

        self.some_functions = [sin(x),sin(3*x),(cos(x)-1)/x,exp(x) - 1,tan(3*x),tan(x),log(1+x)]
        shuffle(self.some_functions)
        self.the_numerator = (self.some_functions[0] + self.some_functions[1])**2
        self.the_denominator = self.some_functions[2] * self.some_functions[3]

        if randint(0,1) == 0:
            self.the_numerator, self.the_denominator = [self.the_denominator, self.the_numerator]

        self.the_function = self.the_numerator / self.the_denominator
        print self.the_function

        #self.the_answer = limit(self.the_function,x=0)
        # this is WAY faster
        self.the_answer = taylor(self.the_function,x,0,0)
        print self.the_answer

    def __init__(self):
        self.perturb()
        super(Question, self).__init__()

#    def distractors(self,count):
#        results = []
#        return results

    def verify(self):
        return True

    def answer(self):
        return self.the_answer
        
