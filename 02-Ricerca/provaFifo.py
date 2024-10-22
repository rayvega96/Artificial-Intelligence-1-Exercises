from ResearchTree import CodaFIFO, CodaLIFO

coda_fifo = CodaFIFO()

coda_fifo.insert(1)
coda_fifo.insert(2)
coda_fifo.insert(3)

coda_lifo = CodaLIFO()

coda_lifo.insert(1)
coda_lifo.insert(2)
coda_lifo.insert(3)


coda_lifo.print()

coda_lifo.pop()

coda_lifo.print()

coda_lifo.pop()

coda_lifo.print()

coda_lifo.pop()

coda_lifo.print()
