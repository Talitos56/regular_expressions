# Meta caracteres: ^ $ * + ? { } ( )

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem vem"!
'''
# + 1 ou n
print(re.findall(r'jo+ão+', texto, flags=re.IGNORECASE))
# * 0 ou n
# print(re.sub(r'jo*ão*', 'Felipe', texto, flags=re.IGNORECASE))
# ? 0 ou 1
print(re.findall(r'jo?ão', texto, flags=re.IGNORECASE))
# {n} {min, máx}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.IGNORECASE))
print(re.findall(r've{3}m{1,2}', texto, flags=re.IGNORECASE))

texto2 = 'João ama ser amado amad ama'
print(re.findall(r'ama[do]*', texto2, flags=re.IGNORECASE))
