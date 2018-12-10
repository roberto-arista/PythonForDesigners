# coding: utf-8

### Modules
from lektor.pluginsystem import Plugin

### Constants
IMAGE_TAGS = ['<abstract_image>', '<small_image>', '<large_image>',
              '<code_image>', '<code_diagram>', '<exercise_image>']

STANDARD_TAG_MAP = {

    '<section_title>': '<h2>',
    '</section_title>': '</h2>',

    '<abstract_text>': "<p class='abstract_text'>",
    '</abstract_text>': "</p>",

    '<inline_code>': "<code>",
    '</inline_code>': "</code>",

    '<pre_code>': '<pre><code>',
    '</pre_code>': '</code></pre>',

    "<exercise_wrapper>": "<div class='exercise_wrapper'>",
    "</exercise_wrapper>": "</div>",

    "<workbook>": "<h2 class='workbook'>Workbook</h2>",

    "<code_image_wrapper>": "<div class='code_image_wrapper'>",
    "</code_image_wrapper>": "</div>",

    "<exercise_content>": "<div class='exercise_content'>",
    "</exercise_content>": "</div>",

    "<solution_code>": "<pre class='solution'><code>",
    "</solution_code>": "</code></pre>",

}


# plugin!
def convertCustomTags(value):
    for source, replacement in STANDARD_TAG_MAP.items():
        value = value.replace(source, replacement)

    for eachImgTag in IMAGE_TAGS:
        value = value.replace(eachImgTag[:-1],
                              "<img class='%s'" % eachImgTag[1:-1])

    return HTML(value)


class HTML(object):
    def __init__(self, html):
        self.html = html

    def __html__(self):
        return self.html


class PfdCustomMarkupFilterPlugin(Plugin):
    name = u'PFD Custom Markup Filter'
    description = u'This filter will convert the custom pfd markup into html'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['convertCustomTags'] = convertCustomTags
