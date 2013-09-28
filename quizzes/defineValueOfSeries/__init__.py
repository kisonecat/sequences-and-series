from questions import *

class Question(StaticQuestion):
    module = __file__
    title = 'define the value of a series'
    video = 'series-definition'
    question = r'To say that \(\displaystyle\sum_{k=4}^\infty a_k = L\) means what?  In order words, what does it mean to say that the &ldquo;value&rdquo; of a series is \(L\)?'
    correct = r'The sequence of partial sums \(s_n = \displaystyle\sum_{k=4}^n a_k \) converges to \(L\).'
    incorrect = []

    incorrect.append((r'The sequence of partial sums \(s_n = \displaystyle\sum_{k=n}^\infty a_k \) converges to \(L\).',
                      r'This is not the correct definition of the sequence of partial sums; it should not, itself, include an infintie series.'))

    incorrect.append((r'The sequence of partial sums \(s_n = \displaystyle\sum_{k=1}^n a_k \) converges to \(L\).',
                      r'The given series begins with \(k=4\), but you are beginning your sequence of partial sums with \(k=1\)'))




