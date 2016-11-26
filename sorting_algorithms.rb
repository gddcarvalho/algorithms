#!/bin/ruby
#Insertion sort algorithm
#Efficient for small number of elements @Cormen

array = [5,6,2,3,8]

for j in 1..(array.length - 1)
	key = array[j]
	i=j-1
	while i >= 0 && array[i] > key
		array[i+1] = array[i]
		i=i-1
	end
	array[i+1]=key
end

#Bubble sort algorithm
#Compara-se o primeiro elemento do conjunto com o segundo e 
#se a ordem não for a desejada, troca-se os dois entre sí

array = [5,6,2,3,8]
k = 0

while k == 0
	k = 1
	for i in 0...(array.length - 1) #i until 5
		if (array[i] > array[i+1])
			aux = array[i]
			array[i] = array[i+1]
			array[i+1] = aux
			k = 0
		end
	end
end

#puts array

#Selection sort algorithm
#Consiste em achar o maior elemento do conjunto e trocá-lo com a ultima posição.
#Em seguida acha-se o maior do conjunto restante e troca-se com a penultima posição...

array = [15, 7, 1, 4 ,18]

for i in 0..(array.length - 1)#0 until 5
	min = i
(i+1).upto(array.length - 1) do |j|
	min = j if array[j] < array[min]
end
	if (min != i)
		aux = array[i]
		array[i] = array[min]
		array[min] = aux
	end
end

puts array
