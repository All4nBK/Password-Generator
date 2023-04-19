#Importação da biblioteca Random;
import random

#Informações dos caracteres que seram permitidos para a criação de senhas;
letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%&*()_+-=[]{}|;:,.<>/?"
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
senha = generationPassword(todos_caracteres,comprimento_senha)
print("Sua senha é: ",senha)
  
  
