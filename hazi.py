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


#2.1 Feladat

szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']

a_betus_szavak = []

a_betu_szamlalo = 0


for word in szavak:
    for letter in word:
        if letter == "a" or "A":
            a_betu_szamlalo += 1
    if a_betu_szamlalo > 0:
        a_betus_szavak.append(word)


print(f"Ennyiszer fordult elő az 'a' vagy az 'A' betű: {a_betu_szamlalo}")
print(f"Ezekben a szavakban voltak a betűk: {a_betus_szavak}")


#Szélsőérték 2. Feladat

szavak = [] 


while True:
    word = input("Adj meg egy szót (vagy nyomj Enter-t a befejezéshez): ")
    if word == "": 
        break
    szavak.append(word)

if szavak:
    print("A megadott szavak:")
    for word in szavak:
        print(word)

    
    leghosszabb = szavak[0]
    legrövidebb = szavak[0]

    for word in szavak: 
        if len(word) > len(leghosszabb):
            leghosszabb = word
        if len(word) < len(legrövidebb):
            legrövidebb = word

    print(f"A leghosszabb szó: {leghosszabb}")
    print(f"A legrövidebb szó: {legrövidebb}")
else:
    print("Nem adtál meg szót!")


#HGY feladat

date_list = [ '1983-06-15', '1991-12-07', '1987-03-24', '2001-08-19', '2015-04-03', '1980-11-21', '1999-02-28', '2008-09-12', '1995-01-05', '2020-07-09', '1986-10-30', '1993-05-14', '2011-06-26', '1989-12-18', '2005-03-11', '2018-09-01', '1997-07-20', '2012-11-03', '2023-01-22', '1990-04-09' ]
september_dates = []


count_before_2000 = 0
for date in date_list:
    year = int(date.split('-')[0])
    if year < 2000:
        count_before_2000 += 1


for date in date_list:
    month = int(date.split('-')[1])
    if month == 9:
        september_dates.append(date)

latest_year = 0
for date in date_list:
    year = int(date.split('-')[0])
    if year > latest_year:
        latest_year = year

print(f"2000 előtt {count_before_2000} dátum volt.")
print("Szeptember hónapra eső dátumok:")

for date in september_dates:
    print(f"{date}")

print(f"A legutolsó év: {latest_year}")
