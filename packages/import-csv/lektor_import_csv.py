# coding: utf-8

### Modules
import os
import codecs
from lektor.context import get_ctx
from lektor.pluginsystem import Plugin

### Functions & Procedures
def importCsv(fileName):
    ctx = get_ctx()
    filePath = os.getcwd() + '/content' + ctx.source.path + '/' + fileName  # 🤷‍♂️

    htmlTable = []
    with codecs.open(filePath, 'r', 'utf-8') as csvFile:
        for eachRow in csvFile.read().split('\n'):
            htmlRow = []
            for eachCell in eachRow.split('\t'):
                htmlRow.append(u"<td>{}</td>".format(eachCell))
            htmlTable.append(u"<tr>{}</tr>".format(''.join(htmlRow)))

    tableTemplate = u"<table><tbody>{}</tbody></table>"
    return HTML(tableTemplate.format('\n'.join(htmlTable)))


class HTML(object):
    def __init__(self, html):
        self.html = html

    def __html__(self):
        return self.html

class ImportCsvPlugin(Plugin):
    name = u'read csv'
    description = u'reads csv and returns html tables'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['importCsv'] = importCsv
