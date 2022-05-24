while True:
    line = input('> ')
    if line [0] == '#' :
        continue
        #continue skips an iteration of the loop
    if line == 'done' :
        break
        #break exits the current loop
    print(line)
print('Done!')
