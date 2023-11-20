def main():
   table = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
   ]

   for y in range(len(table)):
      #print(f"\n{y}:")
      for x in range(len(table[y])):
         print(
            f"|{table[y][x]:_^5x}|", end = " "
            )# перенос строки мы заменяем на " "
      # :b - переводит в бинарный код
      # 5 - резервирует 5 знаков для вывода,
      # центрует значения (^), а все свободные ячейки заполняем символом "_"

      print() #перенос строки

   '''for y in range(len(table)):

      line = ""
      for x in range(len(table[y])):
         line += "{0} ".format(table[x][y]) # format стринги
         
      print(line)'''


if __name__ == "__main__":
     main()
