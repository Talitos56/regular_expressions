# VALIDANDO SENHAS FORTES
import re
from pprint import pprint

senha_forte_regexp = re.compile(
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{12,}'
    r'$',
    flags=re.M
)

string = '''
VÁLIDAS
1uJe9/X6i}:P
c&:4k9UaO:0X
cy2!KA$k$97V
QE97^aKhv^@9
Od0m{Rf7 6{L

SEM MINÚSCULAS
@A}$*7A49KY2
FR$78>;7}D4J
+.6Y`ZQ&W609
B~0,P/519DD^
_U4.1%5AT3>B

SEM MINÚSCULAS E NÚMEROS
`[@L)N?QP]NR
X%PPE;J@]?<C
U>\<GW^U|B^E
,MQ<_~I)T$NK
<WI~)^K"XC@O

SEM NÚMEROS CARACTERES E MINÚSCULAS
GFFDDCIEWSWQ
GPMCDSPRWYWP
NAUKJBTXJMIS
ZNOLHOKHTUGI
QZTXCXOBHUSQ

QUANTIDADE INVÁLIDA (6)
Euf3#1
W!p48n
yVr>71
6|Or1i
Au88r^
'''

pprint(senha_forte_regexp.findall(string))
