from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'taylor-series-center-a'
    forum = 10182
    title = 'compute the Taylor series for a polynomial around some other point'

    def good_enough(self):
        return True

    def perturb(self):
        x = var('x')
        self.x = x
        self.the_degree = 3
        self.the_polynomial = sum([randint(1,4)*((-1)**randint(0,1))*x**p for p in range(0,self.the_degree + 1)])
        self.the_center = randint(1,3)*((-1)**randint(0,1))
        
        self.latex_answer = r'\(' + latex(taylor(self.the_polynomial,x,self.the_center,self.the_degree + 1)(x=x+self.the_center)(x=var('y',latex_name=r'\left(' + latex(var('x',latex_name='x')-self.the_center) + r'\right)'))) + r'\)'

    def __init__(self):
        self.perturb()
        super(Question, self).__init__()

    def verify(self):
        return True

    def distractors(self,count):
        results = []

        for i in range(0,7):

            q =  randint(1,5)*((-1)**randint(0,1))
            x = var('x')
            wrong_answer = r'\(' + latex((q*x*x + taylor(self.the_polynomial,x,self.the_center,self.the_degree + 1)(x=x+self.the_center))(x=var('y',latex_name=r'\left(' + latex(var('x',latex_name='x')-self.the_center) + r'\right)'))) + r'\)'

            results.append( (wrong_answer, r'Focus on the \(' + str(latex(x-self.the_center)) + r'^2\) term.') )
        return results

    def answer(self):
        return self.latex_answer
        
