import os

commands = ['ls', 'read', 'write', 'execute', 'log-out', 'exit']

class Commands():

    def ls(self, dir='../my-filesyst'):
        result = os.listdir(dir)
        print('\n'.join(result))
        return result

    def read(self, file):
        fd = os.open(file, os.O_RDONLY)
        result = os.read(fd, 50)
        os.close(fd)
        print(result)
        return result

    def write(self, file):
        fd = os.open(file, os.O_RDWR|os.O_CREAT)
        to_write = input("Write something:\n")     
        result = os.write(fd, bytes(to_write, encoding= 'utf-8'))
        os.close(fd)
        print('Written!')

    def execute(self, file):
        os.system('python3 ' + file)
        


def execute(command, arg = None):
    c = Commands()
    do = getattr(Commands, command)
    return do(c, arg)
