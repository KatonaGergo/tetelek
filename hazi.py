#2. Feladat

interval = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
total_sum = 0
in_interval = []
count = 0


while count < 5:
    try:
        input_value = int(input("Írj be számokat a [-5; 5] zárt intervallumon!"))
        if input_value in interval:
            in_interval.append(input_value)
            total_sum += input_value
            count += 1
        else:
            print("A szám nincs az intervallumban!")
    except ValueError:
        print("Számot adj meg!")

print(f"Az intervallumba eső számaid: {in_interval}")

print(f"Az összegük: {total_sum}")