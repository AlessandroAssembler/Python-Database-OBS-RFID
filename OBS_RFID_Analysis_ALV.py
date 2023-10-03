
import time

#Scriviamo il path dove abbiamo salavato i nostri file txt
path = '/Users/alessandroloverde/Library/Mobile Documents/com~apple~CloudDocs/Master Statistical Learning e Data Science/Algorithms and programming in Python and R for Data Science - Proff. Bacci e Marino/Assignment/Assignment Python/OBS_data.txt'
path2 = '/Users/alessandroloverde/Library/Mobile Documents/com~apple~CloudDocs/Master Statistical Learning e Data Science/Algorithms and programming in Python and R for Data Science - Proff. Bacci e Marino/Assignment/Assignment Python/RFID_data.txt'

# La funzione riceve in input la diretory dove si trova il file 
# e crea un dizionario in cui le chiavi sono le intestazioni delle colonne del dataset e
# i valori in ciascuna colonna.

def reading_function(path):
    variabili = {}  # Creiamo un dizionario nel quale immagazzinare le variabili
    with open(path, 'r') as f:
        rows = f.readlines()
        intestazione = rows[0].strip().split('\t')  # Estraiamo l'intestazione
        for i in intestazione:
            variabili[i] = []  # Inizializziamo una lista vuota per immagazzinare le colonne

        for row in rows[1:]:  # Si inizia dalla seconda riga
            data = row.strip().split('\t')
            for j in range(len(intestazione)):
                variabili[intestazione[j]].append(data[j])  # Aggiungiamo i dati alla lista corrispondente

    return variabili

# Usiamo la nostra funzione per leggere i due file
OBS = reading_function(path)
RFID = reading_function(path2)
# Accediamo alle variabili OBS
datetimeOBS = OBS["DateTime"]
actor = OBS["Actor"]
recipient = OBS["Recipient"]
behavior = OBS["Behavior"]
category = OBS["Category"]
duration = OBS["Duration"]
point = OBS["Point"]

# Salviamo le variabili Rfid
t = RFID["t"]
first_i = RFID["i"]
second_j = RFID["j"]
datetimeRFID = RFID["DateTime"]

"""
PARTE A

Usando il file OBS DATA.

Definiamo le funzioni utili per svolgere gli esercizi

"""

# Funzione che conta gli elementi partendo da una lista
def conta_lista(lista1, lista_dacontare=None, doppi=True, conteggio = None):
    # Crea un dizionario per il conteggio
    if conteggio is None:
        conteggio = {}
    # Conta gli elementi nella lista
    if lista_dacontare is None:
        lista_dacontare = [1] * len(lista1)
    # Se doppi è True, conta anche per elementi uguali
    if doppi == True:
        for i in range(len(lista1)):
            if lista1[i] != '':
               conteggio[lista1[i]] = conteggio.get(lista1[i], 0) + int(lista_dacontare[i])
    else:
        for i in range(len(lista1)):
            # Conta ogni singolo elemento nella lista_dacontare
            if lista1[i] != '':
                if lista1[i] in conteggio:
                    conteggio[lista1[i]].add(lista_dacontare[i])
                else:
                    conteggio[lista1[i]] = {lista_dacontare[i]}

    return conteggio

def contare_due_liste(lista1, lista2, lista_dacontare=None, doppi=True, coppia=False):
    # Crea dizionari per il conteggio
    conteggio = {}
    # Conta gli elementi nella lista
    if lista_dacontare is None:
        lista_dacontare = [1] * len(lista1)
    if coppia == True:
        # Conta a coppie
        if doppi == True:
            for i in range(len(lista1)):
                if lista1[i] != '' and lista2[i] != '':
                    couple = tuple(sorted([lista1[i], lista2[i]]))
                    if couple in conteggio:
                      conteggio[couple] += int(lista_dacontare[i])
                    else:
                      conteggio[couple] = int(lista_dacontare[i])
        else:
            for i in range(len(lista1)):
                if lista1[i] != '' and lista2[i] != '':
                    couple = tuple(sorted([lista1[i], lista2[i]]))
                    if couple in conteggio:
                        conteggio[couple].add(lista_dacontare[i])
                    else:
                        conteggio[couple] = {lista_dacontare[i]}
    else:
        # Conta le liste
        if doppi == True:
          conteggio = conta_lista(lista1, lista_dacontare, doppi = True)
          conteggio = conta_lista(lista2, lista_dacontare, doppi = True, conteggio = conteggio)
        else:
          conteggio = conta_lista(lista1, lista_dacontare, doppi = False)
          conteggio = conta_lista(lista2, lista_dacontare, doppi = False, conteggio = conteggio)

    return conteggio
    
# Funzione che restituisce il massimo in frequenza e l'elemento corrispondente partendo da un dizionario conteggio in input
def trova_max(conteggio, doppi=True):
    # Trova l'elemento con il conteggio massimo
    max_freq = 0  # Inizializza il conteggio massimo a 0
    max_elementi = []  # Inizializza la lista 

    if doppi == True:  # Se doppi è True, conta più volte gli elementi uguali
        for elemento, conteggio in conteggio.items():
            if conteggio > max_freq:
                # Se il conteggio corrente è maggiore del conteggio massimo precedente,
                # aggiorna il conteggio massimo e resetta la lista degli elementi massimi.
                max_freq = conteggio
                max_elementi = [elemento]
            elif conteggio == max_freq:
                # Se il conteggio corrente è uguale al conteggio massimo precedente,
                # aggiunge l'elemento alla lista degli elementi massimi.
                max_elementi.append(elemento)
    else:  # Se doppi è False, gestisci gli elementi unici
        for elemento, conteggio in conteggio.items():
            conteggio = len(conteggio)  # Calcola il conteggio come lunghezza dell'elemento corrente
            if conteggio > max_freq:
                # Se il conteggio corrente è maggiore del conteggio massimo precedente,
                # aggiorna il conteggio massimo e resetta la lista degli elementi massimi.
                max_freq = conteggio
                max_elementi = [elemento]
            elif conteggio == max_freq:
                # Gestione potenziali ex aequo
                max_elementi.append(elemento)

    return max_freq, max_elementi  # Restituisce il conteggio massimo e la lista degli elementi massimi

# Funzione che restituisce il massimo in frequenza e l'elemento corrispondente partenda da una lista in input
def most_frequent(list, lista_dacontare=None, doppi=True):
    # Richiama la funzione per contare la lista
    conteggio = conta_lista(list, lista_dacontare, doppi)
    # Richiama la funzione per trovare l'elemento più frequente
    [max_freq, max_elemento] = trova_max(conteggio, doppi)
    
    return max_freq, max_elemento


# Funzione che restituisce il massimo in frequenza e l'elemento corrispondente partenda da due liste in input
def most_frequent_twolists(lista1, lista2, lista_dacontare=None, doppi=True, coppia=False):
    # Richiama la funzione per contare due liste
    conteggio = contare_due_liste(lista1, lista2, lista_dacontare, doppi, coppia)

    # Richiama la funzione per trovare l'elemento più frequente
    max_freq, max_elemento = trova_max(conteggio, doppi)

    return max_freq, max_elemento

"""

1.  Qual è il primate che è stato coinvolto in più eventi sia come "Actor" che come "Recipient"?

"""

start = time.time()
# Trova l'elemento primate che appare più frequentemente come actor e recipient
[max_freq, max_primate] = most_frequent_twolists(actor, recipient)
end = time.time()

# Stampa il risultato
print("1. Il primate che è stato coinvolto più volte sia come actor che come recipient è " 
       + str(max_primate) + " che è stato coinvolto in " + str(max_freq) + " eventi.\n")
print(end-start)
"""

2.   Qual è il primate che è stato coinvolto in più eventi come "Actor"?

"""

start = time.time()
# Trova il primate che appare più frequentemente come Actor
[max_freq, max_primate] = most_frequent(actor)
end = time.time()

# Stampa il risultato
print("2. Il primate che è stato coinvolto più volte come actor è " 
       + str(max_primate) + " che è stato coinvolto in " + str(max_freq) + " eventi.\n")
print(end-start)

"""

3.   Qual è il primate che è stato coinvolto in più eventi come "Recipient"?

"""

start = time.time()
# Trova il primate che appare più frequentemente come Recipient
[max_freq, max_primate] = most_frequent(recipient)
end = time.time()

# Stampa il risultato
print("3. Il primate che è stato coinvolto più volte come recipient è " 
       + str(max_primate) + " che è stato coinvolto in " + str(max_freq) + " eventi.\n")
print(end-start)

"""
4.   Qual è il giorno in cui ci sono stati più eventi?

"""

# Funzione che separa data e ora
def separa_data_ora(lista):
    date = []
    time = []

    for elemento in lista:
        # Separazione data e ora
        data, ora = elemento.split(' ')

        # Aggiunta alla lista delle date
        date.append(data)

        # Aggiunta alla lista delle ore
        time.append(ora)

    return date, time

start = time.time()
[data_OBS, ora_OBS] = separa_data_ora(datetimeOBS)
end = time.time()
print(end-start)

start = time.time()
# Trova il giorno in cui si sono registrati più eventi
[max_freq, max_day] = most_frequent(data_OBS)
end = time.time()

# Stampa il risultato
print("4. Il giorno in cui si sono verificati più eventi è stato il " + str(max_day) + " in cui si sono verificati " 
      + str(max_freq) + " eventi.\n")
print(end-start)

"""

5.   Qual è l'ora del giorno in cui ci sono più eventi?

"""

# Funzione che separa ore e minuti
def separa_ore_minuti(lista):
    hours = []
    minutes = []

    for elemento in lista:
        # Separazione data e ora
        ora, minuto = elemento.split(':')

        # Aggiunta alla lista delle ore
        hours.append(ora)

        # Aggiunta alla lista dei minuti
        minutes.append(minuto)

    return hours, minutes

start = time.time()
[ore_OBS, minuti_OBS] = separa_ore_minuti(ora_OBS)
end = time.time()
print(end-start)

start = time.time()
# Trova l'ora del giorno in cui si sono registrati più eventi
[max_freq, max_hour] = most_frequent(ore_OBS)
end = time.time()

# Stampa il risultato
print("5. L'ora del giorno in cui si sono osservati più eventi sono le " + str(max_hour) + " in cui si sono verificati " 
       + str(max_freq) + " eventi.\n")
print(end-start)

"""

6.   Qual è il tipo di comportamento (Behavior) maggiormente registrato?

"""
start = time.time()
# Trova il tipo di comportamento maggiormente registrato
[max_freq, max_behavior] = most_frequent(behavior)
end = time.time()

# Stampa il risultato
print("6. Il comportamento più frequente è stato " + str(max_behavior) + ", il quale è stato osservato " + str(max_freq) + " volte.\n")
print(end-start)

"""

7.   Qual è la coppia di primati coinvolta insieme in più eventi?


"""
start = time.time()
# Trova la coppia di primati coinvolta in più eventi insieme
[max_freq, max_couple] = most_frequent_twolists(actor, recipient, coppia = True)
end = time.time()

# Stampa il risultato
print("7. La coppia di primati che è stata coinvolta in più eventi è stata " + str(max_couple) + " che è stata coinvolta in " 
       + str(max_freq) + " eventi.\n")
print(end-start)

"""

8.   Qual è il primate che è stato coinvolto più a lungo in eventi sia come "Actor" che come "Recipient"? (contando le durate)

"""

start = time.time()
# Trova il primate che è stato coinvolto più a lungo sia come Actor che come Recipient
[max_freq, max_primate] = most_frequent_twolists(actor, recipient, duration)
end = time.time()

# Stampa il risultato
print("8. Il primate che è stato coinvolto più a lungo sia come actor che come recipient è " 
       + str(max_primate) + " che è stato coinvolto per " + str(max_freq) + " secondi.\n")
print(end-start)

"""

9.   Qual è il primate che è stato coinvolto più a lungo in eventi come "Actor"? (contando le durate)

"""
start = time.time()
# Trova il primate che è stato coinvolto più a lungo come Actor
[max_freq, max_primate] = most_frequent(actor, duration)
end = time.time()

# Stampa il risultato
print("9. Il primate che è stato coinvolto più a lungo come actor è " 
       + str(max_primate) + " che è stato coinvolto per " + str(max_freq) + " secondi.\n")
print(end-start)

"""

10.  Qual è il primate che è stato coinvolto più a lungo in eventi come "Recipient"? (contando le durate)

"""

start = time.time()
# Trova il primate che è stata coinvolto più a lungo come Recipient
[max_freq, max_primate] = most_frequent(recipient, duration)
end = time.time()

# Stampa il risultato
print("10. Il primate che è stato coinvolto più a lungo come recipient è " 
      + str(max_primate) + " che è stato coinvolto per " + str(max_freq) + " secondi.\n")
print(end-start)

"""

11.  Qual è la coppia di primati coinvolta insieme più a lungo (in più eventi contando le durate)?

"""
start = time.time()
# Trova la coppia di primati coinvolta in eventi con duration cumulata più grande
[max_freq, max_couple] = most_frequent_twolists(actor, recipient, duration, coppia = True)
end = time.time()

# Stampa il risultato
print("11. La coppia di primati che è stata coinvolta in più eventi è stata " + str(max_couple) 
      + " che è stata coinvolta in " + str(max_freq) + " eventi.\n")
print(end-start)

"""

12.  Qual è il primate con più comportamenti diversi? Se A è coinvolto due volte nel comportamento "Playing with", questo conta una sola volta.

"""
start = time.time()
# Trova il primate con più comportamenti diversi
[max_freq, max_primate] = most_frequent(actor, behavior, doppi = False)
end = time.time()

# Stampa il risultato
print("12. Il primate con più comportamenti diversi osservati è stato " + str(max_primate)
      + " il quale ha mostrato " + str(max_freq) + " comportamenti diversi.\n")
print(end-start)

"""

13.  Qual è la coppia di primati coinvolta insieme in più eventi diversi? Se A e B sono coinvolti due volte nel comportamento "Playing with", questo conta una sola volta

"""

start = time.time()
# Trova la coppia di primati coinvolta insieme in più eventi diversi
[max_freq, max_couple] = most_frequent_twolists(actor, recipient, behavior, doppi = False, coppia = True)
end = time.time()

# Stampa il risultato
print("13. La coppia di primati che è stata coinvolta in più comportamenti diversi è stata " + str(max_couple) 
      + " che è stata coinvolta in " + str(max_freq) + " comportamenti diversi.\n")
print(end-start)

"""

14.  Qual è il giorno con più comportamenti diversi? Se in un giorno compare due volte il comportamento "Playing with", questo conta una sola volta.

"""

start = time.time()
# Trova il giorno in cui si sono osservati più comportamenti diversi
[max_freq, max_day] = most_frequent(data_OBS, behavior, doppi = False)
end = time.time()

# Stampa il risultato
print("14. I giorni in cui si sono verificati più comportamenti diversi sono stati il " + str(max_day) + " in cui si sono osservati " 
      + str(max_freq) + " comportamenti diversi.\n")
print(end-start)




"""
PARTE B
Usando il file RFID DATA

1. Qual è la coppia di primati coinvolta insieme in più interazioni?

"""

start = time.time()
# Trova la coppia di primati coinvolta insieme in più interazioni
[max_freq, max_couple] = most_frequent_twolists(first_i, second_j, coppia = True)
end = time.time()

# Stampa il risultato
print("2.1 La coppia di primati che è stata coinvolta in più interazioni è stata " + str(max_couple) 
       + " che è stata coinvolta in " + str(max_freq) + " interazioni.\n")
print(end-start)
"""

2. Qual è il primate coinvolto in più interazioni?


"""

start = time.time()
# Trova l'elemento primate che è coinvolto in più interazioni
[max_freq, max_primate] = most_frequent_twolists(first_i, second_j)
end = time.time()

# Stampa il risultato
print("2.2 Il primate che è stato coinvolto in più interazioni è " 
      + str(max_primate) + " che è stato coinvolto in " + str(max_freq) + " interazioni.\n")
print(end-start)
"""
3. Qual è il primate che ha interazioni in più giorni? Se in un giorno ha più 
interazioni, il giorno conta uno.

"""

start = time.time()
# Separa la lista Datetime in data e ora
[data_RFID, ora_RFID] = separa_data_ora(datetimeRFID)
end = time.time()

# Trova il primate che è stato coinvolto più a lungo sia come Actor che come Recipient
[max_freq, max_primate] = most_frequent_twolists(first_i, second_j, data_RFID, doppi = False)


# Stampa il risultato
print("2.3 I primati che hanno avuto più interazioni in più giorni diversi sono " 
       + str(max_primate) + " che sono stati coinvolti per " + str(max_freq) + " giorni.\n")
print(end-start)
"""

4.  Qual è la coppia di primati che ha interazioni in più giorni? Se in un giorno hanno più interazioni, il giorno conta uno.

"""

start = time.time()
# Trova la coppia di primati coinvolta insieme in più eventi diversi
[max_freq, max_couple] = most_frequent_twolists(first_i, second_j, data_RFID, doppi = False, coppia = True)
end = time.time()

# Stampa il risultato
print("2.4 Le coppie di primati che hanno avuto interazioni in più giorni diversi sono state " + str(max_couple) 
      + " che sono state coinvolte in " + str(max_freq) + " giorni diversi. \n")
print(end-start)
"""

5. Qual è il giorno con più interazioni?
"""

start = time.time()
# Trova il giorno in cui si sono registrati più eventi
[max_freq, max_day] = most_frequent(data_RFID)
end = time.time()

# Stampa il risultato
print("2.5 Il giorno in cui si sono verificate più interazioni è stato il " + str(max_day) + " in cui si sono verificate " 
      + str(max_freq) + " interazioni.")
print(end-start)