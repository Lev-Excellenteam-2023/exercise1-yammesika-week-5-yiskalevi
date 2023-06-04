# Yiska Levi

def FindMsg(file_open):
    str=''
    with open(file_open, 'rb') as f:
        while True:
            byte = f.read(1)
            if not byte:
                break
            # Check if the byte is a lowercase letter
            elif byte.islower():
                str=str+byte.decode('ascii')
            elif byte == b'!':
                if len(str)>4:
                    str = str + '!'
                    ans=str
                    str=''
                    yield ans
            else:
                str=''
    return ''

fileOpen='Resources/Logo.jpg'
for msg in FindMsg(fileOpen):
    print(msg)
