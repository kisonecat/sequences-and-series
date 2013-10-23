from questions import *

class Question(RandomizedQuestion):
    module = __file__
#    video = ''
    forum = 0
    title = 'identify a power series'

    def good_enough(self):
        return True

    def perturb(self):
        x = var('x')
        self.x = x
        nn = var('n')

        possible_rationals = flatten([[QQ(p)/QQ(q) for p in range(1,q) if gcd(p,q) == 1] for q in range(2,10)])
        shuffle(possible_rationals)

        self.good_function = (possible_rationals[0] * nn**randint(1,3) + possible_rationals[1]) * x**n
        if randint(0,3) == 0:
            self.good_function = (possible_rationals[0] * nn**randint(1,3) + possible_rationals[1] * cos(nn)) * x**n
        if randint(0,3) == 0:
            self.good_function = (possible_rationals[0] * nn**randint(1,3) + possible_rationals[1] * sin(nn)) * x**n
        
        self.bad_functions = []

        self.bad_functions.append((sin(x**randint(1,2)) * x**nn, r'The coefficient involves sine of \(x\).'))
        self.bad_functions.append((cos(x**randint(1,2)) * x**nn, r'The coefficient involves cosine of \(x\).'))
        self.bad_functions.append((tan(x**randint(1,2)) * x**nn, r'The coefficient involves tangent of \(x\).'))
        self.bad_functions.append((sin(x**nn), r'There is no \(x^n\) term.  The only \(x^n\) is inside \(\sin\).'))
        self.bad_functions.append((cos(x**nn), r'There is no \(x^n\) term.  The only \(x^n\) is inside \(\cos\).'))
        self.bad_functions.append((tan(x**nn), r'There is no \(x^n\) term.  The only \(x^n\) is inside \(\tan\).'))

        self.bad_functions.append(((possible_rationals[3] * sin(x) + possible_rationals[2]) * x**nn, r'The coefficient involves sine of \(x\).'))
        self.bad_functions.append(((possible_rationals[4] * cos(x) + possible_rationals[5]) * x**nn, r'The coefficient involves cosine of \(x\).'))

        self.bad_functions.append(((cos(possible_rationals[6] * x) + possible_rationals[7]) * x**nn, r'The coefficient involves cosine of \(x\).'))
        self.bad_functions.append(((sin(possible_rationals[8] * x) + possible_rationals[9]) * x**nn, r'The coefficient involves sine of \(x\).'))

        self.bad_functions.append((sqrt(x) * x**nn, r'The power of \(x\) is not integral.'))

        self.bad_functions.append((x**(randint(1,9)*0.1) * x**nn, r'The power of \(x\) is not integral.'))
        self.bad_functions.append((x**(-nn), r'The power of \(x\) is negative.'))

        shuffle(self.bad_functions)
        self.bad_functions = self.bad_functions[0:4]


    def __init__(self):
        variables = ['n','n','n','n','n','n','n','n','m','m','m','m','m','k','k','k','k']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def verify(self):
        return True

    def distractors(self,count):
        result = []
        for bad_function, explanation in self.bad_functions:
            result.append((r'\(\sum_{n=0}^\infty ' + latex(bad_function) + '\)', explanation))

        return result

    def answer(self):
        return r'\(\sum_{n=0}^\infty ' + latex(self.good_function) + r'\)'
