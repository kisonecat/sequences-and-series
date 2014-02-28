from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'taylor-series'
    forum = 10181
    title = 'find the first few terms of a Taylor series'

    def good_enough(self):
        print self.the_function
        if self.the_function(x=1) == 1:
            return False

        if self.term_count >= 7:
            return False

        if taylor(self.the_function,x,0,2) - taylor(self.the_function,x,0,1)  == 0:
            return False

        return True

    def perturb(self):
        x = var('x')
        self.x = x

        some_functions = [sin(x),1-cos(x),exp(x) - 1,tan(x),x**2]
        f = some_functions[randint(0,len(some_functions)-1)]
        g = some_functions[randint(0,len(some_functions)-1)]

        if randint(0,1) == 0:
            self.the_function = f(x=g)
        else:
            self.the_function = f * g

        self.the_center = 0

        if self.the_function(x=1) == 1:
            return

        self.term_count = 1
        print self.the_function
        p = PolynomialRing(QQ,'x')(taylor(self.the_function,x,0,self.term_count))
        while len([c for c in p.coeffs() if c != 0]) <= 3:
            self.term_count = self.term_count + 1
            p = PolynomialRing(QQ,'x')(taylor(self.the_function,x,0,self.term_count))

        x = var('x')
        p = PolynomialRing(QQ,'x')(taylor(self.the_function,x,0,self.term_count))
        self.the_answer = r'\(0 ' + join([('+' if sign(c) == 1 else '') + latex(c*(x**p)) if c != 0 else '' for p,c in zip( range(0,self.term_count+1), p.coeffs() )], '') + r'+ \cdots \)'


    def __init__(self):
        self.perturb()
        super(Question, self).__init__()

    def verify(self):
        return True

    def distractors(self,count):
        results = []

        for i in range(0,5):
            x = var('x')
            p = PolynomialRing(QQ,'x')(taylor(self.the_function,x,0,self.term_count))
            q = PolynomialRing(QQ,'x')(x*x*QQ(randint(-3,3))/QQ(randint(1,3)))
            if q != 0:
                wrong_answer = r'\(0 ' + join([('+' if sign(c) == 1 else '') + latex(c*(x**p)) if c != 0 else '' for p,c in zip( range(0,self.term_count+1), (p+q).coeffs() )], '') + r'+ \cdots \)'
                results.append( (wrong_answer, 'Focus on the \(x^2\) term.') )

        return results

    def answer(self):
        return self.the_answer
        
