# Qu'est ce qu'HTTP
C'est un protocole de communication utilisé sur internet pour permettre à un client (souvent un navigateur web ou une application) 
de demander des ressources (pages web, images, données,...) à un serveur.

# Qu'est ce qu'HTTPS
C'est la version sécurisé de HTTP. Ce protocole ajoute une couche de chiffrement ssl/tls. Les données échangées entre le navigateur 
et le serveur web sont cryptées.

# Comment un requête HTTP fonctionne?
1. On tape une adresse (ex: example.com) dans un navigateur
2. le navigateur envoie une requête HTTP
3. il l'envoie au serveur web distant
4. le serveur lit la requête et traite la demander
5. il renvoie une réponse HTTP avec la page demandée ou une erreur

Exemple de requête envoyé par le navigateur:
```
GET /index.html HTTP/1.1         # Méthode GET, demande la ressource "/index.html" via HTTP version 1.1
Host: www.example.com            # Nom du serveur (obligatoire avec HTTP/1.1 pour identifier le site)
User-Agent: Mozilla/5.0          # Infos sur le navigateur ou l'application qui fait la requête
Accept: text/html                # Type de contenu souhaité en réponse (ici : HTML)
```
Exemple de réponse du serveur:
```
HTTP/1.1 200 OK                  # Version HTTP, code de statut 200 (OK = succès), avec un message "OK"
Content-Type: text/html; charset=UTF-8  # Type de contenu retourné (HTML avec encodage UTF-8)
Content-Length: 1024            # Taille du contenu en octets

<html>                          # Début du corps HTML (la vraie réponse visible par l'utilisateur)
  <body>Hello!</body>           # Contenu principal de la page
</html>
```
# Les méthodes HTTP
Elles indiquent au serveur ce que le client veut faire.

|Méthodes    |Description                               |Exemples pratiques             |
|:------------|:---------------------------|:----------------------------|
|GET          |Récupérer une ressource    |Lire une page web              |
|POST         |Envoyer des données pour création|Soumettre un formulaire|
|pratiques    |Remplacer une ressource existante|Mettre à jour un article|
|PATCH         |Modifier partiellement une ressource|Changer juste le titre d'un article|
|DELETE        |Supprimer une ressource            |Supprimer un commentaire|

# Les codes de statut HTTP
Après chaque requête le serveur renvoie un code de statut pour indiquer ce qu'il s'est passé.
Le code a toujours 3 chiffres.
    * 1xx : information
    * 2xx : succés
    * 3xx : redirection
    * 4xx : erreur côté client 
    * 5xx : erreur côté serveur

Les plus courants:
|Code       |Nom        |Signification      |
|----------|-------------------|-------------------------|
|200        |ok                 |tout s'est bien passé |
|201        |Created                 |Une ressource a été créée |
|400        |Bad Request                 |Mauvaise syntaxe ou champ manquant |
|401        |Unauthorized                 |Connexion requise |
|401        |Unauthorized                 |Connexion requise |
|404       |Not Found                 |Page ou ressource introuvable |
|500        |Internal Server Error                 |Le serveur a planté |