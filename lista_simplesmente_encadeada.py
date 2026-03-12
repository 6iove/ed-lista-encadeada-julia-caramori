class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None # quando o primeiro nó for adicionado, head apontará para ele
        self.size = 0 # variável para armazenar o tamanho da lista
        
    def insert_beginning(self, value):
        new_node = Node(value) # novo nó é criado passando como parâmetro o dado desejado
        new_node.next = self.head # endereço do próximo nó
        self.head = new_node # o head aponta para o novo nó criado
        self.size += 1
        
    def insert_end(self, value):
        new_node = Node(value) # instancia novo nó
        
        if self.head == None: # se a lista estiver vazia, o novo nó se torna o head
            new_node.next = self.head
            self.head = new_node
        else: # caso contrário, percorre a lista até o final e adiciona o novo nó
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = None
        self.size += 1
    
    '''
    se o nó a ser removido for o head, o head passa a apontar para o próximo nó.
    caso contrário, percorre a lista até encontrar o nó a ser removido, 
    e o nó anterior passa a apontar para o sucessor do nó a ser removido.
    '''       
    def remove(self, value):
        node = self.head
        current_node = self.head
        find = False
        
        if node.value == value:
            self.head = node.next
        else:
            current_node = self.head
            node = node.next
        
        while node != None:
            if node.value == value:
                current_node.next = node.next
                find = True # marca se encontrou o valor a ser removido
                self.size -= 1
                break
            else:
                current_node = node
                node = node.next 
        if find == False:
            print("Valor não encontrado na lista.")
                
    def search(self, target):
        current_node = self.head 
        while current_node:
            if current_node.value == target:
                return True
            current_node = current_node.next
        return False
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
list = LinkedList()

list.insert_beginning(12)
list.insert_beginning(11)
list.insert_beginning(15)
list.insert_end(20)
list.insert_end(22)
list.remove(11)
list.remove(12)
# list.remove(15)
# list.remove(20)
# list.remove(22)
list.remove(30) # valor não encontrado na lista

print("\n== Lista Encadeada ==")
list.print_list()

print("\nExiste valor:", list.search(15))
print("\nTamanho da lista:", list.get_size())
print("\nA lista está vazia?", list.is_empty())