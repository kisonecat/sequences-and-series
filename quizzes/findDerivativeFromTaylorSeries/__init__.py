from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'taylor-series'
#    forum = 10182
    title = 'find the derivative of a function from its Taylor series'

    def good_enough(self):
        return True

    def perturb(self):
        x = var('x')
        self.x = x
        self.the_power = randint(3,5)

        self.the_derivative = self.the_power * randint(7,12) * 2

        self.the_numeric_answer = derivative(cos(x**self.the_power),x,self.the_derivative)(x=0)
        
        self.taylor_coefficient = (-1)**(self.the_derivative/self.the_power/2) /  factorial(2*(self.the_derivative/self.the_power/2))
        assert( self.the_numeric_answer == factorial(self.the_derivative) * self.taylor_coefficient )

        if (-1)**(self.the_derivative/self.the_power/2) == 1:
            self.latex_answer = r'\(\frac{' + latex(self.the_derivative) + r'!}{' + latex((2*(self.the_derivative/self.the_power/2))) + r'!}\)'
        else:
            self.latex_answer = r'\(-\frac{' + latex(self.the_derivative) + r'!}{' + latex((2*(self.the_derivative/self.the_power/2))) + r'!}\)'

    def __init__(self):
        self.perturb()
        super(Question, self).__init__()

    def verify(self):
        return True

    def distractors(self,count):
        results = []

        for i in range(0,10):
            p = randint(1,7)
            d = self.the_derivative

            if randint(0,1) == 0:
                wrong_answer = r'\(\frac{' + latex(d) + r'!}{' + latex((2*(d/p/2))) + r'!}\)'
            else:
                wrong_answer = r'\(-\frac{' + latex(d) + r'!}{' + latex((2*(d/p/2))) + r'!}\)'

            if (-1)**(d/p/2) * factorial(d) /  factorial(2*(d/p/2)) == 1:
                next

            if (-1)**(d/p/2) * factorial(d) /  factorial(2*(d/p/2)) == -1:
                next

            if self.the_numeric_answer != (-1)**(d/p/2) * factorial(d) /  factorial(2*(d/p/2)):
                results.append( wrong_answer )

        results = uniq(results)
        results = [(response,'Think about the Taylor series expansion.') for response in results]
        return results

    def answer(self):
        return self.latex_answer
        
