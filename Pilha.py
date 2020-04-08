class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.last = None
    self._size = 0

  def sizeList(self):
    # ? retorna o tamanho da lista
    return self._size

  def __repr__(self):
    r = ''
    pointer = self.last
    while(pointer):
      r = r + str(pointer.data) + '\n'
      pointer = pointer.next
    
    return r
  
  # ! inserir na pilha
  def push(self, element):
    node = Node(element) # envolver o elemento em um nó

    node.next = self.last # antigo elemento no topo da lista
    self.last = node # adicionar o novo elemento ao topo

    self._size = self._size + 1

  # ! remover da pilha
  def pop(self):
    if self._size > 0 : # checar se a pilha não está vazia
      node = self.last # pegar o ultimo elemento da pilha
      self.last = self.last.next # mover o topo para 1 posição abaixo

      self._size = self._size - 1 # reduzir tamanho da lista

      return node.data
    else:
      print('A pilha está vazia.')

  # ! retorna o topo da pilha sem remover
  def peek(self):
    if self._size > 0 : # checar se a pilha não está vazia
      return self.last.data # retorna quem tá no topo da lista

    else:
      print('A pilha está vazia.')

  def menu(self, contador = 0):
    while contador == 0:
      print(35*'-')
      print('Insira a opcao desejada: \n')
      opcao = (input('(0) para sair\n'
                      '(1) para adicionar elemento\n'
                      '(2) para exluir elemento\n'
                      '(3) para mostrar em tela\n'
                      '(4) para exibir tamanho da lista\n'))

      if opcao == '0':
        contador = 1

      elif opcao == '1':
        print(35*'-')

        print('Adicionando elemento.')
        pilha.push(3)
        pilha.push(4)
        pilha.push(5)
        pilha.push(6)

      elif opcao == '2':
        print(35*'-')

        print('Removendo elemento')
        pilha.pop()

      elif opcao == '3':
        if self._size == 0:
          print(35*'-')
          print('lista vazia')
        else:
          print(35*'-')
          print(pilha)
      
      elif opcao == '4':
        print(35*'-')
        print('Tamanho da lista: {}'.format(pilha.sizeList()))


pilha = Stack()
pilha.menu()