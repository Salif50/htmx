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


7. **`hx-confirm`** :
   L'attribut `hx-confirm` permet de demander une confirmation de l'utilisateur avant d'effectuer une action. Il affiche une boîte de dialogue de confirmation basée sur le navigateur.

   Exemple :
   ```html
   <button hx-post="/api/delete" hx-trigger="click" hx-confirm="Êtes-vous sûr de vouloir supprimer ?">Supprimer</button>
   ```

8. **`hx-boost`** :
   L'attribut `hx-boost` permet de définir des options de performance pour les requêtes HTMX. Il peut être utilisé pour spécifier le prefetching, le prerendering et d'autres améliorations de performances.

   Exemple :
   ```html
   <div hx-get="/api/data" hx-trigger="click" hx-boost="true"></div>
   ```

9. **`hx-headers`** :
   L'attribut `hx-headers` vous permet d'ajouter des en-têtes personnalisés à votre requête HTTP.

   Exemple :
   ```html
   <button hx-get="/api/data" hx-trigger="click" hx-headers="{'Authorization': 'Bearer myToken'}">Charger les données</button>
   ```

10. **`hx-indicator`** :
    L'attribut `hx-indicator` permet d'afficher un indicateur de chargement pendant la requête HTMX.

    Exemple :
    ```html
    <button hx-get="/api/data" hx-trigger="click" hx-indicator="loading...">Charger les données</button>
    ```

11. **`hx-prompt`** :
    L'attribut `hx-prompt` permet de demander une saisie de l'utilisateur avant d'effectuer une action.

    Exemple :
    ```html
    <button hx-post="/api/update" hx-trigger="click" hx-prompt="Nouvelle valeur :">Mettre à jour</button>
    ```

12. **`hx-select`** :
    L'attribut `hx-select` permet de définir un sélecteur CSS pour cibler un élément spécifique pour la mise à jour après la requête HTMX.

    Exemple :
    ```html
    <button hx-get="/api/data" hx-trigger="click" hx-target="#result" hx-select=".data-item"></button>
    ```

13. **`hx-preserve`** :
    L'attribut `hx-preserve` permet de conserver les données du formulaire lors d'un échec de soumission.

    Exemple :
    ```html
    <form hx-post="/api/save" hx-trigger="submit" hx-target="#result" hx-preserve="true">
      <!-- Champs du formulaire -->
      <input type="text" name="name" />
      <button type="submit">Enregistrer</button>
    </form>
    ```

Ces attributs ajoutent des fonctionnalités et un comportement spécifique aux requêtes HTMX, ce qui permet une plus grande flexibilité dans la manière dont vous concevez et gérez les interactions de votre site web. Il est important de choisir les attributs appropriés en fonction des besoins de votre application.

Ces attributs sont essentiels pour définir le comportement des requêtes HTMX et pour mettre à jour dynamiquement le contenu des pages web sans recharger complètement la page.

# Exemple avec CRUD

1. **Modèle pour l'article** :

```python
# models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
```

2. **Formulaire pour l'article** :

```python
# forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
```

3. **Vues pour gérer les articles** :

```python
# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleForm

class ArticleListView(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'article_list.html', {'articles': articles})

class ArticleDetailView(View):
    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        return JsonResponse({'title': article.title, 'content': article.content})

class ArticleCreateView(View):
    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Article ajouté avec succès!'}, status=201)
        else:
            return JsonResponse({'error': 'Erreur de validation'}, status=400)

class ArticleUpdateView(View):
    def patch(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Article mis à jour avec succès!'})
        else:
            return JsonResponse({'error': 'Erreur de validation'}, status=400)

class ArticleDeleteView(View):
    def delete(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return JsonResponse({'message': 'Article supprimé avec succès!'})
```

4. **URLs pour les vues** :

```python
# urls.py

from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('add/', ArticleCreateView.as_view(), name='article_add'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
]
```

5. **Templates pour les vues** :

- `article_list.html` :

```html
<!-- article_list.html -->

<h1>Liste des Articles</h1>

<ul>
  {% for article in articles %}
    <li>{{ article.title }} - <button hx-get="{% url 'article_detail' article.id %}" hx-trigger="click" hx-target="#article-detail" hx-swap="outerHTML">Voir détails</button></li>
  {% endfor %}
</ul>

<div id="article-detail">
  <!-- Les détails de l'article seront chargés ici -->
</div>
```

- `article_detail.html` :

```html
<!-- article_detail.html -->

<h1>Détails de l'Article</h1>

<h2>{{ title }}</h2>
<p>{{ content }}</p>

<button hx-get="{% url 'article_list' %}" hx-trigger="click" hx-target="#article-list" hx-swap="outerHTML">Retour à la liste</button>
```

- `article_form.html` (utilisé pour l'ajout et la mise à jour d'articles) :

```html
<!-- article_form.html -->

<h1>{% if article.id %}Modifier{% else %}Ajouter{% endif %} un Article</h1>

<form {% if article.id %}hx-patch="{% url 'article_update' article.id %}"{% else %}hx-post="{% url 'article_add' %}"{% endif %} hx-trigger="submit" hx-target="#article-list" hx-swap="outerHTML">
  {% csrf_token %}
  <label for="title">Titre :</label>
  <input type="text" id="title" name="title" value="{{ article.title }}" required><br>
  <label for="content">Contenu :</label>
  <textarea id="content" name="content" required>{{ article.content }}</textarea><br>
  <button type="submit">{% if article.id %}Mettre à jour{% else %}Ajouter{% endif %} l'article</button>
</form>
```

Avec ces éléments, vous avez la structure de base pour gérer les articles avec les fonctionnalités d'ajout, de modification, de suppression et de listing en utilisant HTMX. Vous pouvez personnaliser davantage les templates et les vues en fonction de vos besoins spécifiques.
