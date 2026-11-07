from carro import Carro

murcielago = Carro("Lamborghini", "Murcielago", 2005)
impala = Carro("Chevrolet", "Impala", 1967)
kia = Carro("Kia", "K3", 2026)

murcielago.encenderCarro()
murcielago.acelerar(5)
murcielago.mostrarEstado()

impala.encenderCarro()
impala.acelerar(1)
impala.mostrarEstado()

kia.encenderCarro()
kia.acelerar(10)
kia.mostrarEstado()