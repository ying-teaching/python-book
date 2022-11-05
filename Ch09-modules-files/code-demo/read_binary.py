READ_BINARY = 'rb'
filename = 'sample.jpg'

with open(filename, READ_BINARY) as file:
    contents = file.read()
    print(f'Contents of binary file {filename}:\n')
    print(contents)
