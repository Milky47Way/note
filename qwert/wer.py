with open('стих.txt', 'r', encoding='utf-8') as file:
    for i in file:
        print(i)
author = input('Хто написав ці рядки?')
with open('стих.txt', 'a', encoding='utf-8') as file:
    file.write(author)
while True:
    answer = input('Бажаєте додати ще цитату? (так/ні)')
    if answer == 'так':
        quote = input('Введіть цитату:')
        author = input('Введіть автора:')
        with open('стих.txt', 'a', encoding='utf-8') as file:
            file.write(quote + '\n' + author + '\n')
    else:
        break
    with open('стих.txt', 'r', encoding='utf-8') as file:
        for i in file:
            print(i)

