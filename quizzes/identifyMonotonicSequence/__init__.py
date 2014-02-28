from questions import *
import re

def terms_to_latex(terms):
    return r'\(' + (r',\quad '.join([latex(x) for x in terms])) + r',\quad\ldots \)'

class Question(RandomizedQuestion):
    module = __file__
    title = 'identify a monotonic sequence'
    video = 'sequence-monotone'
    textbook = 'subsection:monotonicity'
    forum = 10060
    def __init__(self):
        self.direction = (-1)**randint(0,1)

        self.direction_word = 'increasing'
        self.direction_symbol = r' < '
        if self.direction < 0:
            self.direction_word = 'decreasing'
            self.direction_symbol = r' > '

        initial_value = randint(1,5)

        self.terms = [initial_value]
        for _ in range(0,5):
            self.terms.append(self.terms[-1] + self.direction * randint(1,6))

        self.terms_latex = terms_to_latex(self.terms)

        self.wrong_ones = []
        for i in range(0,5):
            wrong_one = [initial_value]
            for j in range(0,5):
                if (i == j):
                    wrong_one = wrong_one + [wrong_one[-1] - self.direction * randint(1,6)]
                else:
                    wrong_one = wrong_one + [wrong_one[-1] + self.direction * randint(1,6)]

            self.wrong_ones.append( wrong_one )

        self.wrong_ones_latex = [terms_to_latex(terms) for terms in self.wrong_ones]

        super(Question, self).__init__()

    def distractors(self,count):
        explanations = []
        for i in range(0,5):
            explanation = 'Mostly these initial terms are ' + self.direction_word + ' except that \(a_' + str(i) + r' = ' + str(self.wrong_ones[i][i]) + '\) and \(a_' + str(i+1) + ' = ' + str(self.wrong_ones[i][i+1]) + '\) so these cannot be the initial terms of a monotonic sequence.'
            explanations.append((self.wrong_ones_latex[i], explanation))

        return explanations
        
    def verify(self):
        return True

    def answer(self):
        return terms_to_latex(self.terms)
