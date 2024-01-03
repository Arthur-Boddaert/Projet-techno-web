# Projet-techno-web

## Description du projet
Pour le rendu de technologie du web je pensais utiliser l'un de mes projets réalisés lors du M1.
Le but de ce projet était dans un premier temps de définir un pattern prosite à partir de séquences protéiques alignées, pour ensuite utiliser ce pattern afin de vérifier si une nouvelle séquence contient le pattern.

Mon idée est donc de réutiliser mes scripts pour les lancer avec des fichiers qui seront demandés sur la page web, pour ensuite afficher les sorties des scripts ainsi que des informations et ou des statistiques sur les séquences. La dernière partie me permet d'ajouter des tableaux.

Pour faire cela j'ai commencer à me renseigner Django.

## Structure du site

Le site est composé de 5 pages html. La page d'accueil contient des informations sur le projet, le fonctionnement des
scripts et des pistes d'améliorations de ces derniers. Un menu permet d’accéder aux autres pages (la structure html 
et css dernière ce menu ont été trouver sur ce lien : https://www.eprojet.fr/cours/html_css/15-html_css-menu-de-navigation).

En accédant à l’application, nous arrivons sur la page contenant le formulaire à compléter pour pouvoir lancer 
le programme, dont les résultats sont affichés sur une autre page. Les pages html et python dernières le formulaire 
ont été réalisés en suivant la documentation de django (https://docs.djangoproject.com/fr/5.0/topics/forms/). 

La page "Guide d'utilisation" contient les informations sur les paramètres du formulaire et la manière de lancer le 
programme en ligne de commande.

Les deux derniers liens renvoient pour le premier vers la page git contenant mes scripts du projet (pour ne pas recréer 
un git juste pour le fichier compressé le lien renvoie vers ce fichier mais pour le git du rendu de technologie du web).

Le dernier lien “Information sur le projet initial” renvoie vers une copie de la page html des consignes pour le projet 
du M1 (https://www.fil.univ-lille.fr/%7Evarre/portail/poo-miso/projet2-2022.html). Pour cette page le CSS est directement 
intégré dans le fichier html, le fichier est le même que le fichier original avec quelques modifications, notamment un 
lien vers la page d'accueil en haut de la page.

Appart ce qui est issu des trois liens au-dessus, j’ai également utilisé la documentation django 
(https://docs.djangoproject.com/fr/5.0/) pour la structure du projet mais sinon le reste du code n’est pas 
issu de source externe.

## Amélioration

Certaines choses sont à améliorer dans ce projet :
- Les adresses des liens sont directement écrits dans le fichier html, cela peut poser des problèmes 
si les liens changent dans le futur.
- Les scripts initiaux n’ont pas été prévu pour un usage par un site web, certaines fonctionnalités 
devrait donc être réécrite pour une meilleure utilisation.
- La page des résultats pourra être approfondie pour contenir plus d’informations et / ou des informations plus pertinentes.
