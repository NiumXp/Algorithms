# Busca binária
Ela parte do pressuposto de que o vetor está ordenado e realiza sucessivas divisões do espaço de busca comparando o elemento buscado (chave) com o elemento no meio do vetor. Se o elemento do meio do vetor for a chave, a busca termina com sucesso. Caso contrário, se o elemento do meio vier antes do elemento buscado, então a busca continua na metade posterior do vetor. E finalmente, se o elemento do meio vier depois da chave, a busca continua na metade anterior do vetor.

## Como eu entendi
Entendi que o vetor deve estar ordenado de forma crescente para que o algoritmo possa ser usado.

Que a ideia do algoritmo é pegar o item no meio do vetor e verificar se o item é menor ou maior do que o elemento que está sendo buscado, se for menor, os itens à esquerda do item central são ignorados, caso seja maior, os itens à direita são ignorados, caso nenhum desses casos seja verdadeiro, significa que o item central é igual ao elemento que está sendo buscado.

A ideia que eu tive é, criar dois pivôs (`start` e `end`) para que eu "crie uma cópia do vetor" e olhe o item que está no centro destes pivôs utilizando esta expressão `(start + end) // 2`, mas, caso a quantidade de items seja par, não haverá um item no centro, mas terá dois, então ele irá pegar o segundo item, exemplo:
```py
lista = [1, 3, 5, 6]
# Podemos afirmar que essa lista possuí uma quantidade par de items,
# logo, essa sequência não tem um item que fique exatamente no meio, mas
# dois items (que são `3` e `5`), então devemos escolher um lado para
# usar em todo o programa, no meu caso, eu escolhi a direita (`3`).
# Para que eu possa definir um valor *default* no paramêtro quando eu
# criar a função e não ter que decrementar 1 do tamanho do vetor - que
# será o valor *default*.

# Demonstração:
start = 0
end   = len(lista)

middle_index = (start + end) // 2
# Lembrando que o operador `//` é de divisão inteira e é ele quem pega o
# indíce do item no centro do vetor.
#
# Usando a lista [1, 3, 5, 6] e `start` como `0` e `end` como `4`, temos
# o indíce do meio `2` pois `(0 + 4) // 2 = 2`.
```
Agora a ideia é fazer com que quando o item no centro de `start` e `end` seja menor ou maior que o elemento buscado, `start` e `end` sejam modificados para que o item no centro seja outro, mas antes, é necessário fazer duas verificações:

- Se o item no centro entre o pivôs é igual ao item buscado;
- Se os pivôs são iguais.

Se algum desses casos for verdadeiro, a função acaba, caso isso não aconteça, devemos continuar a função com o seguinte caso:

- Se o item no centro for menor que o item procurado, `start` deve ser incrementado em um, se não, `end` deve ser decrementado em um.

Depois disso é só repetir o processo!

# O que eu usei para aprender?
https://www.techiedelight.com/binary-search/
https://pt.wikipedia.org/wiki/Pesquisa_binária#:~:text=A%20pesquisa%20ou%20busca%20binária,paradigma%20de%20divisão%20e%20conquista.