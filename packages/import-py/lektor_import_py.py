# coding: utf-8
from lektor.pluginsystem import Plugin
from lektor.context import get_ctx
import os
import codecs

### Functions
def importPy(fileName):
    ctx = get_ctx()
    filePath = os.getcwd() + ctx.source.path + '/' + fileName  # 🤷‍♂️
    with codecs.open(filePath, 'r', 'utf-8') as pyFile:
        pyStr = pyFile.read()
    return HTML(u'<code class="language-python">{}</code>'.format(pyStr))

class HTML(object):
    def __init__(self, html):
        self.html = html

    def __html__(self):
        return self.html

class ImportPyPlugin(Plugin):
    name = u'import py'
    description = u'reads py file and returns <code>python code</code>'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['importPy'] = importPy
