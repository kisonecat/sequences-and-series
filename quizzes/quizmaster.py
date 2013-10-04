def random_choice( list ):
    return list[randint(0,len(list)-1)]

################################################################
class Question:
    """Base class for all questions"""

    def __init__(self):
        self.data = []

    @classmethod
    def variation_count(cls):
        return 1

    def text(self):
        return "This question is missing the problem text."

    with open('positive-feedback.txt') as f:
        positive_feedback = [s.strip() for s in f.readlines()]
    def praise(self):
        return random_choice(Question.positive_feedback)

    def potential_distractor(self):
        return self.__class__().answer()

    def distractors(self, count):
        results = []
        while( len(results) < count ):
            distractor = self.potential_distractor()
            if not (distractor in results):
                results.append( distractor )
        return results

    def __repr__(self):
        return "A question."

################################################################
class StaticQuestion(Question):
    """Base class for a question without any randomization."""

    def __init__(self):
        Question.__init__(self)
    def text(self):
        return self.__class__.question
    def correct(self):
        return self.__class__.answer
    def distractors(self,count):
        return self.__class__.incorrect

################################################################
class QuestionBag(Question):
    """A random question from a list of question classes"""

    @classmethod
    def variation_count(cls):
        return sum([b.variation_count() for b in cls.questions])

    def __init__(self):
        questions = self.__class__.questions
        self.__class__ = questions[randint(0,len(questions)-1)]
        self.__class__.__init__(self)

################################################################
# OBJECTIVE Define what it means for a sequence to be bounded

class DefinitionSequenceBoundedAboveQuestion(StaticQuestion):
    question = 'To say that the sequence $a_n$ is bounded above is to say what?'
    answer = 'There exists an $M \in \mathbb{R}$, so that for all $n \in \mathbb{N}$, we have $a_n < M$.'
    incorrect = []
    incorrect.append(('There exists an $n \in \mathbb{N}$, so that for all $M \in \mathbb{R}$, we have $a_n < M$.', 
                      'You have exchanged the roles of $n$ and $M$.'))
    incorrect.append(('For all $M \in \mathbb{R}$, there exists an $n \in \mathbb{N}$, so that $a_n < M$.',
                      'You have exchanged the "for all" and "there exists."'))
    incorrect.append(('For all $n \in \mathbb{N}$, there exists an $M \in \mathbb{R}$, so that $a_n < M$.', 
                      'You have exchanged the "for all" and "there exists" and the roles of $n$ and $M$.'))
    incorrect.append(('There exists an $M \in \mathbb{R}$, so that for all $n \in \mathbb{N}$, we have $a_n > M$.', 
                      'You have the inequality going in the wrong direction.'))

    incorrect.append(('There exists an $n \in \mathbb{N}$, so that for all $M \in \mathbb{R}$, we have $a_n > M$.', 
                      'You have exchanged the roles of $n$ and $M$, and you have the inequality in the wrong direction.'))
    incorrect.append(('For all $M \in \mathbb{R}$, there exists an $n \in \mathbb{N}$, so that $a_n > M$.',
                      'You have exchanged the "for all" and "there exists" and you have the inequality in the wrong direction.'))
    incorrect.append(('For all $n \in \mathbb{N}$, there exists an $M \in \mathbb{R}$, so that $a_n > M$.', 
                      'You have exchanged the "for all" and "there exists" and the roles of $n$ and $M$ and you have the inequality in the wrong direction.'))

class DefinitionSequenceBoundedBelowQuestion(StaticQuestion):
    question = 'To say that the sequence $a_n$ is bounded below is to say what?'
    answer = 'There exists an $M \in \mathbb{R}$, so that for all $n \in \mathbb{N}$, we have $a_n > M$.'
    incorrect = []
    incorrect.append(('There exists an $n \in \mathbb{N}$, so that for all $M \in \mathbb{R}$, we have $a_n > M$.', 
                      'You have exchanged the roles of $n$ and $M$.'))
    incorrect.append(('For all $M \in \mathbb{R}$, there exists an $n \in \mathbb{N}$, so that $a_n > M$.',
                      'You have exchanged the "for all" and "there exists."'))
    incorrect.append(('For all $n \in \mathbb{N}$, there exists an $M \in \mathbb{R}$, so that $a_n > M$.', 
                      'You have exchanged the "for all" and "there exists" and the roles of $n$ and $M$.'))
    incorrect.append(('There exists an $M \in \mathbb{R}$, so that for all $n \in \mathbb{N}$, we have $a_n < M$.', 
                      'You have the inequality going in the wrong direction.'))

    incorrect.append(('There exists an $n \in \mathbb{N}$, so that for all $M \in \mathbb{R}$, we have $a_n < M$.', 
                      'You have exchanged the roles of $n$ and $M$, and you have the inequality in the wrong direction.'))
    incorrect.append(('For all $M \in \mathbb{R}$, there exists an $n \in \mathbb{N}$, so that $a_n < M$.',
                      'You have exchanged the "for all" and "there exists" and you have the inequality in the wrong direction.'))
    incorrect.append(('For all $n \in \mathbb{N}$, there exists an $M \in \mathbb{R}$, so that $a_n < M$.', 
                      'You have exchanged the "for all" and "there exists" and the roles of $n$ and $M$ and you have the inequality in the wrong direction.'))

class DefinitionSequenceBoundedQuestion(QuestionBag):
    questions = [DefinitionSequenceBoundedBelowQuestion, DefinitionSequenceBoundedAboveQuestion]

################################################################
class DetermineSequenceBoundedQuestion(Question):
    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','k']
        sequences = ['a','b','c']
        x = var( variables[randint(0, len(variables)-1)] )
        a_n = var( sequences[randint(0, len(sequences)-1)] )
        self.variable = x
        self.sequence = a_n
        self.term = x
        Question.__init__(self)

    def text(self):
        term = latex(self.term)
        return "Consider the sequence ${self.sequence}_{{{n}}} = {term}$.  Is the sequence bounded above?  Bounded below?".format(n=self.variable,self=self,term=term)

    def answer(self):
        value = limit( self.term, **{str(self.variable): oo} )
        if value.is_real() and value.is_infinity() and value.is_positive():
            return 'Bounded below, but not bounded above.'
        if value.is_real() and value.is_infinity() and value.is_negative():
            return 'Bounded above, but not bounded below.'
        if not value.is_real() and str(value) == 'ind':
            return 'Bounded above and bounded below.'
        if not value.is_real() and str(value) == 'und':
            return 'Bounded neither above nor below.'
    
class DetermineSequenceBoundedQuadraticQuestion(DetermineSequenceBoundedQuestion):
    def __init__(self):
        DetermineSequenceBoundedQuestion.__init__(self)
        x = self.variable
        print x
        self.term = randint(-5,5)*x*x + randint(-5,5)*x + randint(-5,5)

################################################################
class EvaluateGeometricSeriesFractionQuestion(Question):
    def perturb(self):
        denominator = randint(2,10)
        numerator = randint(1,denominator - 1)
        sign = 2*randint(0,1) - 1
        self.ratio = Rational((sign * numerator, denominator))
        self.initial = randint(0,5)

    def __init__(self):
        self.perturb()
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        Question.__init__(self)

    def text(self):
        summand = latex(self.ratio ** self.variable)
        return "Evaluate $\sum_{{{n}={self.initial}}}^\\infty {summand}$.".format(n=self.variable,self=self, summand=summand)

    def verify(self):
        return sum(self.ratio ** self.variable, self.variable, self.initial, oo) == self.answer()

    def answer(self):
        return (self.ratio ** self.initial) / (1 - self.ratio)

class EvaluateShortSumQuestion(Question):
    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.initial = randint(0,10)
        self.final = self.initial + randint(2,5)
        Question.__init__(self)

    def text(self):
        return "Evaluate $\sum_{{{self.variable}={self.initial}}}^{{{self.final}}} \\left( {summand} \\right)$.".format(self=self, summand=latex(self.summand))

    def verify(self):
        return sum(self.summand, self.variable, self.initial, self.final) == self.answer()

    def answer(self):
        return sum(self.summand, self.variable, self.initial, self.final)

class EvaluateSumOfArithmeticSequenceQuestion(EvaluateShortSumQuestion):
    def __init__(self):
        EvaluateShortSumQuestion.__init__(self)
        self.summand = randint(-7,7) + self.variable * randint(-7,7)

class EvaluateSumOfQuadraticPolynomialQuestion(EvaluateShortSumQuestion):
    def __init__(self):
        EvaluateShortSumQuestion.__init__(self)
        self.summand = randint(-7,7) + self.variable * randint(-7,7) + self.variable * self.variable * randint(-7,7)
