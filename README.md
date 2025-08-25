# Test algorithmique

Outil de planification des échantillons en laboratoire.  
Il permet d’assigner automatiquement des **techniciens** et des **équipements** aux **échantillons** en respectant :

- les contraintes de **priorité** (`STAT`, `URGENT`, `ROUTINE`),
- la disponibilité des ressources,
- les spécialités des techniciens,
- et la gestion du temps.

---

## 🚀 Fonctionnalités

- 📌 Groupement des échantillons par priorité
- 👩‍🔬 Attribution automatique des techniciens
  - Priorité aux **spécialistes** lorsqu’ils existent
  - Recours aux **généralistes** sinon
- ⚙️ Gestion dynamique de la disponibilité des équipements
- ⏱️ Planification temporelle
- 🔄 Algorithme **récursif** pour recalculer à chaque assignation
- 📊 Génération de **métriques** sur l’efficacité de la planification

---

## 📂 Structure du projet

```text

├── src/
│   ├── main.py
│   ├── config.py
│   ├── scheduler/
│   │   ├── assign.py
│   │   ├── availability.py
│   │   ├── priority.py
│   │   └── recursive.py
│   ├── parsers/
│   │   └── parser.py
│   ├── utils/
│   │   ├── io_json.py
│   │   └── normalize_results.py
│   ├── metrics/
│   │   └── metrics.py
│   └── config.py
├── data/
│   ├── input/
│   └── output/
├── tests/
└── README.md
```

## Configuration des priorités

Le fichier config.py permet d'enumérer les priorités possible et d'en fixer l'ordre.

```
PRIORITY_ORDER = {"STAT": 0, "URGENT": 1, "ROUTINE": 2}

SORTED_CATEGORIES = sorted(PRIORITY_ORDER.keys(), key=lambda x: PRIORITY_ORDER[x])
```
