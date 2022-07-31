 #Lembre de incluir um método para criptografar e um para descriptografar
 #- Cifra de troca simples
   #- Realize as seguintes trocas: E por 3, A por 4, S por 5
 #- Cifra de troca numérica
   #- Cada letra da mensagem deve ser trocada pela sua posição no alfabeto (por exemplo A deve ser 1, B deve ser 2...)
   #- Para ser possível descriptografar a mensagem depois a sugestão é fazer com que cada letra criptografada fique separada da seguinte por um espaço ou por um hífen. (Ex: ASA viraria 1-19-1 ao invés de 1191)
 #- Cifra de César
   #- Cada letra da mensagem deve ser deslocada um número N de posições no alfabeto. Para isso considere que o alfabeto é cíclico, ou seja, depois de Z a próxima letra é A novamente. Elementos não-alfabéticos (números, pontuações, espaços) devem permanecer inalterados.
   #- Para fins de implementação considere que o métodos devem receber como entrada um número N e uma string msg. A função deve retornar a string criptografada ou descriptografada
 #- DESAFIO: Cifra por palavra-chave (Cifra de Vigenère)
   #- Atenção, este desafio é BEM DESAFIADOR. Só se arrisque aqui depois que estiver confortável com as outras etapas.
   #- Como a explicação é longa, vamos adicionar um elemento de dificuldade e deixar um link com a explicação