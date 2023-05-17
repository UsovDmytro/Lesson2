
def main():
    candidates = {}
    while True:
        fio = input('Введіть ПІБ кандидата: ')
        if fio == 'q':
            break
        if fio in candidates:
            print('Такий кандидат вже є')
            continue
        candidates[fio] = 0
    for candidate in candidates.keys():
        while True:
            voice = input(candidate + ', за кого ви голосуєте: ')
            if voice in candidates:
                candidates[voice] += 1
                break
            else:
                print('Нема такого кандидата')
    vote = sorted(list(candidates.values()), reverse=True)
    if vote.count(vote[0]) > 1:
        print('Декілька переможців:')
    else:
        print('Переможець:')
    for data in candidates.items():
        if data[1] == vote[0]:
            print(data[0])


if __name__ == '__main__':
    main()
