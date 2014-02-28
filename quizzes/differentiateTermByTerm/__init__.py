from questions import *

class Question(RandomizedQuestion):
    module = __file__
    video = 'differentiate-power-series'
    forum = 10158
    title = 'differentiate a power series term-by-term'
    textbook = 'thm:term-by-term-calculus'

    def good_enough(self):
        self.verify()
        return True

    def perturb(self):
        x = var('x')
        self.x = x
        monomials = [a*((-1)**b)*x + c for a in range(1,10) for b in range(0,2) for c in range(0,10) if gcd(a,c) == 1]
        shuffle(monomials)

        self.term_coeff_x = monomials[0] / monomials[1]
        self.term_coeff = (self.term_coeff_x)(x=self.variable)
        self.term = self.term_coeff * x**self.variable
        self.initial = 0

        self.d_term_coeff_x = (x+1) * self.term_coeff_x(x=x+1)
        self.d_term_coeff = (self.d_term_coeff_x)(x=self.variable)
        self.d_term = self.my_expand(self.d_term_coeff) * x**self.variable

    def __init__(self):
        variables = ['n','n','n','n','n','n','n','n','m','m','m','m','m','k','k','k','k']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.perturb()
        super(Question, self).__init__()

    def possible_answer(self,f):
        return r'\(f' + "'" + r'(x) = \sum_{' + str(self.variable) + r'=0}^\infty \left( ' + latex(f) + r'\right)\)'

    def verify(self):
        print self.term
        df = derivative(sum( self.term, self.variable, 0, 10),x)
        claimed_df = sum( self.d_term, self.variable, 0, 9 )
        assert( df == claimed_df )
        return df == claimed_df

    def my_expand(self,f):
        return f.numerator().expand() / f.denominator()

    def distractors(self,count):
        results = []

        wrong_d_term_coeff_x = (x) * self.term_coeff_x(x=x)
        wrong_d_term_coeff = (wrong_d_term_coeff_x)(x=self.variable)
        wrong_d_term = self.my_expand(wrong_d_term_coeff) * x**self.variable
        results.append(( self.possible_answer(wrong_d_term), 'It looks like you have neglected to reindex the series.'))

        wrong_d_term_coeff_x = (x+1) * self.term_coeff_x(x=x)
        wrong_d_term_coeff = (wrong_d_term_coeff_x)(x=self.variable)
        wrong_d_term = self.my_expand(wrong_d_term_coeff) * x**self.variable
        results.append(( self.possible_answer(wrong_d_term), r'It looks like you are multiplying by \(' + str(self.variable) + r'+1\) instead of just \(' + str(self.variable) + r'\)' ))

        wrong_d_term_coeff_x = (x) * self.term_coeff_x(x=x+1)
        wrong_d_term_coeff = (wrong_d_term_coeff_x)(x=self.variable)
        wrong_d_term = self.my_expand(wrong_d_term_coeff) * x**self.variable
        results.append(( self.possible_answer(wrong_d_term), r'It looks like you made an error differentiating \(x^' + str(self.variable) + r'\)' ))

        wrong_d_term_coeff_x = self.term_coeff_x(x=x)
        wrong_d_term_coeff = (wrong_d_term_coeff_x)(x=self.variable)
        wrong_d_term = self.my_expand(wrong_d_term_coeff) * x**(self.variable - 1)
        f = wrong_d_term
        bad = r'\(f' + "'" + r'(x) = \sum_{' + str(self.variable) + r'=1}^\infty \left( ' + latex(f) + r'\right)\)'
        results.append(( bad, r'It looks like you neglected to multiply by \(' + str(self.variable) + r'\) when you differentiated.' ))

        wrong_d_term_coeff_x = x * self.term_coeff_x(x=x)
        wrong_d_term_coeff = (wrong_d_term_coeff_x)(x=self.variable)
        wrong_d_term = self.my_expand(wrong_d_term_coeff) * x**(self.variable - 1)
        f = wrong_d_term
        bad = r'\(f' + "'" + r'(x) = \sum_{' + str(self.variable) + r'=0}^\infty \left( ' + latex(f) + r'\right)\)'
        results.append(( bad, r'This is a very subtle mistake: you have included the \(' + str(self.variable) + r'=0\) term, but you should have removed it and then reindexed.' ))

        return results

    def answer(self):
        return self.possible_answer(self.d_term)
