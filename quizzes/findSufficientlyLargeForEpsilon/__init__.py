from questions import *

class Question(RandomizedQuestion):
    module = __file__
    title = r'find a sufficiently large index to guarantee a sequence is within epsilon of L'
    video = 'n-for-epsilon'
    forum = 10055
    def __init__(self):
        denominator = randint(2,10)
        numerator = randint(1,denominator - 1)
        sign = 2*randint(0,1) - 1
        self.ratio = Rational((sign * numerator, denominator))
        self.initial = randint(0,5)
        variables = ['n','n','n','n','n','n','n','m','m','m','k','k']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        super(Question, self).__init__()

        sequences = ['a','b','c']
        self.sequence_name = sequences[randint(0, len(sequences)-1)]

        a = randint(1,12)
        b = randint(1,12)
        c = randint(1,5)
        d = c*randint(3,6)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.sequence = (a*self.variable + b)/(c*self.variable + d)
        self.sequence_latex = r'\displaystyle\frac{' + latex(a*self.variable+b) + '}{' + latex(c*self.variable+d) + '}'

        self.epsilon = Rational((1, 2**randint(0,3) * 5**randint(0,2) * (c*c / (gcd(a*d - b*c, c*c)))))
        self.sequence_limit = Rational((a,c))

        self.bound = QQ((-(c*d*self.epsilon + a*d - b*c)))/(c*c*self.epsilon)
        if self.bound < 0:
            self.bound = QQ((-(c*d*self.epsilon - (a*d - b*c))))/(c*c*self.epsilon)

        if self.bound.is_integral():
            self.bound = self.bound + 1
        else:
            self.bound = ceil(self.bound)

        self.none_of_above = True
        if randint(0,1) == 0:
            self.none_of_above = False

    def good_enough(self):
        return (self.bound < 1000) and (self.bound > 10) and (self.c * (self.bound - 2) + self.d > 0)

    def distractors(self,count):
        explanations = []

        distractor_count = 5
        if not self.none_of_above:
            distractor_count = 4
            
        for i in range(1,distractor_count):
            choice = self.bound - 2 * i
            distractor = '\(' + str(self.variable).capitalize() + ' = ' + latex(choice) + '\)'
            explanation = 'But \(' + str(self.sequence_name) + '_{' + latex(choice) + '} = ' + latex(Rational((self.a * choice + self.b,self.c * choice + self.d))) + '\) which is not within \(' + latex(self.epsilon) + '\) of \(' + latex(self.sequence_limit) + '\).'
            explanations.append((distractor, explanation))

        if not self.none_of_above:
            explanations.append(('None of these choices for \(' + str(self.variable).capitalize() + '\) is large enough.',
                                 'The choice of \(' + str(self.variable).capitalize() + ' = ' + latex(self.bound) + '\) is large enough.'))

        return explanations

    def verify(self):
        return abs( (a*self.bound + b) / (c*self.bound + d) - (a/c) ) <= self.epsilon

    def answer(self):
        if self.none_of_above:
            return 'None of these choices for \(' + str(self.variable).capitalize() + '\) is large enough.'
        else:
            return '\(' + str(self.variable).capitalize() + ' = ' + latex(self.bound) + '\)'
