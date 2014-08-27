from sage.all import *
import re
import subprocess

from chameleon import PageTemplate

COURSE_NAME="sequence-002"

def random_choice( list ):
    return list[randint(0,len(list)-1)]

guid_index = randint(0,10**10)
def guid():
    global guid_index
    guid_index = guid_index + 1
    return "guid" + str(guid_index)

import json
video_identifiers = json.load(open('../identifiers/videos.json'))

################################################################
# load some gently discouraging phrases
with open('negative-feedback.txt') as f:
    negative_feedback = [s.strip() for s in f.readlines()]
def gentle_discouragement():
    global negative_feedback
    return random_choice(negative_feedback)

################################################################
# load some overwhelmingly positive phrases for encouragement
with open('positive-feedback.txt') as f:
    positive_feedback = [s.strip() for s in f.readlines()]
def encouragement():
    global positive_feedback
    return random_choice(positive_feedback)

################################################################
def filter_coursera(thing):
    if (isinstance( thing, SageObject )):
        thing = '$' + str(latex(thing)) + '$'

    thing = str(thing)

    pieces = thing.split('$$')
    pieces = flatten( zip( pieces, ['\[','\]']*len(pieces) ) )
    thing = re.sub( r'\[$', '', join( pieces, '' ) )

    pieces = thing.split('$')
    pieces = flatten( zip( pieces, ['\(','\)']*len(pieces) ) )
    thing = join( pieces, '' )
    thing = re.sub( r'\\\\\($', '', join( pieces, '' ) )

    pieces = thing.split('"')
    pieces = flatten( zip( pieces, ["""``""","""''"""]*len(pieces) ) )
    thing = join( pieces, '' )
    thing = re.sub( r'``$', '', join( pieces, '' ) )

    thing = re.sub( r'\\frac', r'\\displaystyle\\frac', thing )
    thing = re.sub( r'\\sum', r'\\displaystyle\\sum', thing )
    thing = re.sub( r'\\int', r'\\displaystyle\\int', thing )

    # potentially should encode other HTML entities at this point
    thing = re.sub( r'---', r'&mdash;', thing )
    thing = re.sub( r'--', r'&ndash;', thing )

    thing = re.sub( r'``', r'&ldquo;', thing )
    thing = re.sub( """''""", r'&rdquo;', thing )

    # these are the most important entities to encode
    thing = re.sub( r'<', r'&lt;', thing )
    thing = re.sub( r'>', r'&gt;', thing )

    # but paragraphs should NOT be encoded
    thing = re.sub( r'&lt;p&gt;', r'<p>', thing )
    thing = re.sub( r'&lt;/p&gt;', r'</p>', thing )

    return thing

################################################################
def filter_latex(thing):
    if (isinstance( thing, SageObject )):
        thing = '$' + str(latex(thing)) + '$'

    thing = str(thing)

    pieces = thing.split('$$')
    pieces = flatten( zip( pieces, ['\[','\]']*len(pieces) ) )
    thing = re.sub( r'\[$', '', join( pieces, '' ) )

    pieces = thing.split('$')
    pieces = flatten( zip( pieces, ['\(','\)']*len(pieces) ) )
    thing = join( pieces, '' )
    thing = re.sub( r'\\\\\($', '', join( pieces, '' ) )

    pieces = thing.split('"')
    pieces = flatten( zip( pieces, ["""``""","""''"""]*len(pieces) ) )
    thing = join( pieces, '' )
    thing = re.sub( r'``$', '', join( pieces, '' ) )

    thing = re.sub( r'\\frac', r'\\displaystyle\\frac', thing )
    thing = re.sub( r'\\sum', r'\\displaystyle\\sum', thing )
    thing = re.sub( r'\\int', r'\\displaystyle\\int', thing )

    return thing

################################################################
class BaseQuestion(object):
    """Base class for all questions"""

    def good_enough(self):
        return True

    def __init__(self):
        self.data = []

    @classmethod
    def variation_count(cls):
        return 1

    preamble = ''
    @classmethod
    def coursera_xml(cls):
        xml = """<preamble><![CDATA[{preamble}]]></preamble>""".format(preamble=cls.preamble)
        questions = []
        while len(questions) < 10:
            potential_question = cls()
            if potential_question.good_enough():
                questions.append( potential_question)

        for question in questions:
            xml = xml + question.question_xml()
        return xml

    @classmethod
    def ximera(cls):
        xml = ""
        questions = []
        while len(questions) < 1:
            potential_question = cls()
            if potential_question.good_enough():
                questions.append( potential_question)

        for question in questions:
            xml = xml + question.question_ximera()
        return xml

    def text(self):
        filename = self.module.replace( '__init__.pyc', 'text.html' ).replace( '__init__.py', 'text.html' )
        f = open(filename)
        template = PageTemplate(f.read().replace('#{','${').replace("condition=","tal:condition="))
        dictionary = dict(self.__dict__, **globals())
        dictionary['answer'] = self.answer()
        return template.render(**dictionary)

    def text_tex(self):
        result = self.text()
        return join([x.replace('<p>','').replace('</p>','') for x in re.sub("\n+","\n",result).split( "</p>\n<p>" )],"\n\n")

    def response(self):
        return encouragement()

    def potential_distractor(self):
        question = self.__class__()
        while not question.good_enough():
            question = self.__class__()
        return question.answer()

    def distractors(self, count):
        results = []
        while( len(results) < count ):
            distractor = self.potential_distractor()
            if not (distractor in results):
                if not self.is_correct( distractor ):
                    results.append( distractor )
        return results

    def is_correct(self,response):
        return response == self.answer()

    title = 'nothing at all'
    def __repr__(self):
        return "A question about " + self.__class__.title

    def explanation(self):
        return join(self.hints(), ' ')
        
    hint_filename = 'hints.html'

    def hints(self):
        filename = self.module.replace( '__init__.pyc', self.__class__.hint_filename ).replace( '__init__.py', self.__class__.hint_filename )
        f = open(filename)
        template = PageTemplate(f.read().replace('#{','${').replace("condition=","tal:condition="))
        dictionary = dict(self.__dict__, **globals())
        dictionary['answer'] = self.answer()
        return [x.replace('<p>','').replace('</p>','') for x in re.sub("\n+","\n",template.render(**dictionary)).split( "</p>\n<p>" )]

    video = ""
    def question_xml(self):
        question_id = guid()

        forum_button = """<button class="btn btn-inverse btn-disabled" disabled><i class="icon-comment"></i>&nbsp;Discuss</a>"""
        if hasattr(self.__class__,'forum') and self.__class__.forum > 0:
            forum_button = """<a class="btn btn-inverse" target="_blank" href="https://class.coursera.org/{course}/forum/list?forum_id={forum}"><i class="icon-comment"></i>&nbsp;Discuss</a>""".format(course=COURSE_NAME, forum=self.__class__.forum)

        video_button = """<button class="btn btn-inverse btn-disabled" disabled><i class="icon-film"></i>&nbsp;Watch video</a>"""
        if hasattr(self.__class__,'video') and self.__class__.video != "":
            video_button = """<a class="btn btn-inverse" target="_blank" href="https://class.coursera.org/{course}/lecture/{lecture}"><i class="icon-film"></i>&nbsp;Watch video</a>""".format(course=COURSE_NAME, lecture=video_identifiers[self.__class__.video])

        textbook_button = ""
        if hasattr(self.__class__,'textbook') and self.__class__.textbook != "":
            textbook_button = '<div class="btn-group">' + subprocess.check_output("ruby textbook-link.rb " + self.__class__.textbook, shell=True) + '</div>'

        hint_button = """<button class="btn btn-warning" onclick="$(this).parents('.course-quiz-question-text').children('div.hints').children('div.hint').first().removeClass('hint').hide().css('visibility','visible').css('position','').css('width','').css('height','').css('overflow','').slideDown('slow'); var steps = $(this).parents('.course-quiz-question-text').children('div.hints').children('div.hint').length; if (steps != 1) $(this).children('.hint-count').text( ' (' + steps + ' steps remain)' ); if (steps == 1) $(this).children('.hint-count').text( ' (1 step remains)' ); if (steps == 0) $(this).prop( 'disabled', true ); return false;"><i class=\"icon-question-sign\"></i>&nbsp;Get hint<span class="hint-count"></span></button>""".format(button="""""")

        ## FOR THE FINAL
        hint_button = ''

        hint_text = """<div class="hints">"""
        for hint in self.hints():
            # The bizarre style is needed because display: none will confuse mathjax's metric computations
            hint_text = hint_text + """<div class="hint" style="visibility:hidden; position:absolute; width:0; height:0; overflow:hidden;">{hint}</div>""".format( hint = filter_coursera(hint) )
        hint_text = hint_text + """</div>"""

        ## FOR THE FINAL
        hint_text = ''

        new_title = self.__class__.title
        javascript = re.sub( 'NEW_TITLE', new_title,
                             re.sub( 'THE_ID', 'question-' + question_id, """<div id="THE_ID"></div>
        <script>
        window.addEventListener('load', function() {
          var title = $('#THE_ID').parents('.course-quiz-question-body').children('.course-quiz-question-number');
          title.html( title.text() + ' ' + '<small style="color: #555555;">NEW_TITLE</small>' );
        });
        </script>""" ))

        buttons = """<div class="btn-toolbar question-buttonbar" style="float: right;">
        <div class="btn-group">{hint}</div>
        <div class="btn-group">{forum}</div>
        <div class="btn-group">{video}</div>
        {textbook}
        </div>""".format( hint=hint_button, forum=forum_button, video=video_button, textbook=textbook_button )

        header = """<question id="{id}" type="GS_Choice_Answer_Question">
          <metadata>
            <parameters>
              <rescale_score>9</rescale_score>
              <choice_type>radio</choice_type>
            </parameters>
          </metadata>
          <data>
            <text><![CDATA[{text}]]></text>
            <explanation><![CDATA[{explanation}]]></explanation>
            """.format(id=question_id, text="<hr/>" + buttons + filter_coursera(self.text()) + hint_text + r'<div style="clear: both;"></div><hr/>' + javascript, explanation=filter_coursera(self.explanation()))

        footer = """</data></question>"""
        
        correct_group = """<option_group select="all">
                <option id="{id}correct" selected_score="1" unselected_score="0">
                  <text><![CDATA[{answer}]]></text>
                  <explanation><![CDATA[{response}]]></explanation>
                </option>
              </option_group>""".format(id=question_id, answer=filter_coursera(self.answer()), response=filter_coursera(self.response()))

        some_distractors = self.distractors(6)
        incorrect_group = """<option_group select="{count}">""".format(count=min(len(some_distractors),4))
        index = 0
        for distractor in some_distractors:
            text = distractor
            response = gentle_discouragement()
            if isinstance(distractor, tuple):
                text = distractor[0]
                response = distractor[1]

            incorrect_group = incorrect_group + """<option id="{id}-{index}" selected_score="0" unselected_score="0">
                  <text><![CDATA[{text}]]></text>
                  <explanation><![CDATA[{response}]]></explanation>
                </option>""".format(id=question_id, index=index, text=filter_coursera(text), response=filter_coursera(response))
            index = index + 1
        incorrect_group = incorrect_group + """</option_group>"""

        xml = header + """<option_groups randomize="true">""" + correct_group + incorrect_group + """</option_groups>""" + footer

        return xml

    def question_ximera(self):
        video_button = ""
        if hasattr(self.__class__,'video') and self.__class__.video != "":
            video_button = "% Relevant video: " + self.__class__.video

        new_title = self.__class__.title

        indent = "                "
        hint_text = """"""
        for hint in self.hints():
            # The bizarre style is needed because display: none will confuse mathjax's metric computations
            hint_text = hint_text + """{indent}\\begin{{hint}}\n{indent}  {hint}\n{indent}\\end{{hint}}\n""".format( hint = filter_latex(hint), indent=indent )
        hint_text = hint_text + """\n"""

        some_distractors = self.distractors(6)
        incorrects = ""
        for distractor in some_distractors[0:4]:
            text = distractor
            response = gentle_discouragement()
            if isinstance(distractor, tuple):
                text = distractor[0]
                response = distractor[1]

            incorrects = incorrects + """{indent}\\choice{{{text}}}\n""".format(text=filter_latex(text), indent=indent)

        tex = video_button + """
            \\begin{{question}}
              {text}
              \\begin{{solution}}
{hint}
              \\begin{{multiple-choice}}
                \\choice[correct]{{{correct}}}
{incorrects}
              \\end{{multiple-choice}}

              \\end{{solution}}
            \\end{{question}}
            """.format(text=filter_latex(self.text_tex()), hint=hint_text, explanation=filter_latex(self.explanation()), correct=filter_latex(self.answer()), incorrects=incorrects)

        return tex



        xml = header + """<option_groups randomize="true">""" + correct_group + incorrect_group + """</option_groups>""" + footer

        return xml

################################################################
class StaticQuestion(BaseQuestion):
    """Base class for a question without any randomization."""

    title = 'something static'
    def __init__(self):
        BaseQuestion.__init__(self)
    def text(self):
        return self.__class__.question
    def answer(self):
        return self.__class__.correct
    def distractors(self,count):
        return self.__class__.incorrect

################################################################
class QuestionBag(BaseQuestion):
    """A random question from a list of question classes"""

    title = 'something from a bag'
    @classmethod
    def variation_count(cls):
        return sum([b.variation_count() for b in cls.questions])

    def __init__(self):
        questions = self.__class__.questions
        self.__class__ = questions[randint(0,len(questions)-1)]
        self.__class__.__init__(self)

################################################################
# OBJECTIVE Define what it means for a sequence to be bounded

class RandomizedQuestion(BaseQuestion):

    @classmethod
    def variation_count(cls):
        return oo




class EvaluateShortSumQuestion(RandomizedQuestion):
    def __init__(self):
        variables = ['n','n','n','n','n','n','n','m','m','m','k','i','j']
        self.variable = var( variables[randint(0, len(variables)-1)] )
        self.initial = randint(0,10)
        self.final = self.initial + randint(2,5)
        BaseQuestion.__init__(self)

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
