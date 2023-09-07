# Gerenciamento de Senhas

Este repositório contém um script Python para gerenciar senhas de forma segura. O script permite que os usuários crier senhas aleatórias e as armazenem para uso posterior. O código é dividido em várias partes e oferece funcionalidades como geração de senhas fortes, avaliação da força da senha e armazenamento seguro das senhas. Abaixo, explicaremos cada parte do código em detalhes.

---

## Resumo do Código

O código é projetado para:

- Criar senhas aleatórias com base em critérios específicos.
  - Letras Maiúsculas
  - Letras Minúsculas
  - Contém Números
  - Contém Caracteres
  - Tamanho da Senha
- Avaliar a força das senhas geradas.
- Armazenar as senhas associadas a um software específico em um arquivo de texto.
- Permitir que os usuários escolham se desejam trocar uma senha recém-gerada ou salvá-la.
- Exibir informações sobre a força da senha ao usuário.

---

## Partes do Código

O código está dividido em várias seções distintas:

---

### Identificação de Pastas e Criação de Diretórios

Nesta seção, o código identifica a pasta do usuário e cria uma pasta chamada "Password" se ela não existir. Também verifica se o arquivo "password.txt" já existe e o atualiza se necessário.

---

### Geração de Senhas Aleatórias

Esta seção contém uma função `generationPassword` que gera senhas aleatórias com base em caracteres permitidos, como letras maiúsculas, minúsculas, números e símbolos. O comprimento da senha é ajustável.
```python
def generationPassword(a,b):
  senha = ''
  for i in range(b):
    senha += random.choice(a)
  return senha
```

---

### Avaliação da Força da Senha

Uma função chamada `avaliar_senha` é definida para avaliar a força da senha gerada. Ela verifica o comprimento da senha e se a senha inclui letras maiúsculas, minúsculas, números e símbolos. Também verifica se a senha segue um padrão fácil de adivinhar.

```python
def avaliar_senha(senha):
    if len(senha) < 8:
        return "Senha fraca. A senha deve ter pelo menos 8 caracteres."
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
    if senha.isnumeric() or senha.isalpha():
        return "Senha fraca. A senha não deve ser uma sequência simples de números ou letras."
    return "Senha forte!"
```

---

### Geração e Armazenamento de Senhas

Nesta seção, o código entra em um loop onde o usuário pode especificar para qual software a senha será salva. A senha é gerada e avaliada quanto à sua força. O usuário pode optar por trocar a senha ou salvá-la. Se a senha for salva, ela é registrada em um arquivo "password.txt" com informações sobre o software associado.

```python
info = input('Para qual software você quer salvar essa senha: ')

while trocar_senha == 1:
    senha = generationPassword(todos_caracteres,comprimento_senha)
    print("Sua senha é:",senha)
    
    print(avaliar_senha(senha),'\nA chance de adivinhar essa senha é 1/'+str(con**comprimento_senha))
    
    trocar_senha = int(input('Você deseja trocar essa senha:\n[0/Não]\n[1/Sim]\n'))

```

---

### Exibição da Senha

Após a criação da senha, o código exibe a senha gerada ao usuário.

---

## Uso

Para usar este código:

1. Clone o repositório.
2. Abra o arquivo `passwordGeneration/passwordGeneration.py` em um editor de texto.
3. Altere a variável `comprimento_senha` para o comprimento desejado da senha.
4. Execute o script.
5. A senha será gerada e salva no arquivo `password.txt` na pasta `Documents\Password`.

---

## Nota

É importante lembrar que a segurança das senhas é fundamental, e este código fornece uma maneira conveniente de gerar senhas fortes e armazená-las de forma segura. Certifique-se de tomar medidas adicionais para proteger os arquivos de senhas gerados e garantir que eles não sejam acessíveis a terceiros não autorizados.