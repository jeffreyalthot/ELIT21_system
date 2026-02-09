# Démarrage du développement : plateforme unifiée (25 modules)

## Objectif
Poser le socle technique pour une plateforme unique qui regroupe les 25 programmes listés dans le guide.
Ce socle fournit :
- un **registre de modules** (catalogue),
- un **bus d'événements** (communication interne),
- un **bootstrap** minimal (initialisation).

## Structure proposée
```
/unified_platform
  __init__.py        # exports principaux
  bus.py             # EventBus (publish/subscribe)
  registry.py        # ModuleRegistry (catalogue)
  modules.py         # liste des 25 modules
  bootstrap.py       # assemblage minimal
```

## Prochaine étape recommandée
1. Définir le **format des événements** (ex: "lead.created", "report.generated").
2. Ajouter un **port d'API** (ex: FastAPI) pour exposer le catalogue et lancer des jobs.
3. Brancher 2-3 modules prioritaires pour un MVP.
