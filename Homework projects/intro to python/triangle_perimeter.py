# -*- coding: utf-8 -*-
"""triangle-perimeter

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DR-xwmoeuoyFuKlUOUKHGVyFOFnETwJU
"""

def main():
  side1 = float(input("what is the length of side 1? "))
  side2 = float(input("what is the length of side 2? "))
  side3 = float(input("what is the length of side 3? "))

  perimeter = side1 + side2 + side3

  print(f"The perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
  main()