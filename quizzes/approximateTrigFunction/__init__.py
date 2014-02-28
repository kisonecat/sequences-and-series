from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'taylor-for-limits'
    forum = 10187
    title = 'approximate the value of sine'

    def good_enough(self):
        # don't want just a single term to be good enough
        if (self.the_point**3) / factorial(3) < self.goal_accuracy:
            return False

        #wrong_error = abs(self.actual_value - sum([self.term_x(x=i) for i in range(self.initial,self.need_terms)]))
        #if n(wrong_error) <= n(self.goal_accuracy):
        #    print 'not inaccurate'
        #    return False

        return True
        
    def is_correct(self,response):
        return abs(sin(self.the_point) - response) < self.goal_accuracy

    def perturb(self):
        x = var('x')
        self.x = x
        nn = randint(1,6)
        self.the_point = QQ(nn)/QQ(randint(nn,nn+5))
        

        self.need_terms = [3,3][randint(0,1)]

        self.desired_accuracy = self.the_point**(self.need_terms + 2) / factorial(self.need_terms + 2)
        self.goal_accuracy = RR(2 * self.desired_accuracy).nearby_rational(max_error = self.desired_accuracy)

        if self.goal_accuracy.denominator() > 400:
            self.goal_accuracy = 10**floor(log(self.goal_accuracy.denominator())/log(10))

        self.rational_answer = taylor(sin(x),x,0,self.need_terms)(x=self.the_point)

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def other_distractors(self,count):
        results = []

        for term_count in range(self.initial,self.need_terms):
            value = sum([self.term_x(x=i) for i in range(self.initial,term_count+1)])
            wrong_error = self.actual_value - sum(self.term_x, var('x'), self.initial, term_count)
            if n(value - self.actual_value) > self.goal_accuracy:
                results.append((value,
                                 r'This is the sum of the terms through the \(' + str(self.variable) + ' = ' + str(i) + '\) term, but the next term is \(' + latex(self.term_x(x=term_count+1)) + '\) which is not small enough to ensure that the error is bounded by \(' + latex(self.goal_accuracy) + '\).'))
                #            else:
                #                results.append((value,
                #                                 r'This is the sum of the terms through the \(' + str(self.variable) + ' = ' + str(i) + '\) term, and it turns out to be within \(' + latex(self.goal_accuracy) + '\) of \(L\), but the alternating series test would not tell you that.'))
                
        approximate_value = sum([self.term_x(x=i) for i in range(self.initial,self.need_terms+1)])
        bad_guess = RR(approximate_value - 2 * self.goal_accuracy).nearby_rational(max_error=0.9*self.goal_accuracy)
        if bad_guess > 0 and all([r[0] != bad_guess for r in results]):
            results.append(( bad_guess, r'This is lower than the true value of \(L\).' ))
        bad_guess = RR(approximate_value - 3 * self.goal_accuracy).nearby_rational(max_error=0.9*self.goal_accuracy)
        if bad_guess > 0 and all([r[0] != bad_guess for r in results]):
            results.append(( bad_guess, r'This is much lower than the true value of \(L\).' ))
        bad_guess = RR(approximate_value + 2 * self.goal_accuracy).nearby_rational(max_error=0.9*self.goal_accuracy)
        if all([r[0] != bad_guess for r in results]):
            results.append(( bad_guess, r'This is higher than the true value of \(L\).' ))
        bad_guess = RR(approximate_value + 3 * self.goal_accuracy).nearby_rational(max_error=0.9*self.goal_accuracy)
        if all([r[0] != bad_guess for r in results]):
            results.append(( bad_guess, r'This is higher than the true value of \(L\).' ))

        return results

    def answer(self):
        return self.rational_answer
