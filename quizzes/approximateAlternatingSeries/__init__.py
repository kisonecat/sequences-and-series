from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'alternating-series-important'
    forum = 10147
    title = 'approximate the value of an alternating series'

    def good_enough(self):
        wrong_error = abs(self.actual_value - sum([self.term_x(x=i) for i in range(self.initial,self.need_terms)]))
        #if n(wrong_error) <= n(self.goal_accuracy):
        #    print 'not inaccurate'
        #    return False

        if len(self.distractors(2)) < 2:
            print 'too few distractors'
            return False

        if self.answer().denominator() >= 1000:
            return False

        if self.l.denominator() >= 100000:
            return False
        if self.r.denominator() >= 100000:
            return False
        if self.l.numerator() >= 100000:
            return False
        if self.r.numerator() >= 100000:
            return False

        if QQ(self.rational_answer) >= QQ(self.r):
            return False

        if QQ(self.rational_answer) <= QQ(self.l):
            return False

        return True

    def perturb(self):
        x = var('x')
        self.x = x
        self.p = randint(1,3)*2
        possible_numerators = ZZ(QQ((sum(((-1)**(x+1))/(x**self.p),x,1,oo)/pi**self.p).denominator())).divisors()
        shuffle(possible_numerators)
        self.term_x = ((-1)**(x+1) * possible_numerators[0]) / (x**self.p)
        self.term = (self.term_x)(x=self.variable)

        self.initial = randint(1,4)
        self.initial = 1

        self.actual_value = sum(self.term_x, x, self.initial, oo)

        self.need_terms = randint(self.initial + 1,self.initial+4)
        self.desired_accuracy = abs((self.term_x)(x = self.need_terms + 1))
        self.desired_accuracy_overestimate = abs((self.term_x)(x = self.need_terms))
        print self.desired_accuracy, self.desired_accuracy_overestimate
        self.goal_accuracy = RR((self.desired_accuracy + self.desired_accuracy_overestimate)/2).nearby_rational(max_error = abs(self.desired_accuracy_overestimate - self.desired_accuracy)/2.001)
        print self.goal_accuracy > self.desired_accuracy
        print self.desired_accuracy_overestimate > self.goal_accuracy 

        l = sum(self.term_x, var('x'), self.initial, self.need_terms)
        r = sum(self.term_x, var('x'), self.initial, self.need_terms + 1)
        l,r = sorted([l,r])
        self.l = l
        self.r = r
        self.rational_answer = RR((l+r)/2).nearby_rational(max_error = abs(l - r))

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
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

    def verify(self):
        actual_error = self.actual_value - sum(self.term_x, var('x'), self.initial, self.need_terms)
        assert( actual_error <= self.goal_accuracy )
    
    def answer(self):
        return self.rational_answer

        #return sum(self.term_x, var('x'), self.initial, self.need_terms)
#        return r'\(\left| L - \sum_{' + str(self.variable) + r'=1}^{' + str(self.need_terms) + '} ' + latex(self.term) + r'\right| < ' + latex(self.goal_accuracy) + '\)'

