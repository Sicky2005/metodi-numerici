"""
    Autore: Sicky2005
    Corso: Metodi Numerici per l'Ingegneria
    Descrizione: Programma per il Metodo dei Trapezi
"""

def trap_rule(func, a, b, n):
    """
    func: La funzione da integrare
    a: Inizio dell'intervallo
    b: Fine dell'intervallo
    n: Numero di intervalli
    """
    # Calcolo del passo (h)
    h = (b - a) / n

    # Valutazione estremi (f(a) + f(b))
    somma = func(a) + func(b)

    # Sommatoria dei punti interni moltiplicati per 2
    for i in range(1, n):
        x = a + i * h
        somma += 2 * func(x)

    # Calcolo finale
    return (h / 2) * somma