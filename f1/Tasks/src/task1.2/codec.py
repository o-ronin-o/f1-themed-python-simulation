#this is a codec class that recieves an array of strings, encode it and a decode it


class Codec:
    def __init__(self):
        self.__command_length = []
        self.encoded_message = ""

    def encode(self,commands): 
        for x in commands:
            self.__command_length.append(len(x))
            self.encoded_message += x
        return self.encoded_message
    def decode(self):
        start = 0
        commands =[]
        for x in self.__command_length:
            commands.append(self.encoded_message[start:start+x])
            start+= x
        return commands

def main():
    commands = ["Push","Box,box","Push","Overtake"]
    codec = Codec()
    encoded_message =codec.encode(commands)
    print(encoded_message)
    decoded_message = codec.decode()
    print(decoded_message)

if __name__ == "__main__":
    main()
