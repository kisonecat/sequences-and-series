from questions import *
import re

def terms_to_latex(terms):
    return r'\(' + (r',\quad '.join([latex(x) for x in terms])) + r',\quad\ldots \)'

class Question(RandomizedQuestion):
    module = __file__
    title = 'identify an arithmetic progression'
    video = 'arithmetic-progression'
    textbook = 'subsection:arithmetic-sequences'
    forum = 10058
    def __init__(self):
        initial_value = randint(1,5)
        common_ratio = randint(2,5) * ((-1)**randint(0,1))
        self.common_ratio = common_ratio

        self.terms = [initial_value]
        for _ in range(0,5):
            self.terms.append(self.terms[-1] + common_ratio)

        self.terms_latex = terms_to_latex(self.terms)

        self.wrong_ones = []
        for i in range(0,5):
            wrong_one = [initial_value]
            for j in range(0,5):
                if (i == j):
                    wrong_one = wrong_one + [wrong_one[-1] + (common_ratio + ((-1)**randint(0,1)))]
                else:
                    wrong_one = wrong_one + [wrong_one[-1] + common_ratio]

            self.wrong_ones.append( wrong_one )

        self.wrong_ones_latex = [terms_to_latex(terms) for terms in self.wrong_ones]

        super(Question, self).__init__()

    def distractors(self,count):
        explanations = []
        for i in range(0,5):
            explanation = 'Most of the terms differ by ' + str(self.common_ratio) + ' except that \(a_' + str(i) + r' = ' + str(self.wrong_ones[i][i]) + '\) and \(a_' + str(i+1) + ' = ' + str(self.wrong_ones[i][i+1]) + '\) differ by  ' + str(self.wrong_ones[i][i+1] - self.wrong_ones[i][i]) + ' so this cannot be the beginning of an arithmetic progression.'
            explanations.append((self.wrong_ones_latex[i], explanation))

        return explanations
        
    def verify(self):
        return True

    def answer(self):
        return terms_to_latex(self.terms)
