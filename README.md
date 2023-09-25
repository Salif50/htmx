# htmx
HTMX est un terme qui fait référence à une bibliothèque JavaScript open-source qui permet d'améliorer l'interactivité des sites web en utilisant des technologies web standard telles que HTML, CSS, et JavaScript. Le terme "HTMX" peut être compris comme un jeu de mots qui combine "HTML" (HyperText Markup Language) et "X", qui symbolise l'interaction dynamique et asynchrone, évoquant un moyen d'enrichir l'expérience utilisateur au-delà de la simple utilisation statique d'HTML.

Plus spécifiquement, HTMX permet de mettre à jour des parties spécifiques d'une page web sans recharger complètement la page, en utilisant des requêtes HTTP asynchrones et des éléments HTML dotés d'attributs spéciaux. Cela donne aux développeurs la possibilité de créer des applications web réactives et interactives tout en tirant parti des principes de base du web.

L'objectif d'HTMX est de fournir une manière simple et efficace d'ajouter des fonctionnalités dynamiques aux sites web sans avoir besoin de JavaScript complexe ou de cadres de développement frontaux lourds. Cela permet aux développeurs de maintenir la simplicité et la performance tout en offrant une expérience utilisateur riche et dynamique.

HTMX utilise des attributs HTML spéciaux pour ajouter des fonctionnalités dynamiques aux éléments HTML, permettant d'effectuer des mises à jour du DOM et des requêtes HTTP asynchrones. Voici quelques attributs importants de HTMX :

1. **`hx-get`** :
   L'attribut `hx-get` déclenche une requête HTTP GET vers l'URL spécifiée lorsqu'un événement défini se produit (par exemple, un clic). Les données de la réponse peuvent être insérées dans l'élément spécifié par `hx-target`.

   Exemple :
   ```html
   <button hx-get="/api/data" hx-trigger="click" hx-target="#result">Charger les données</button>
   ```

2. **`hx-post`** :
   L'attribut `hx-post` déclenche une requête HTTP POST vers l'URL spécifiée lorsqu'un événement défini se produit. Les données du formulaire sont envoyées dans le corps de la requête POST.

   Exemple :
   ```html
   <form hx-post="/api/save" hx-trigger="submit" hx-target="#result">
     <!-- Champs du formulaire -->
     <input type="text" name="name" />
     <button type="submit">Enregistrer</button>
   </form>
   ```

3. **`hx-trigger`** :
   L'attribut `hx-trigger` spécifie l'événement qui déclenche la requête HTTP. Il peut être associé à divers événements tels que "click", "submit", "change", etc.

   Exemple :
   ```html
   <button hx-get="/api/data" hx-trigger="click">Charger les données</button>
   ```

4. **`hx-target`** :
   L'attribut `hx-target` spécifie l'élément HTML où les données de la réponse HTTP seront insérées. Vous pouvez utiliser un sélecteur CSS pour cibler un élément spécifique.

   Exemple :
   ```html
   <div hx-get="/api/data" hx-trigger="click" hx-target="#result"></div>
   ```

5. **`hx-params`** :
   L'attribut `hx-params` vous permet d'envoyer des paramètres supplémentaires avec votre requête HTMX. Vous pouvez spécifier les paramètres sous forme de dictionnaire JSON.

   Exemple :
   ```html
   <button hx-get="/api/data" hx-trigger="click" hx-params="{'param1': 'value1'}">Charger les données</button>
   ```

6. **`hx-swap`** :
   L'attribut `hx-swap` spécifie comment le contenu de l'élément cible (`hx-target`) doit être mis à jour après la requête. Par exemple, `"outerHTML"` remplace tout le contenu de l'élément.

   Exemple :
   ```html
   <div hx-get="/api/data" hx-trigger="click" hx-target="#result" hx-swap="outerHTML">Initial Content</div>
   ```

Ces attributs sont essentiels pour définir le comportement des requêtes HTMX et pour mettre à jour dynamiquement le contenu des pages web sans recharger complètement la page.
