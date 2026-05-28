color = {"red","blue","yellow"}
newcolor ={"brown","purple"}
print("The color are",color)
print(type(color))
print(len(color))
color.add("green")#for add new color
print(color)
color.remove("blue")#for remove elements
print(color)
#for update new items
color.update(newcolor)
print(color)
#for clear set
color.clear()
print(color)

num ={2,3,4,4,5,}
print(num)
print(type(num))

#for add num
num.add(9)
print(num)

num.remove(2)
print(num)

num.discard(5)
print(num)

set1={'a','b','c','d'}
set2={2,3,4,5,5,6}
#in set for join using union
set3=set1.union(set2)
print(set3)