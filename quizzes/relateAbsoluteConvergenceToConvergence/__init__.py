from questions import *

class Question(StaticQuestion):
    module = __file__
    title = 'relate absolute convergence to convergence'
    video = 'absolute-convergence'
    textbook = 'thm:absolute-convergence-implies-convergence'
    forum = 10143
    question = r'Suppose \((a_n)\) is a sequence involving both positive and negative numbers, and suppose that the series \(\sum_{n=1}^\infty |a_n|\) converges.  What can be known for certain about the series \(\sum_{n=1}^\infty a_n\)?'
    correct = r'The series \(\sum_{n=1}^\infty a_n\) converges.'
    incorrect = []

    incorrect.append((r'The series \(\sum_{n=1}^\infty a_n\) diverges.',
                      'Actually, the series necesarily converges.  An absolutely convergent series is also just a convergent series.'))

    incorrect.append((r'The series \(\sum_{n=1}^\infty a_n\) converges conditionally.',
                      'The series converges, and not just conditionally: conditional convergence would mean that the series \(\sum_{n=1}^\infty |a_n|\) diverged.'))

    incorrect.append((r'The series \(\sum_{n=1}^\infty a_n\) may converge or diverge.',
                      'Actually, the series necesarily converges.  An absolutely convergent series is also just a convergent series.'))

    incorrect.append((r'The series \(\sum_{n=1}^\infty a_n\) converges to a positive value.',
                      'This is not necessarily true.  For instance, it might have happened that \(a_1 = -3\) and \(a_2 = 2\) but all other values in the sequence \((a_n)\) are zero.'))

    incorrect.append((r'The series \(\sum_{n=1}^\infty a_n\) converges to a negative value.',
                      'This is not necessarily true.  For instance, it might have happened that \(a_1 = 3\) and \(a_2 = -2\) but all other values in the sequence \((a_n)\) are zero.'))
