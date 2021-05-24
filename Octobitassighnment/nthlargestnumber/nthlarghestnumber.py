# _author_='Rahul kharatmol'

def Maximumelements(list1, N):
    List = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j];

        list1.remove(max1);
        List.append(max1)

    print(List)


# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 1

# Calling the function
Maximumelements(list1, N)

