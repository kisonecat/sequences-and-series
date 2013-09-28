from sage.all import *
from questions import *
import time

################################################################
class Quiz:
    """Base class for all quizzes"""

    question_classes = []
    title = 'Quiz'
    preamble = ''

    def __init__(self):
        self.questions = [question_class() for question_class in self.__class__.question_classes]

    @classmethod
    def forum_list(cls):
        problem_number = 1
        for question_class in cls.question_classes:
            print("Q{problem_number}: {title}".format(problem_number = problem_number, title=question_class.title))
            problem_number = problem_number + 1

    @classmethod
    def coursera_xml(cls):
        header = """<quiz>
  <metadata>
    <title><![CDATA[{title}]]></title>
    <open_time>2012-12-31 1900</open_time>
    <soft_close_time>2013-07-24 1611</soft_close_time>
    <hard_close_time>2013-08-07 1611</hard_close_time>
    <duration>0</duration>
    <retry_delay>0</retry_delay>
    <maximum_submissions>999</maximum_submissions>
    <modified_time>{modified_time}</modified_time>
    <is_ace_exam_flag>none</is_ace_exam_flag>
    <authentication_required>1</authentication_required>
    <parameters>
      <show_explanations>
        <question>before_soft_close_time</question>
        <option>before_soft_close_time</option>
        <score>before_soft_close_time</score>
      </show_explanations>
    </parameters>
    <maximum_score>{maximum_score}</maximum_score>
  </metadata>
  <preamble><![CDATA[{preamble}]]></preamble>
  <data><question_groups>
        """.format(title=cls.title, maximum_score=len(cls.question_classes), modified_time=int(1000*time.time()), preamble=cls.preamble)

        footer = """    </question_groups>
  </data>
</quiz>"""
        return header + join(['<question_group select="1">' + question_class.coursera_xml() + '</question_group>' for question_class in cls.question_classes],"\n") + footer

################################################################
import evaluateGeometricSeriesFraction
import computeSequenceRecursively
import identifyGeometricProgression
import identifyArithmeticProgression
import identifyMonotonicSequence
import defineSequenceBounded
import defineLimitOfSequence
import findSufficientlyLargeForEpsilon
import findSequenceLimit
import determineSequenceBounded
import applyMonotoneConvergence

class SecondQuiz(Quiz):
    title = 'Homework 2'
    preamble = ''
    question_classes = [ evaluateGeometricSeriesFraction.Question
                       ]

class FirstQuiz(Quiz):
    title = 'Homework 1'
    preamble = 'This homework, like all the homeworks in this course, is an example of &ldquo;formative assessment.&rdquo;  As such, this homework is not so much about you showing me how much you have learned; the final exam will handle that.  Rather, this homework is part of the process of learning.  Use the hints when you get stuck.  Discuss freely on the forums.  Take the quiz again and again.  Feel free to use the provided resources in whatever way helps you to understand the material.  I want you to succeed, and, with practice, I know you will.  ~jim'

    question_classes = [ 
        computeSequenceRecursively.Question,
        defineLimitOfSequence.Question,
        findSequenceLimit.Question,
        findSufficientlyLargeForEpsilon.Question,
        defineSequenceBounded.Question,
        determineSequenceBounded.Question,
        identifyArithmeticProgression.Question,
        identifyGeometricProgression.Question,
        identifyMonotonicSequence.Question,
        applyMonotoneConvergence.Question,
#                         something about monotone convergence theorem?
#                       ,
                       ]

f = open('quiz1.xml','w')
f.write(FirstQuiz.coursera_xml())
f.close()
FirstQuiz.forum_list()

