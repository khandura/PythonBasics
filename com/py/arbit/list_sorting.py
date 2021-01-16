def sort_list():
    names = ['Ak', 'Pk', 'P', 'Ack', 'Pk']
    print('names : ', names)
    names.sort()
    print('names : ', names)

    sorted_names = sorted(names, reverse=True)
    print('names : ', sorted_names)


sort_list()
