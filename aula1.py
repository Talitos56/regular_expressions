import re

# findall
# search
# sub
# compile

string = 'Este é um teste de expressões teste regulares.'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'abcd', string, count=0))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))

# Cuidado com as letras maiúsculas e minúsculas
