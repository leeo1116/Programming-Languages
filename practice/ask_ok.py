def ask_ok(prompt, retries = 4, complaint = 'Yes or no please!'):
    while True:
        ok = input(prompt)
        if ok in ['y', 'ye', 'yes']:
            return True
        if ok in ['n', 'no', 'nope']:
            return False
        retries -= 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)

print(ask_ok('ok to overwrite the file', 2, 'come on, only yes or no'))