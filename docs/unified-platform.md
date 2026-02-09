# Démarrage du développement : plateforme unifiée (15 modules)

## Objectif
Poser le socle technique pour une plateforme unique qui regroupe 15 programmes unifiés (MVP).
Ce socle fournit :
- un **registre de modules** (catalogue),
- un **bus d'événements** (communication interne),
- un **bus de commandes** (orchestration),
- un **bootstrap** minimal (initialisation),
- une **gestion d'abonnement** simple (plans + accès modules).

## Structure proposée
```
/unified_platform
  __init__.py        # exports principaux
  bus.py             # EventBus & CommandBus
  registry.py        # ModuleRegistry (catalogue)
  modules.py         # liste des modules (25 + pack 15)
  bootstrap.py       # assemblage minimal
  subscription.py    # abonnements + accès
```

## Format des événements & commandes
Chaque message publié sur les bus est normalisé afin d'être traçable et exploitable :
- `event_id` / `command_id` (UUID),
- `name` (ex: `lead.created`),
- `payload` (données métier),
- `occurred_at` / `issued_at` (timestamp UTC),
- `metadata` (contextes techniques: source, trace, etc.).

## Prochaine étape recommandée
1. Définir le **format des événements** (ex: "lead.created", "report.generated").
2. Ajouter un **port d'API** (ex: FastAPI) pour exposer le catalogue et lancer des jobs.
3. Brancher 2-3 modules prioritaires pour un MVP.
4. Connecter la gestion d'abonnement à la facturation (Stripe).
