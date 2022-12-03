def stevilo_ovir(ovire):
    return len(ovire)

def dolzina_ovir(ovire):
    return sum([x1 - x0 + 1 for x0, x1, _ in ovire])

def sirina(ovire):
    return max(ovire)[1]

def dodaj_vrstico(bloki, y):
    return [(x0, x1, y) for x0, x1 in bloki]

def globina(ovire, x):
    return [int(str([min([y if x0 <= x <= x1 else 1000 for x0, x1, y in ovire])])[1:-1])
            if int(str([min([y if x0 <= x <= x1 else 1000 for x0, x1, y in ovire])])[1:-1]) != 1000 else None][0]

def senca(ovire):
    return [True if globina(ovire, x) == None else False for x in range(1, sirina(ovire) + 1)]

#dodatna

def indeksi(s, subs):
    return [i for i in range(len(s)) if str(s[i:i+len(subs)]) == subs]

def pretvori_vrstico(vrstica):
    return [([i for i in range(len("." + vrstica + ".") - 1)
              if ("." + vrstica + ".")[i] == "#" and ("." + vrstica + ".")[i - 1] == "."][i],
            [i for i in range(len("." + vrstica + ".") - 1)
             if ("." + vrstica + ".")[i] == "#" and ("." + vrstica + ".")[i + 1] == "."][i])
            for i in range(len([i for i in range(len("." + vrstica + ".") - 1)
              if ("." + vrstica + ".")[i] == "#" and ("." + vrstica + ".")[i - 1] == "."]))]