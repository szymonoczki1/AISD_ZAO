from queue import minHeap
from tree import Node, Tree

class Huffman:
    def __init__(self):
        self.txt = []
        self.char_dict = {}
        self.q = minHeap()
        self.code_dict = {}
        self.tree = Tree()

        self.read_file('input_file.txt')
        self.parse_input()
        self.insert_data()
        self.huffman()
        self.make_code_dict()
        self.make_coded_file()


    def read_file(self, file):
        with open(file, 'r', encoding="utf-8") as file:
            self.txt = file.readlines()
            self.txt = list("".join(self.txt))

    def parse_input(self):
        for char in self.txt:
            if char not in self.char_dict.keys():
                self.char_dict.update({char:1})
            else:
                self.char_dict[char] += 1

    def insert_data(self):
        for key, value in self.char_dict.items():
            node = Node(name=key,number=value)
            self.q.heap_insert(node)
            self.tree.addNode(node)

    def huffman(self):
        n = len(self.q.heap)
        for _ in range(n-1):
            x = self.q.heap_remove()
            y = self.q.heap_remove()
            new_number = x.number + y.number
            new_name = x.name + y.name
            node = Node(left=x, right=y, name=new_name, number=new_number)
            self.q.heap_insert(node)
            self.tree.addNode(node)

    def find_code(self, node, char, code=''):
        if node.left != None and char in node.left.name:
            code+='0'
            return self.find_code(node.left, char, code)
        elif node.right != None and char in node.right.name:
            code+='1'
            return self.find_code(node.right, char, code)
        
        return code
        
        
    def make_code_dict(self):
        root = self.tree.nodes[-1]
        char_order = root.name
        for char in char_order:
            code = self.find_code(root,char)
            self.code_dict.update({char: code})

    def make_coded_file(self):
        binary_code = ''.join(self.code_dict[char] for char in self.txt)
        byte_data = int(binary_code, 2).to_bytes((len(binary_code) + 7) // 8)

        header = f'{len(binary_code)}\n'
        for key, code in self.code_dict.items():
            header += f"{repr(key)}:{code} "
        header += "\n"
        header_bytes = header.encode('utf-8')

        with open('coded_file.bin', 'wb') as file:
            file.write(header_bytes)

            file.write(byte_data)

    

            




Huffman()