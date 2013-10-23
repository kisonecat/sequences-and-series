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
# Quiz 1
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

################################################################
# Quiz 2
import defineValueOfSeries
import evaluateGeometricSeriesFraction
import evaluateTelescopingSeries
import analyzeGeometricSeries
import applyNthTermTest
import applyComparisonTest
import analyzeHarmonicSeries

################################################################
# Quiz 3
import applyRatioTest
import applyRatioTestWithFactorials
import applyRatioTestWithFactorialsAndPowers
import comparePSeries
import identifyPSeries
import applyRootTest
import boundSeriesByIntegrating

################################################################
# Quiz 4
import relateAbsoluteConvergenceToConvergence
import applyLimitComparisonTest
import applyAlternatingSeriesTest
import identifyAlternatingPSeries
import approximateAlternatingSeries
import approximateLogarithm
import considerNonmonotoneAlternatingSeries

################################################################
# Quiz 5

import findIntervalOfConvergence
import findRadiusOfConvergence
import identifyPowerSeries
import transformGeometricSeries
import multiplyPowerSeries

class FifthQuiz(Quiz):
    title = 'Homework 5'
    preamble = 'This homework, like all the homeworks in this course, is an example of &ldquo;formative assessment.&rdquo;  That does not mean it is not worth points, but the points are there to encourage you to complete it, not to judge you.  Please, use the hints when you get stuck.  Discuss freely on the forums.  If you get the right answer but do not understand why, please ask.  Take the quiz again and again&mdash;the questions will change each time.  Feel free to use the provided resources in whatever way helps you to understand the material.  I know that you can do it.  ~jim'
    question_classes = [ 
#        identifyPowerSeries.Question,
#        findIntervalOfConvergence.Question,
#        findRadiusOfConvergence.Question,
#        transformGeometricSeries.Question,
#        multiplyPowerSeries.Question,
    ]


class FourthQuiz(Quiz):
    title = 'Homework 4'
    preamble = 'This homework, like all the homeworks in this course, is an example of &ldquo;formative assessment.&rdquo;  As such, this homework is not so much about you showing me how much you have learned; the final exam (in just a few weeks now!) will handle that.  Rather, this homework is part of the process of learning.  Use the hints when you get stuck.  Discuss freely on the forums.  Take the quiz again and again.  Feel free to use the provided resources in whatever way helps you to understand the material.  You are making progress on the homework, and with just a few more weeks of work, I know you will do a great job on the final exam.  ~jim'
    question_classes = [ 
        relateAbsoluteConvergenceToConvergence.Question,
        applyLimitComparisonTest.Question,
        identifyAlternatingPSeries.Question,
        applyAlternatingSeriesTest.Question,
        approximateAlternatingSeries.Question,
        approximateLogarithm.Question,
        considerNonmonotoneAlternatingSeries.Question
    ]

class ThirdQuiz(Quiz):
    title = 'Homework 3'
    preamble = 'This homework, like all the homeworks in this course, is an example of &ldquo;formative assessment.&rdquo;  As such, this homework is not so much about you showing me how much you have learned; the final exam (in just a few weeks now!) will handle that.  Rather, this homework is part of the process of learning.  Use the hints when you get stuck.  Discuss freely on the forums.  Take the quiz again and again.  Feel free to use the provided resources in whatever way helps you to understand the material.  You are making progress on the homework, and with just a few more weeks of work, I know you will do a great job on the final exam.  ~jim'
    question_classes = [ 
        applyRatioTest.Question,
        applyRatioTestWithFactorials.Question,
        applyRatioTestWithFactorialsAndPowers.Question,
        identifyPSeries.Question,
        comparePSeries.Question,
        applyRootTest.Question,
        boundSeriesByIntegrating.Question,
    ]

class SecondQuiz(Quiz):
    title = 'Homework 2'
    preamble = 'This homework, like all the homeworks in this course, is an example of &ldquo;formative assessment.&rdquo;  As such, this homework is not so much about you showing me how much you have learned; the final exam will handle that.  Rather, this homework is part of the process of learning.  Use the hints when you get stuck.  Discuss freely on the forums.  Take the quiz again and again.  Feel free to use the provided resources in whatever way helps you to understand the material.  I want you to succeed, and, with practice, I know you will.  ~jim'
    question_classes = [ 
        defineValueOfSeries.Question,
        evaluateGeometricSeriesFraction.Question,
        analyzeGeometricSeries.Question,
        evaluateTelescopingSeries.Question,
        applyNthTermTest.Question,
        analyzeHarmonicSeries.Question,
        applyComparisonTest.Question,
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
    ]

f = open('quiz5.xml','w')
f.write(FifthQuiz.coursera_xml())
f.close()
FifthQuiz.forum_list()
