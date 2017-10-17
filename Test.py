
with open('text.txt', 'r') as f:

    size_to_read = 20

    f.seek(100)

    f_contents = f.read(size_to_read)
    print(f_contents)

f.close()


    #while len(f_contents) > 0:
    #    print(f_contents, end='*')
    #    f_contents = f.read(size_to_read)

