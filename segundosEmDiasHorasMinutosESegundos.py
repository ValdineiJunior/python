quantidadeDeSegundosString = input("qual a quantidade de sugundos que deseja calcular: ")

quantidadeDeSegundos = int(quantidadeDeSegundosString)

dias = quantidadeDeSegundos // 86400
restanteHoras = quantidadeDeSegundos % 86400
horas = restanteHoras // 3600
restanteMinutos = restanteHoras % 3600
minutos = restanteMinutos // 60
segundos = restanteMinutos % 60

print(dias,"dias",horas,"horas",minutos,"minutos",segundos,"segundos")
