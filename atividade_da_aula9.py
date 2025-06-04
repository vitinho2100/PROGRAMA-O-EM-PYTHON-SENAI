# ATIVIDADE  1
n = 0 
while n <= 1001:
     print(n)
     n = n + 1
     
#1.2
lista_nomes = []
for n in range(0,10):
    nome = input('digite o seu nome')
    lista_nomes.append(nome)
    print(lista_nomes)
    
    
#ATIVIDADE 2
# Sistema de Notas de Alunos

# Dados do usuário (pode ser alterado conforme necessidade)
usuario_correto = "yasmim"
senha_correta = "0406"

tentativas = 0
acesso_liberado = False

# Login com 3 tentativas
while tentativas < 3:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    
    if usuario == usuario_correto and senha == senha_correta:
        print("\n✅ Acesso liberado!")
        acesso_liberado = True
        break
    else:
        tentativas += 1
        print(f"❌ Usuário ou senha incorretos. Tentativas restantes: {3 - tentativas}")

if not acesso_liberado:
    print("\n🔒 Conta bloqueada após 3 tentativas.")
else:
    # Inserção de notas
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a nota {i}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("⚠️ A nota deve estar entre 0 e 10.")
            except ValueError:
                print("⚠️ Entrada inválida. Digite um número.")

    # Cálculo da média
    media = sum(notas) / len(notas)
    print(f"\n📘 Notas inseridas: {notas}")
    print(f"📊 Média final: {media:.2f}")

    # Verificação de aprovação
    if media >= 7:
        print("🎉 Aluno aprovado!")
    elif media >= 5:
        print("📋 Aluno em recuperação.")
    else:
        print("❌ Aluno reprovado.")
    
    
     