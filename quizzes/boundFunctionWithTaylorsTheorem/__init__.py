from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'taylor-as-mvt'
    forum = 10185
    title = 'bound the value of a function using Taylor\'s theorem'

    def good_enough(self):
        if self.maximum_possible >= 40:
            return False

        if self.minimum_possible <= -20:
            return False

        return True

    def perturb(self):
        x = var('x')
        self.x = x
        self.p = randint(1,3)*2

        self.the_center = randint(1,5)
        self.the_point = self.the_center + randint(1,3)

        self.f_at_center = randint(1,5)
        self.derivative_at_center = randint(1,5)
        self.second_derivative_at_center = randint(1,5) * 2

        self.third_derivative_bound = randint(1,5) * 6

        x = self.the_point
        a = self.the_center
        self.maximum_possible = self.f_at_center + (x-a) * self.derivative_at_center + ((x-a)**2) * self.second_derivative_at_center / 2 + ((x-a)**3) * self.third_derivative_bound / 6
        self.minimum_possible = self.f_at_center + (x-a) * self.derivative_at_center + ((x-a)**2) * self.second_derivative_at_center / 2 - ((x-a)**3) * self.third_derivative_bound / 6

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def distractors(self,count):
        results = []

        for i in range(-5,6):
            if i != 0:
                wrong_answer = r'\(' + latex(self.minimum_possible+i) + r' \leq f(' + latex(self.the_point) + r') \leq ' + latex(self.maximum_possible+i) + r'\)'
                results.append( (wrong_answer, 'This is not the correct interval.') )
        return results


    def answer(self):
        return r'\(' + latex(self.minimum_possible) + r' \leq f(' + latex(self.the_point) + r') \leq ' + latex(self.maximum_possible) + r'\)'
