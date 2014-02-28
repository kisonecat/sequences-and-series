from questions import *

class Question(StaticQuestion):
    forum = 10082
    module = __file__
    title = 'define the value of a series'
    video = 'series-definition'
    textbook = 'definition:value-of-series'
    question = r'To say that \(\displaystyle\sum_{k=4}^\infty a_k = L\) means what?  In order words, what does it mean to say that the &ldquo;value&rdquo; of a series is \(L\)?'
    correct = r'The sequence of partial sums \(s_n = \displaystyle\sum_{k=4}^n a_k \) converges to \(L\).'
    incorrect = []

    incorrect.append((r'The sequence of partial sums \(s_n = \displaystyle\sum_{k=n}^\infty a_k \) converges to \(L\).',
                      r'This is not the correct definition of the sequence of partial sums; it should not, itself, include an infinite series.'))

    incorrect.append((r'The sequence of partial sums \(s_n = \displaystyle\sum_{k=4}^n a_n \) converges to \(L\).',
                      r'This is not the correct definition of the sequence of partial sums; the sum should involve \(a_k\) rather than \(a_n\).'))

    incorrect.append((r'The sequence of partial sums \(s_n = \displaystyle\sum_{k=1}^n a_k \) converges to \(L\).',
                      r'The given series begins with \(k=4\), but you are beginning your sequence of partial sums with the \(k=1\) term.'))

    incorrect.append((r'The sequence of partial sums \(s_n = \displaystyle\sum_{k=1}^n a_k \) is bounded by \(L\).',
                      r'The given series begins with \(k=4\), but you are beginning your sequence of partial sums with the \(k=1\) term.'))

    incorrect.append((r'The sequence of partial sums \(s_n = \displaystyle\sum_{k=4}^n a_k \) is bounded by \(L\).',
                      r'It is not enough that the sequence of partial sums is bounded by \(L\); to say that \(\displaystyle\sum_{k=4}^\infty a_k = L\) is to say something about convergence.'))

    incorrect.append((r'In the sequence of partial sums \(s_n = \displaystyle\sum_{k=1}^n a_k \), it is the case that \(s_4 = L\).',
                      r'The given series begins with \(k=4\), but you are beginning your sequence of partial sums with the \(k=1\) term.'))

    incorrect.append((r'In the sequence of partial sums \(s_n = \displaystyle\sum_{k=4}^n a_k \), it is the case that \(s_4 = L\).',
                      r'In this case, the term \(s_4\) is equal to \(a_4\), but the series should involve adding up many terms.'))

    incorrect.append((r'The sequence of partial sums \(s_n = \displaystyle\sum_{k=1}^4 a_k \) converges to \(L\).',
                      r'The given series begins with \(k=4\), but you are ending your sequence of partial sums with the \(k=4\) term.'))
