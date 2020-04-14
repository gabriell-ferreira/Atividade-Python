class Node:

    def __init__(self, name, age): # define as variaveis utilizadas
        self.name = name
        self.age = age
        self.next = None

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, name, age, index): ## inserir as variaveis que serão utilizadas

        if index >= 0:

            # cria o novo nó
            node = Node(name, age) ## cria o nó com os campos nome e idade

            # verifica se a lista está vazia
            if self.empty():
                self.first = node
                self.last = node
            else:

                if index == 0:
                    # inserção no início
                    node.setNext(self.first)
                    self.first = node
                elif index >= self.len_list:
                    # inserção ao final
                    self.last.setNext(node)
                    self.last = node
                else:
                    # inserção no meio
                    prev_node = self.first
                    curr_node = self.first.getNext()
                    curr_index = 1

                    while curr_node != None:

                        if curr_index == index:
                            # seta o curr_node como o próximo do nó
                            node.setNext(curr_node)
                            # seta o node como o próximo do prev_nodes
                            prev_node.setNext(node)

                        prev_node = curr_node
                        curr_node = curr_node.getNext()
                        curr_index += 1

            # atualiza o tamanho da lista
            self.len_list += 1

    def empty(self):
        if self.first == None:
            return True
        return False

    def length(self):
        return self.len_list

    def show(self):

        curr_node = self.first
        print(35 * '-')
        print('')
        while curr_node != None:

            print(curr_node.getName(), end=5*' ') ## mostrar o nome informado
            print(curr_node.getAge(), end=' ' + 'anos') ## mostrar a idade informada
            print('')
            curr_node = curr_node.getNext()
        print('')

    def menu(self, contador = 0):
        while contador == 0: ## contador do menu
            print(35*'-')
            print('Insira a opcao desejada: \n')
            opcao = (input('(0) para sair\n'
                              '(1) para adicionar\n'
                              '(2) para mostrar em tela\n'
                              '(3) para exibir tamanho da lista\n'))

            if opcao == '0':
                contador = 1

            elif opcao == '1':
                print(35*'-')
                nome = input('insira seu nome: ')
                idade = int(input('insira sua idade: '))
                posicao = int(input('insira a posiçao: '))
                lista.push(nome, idade, posicao) ## inserir o nome, idade e posicao dos valores informados

            elif opcao == '2':
                if lista.empty():
                    print(35*'-')
                    print('lista vazia')
                else:
                    lista.show()

            elif opcao == '3':
                print(35*'-')
                print('Tamanho da lista: %d\n' % lista.length())

lista = LinkedList()
lista.menu()
