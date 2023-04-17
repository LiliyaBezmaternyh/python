# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120
n = int(input())
f = 1
i = 1
while i <= n:
  f = f * i 
  i = i + 1
print(f)


# length = int(input("Количество дней: "))
# mx = 0
# current = 0
# for i in range(length):
#     temp = int(input("Температура: "))
#     if temp > 0:
#         current += 1
#     else:
#         current = 0

#     if mx < current:
#         mx = current

# print(f"max: {mx}")

length = int(input("Количество дней: "))
mx = 0
current = 0
for i in range(length):
    temp = int(input("Температура: "))
    if temp > 0:
        current += 1
    if temp < 0 or i == length - 1:
        print(mx, current, temp)
        if mx < current:
            mx = current
        current = 0


print(f"max: {mx}")


# n = int(input("Введите количество арбузов: "))
# massa1 = int(input("Введите массу  арбуза: "))
# min_mass = massa1
# max_mass = massa1
# i = 2
# while i <= n:
#     massa = int(input("Введите массу  арбуза: "))
#     if massa < min_mass:
#         min_mass = massa
#     if massa > max_mass: 
#         max_mass = massa
#     i=i+1
# print("Максимальный вес:", max_mass)    
# print("Минимальный вес:", min_mass)