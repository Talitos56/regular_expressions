# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# | significa OU
# ponto significa qualquer caracter - com EXCEÇÃO de uma quebra de linha
print(re.findall(r'João|Maria|ad..tos', texto))
# [] conjunto de caracteres
print(re.findall(r'[Jj]oão|[Mm]aria', texto))
# usando um range
print(re.findall(r'[a-z]aria', texto))  # somente letras minúsculas
print(re.findall(r'[A-Z]aria', texto))  # somente letras maiúsculas
# ranges numéricos
print(re.findall(r'[a-zA-Z0-9]aria|[a-zA-Z0-9]oão', texto))
print(re.findall(r'MaRia|JoÃo', texto, flags=re.IGNORECASE))
