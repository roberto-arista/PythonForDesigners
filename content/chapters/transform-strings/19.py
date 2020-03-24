# US standard
value = 2345.67
f'{value:n}'
# 2,345.67

# Italian standard
import locale
locale.setlocale(locale.LC_ALL, 'it_IT')
f'{value:n}'
# 2345,67