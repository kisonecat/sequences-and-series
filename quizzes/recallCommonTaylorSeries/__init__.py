from questions import *

class CosineQuestion(StaticQuestion):
    module = __file__
    video = 'series-for-sine'
    forum = 10183
    hint_filename = 'cosine-hints.html'
    title = 'recall the Taylor series for cosine'
    question = 'Consider the function \(f(x) = \cos x\).  Which of the following is the Taylor series for \(f\) around zero?'
    correct = r'\(\sum_{n=0}^\infty \frac{(-1)^n}{(2n)!} x^{2n}\)'
    incorrect = []
    incorrect.append((r'\(\sum_{n=0}^\infty \frac{(-1)^{n+1}}{(2n)!} x^{2n}\)',
                      'You have included an extraneous factor of \(-1\).'))
    incorrect.append((r'\(\sum_{n=0}^\infty \frac{(-1)^{n+1}}{(2n+1)!} x^{2n}\)',
                      'You have included an extraneous factor of \(-1\), and the denominator should have \((2n)!\).'))
    incorrect.append((r'\(\sum_{n=0}^\infty \frac{(-1)^{n}}{(2n+1)!} x^{2n}\)',
                      'The denominator should have \((2n)!\).'))
    incorrect.append((r'\(\sum_{n=0}^\infty \frac{(-1)^{n+1}}{(2n)!} x^{2n+1}\)',
                      'You have included an extraneous factor of \(-1\), and you should have \(x^{2n}\) instead of \(x^{2n+1}\).'))
    incorrect.append((r'\(\sum_{n=0}^\infty \frac{(-1)^{n+1}}{(2n+1)!} x^{2n+1}\)',
                      'You have included an extraneous factor of \(-1\), and the denominator should have \((2n)!\), and you should have \(x^{2n}\) instead of \(x^{2n+1}\).'))
    incorrect.append((r'\(\sum_{n=0}^\infty \frac{(-1)^{n}}{(2n+1)!} x^{2n+1}\)',
                      'The denominator should have \((2n)!\), and you should have \(x^{2n}\) instead of \(x^{n}\).'))
    incorrect.append((r'\(\sum_{n=0}^\infty \frac{(-1)^{n+1}}{(2n)!} x^{n}\)',
                      'You have included an extraneous factor of \(-1\), and you should have \(x^{2n}\) instead of \(x^{n}\).'))
    incorrect.append((r'\(\sum_{n=0}^\infty \frac{(-1)^{n+1}}{(2n+1)!} x^{n}\)',
                      'You have included an extraneous factor of \(-1\), and the denominator should have \((2n)!\), and you should have \(x^{2n}\) instead of \(x^{2n+1}\).'))
    incorrect.append((r'\(\sum_{n=0}^\infty \frac{(-1)^{n}}{(2n+1)!} x^{n}\)',
                      'The denominator should have \((2n)!\), and you should have \(x^{2n}\) instead of \(x^{n}\).'))

class Question(QuestionBag):
    title = 'recall the Taylor series for common functions'
    questions = [CosineQuestion]
