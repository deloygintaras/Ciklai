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



# 9. Leiskite vartotojui įvesti savo vardą. Ciklą for vykdykite tiek kartų kiek
# tame varde yra raidžių. Visais atvejais išveskite tą patį pasisveikinimą,
# pavyzdžiui "Labas, Ieva" (ši eilutė kartotųsi 4 kartus).


# 10.Susikurkite tokį ciklą: for elementas in [88, 65, 21, 26, 47]
# Iš duotų skaičių išveskite visus skaičius, kurie yra lyginiai.

