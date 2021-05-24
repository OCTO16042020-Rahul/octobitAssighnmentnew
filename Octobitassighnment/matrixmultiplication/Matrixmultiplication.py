# _author_='Rahul kharatmol'


J = [[1, 17, 43],
     [44, 55, 61],
     [74, 85, 93]]

K = [[5, 8, 1, 2],
     [6, 7, 3, 0],

     [4, 5, 9, 1]]

result = [[sum(a * b for a, b in zip(A_row, B_col))
           for B_col in zip(*J)]
          for A_row in K]

for r in result:
    print(r)