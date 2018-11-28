#Aulas Strings
import string


print("abc" == 'abc')

texto = "A" 

print(texto[0])

print("ascii_letters: ", string.ascii_letters)
print("ascii_lowercase: ", string.ascii_lowercase)
print("ascii_uppercase: ", string.ascii_uppercase)
print("digits: ", string.digits)
print("hexdigits: ", string.hexdigits)
print("octdigits: ", string.octdigits)
print("punctuation: ", string.punctuation)
print("printable: ", string.printable)
print("whitespace: ", string.whitespace)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

nome = "Ricardo"
print(nome.upper())
print("Ricardo".lower())

str = "0000000this is string example....wow!!!0000000"
print(str.strip('0'))
print("1234 - É Alpha? ", "1234".isalpha())
print("1234 - É Digito? ", "1234".isdigit())
print("1234 - É Espaço? ", "1234".isspace())

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("Startswith:  ", "ricardo araujo".startswith('ara'))
print("Posição: ", "ricardo araujo".find('a'))
print("Replace: ", "ricardo araujo".replace('araujo','palhares'))
print("Split com parametro vazio: ", "ricardo araujo".split())
print("Split com parametro vazio: ", "laranja;banana;maçã".split(";"))
print("Replace e Split: ", "aadsjasojasdoasodjoadsjoasdjbbggfr".replace('j','j*').split('*'))
print("Join: ", "-->".join(['a','b','c','d']))

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print('{0},{1},{2}'.format('a','b','c'))
print('{0},{1},{2}'.format('ricardo','araujo','palhares'))
print('Coordenadas são: {latitude}, {longitude}'.format(latitude='3.2321',longitude = '0.3432'))
dicionario = {'nome': 'Ricardo', 'idade': '25'}
print('Dicionário : {nome}, {idade}'.format(**dicionario))
