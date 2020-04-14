class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
  def getData(self):
    return self.data

  def setData(self, data):
    self.data = data

class Queue:
  # TODO: inicializar fila
  def __init__(self):
    self.first = None # ? inicio da fila
    self.last = None # ? fim da fila
    self._size = 0

  # TODO: adicionar elemento na fila
  def push(self, data):
    node = Node(data) # ? colocar o elemento em um nó
    
    if self.first is None: # ? verificar se a fila possui um primeiro elemento
      self.first = node

    if self.last is None: # ? verificar se a fila tem um último elemento
      self.last = node
    else:
      self.last.next = node
      self.last = node

    
    self._size = self._size + 1

  # TODO: remover elemento da fila
  def pop(self):
    if self._size > 0: # ? checar se a fila está vazia
      data = self.first.data
      self.first = self.first.next
      self._size = self._size - 1
      
      return data
    else:
      print('A fila está vazia.')


  # TODO: mostrar elementos da fila
  def show(self):
    if self._size > 0: # ? checar se a fila está vazia
      data = self.first.data
      
      return data
    else:
      print('A fila está vazia.')

  # TODO: exibir tamanho da fila
  def sizeQueue(self):
    return self._size

  # TODO: reproduzir formato de fila
  def __repr__(self):
    if self._size > 0:
      r = ''
      pointer = self.first
      while(pointer):
        r = r + str(pointer.data) + ' '
        pointer = pointer.next

      return r
    else:
      print('A fila está vazia.')

  def __str__(self):
    return self.__repr__()

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

        dado = input('insira um valor: ')
        fila.push(dado)

      elif opcao == '2':
        print(35*'-')

        print('Removendo elemento')
        fila.pop()

      elif opcao == '3':
        if self._size == 0:
          print(35*'-')
          print('lista vazia')
        else:
          print(35*'-')
          print(fila)
      
      elif opcao == '4':
        print(35*'-')
        print('Tamanho da lista: {}'.format(fila.sizeQueue()))

fila = Queue()
fila.menu()