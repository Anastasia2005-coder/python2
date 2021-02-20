friends=[]
while len(friends)<5:
    name=input("Введите имя: ")
    # проверить если переменная name не в списке
    if name not in friends:
        friends.append(name)
    else:
        print("Ошибка")

# отсортировать по алфавиту 
sorted_friends = sorted(friends)
# вывести при помощи цыкла for in range 
# print(sorted_friends)

for i, friends in enumerate(friends):
    print(i+1, friends)