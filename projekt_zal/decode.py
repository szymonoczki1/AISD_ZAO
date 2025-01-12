class DecodeHuffman:
    def __init__(self, decodefile, outputfile):
        self.decode_file = decodefile
        self.output_file = outputfile
        self.code = ''
        self.code_dict = {}
        self.rev_code_dict = {}
        self.decoded_string = []
        self.code_len = -1
        self.read_coded_file()
        self.reverse_dict()
        self.decode_data()
        self.write_output()

    def read_coded_file(self):
        with open(self.decode_file, 'rb') as file:
            self.code_len = int(file.readline().decode('utf-8').strip())

            header_bytes = file.readline()
            header = header_bytes.decode('utf-8')
            
            for item in header.split():
                if ":" in item:
                    key, value = item.split(":")
                    key = key[1:-1]
                    self.code_dict[key] = value

            byte_data = file.read()
            self.code = bin(int.from_bytes(byte_data))[2:]
            self.code = self.code.zfill(self.code_len)

    def parse_special_characters(self, key):
        if key == '\\n':
            return'\n'
        elif key == '\\t':
            return '\t'
        elif key == '\\\\':
            return '\\'
        elif key == '\\\'':
            return '\''
        elif key == '\\\"':
            return '\"'
        elif key == '':
            return ' '
        return key

    def reverse_dict(self):
        for key, value in self.code_dict.items():
            key = self.parse_special_characters(key)
            self.rev_code_dict[value] = key


    def decode_data(self):
        i = 0
        min_code_len = min([len(x) for x in self.code_dict.values()])
        max_code_len = max([len(x) for x in self.code_dict.values()])
        while i < len(self.code):
            for length in range(min_code_len, max_code_len + 1):
                code_snippet = self.code[i:i+length]
                if code_snippet in self.rev_code_dict:
                    self.decoded_string.append(self.rev_code_dict[code_snippet])
                    i += length
                    break

    def write_output(self):
        with open(self.output_file, 'w') as file:
            for char in self.decoded_string:
                file.write(char)

        

DecodeHuffman('coded_file.bin', 'output_file.txt')

