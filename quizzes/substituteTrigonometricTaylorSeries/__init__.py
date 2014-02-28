from questions import *

class Question(RandomizedQuestion):
    module = __file__
#    video = ''
    forum = 0
    title = 'substitute a Taylor series for a trigonometric function into a polynomial'
    textbook = 'example:substitute-in-polynomial-to-taylor-series'

    def good_enough(self):
        return True

    def perturb(self):
        x = var('x')
        self.x = x

        self.the_polynomial = expand(chebyshev_T(randint(2,5),x))
        self.the_degree = self.the_polynomial.degree(x)
        self.the_trig_function = [sin(x),cos(x)][randint(0,1)]
        self.the_function = self.the_polynomial(x = self.the_trig_function)

        self.term_count = 5
        x = var('x')
        p = PolynomialRing(QQ,'x')(taylor(self.the_function,x,0,self.term_count))
        self.the_answer = r'\(' + join([('+' if sign(c) == 1 and (p != 0) else '') + latex(c*(x**p)) if c != 0 else '' for p,c in zip( range(0,self.term_count+1), p.coeffs() )], '') + r'+ \cdots \)'

        R = PolynomialRing(QQ,'x')
        self.the_ring = R
        self.xx = R.gens()[0]
        
        if self.the_trig_function == cos(x):
            self.trig_x = R(taylor(self.the_trig_function,x,0,4)) + O(self.xx**4)
        if self.the_trig_function == sin(x):
            self.trig_x = R(taylor(self.the_trig_function,x,0,4)) + O(self.xx**5)

        self.reduced_trig_x = self.the_polynomial(x=self.the_trig_function).reduce_trig()

    def __init__(self):
        self.perturb()
        super(Question, self).__init__()

    def verify(self):
        return True

    def distractors(self,count):
        results = []

        for i in range(0,7):
            x = var('x')
            p = PolynomialRing(QQ,'x')(taylor(self.the_function,x,0,self.term_count))
            q = 0
            focus = 0
            if p.coeffs()[2] != 0:
                q = PolynomialRing(QQ,'x')(x*x*QQ(i-3)/QQ(3))
                focus = 2
            if p.coeffs()[3] != 0:
                q = PolynomialRing(QQ,'x')(x*x*x*QQ(i-3)/QQ(6))
                focus = 3
            if q != 0:
                wrong_answer = r'\(' + join([('+' if sign(c) == 1 and (p != 0) else '') + latex(c*(x**p)) if c != 0 else '' for p,c in zip( range(0,self.term_count+1), (p+q).coeffs() )], '') + r'+ \cdots \)'
                results.append( (wrong_answer, 'Pay attention to the \(x^' + str(focus) + '\) term.') )

        return results

    def answer(self):
        return self.the_answer
        
