"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
age = int(input('Введите ваш возраст: '))


def main(age):
  if age > 0 and age < 6:
    print("Вы должны ходить в детский сад.")
  elif age >= 6 and age < 18:
    print("Вы должны учиться в школу.")
  elif age >= 18 and age <= 23:
    print("Вы должны учиться в ВУЗе")
  else:
    print("Вы должны работать.")
         


    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код

    """
    pass

if __name__ == "__main__":
  main(age)

