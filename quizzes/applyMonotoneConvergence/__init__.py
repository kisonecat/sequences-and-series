from questions import *
import re

class Question(RandomizedQuestion):
    module = __file__
    title = 'apply the monotone convergence theorem'
    video = 'monotone-convergence'
    forum = 10061

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','k']
        sequences = ['a','b','c']
        x = var( variables[randint(0, len(variables)-1)] )
        self.variable = x
        self.sequence = sequences[randint(0, len(sequences)-1)]

        self.initial = randint(-5,5)
        self.direction = (-1)**randint(0,1)

        self.next_term = self.initial + self.direction*randint(1,3)
        self.bound_below = self.next_term + randint(-5,-1)
        self.bound_above = self.next_term + randint(1,5)

        self.strictly_monotone = randint(0,1)

        if self.direction > 0:
            if self.strictly_monotone == 0:
                self.direction_name = 'nondecreasing'
            else:
                self.direction_name = 'increasing'
        if self.direction < 0:
            if self.strictly_monotone == 0:
                self.direction_name = 'nonincreasing'
            else:
                self.direction_name = 'decreasing'

        super(Question, self).__init__()

    def distractors(self, count):
        result = []

        result.append( ('No, the sequence does not converge.', 'The sequence is bounded and monotone, so by the Monotone Convergence Theorem, the sequence converges.') )

        if self.direction > 0:
            result.append( ('Yes, with limit between \({bound_below}\) and \({next_term}\).'.format( next_term=self.next_term, bound_below=self.bound_below ),
                            'It converges, but the sequence is ' + self.direction_name + '.') )
        else:
            result.append( ('Yes, with limit between \({next_term}\) and \({bound_above}\).'.format( next_term=self.next_term, bound_above=self.bound_above ),
                            'It converges, but the sequence is ' + self.direction_name + '.') )

        return result

    def answer(self):
        if self.direction > 0:
            return 'Yes, with limit between \({next_term}\) and \({bound_above}\).'.format( next_term=self.next_term, bound_above=self.bound_above )
        else:
            return 'Yes, with limit between \({bound_below}\) and \({next_term}\).'.format( next_term=self.next_term, bound_below=self.bound_below )
    
