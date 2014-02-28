from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'alternating-series-important'
#    forum = 10187
    title = 'approximate a value of arctangent'
    textbook = 'example:approximate-alternating-harmonic-series'

    def good_enough(self):
        # don't want just a single term to be good enough
        #if (self.the_point**3) / factorial(3) < self.goal_accuracy:
        #    return False

        if abs(arctan(self.the_point) - self.rational_answer) > self.goal_accuracy:
            print 'inaccurate'
            return False

        # two terms suffice
        if (self.the_point ** 5)/5 >= self.goal_accuracy:
            return False

        return True
        
    def is_correct(self,response):
        return abs(sin(self.the_point) - response) < self.goal_accuracy

    def perturb(self):
        x = var('x')
        self.x = x
        nn = randint(1,6)

        self.the_point = QQ(1)/QQ(randint(2,5))
        self.need_terms = 2

        self.desired_accuracy = self.the_point ** (2 * self.need_terms + 1) / (2 * self.need_terms + 1)
        self.not_enough_accuracy = self.the_point ** (2 * self.need_terms - 1) / (2 * self.need_terms - 1)
        ff = 0.1 + 0.05 * randint(1,6)
        self.goal_accuracy = RR(0.5 * self.desired_accuracy + 0.5 * self.not_enough_accuracy).nearby_rational(max_error = abs(self.not_enough_accuracy - self.desired_accuracy) * ff)

        self.term_x = (-1)**x / (2*x + 1)

        self.rational_answer = taylor(arctan(x),x,0,2*self.need_terms - 1)(x=self.the_point)
        self.actual_value = arctan(self.the_point)
        
    def __init__(self):
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
        results = []

        spacing = ceil(self.goal_accuracy * self.rational_answer.denominator())

        for v in range(-10,10):
            guess = ((self.rational_answer.numerator() + spacing*v)/(self.rational_answer.denominator()))
            if QQ((self.rational_answer.numerator() + spacing*v)/(self.rational_answer.denominator())).denominator() == self.rational_answer.denominator():
                if abs(guess - arctan(self.the_point)) > self.goal_accuracy:
                    if (v < 0):
                        results.append(( guess, r'This is lower than the true value.' ))            
                    if (v > 0):
                        results.append(( guess, r'This is higher than the true value.' ))

        return results
        
        for term_count in range(0,self.need_terms):
            value = sum([self.term_x(x=i) * (self.the_point ** (2*i+1)) for i in range(0,term_count+1)])
            wrong_error = self.actual_value - value
            if n(value - self.actual_value) > self.goal_accuracy:
                results.append((value,
                                 r'This is the sum of the terms through the \(x^{' + str(2*term_count+1) + '}\) term, but the next term is not small enough to ensure that the error is bounded by \(' + latex(self.goal_accuracy) + '\).'))
                #            else:
                #                results.append((value,
                #                                 r'This is the sum of the terms through the \(' + str(self.variable) + ' = ' + str(i) + '\) term, and it turns out to be within \(' + latex(self.goal_accuracy) + '\) of \(L\), but the alternating series test would not tell you that.'))
                
        approximate_value = sum([self.term_x(x=i) * (self.the_point ** (2*i+1)) for i in range(0,self.need_terms+1)])

        bad_guess = RR(approximate_value - 2 * self.goal_accuracy).nearby_rational(max_error=0.9*self.goal_accuracy)
        if bad_guess > 0 and all([r[0] != bad_guess for r in results]):
            results.append(( bad_guess, r'This is lower than the true value.' ))
        bad_guess = RR(approximate_value - 3 * self.goal_accuracy).nearby_rational(max_error=0.9*self.goal_accuracy)
        if bad_guess > 0 and all([r[0] != bad_guess for r in results]):
            results.append(( bad_guess, r'This is much lower than the true value.' ))
        bad_guess = RR(approximate_value + 2 * self.goal_accuracy).nearby_rational(max_error=0.9*self.goal_accuracy)
        if all([r[0] != bad_guess for r in results]):
            results.append(( bad_guess, r'This is higher than the true value.' ))
        bad_guess = RR(approximate_value + 3 * self.goal_accuracy).nearby_rational(max_error=0.9*self.goal_accuracy)
        if all([r[0] != bad_guess for r in results]):
            results.append(( bad_guess, r'This is higher than the true value.' ))

        return results

    def answer(self):
        return self.rational_answer
