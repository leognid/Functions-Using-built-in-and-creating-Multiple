documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directoriers = {
  '1':['2207 876234', '11-2', '10006'],
  '2':['1006'],
  '3':[]
}

def people(numbers):
  for doc_numbers in documents:
    if doc_numbers["number"] == numbers:
      print(doc_numbers["name"])
      return
  else:
    print('Такого номера нет')

def people_list():
  for persons in documents:
    print(persons['type'], persons['number'], persons['name'])
    
def shelf(numbers):
  for shelf_directoriers in directoriers.items():
    for doc_numbers in shelf_directoriers[1]:
      if doc_numbers == numbers:
        print('Документ на полке', shelf_directoriers[0])
        return
  else:
    print('Такого номера нет')
    
def add_command(params_type, number, name, directoriers_number):
  if int(directoriers_number) == 1 or int(directoriers_number) == 2 or int(directoriers_number) == 3:
    documents.append({"type": params_type, "number": number, "name": name})
    directoriers[directoriers_number].append(number)
  else:
    print('Введенной полки не существует. Запись не осуществлена.')
        
while True:
  user_search = input('Введите команду: ')
  if user_search == 'p':
    people(input('Введите номер документа:'))
  elif user_search == 'l':
     people_list()
  elif user_search == 's':
    shelf(input('Введите номер документа:'))
  elif user_search == 'a':
    add_command(input('Введите тип документа:'), input('Введите номер документа:'), input('Введите имя:'), input('Введите номер полки (1, 2, 3):'))
  elif user_search == 'out':
    print('До свидания')
  else:
     print('Вы ввели некорректную команду, повторите ввод.')
    