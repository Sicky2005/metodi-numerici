"""
    Autore: Sicky2005
    Corso: Metodi Numerici per l'Ingegneria
    Descrizione: Programma per il Metodo di Gauss-Seidel con Fattore di Rilassamento
"""

def gseid(a, b, n, x, max_iter, tol, lam):
    """
    a        : Matrice dei coefficienti (lista di liste n x n)
    b        : Vettore dei termini noti (lista di dimensione n)
    n        : Numero di equazioni/incognite
    x        : Vettore per la stima iniziale (viene aggiornato con la soluzione)
    max_iter : Numero massimo di iterazioni consentite
    tol      : Tolleranza per l'errore percentuale (criterio di arresto)
    lam      : Fattore di rilassamento (lambda)
    """
    # Normalizzazione delle righe
    # Divide ogni riga per l'elemento diagonale affinché a[i][i] diventi 1.
    for i in range(n):
        dummy = a[i][i]
        for j in range(n):
            a[i][j] = a[i][j] / dummy
        b[i] = b[i] / dummy

    # Stima iniziale
    # Prima passata per calcolare un valore iniziale migliore per x
    for i in range(n):
        somma = b[i]
        for j in range(n):
            if i != j:
                somma = somma - a[i][j] * x[j]
        x[i] = somma

    # Ciclo iterativo principale
    iter_count = 1

    while True:
        sentinel = 1  # Flag "ottimista": assume convergenza (1). Se un errore > tol, diventa 0 per continuare.

        for i in range(n):
            old = x[i]  # Memorizza il vecchio valore di x[i]
            somma = b[i]

            for j in range(n):
                if i != j:
                    somma = somma - a[i][j] * x[j]

            # Applica la formula SOR (Rilassamento)
            # x_nuovo = lambda * calcolato + (1 - lambda) * vecchio
            x[i] = lam * somma + (1.0 - lam) * old

            # Controllo dell'errore
            # Calcoliamo l'errore solo se sentinel è ancora 1 e x[i] non è zero
            if sentinel == 1 and x[i] != 0:
                ea = abs((x[i] - old) / x[i]) * 100
                if ea > tol:
                    sentinel = 0  # L'errore è troppo alto, continuiamo a iterare

        iter_count += 1

        # Condizione di uscita:
        # Se sentinel è rimasto 1 (errore sotto la soglia per tutti)
        # OPPURE abbiamo raggiunto il massimo delle iterazioni.
        if sentinel == 1 or iter_count >= max_iter:
            break

    return x, iter_count