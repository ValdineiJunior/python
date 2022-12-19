print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato 2")
decisao = input("")

def computador_escolhe_jogada(n, m):
  deixar = m+1
  pecasQueDeveretirar = n - deixar
  if (pecasQueDeveretirar > n):
    pecasQueDeveretirar = n
    if ((pecasQueDeveretirar * 2) < n):
      pecasQueDeveretirar = pecasQueDeveretirar * 2
  return pecasQueDeveretirar

def usuario_escolhe_jogada(n,m):
  jogada = int(input("informe sua jogada: "))
  if (jogada < m):
    return jogada
  else:
    print("jogada invalida, vamos tentar novamente.")
    return usuario_escolhe_jogada(n,m)

def partida():
  n = int(input("informe o valor de n: "))
  m = int(input("informe o valor de m: "))
  jogadorComeça = n % (m+1) == 0
  if jogadorComeça:
    print("Você começa!")
    while (n > 0):
      
  else:
    print("Computador começa!")

  if computadorGanhou:
    print("O computador ganhou!")
  else:
    print("Você ganhou!")

def campeonato():
  