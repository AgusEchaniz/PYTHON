def es_primo(num):
	if num < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
		return False
	for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos
		if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
			return False
	return True    #de lo contrario devuelve Verdadero

word = input('Ingrese una palabra: ') #PARA SACAR TODAS LAS LETRAS PRIMAS
counts = {}
primeLetters = []

for letter in set(word):
	count = word.count(letter)
	print (count)
	counts[letter] = count
	if es_primo(count):
		primeLetters.append(letter)

print(primeLetters)



