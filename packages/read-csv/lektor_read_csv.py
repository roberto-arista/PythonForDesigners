# coding: utf-8

### Modules
import codecs
import csv
from lektor.pluginsystem import Plugin

### Functions
def readCsv(aPath):
    htmlTable = []
    with codecs.open(aPath, 'r', 'utf-8') as csvFile:
        for eachRow in csv.reader(csvFile,
                                  delimiter='\t',
                                  quotechar='|'):

            htmlRow = []
            for eachCell in eachRow:
                htmlRow.append("<td>{}</td>".format(eachCell))

            htmlTable.append("<tr>{}</tr>".format(''.join(htmlRow)))

    tableTemplate = "<table><tbody>{}</tbody></table>"
    return HTML(tableTemplate.format('\n'.join(htmlTable)))


class HTML(object):
    def __init__(self, html):
        self.html = html

    def __html__(self):
        return self.html


class ReadCsvPlugin(Plugin):
    name = u'read csv'
    description = u'reads csv and returns html tables'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['readCsv'] = readCsv
