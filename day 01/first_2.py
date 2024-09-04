 #one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".you now need to find the real first and last digit on each line
mio_dict = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
# with open('input_a.txt') as file:
#     for l in file.readlines():


t = "Ciao, mi chiamo Valentina e mia madre mi mena"
idx = t.find("Valentina")
print(idx)

sum=0
with open('input_a.txt') as file:
    for l in file.readlines():
        l = l.strip()
        # Inizio ad analizzare le righe una alla volta
        print(f"** {l}")
        last_n=""
        last_pos=-1
        # Cerchiamo prima i numeri all'interno della stringa
        for k in mio_dict:
            idx = l.find(k)
            if last_pos == -1 or (last_pos > idx) and idx != -1:
                last_n = mio_dict[k]
                last_pos = idx
        for n in range(1, 10):
            n = str(n)
            idx = l.find(n)
            if last_pos == -1 or (last_pos > idx and idx != -1):
                last_n = n
                last_pos = idx
        first_n = last_n

        last_n = ""
        last_pos=-1
        # Dobbiamo fare lo stesso, ma invertendo il ragionamento
        for k in mio_dict:
            idx = l.rfind(k)
            if last_pos < idx:
                last_n = mio_dict[k]
                last_pos = idx
                print(f"{idx} e n: {n}")
        print(last_n)
        for n in range(1, 10):
            n = str(n)
            idx = l.rfind(n)
            if last_pos < idx:
                print(f"{idx} e n: {n}")
                last_n = n
                last_pos = idx
        print(last_n)

        # Creiamo il numero a due cifre
        # first_n si trova la prima cifra
        # last_n si trova la seconda cifra
        n = int(first_n) * 10 + int(last_n)
        print(f"Numero contenuto: {n}")
        sum += n

print("La somma totale è " + str(sum))
            
