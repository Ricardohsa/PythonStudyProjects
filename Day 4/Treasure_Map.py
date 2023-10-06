# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
location = 'X'
column = int(position[0])
row = int(position[1])

if column >= 1 and column <=3  and row >= 1 and row <=3:
    
    if column == 1:
        column = 0
    elif column == 2:
        column = 1
    elif column == 3:
        column = 2    
    
    if row == 1:
        row = 0
    elif row == 2:
        row = 1
    elif row == 3:
        row = 2        
        
    map[row][column] = location
    
else:
    print("This position doens't exists")    
        


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")