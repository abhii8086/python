# break to exit the loop 
for i in range(5):
    if i == 3:
        break
    print(i)

# continue is used to skip current statement and moved to next 
print("\n")
for i in range(5):
    if i == 3:
        continue
    print(i)