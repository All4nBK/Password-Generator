#Importação da biblioteca Random;
import random
#Importação da biblioteca OS;
import os

#Identificar as pastas do Usuario
usarname = os.environ
try:
  os.makedirs(os.path.join(r'C:\Users',usarname['USERNAME'],r'Documents\Password'))
  try:
    open(os.path.join(folder,"password.txt"), 'x')
  except:
    print('Atualizado')
  print('criado')
except:
  print('')
folder = os.path.join(r'C:\Users',usarname['USERNAME'],'Documents\Password')

# Abrir o arquivo em modo de leitura para ler o conteúdo original
with open(os.path.join(folder,"password.txt"), 'r') as arquivo:
    conteudo_original = arquivo.read()

#Informações dos caracteres que seram permitidos para a criação de senhas;
letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%&*()_+=[]{}|;:,.<>/?"
todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos

#Agora irei definir uma variavel do comprimento da senha;
comprimento_senha = 8

#agora criar um função que gera um senha aleatoria e mostrar a senha;
def generationPassword(a,b):
  senha = ''
  for i in range(b):
    senha += random.choice(a)
  return senha

#Agora é vamos fazer uma forma de mostrar a senha na tela;
info = input('Para qual software você quer salvar essa senha: ')
senha = generationPassword(todos_caracteres,comprimento_senha)
print("Sua senha é: ",senha)

with open(os.path.join(folder,"password.txt"), 'a') as arquivo:
  arquivo.write(senha+'- Senha salva para software - '+info+'\n')
  
print('Criado com Sucesso👌\nAtualizado')
  
  