from questions import *

class Question(StaticQuestion):
    module = __file__
    title = 'define limit of a sequence'
    video = 'sequence-limit'
    forum = 10053
    question = r'To say that the sequence \(a_n\) converges to \(L\) means what?  In other words, what is the definition of the statement \(\displaystyle\lim_{n \to \infty} a_n = L\)?'
    correct = r'For every positive real number \(\epsilon > 0\) there exists an \(N \in \mathbb{N}\) so that whenever \(n \geq N\), we have \( |a_n - L| < \epsilon \).'
    incorrect = []

    incorrect.append((r'For every real number \(\epsilon > 0\) there exists an \(N \in \mathbb{N}\) so that \( |a_N - L| < \epsilon \).',
                      'It is not enough that some term \(a_N\) is close to \(L\); all terms, after some index \(N\), must be close \(L\).'))

    incorrect.append((r'For every real number \(\epsilon \in \mathbb{R}\) there exists an \(N \in \mathbb{N}\) so that whenever \(n \geq N\), we have \( |a_n - L| < \epsilon \).',
                      'The number \(\epsilon\) must be assumed to be positive; it is controlling the distance between \(a_n\) and \(L\), and distances cannot be negative.'))
    incorrect.append((r'For every whole number \(N > 0\) there exists a positive real number \(\epsilon > 0\) so that whenever \(n \geq N\), we have \( |a_n - L| < \epsilon \).',
                      'You have exchanged the roles of \(N\) and \(\epsilon\).'))
    incorrect.append((r'For every whole number \(N > 0\) there exists a real number \(\epsilon \in \mathbb{R}\) so that whenever \(n \geq N\), we have \( |a_n - L| < \epsilon \).',
                      'You have exchanged the roles of \(N\) and \(\epsilon\).  Additionally, \(\epsilon\) must be assumed to be positive.'))

    incorrect.append((r'There exists a positive real number \(\epsilon > 0\) so that for all \(N \in \mathbb{N}\), there exists \(n \geq N\) so that \( |a_n - L| < \epsilon \).',
                      'You have exchanged "for every" and "there exists".'))

    incorrect.append((r'There exists a positive real number \(\epsilon > 0\) so that for all \(N \in \mathbb{N}\), we have \( |a_N - L| < \epsilon \).',
                      'You have exchanged "for every" and "there exists".  Additionally, initial terms need not be close to \(L\); terms only need to be close to \(L\) after some index \(N\).'))

    incorrect.append((r'There exists a real number \(\epsilon \in \mathbb{R}\) so that for all \(N \in \mathbb{N}\), there exists \(n \geq N\) so that \( |a_n - L| < \epsilon \).',
                      'You have exchanged "for every" and "there exists".  Additionally, \(\epsilon\) must be assumed to be positive.'))

    incorrect.append((r'For every positive real number \(\epsilon > 0\) there exists an \(N \in \mathbb{N}\) so that whenever \(n \geq N\), we have \( |a_N - L| < \epsilon \).',
                      'Not just \(a_N\) but every term \(a_n\) with \(n \geq N\) must satisfy the condition \( |a_N - L| < \epsilon \).'))

