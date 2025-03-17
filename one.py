a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


res = [val for val in a if val % 2 == 0]
re = [v * v for v in res]
b=["Ayush","Abhishek","Alam","Aman"]
ans=[c for c in b if len(c)>5]
print(ans)
array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print("2D Array:")
for row in array_2d:
    print(row)

flattened_array = [item*item for row in array_2d for item in row if item % 2 == 0]
# for item in flattened_array:
#     if item % 2 == 0:
#         print(item)
print(flattened_array)
row1=[1,2,3,4]
row2=[1,2,3,4]
new=[item+item2 for item in row1 for item2 in row2]

print(new)