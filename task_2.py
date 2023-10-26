# -*- coding: utf-8 -*-
"""
Напишите функцию которая на вход получает строку с госномером автомибиля и
выводит к какому типу относится данный госномер, или возвращает Fail! если это
не госномер.

Типы гос.номеров:

Тип |    Пример
----+----------
 1А | с227на 69
 1Б |  ао365 78
  2 | ан7331 47
  3 | 3733мм 55

Для корректной работы автоматических тестов не переименовывайте функцию
get_plate_type!
"""

import re


def get_plate_type(plate):
  car_num = {
      "1А": r"\b[авекмнорстух]{1}\d{3}[авекмнорстух]{2} \d{2}",
      "1Б": r"\b[авекмнорстух]{2}\d{3} \d{2}",
      "2" : r"\b[авекмнорстух]{2}\d{4} \d{2}",
      "3" : r"\b\d{4}[авекмнорстух]{2} \d{2}"
  }
  for k in car_num:
    if re.findall(car_num[k], plate) != [] and re.findall(car_num[k], plate) == [plate]:
      return k
  return "Fail!"
