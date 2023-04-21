# Importação da biblioteca Random;
import random
# Importação da biblioteca OS;
import os

# Identificar as pastas do Usuario;
usarname = os.environ
folder = os.path.join(r'C:\Users',usarname['USERNAME'],'Documents\Password')

try:
  os.makedirs(os.path.join(r'C:\Users',usarname['USERNAME'],r'Documents\Password'))
  try:
    open(os.path.join(folder,"password.txt"), 'x')
  except:
    print('Atualizado')
  print('criado')
except:
  print('')


# Abrir o arquivo em modo de leitura para ler o conteúdo original;
with open(os.path.join(folder,"password.txt"), 'r') as arquivo:
    conteudo_original = arquivo.read()

# Informações dos caracteres que seram permitidos para a criação de senhas;
letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%&*()_-+=[]{}|;:,.<>/?"
todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos
con = len(todos_caracteres)

# Agora irei definir uma variavel do comprimento da senha;
comprimento_senha = 12

# Variavel de pedi para troca senha;
trocar_senha = 1

# Vamos criar um função que possa olhar se a senha criado é forte ou fraca;
def avaliar_senha(senha):
    # Checar o comprimento da senha;
    if len(senha) < 8:
        return "Senha fraca. A senha deve ter pelo menos 8 caracteres."
    
    # Checar se a senha inclui letras maiúsculas, minúsculas, números e símbolos
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_simbolo = False
    
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isnumeric():
            tem_numero = True
        elif caractere in "!@#$%&*()_+-=[]{}|;:,.<>/?":
            tem_simbolo = True
    
    if not (tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo):
        return "Senha fraca. A senha deve incluir letras maiúsculas, minúsculas, números e símbolos."
    
    # Checar se a senha segue um padrão fácil de adivinhar
    if senha.isnumeric() or senha.isalpha():
        return "Senha fraca. A senha não deve ser uma sequência simples de números ou letras."
    
    # Se a senha passar em todos os testes acima, ela é considerada forte
    return "Senha forte!"


# Agora criar um função que gera um senha aleatoria e mostrar a senha;
def generationPassword(a,b):
  senha = ''
  for i in range(b):
    senha += random.choice(a)
  return senha

while True:
  # Agora vamos pedir para qual software essa senha sera salva;
  info = input('Para qual software você quer salvar essa senha: ')
  trocar_senha = 0
  # Agora é criado um While com a variavel 'trocar_senha' com seu valor '1' e para que o usuario possa trocar a senha novamente;
  while trocar_senha == 1:
    senha = generationPassword(todos_caracteres,comprimento_senha)
    print("Sua senha é:",senha)
    # Agora sera mostrado para o usuario se a senha criado é forte ou fraca;
    print(avaliar_senha(senha),'\nA chance de adivinar essa senha é 1/'+str(con**comprimento_senha))
    # Aqui é perguntado ao usuario se ele deseja outra senha se sua entra for 0 sera salva essa senha, se for 1 sera gerada outra senha;
    trocar_senha = int(input('Você deseja trocar essa senha:\n[0/Não]\n[1/Sim]\n'))

  with open(os.path.join(folder,"password.txt"), 'a') as arquivo:
    arquivo.write(senha+'- Senha salva para software - '+info+'\n')
    
  print('Criado com Sucesso👌\nAtualizado')
