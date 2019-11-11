/*
HTML focus on THE TEXT
CSS focus on THE STYLE
JS focus on THE ACTION


document is an OBJECT.
document is the webpage.
window is an object with many propreties (one of them is DOCUMENT)

window.write("hello there"); NOT WORK !!
cause write is a proprety of DOCUMENT and not of window.
we use : document.write("hello there");
but we can also use window.document.write("hello there");
cause window is a parent of document that is a parent of write...
*/

 
DOM SELECTORS
---------------
getElementByTagName
getElementNyClassName
getElementbyId

querySelector
querySelectorAll

getAttribute
setAttribute

##CHANGING STYLES >
style.{property} //ok

className //best
classList //best

classList.add
classList.remove
classList.toggle //annuler = crtl z en gros.

##BONUS >
innerHTML //DANGEROUS

createElement

parentElement
children

##It is Important to CACHE selectors in variables >

dans le cas d'un ARRAY, acceder à UN SEUL element en partictulier:
document.getElementBy....("")[0]
ajouter les crochets à la fin avec la position de l'element que
l'on souhaite.

Mieux que getElementBy il y a querySelector !!
si on fait document.querySelector("li");
cela selectionnera LE PREMIER LI à partir du debut du code.
pour selectionner TOUS les LI il faudra :
document.querySelectorAll("li");
Si je veux selectionner TOUS les Elements de PLUSIEURS TYPES :
PAREIL > document.querySelectorAll("h1, li");

Pour utiliser getAttribute, il faut selectionner le type avant :
soit en deux etapes :
document.querySelector("li");
puis
getAttribute("random");

soit UNE ETAPE (mieux) :
document.querySelector("li").getAttribute("random");

apres selection : pour MODIFIER cet attribut : SetAttribute:
document.querySelector("li").setAttribute("random", "1000");
undefined (le resultat sera ecrit undefined mais en fait :)
on tape malgré tout document.querySelector("li").getAttribute("random", "1000");
cela affichera 1000 !!

pour modifier le style, le css :
document.querySelector("h1") //on selectionne ce qu'on veut modifier
document.querySelector("h1").style; //optionnel pour afficher nos
differenttes possibilités de changement...
document.querySelector("h1").style.background = "yellow";
//cela a changé le css, le backgroung en jaune, ATTENTION avec 
GUILLEMETS (cest un String).
LA FAÇON CI DESSUS EST ACCEPTABLE MAIS PAS LA MEILLEURE !!!
voir ci dessous :
nous avons fait ou copié un css magnifique pour notre titre
sous le nom d'une class .cooltitle !
ajoutons cette classe à notre h1 dans le html (par JS pas manuel!)
et voyons :
var h1 = document.querySelector("h1"); //declarer dans une variable
undefined (sera la reponse alors juste faites h1 et entrer):
h1
<h1>​…​</h1>​"My Best Champions"<br>​"in League Of Legends"</h1>​
h1.className = "cooltitle"; //ajouter la class au h1
"cooltitle" //effet activé via ajout class cooltitle au h1

pour enelever REMOVE :
document.querySelector("ul").classList.add("cooltitle")
undefined (OSEF)
document.querySelector("ul").classList.remove("cooltitle")
undefined (OSEF)

nous allons barrer les item de la liste qui n'ont pas de skin
par exemple (skin en rapport avec LoL)
ajoutons notre class css .noskin{text-decoration: line-through;}
document.querySelector("li").classList.add("noskin");
undefined (osef)

nous pouvons retablir comme avant via REMOVE ou 
via TOGGLE (annulation de la commande precedante);
puis RETABLIR l'item barré via TOGGLE car cela annule la 
precedante commande etc...
document.querySelector("li").classList.toggle("noskin");
false
document.querySelector("li").classList.toggle("noskin");
true
LE TOGGLE PEUT AUSSI ETRE AJOUTER POUR DONNER UN EFFET 
ON / OFF EN APPUYANT SUR UN BOUTON PAR EXEMPLE xD héhé :P


innerHTML // MODIFIE CARREMENT LE CONTENU DU HTML !!
par exemple mettons des Points d'Exclamations à 
la place du titre actuel :
document.querySelector("h1") //declarer-selectionner le h1
document.querySelector("h1").innerHTML = "<strong>!!!!!!</strong>";
//et oui on peut carrement ajouter une balise comme strong, em...
document.querySelector("h1") //verification-visioner le html

parentElement :
si on selectionne le 3element de la liste :
document.querySelectorAll("li")[2];
maintenant on veut acceder à son parent :
document.querySelectorAll("li")[2].parentElement;
<ul>...</ul> (la reponse affichée, nous avons accédé au parent de li)

et si on peut le parent du parent ? mdr xD
document.querySelectorAll("li")[2].parentElement.parentElement;
on tombera sur <body>...</body> !!

children :

document.querySelectorAll("body").children;
on aura tous les children du body donc (h1, p, ul...)


createElement :
newHeading.innerHTML = "This is now a new heading"
document.querySelector("body").appendChild(newHeading)
newHeading.style.background = "beige"
"beige"
var body = document.querySelector("body")
undefined (osef)
body.insertBefore(newHeading, document.querySelector("p"));
/*le insertBefore permet de deplace l'element avant un autre,
ici notre newHeading est placé avant "p" (le 1er p du code)*/

IMPORTANT TO CACHE SELECTORS IN VARIABLES :

utiliser toujours ces commandes longues use la memoire....
car elle doit tjrs rechercher dans le dom etc etc...
il vaut mieux stocker nos commandes selector dans des variables :

var h1 = document.querySelector("h1");
