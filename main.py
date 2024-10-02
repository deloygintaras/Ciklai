# 1. Su for pagalba penkis kartus išveskite savo vardą.
# vardas = "Gintaras"
# for i in range(5):
#     print(vardas)


# 2. Parašyti for, kuris išvestų kiekvieną skaičių pradedant nuo 0 ir baigiant 10.

# for i in range(0, 11):
#     print(i)


# 3. Parašyti for, kuris išvestų kas antrą skaičių pradedant 0 ir baigiant 15.

# for i in range(0, 15, 2):
#     print(i)


# 4. Parašyti for, kuris išvestų kas trečią skaičių, pradedant 1 ir baigiant 20.
#
# for i in range(1, 21, 3):
#     print([i])


# Kiekvieną skaičių apskliausti laužtiniais skliaustais. Pvz.: [1][4][7]...





# 5. Parašyti for, kuris eitų pro kiekvieną skaičių nuo 1 iki 20. Jame apsirašyti if
# sąlygą, kuri patikrintų ar dabartinis skaičius dalinasi iš 4, jei taip tai šį
# skaičių išvesti.

# for i in range(1, 20):
#     if i % 4 == 0:
#         print(f"Skaicius {i} dalinasi is 4")
#     else:
#         print(f"Skaicius {i} nesidalina is 4")


# 6. Išveskite visus skaičius nuo 1 iki 15, prie kiekvieno jų nurodant tai lyginis
# ar nelyginis skaičius. Pvz:
# 1 - nelyginis
# 2 - lyginis
# 3 - nelyginis

# for i in range(1, 15):
#     if i % 2 ==0:
#         print(f"{i} - lyginis")
#     else:
#         print(f"{i} - NElyginis")



# 7. Susikurkite kintamuosius rėžių pradžiai ir pabaigai nusakyti. Patikrinkite,
# kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga). Jei rėžiai
# tinkami, tuomet vykdyti for, kuris atskirose eilutėse išvestų kiekvieną
# skaičių iš tų rėžių, bei atskiriant tarpu - tų skaičių kvadratus.


# kint1 = 1
# kint2 = 20
# if kint1 < kint2:
#     print("Nustatyti reziai - tinkami")
#     for i in range(kint1, kint2 + 1):
#         kv = i ** 2
#         print(f"{i} {kv}")
# else:
#     print("Klaida, pradzios reziai turi buti mazesni uz pabaigos")


# 8. Susikurkite kintamuosius rėžių pradžiai ir pabaigai nusakyti. Patikrinkite,
# kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga). Jei rėžiai
# tinkami, tuomet vykdyti for, kuris iš duotų skaičių išvestų visus nelyginius
# skaičius arba tuos, kurie dalinasi iš 8.
#
# kint1 = 1
# kint2 = 10
# if kint1 < kint2:
#     print("Nustatyti reziai - tinkami")
#     for i in range(kint1, kint2 + 1):
#         if i % 2 != 0 or i % 8 == 0:
#             print(i)
# else:
#     print("Klaida")

# 9. Leiskite vartotojui įvesti savo vardą. Ciklą for vykdykite tiek kartų kiek
# tame varde yra raidžių. Visais atvejais išveskite tą patį pasisveikinimą,
# pavyzdžiui "Labas, Ieva" (ši eilutė kartotųsi 4 kartus).

# klientas = input("iveskite savo varda\n")
# raides = len(klientas)
# print(raides)
# for i in range(raides):
#     print(f"Labas, {klientas}")



# 10.Susikurkite tokį ciklą: for elementas in [88, 65, 21, 26, 47]
# Iš duotų skaičių išveskite visus skaičius, kurie yra lyginiai.

# for elementas in [88, 65, 21, 26, 47]:
#     if elementas % 2 == 0:
#         print(f"{elementas} - lyginis")


# 11.Leiskite vartotojui nurodyti rėžių pradžią, pabaigą, žingsnį. Taip pat, kokius
# skaičius jis nori matyti (lyginius ar nelyginius). Patikrinkite ar rėžiai tinkami,
# jei taip vykdykite ciklą, kuris eitų per nurodytą rėžių, darant atitinkamą
# žingsnį. Išveskite tik tokius skaičius kokius vartotojas pasirinko (lyginius
# arba nelyginius).

# pradzia = int(input("Pasirinkite rėžio pradžią\n"))
# pabaiga = int(input("Pasirinkite rėžio pabaigą\n"))
# zingsnis = int(input("Įveskite žingsnį\n"))
# pasirinkimas = input("Norite matyti lyginius ar nelyginius skaičius? (lyginius/nelyginius)\n")
# if zingsnis == 0 or (pradzia < pabaiga and zingsnis < 0) or (pradzia > pabaiga and zingsnis > 0):
#     print("Režis - klaidingas")
# else:
#     for i in range(pradzia, pabaiga + (1 if zingsnis > 0 else -1), zingsnis):
#         if (pasirinkimas == 'lyginis' and i % 2 == 0) or (pasirinkimas == 'nelyginis' and i % 2 != 0):
#             print(i)
#
# isEven = skaicius == "lyginius"
# for i in range(pradzia, pabaiga +1, zingsnis):
#     if isEven and i % 2 == 0:
#         print(i)
#         elif not isEven

# 12.Su for pagalba, pamėginkite išvesti tokią eglutę:
# *
# **
# ***
# ****
# *****
# (papildomai) leiskite vartotojui pasirinkti kokio dydžio eglutė turėtų būti
# išvesta.

# egle = int(input("Iveskite eglutes dydi simboliais\n"))
# for i in range(1, egle, + 1):
#     print('*' * i)

# 13.Leiskite vartotojui įvesti bet kokį žodį, bei pasirinkti po kiek kartų turėtų
# būti pakartojama kiekviena raidė. Su ciklo pagalba išveskite kiekvieną
# raidę iš žodžio atskiroje eilutėje, taip pat, tą raidę eilutėje kartokite tiek
# kartų kiek pasirinko vartotojas (16 pvz).

# zodis = str(input("Iveskite norima zodi\n"))
# pakart = int(input("kiek kartu turi buti pakartojama kiekviena raide?\n"))
# for i in zodis:
#     print(i * pakart)



# 14.(papildomai, sunkiau) Be daugybos veiksmo programoje, sudauginkite du
# skaičius.
# a = 3
# b = 1
# def multiply(a, b):
#     result = 0
#     for _ in range(b):
#         result += a
#     return result



# 15.Raskite visų skaičių nuo 1 iki 100 sumą.

# suma = 0
# for i in range(100):
#     suma += i
# print(f"gauta suma = {suma}")


# 16.Raskite visų lyginių skaičių nuo 20 iki 50 sumą.
# suma = 0
# for i in range(20, 50):
#     if i % 2 == 0:
#         suma += i
# print(f"lyginiu gauta suma = {suma}")


# 17.Raskite visų nelyginių skaičių nuo 30 iki 60 sumą.
# suma = 0
# for i in range(30, 60):
#     if i % 2 != 0:
#         suma += i
# print(f"nelyginiu gauta suma = {suma}")


# 18.Rasti visų skaičių, žemesnių už 1000 ir kurie dalinasi iš 3 arba 5, sumą.
# Pavyzdys:
# Visi skaičiai mažesni už 10 ir kurie dalinasi iš 3 arba 5 yra: 3, 5, 6, 9.
# Šių skaičių suma yra 23.
# Turite gauti 233168 atsakymą.
# suma = 0
# for i in range(0, 1000):
#     if i % 3 == 0 or i % 5 == 0:
#         suma += i
#         print(f"Gauta suma is skaiciu < 1000 ir kurie dalinasi is 3 arba 5 = {suma}")



# 19.The "Fizz-Buzz test" is an interview question designed to help filter out the
# 99.5% of programming job candidates who can't seem to program their
# way out of a wet paper bag. The text of the programming assignment is
# as follows:
#
# "Write a program that prints the numbers from 1 to 100. But for multiples
# of three print “Fizz” instead of the number and for the multiples of five
# print “Buzz”. For numbers which are multiples of both three and five print
# “FizzBuzz”."
#
# for i in range(1, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"{i} = FizzBuzz")
#     elif i % 3 == 0:
#         print(f"{i} = Fizz")
#     elif i % 5 == 0:
#         print(f"{i} = Buzz")
#     else:
#         print(i)

# 20.(sunkesnė) Parašyti for ciklą, kuris išvestų norimą kiekį fibonačiaus skaičių
# į ekraną. Fibonačiaus sekoje kiekvienas skaičius yra lygus prieš jį ėjusių
# dviejų skaičių sumai: 1, 1, 2, 3, 5, 8, 13, 21...
# 1. Susikurkite tris sveikųjų skaičių kintamuosius, kurie jums padės tai pasiekti.
# 1. Pirmi du kintamieji saugos paskutinius du skaičius.
# 2. Trečiasis bus šių pirmų dviejų skaičių suma.
# 2. Pirmus du skaičius išveskite ne cikle, o prieš jį ir ciklą pradėkite vykdyti nuo 2, o ne nuo 0.
# 3. Kiekvieno ciklo metu turite perskaičiuot trečiąjį skaičių (pirmų dviejų skaičių sudėtis),
# tuomet pirmasis skaičius yra lygus antram, o antrasis lygus trečiam, išvesti į ekraną trečią skaičių.

# n = 25
# sk1 = 5
# sk2 = 7
# print(f"Pirmasis kintamasis = {sk1}")
# print(f"Antras kintamasis = {sk2}")
# for i in range(2, n):
#     sk3 = sk1 + sk2
#     print(f"Trecias kintamasis = {sk3}")
