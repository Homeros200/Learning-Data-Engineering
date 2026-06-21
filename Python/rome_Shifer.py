class RomShifer:
    def __init__(self, word, key):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.word = word
        self.key = key
        self.message = ""

        for i in word:
            if i in alphabet:
                
                self.message += alphabet[(alphabet.find(i) + key) % 26]

    def __repr__(self):
        return self.message
        

    
            
            
message1 = RomShifer("hello", 5)


print(message1)


print(type(RomShifer))

print(dir(message1))

