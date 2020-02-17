// trie n'importe quel tableau en utilisant une boucle for
// après avoir résumé le résultat sera [9,8,7,6,5,4,3,2,1,0]

var tab = [5,0,9,1,7,4,2,6,3,8];

// résultat 5,0,9,1,7,4,2,6,3,8

// conseil - utilisez une VARIABLE temporaire
for (i = 0; i < tab.length; i ++){
	for (j = 0; j < tab.length; j ++){
		if (tab[i] > tab[j]){
			var c = tab[i];
			tab[i] = tab[j];
			tab[j] = c;
		}
    }
    console.log(tab);
}
// indice # 2 - utilisez 2 boucles

// alert (arr.toString ());
// résultat - 9,8,7,6,5,4,3,2,1,0