# Algorithme d’assignation des tâches

## Étapes de l’algorithme

### 1. Groupement ordonné des `samples` par priorité

- Les échantillons sont classés en catégories (STAT, URGENT, ROUTINE) selon les règles définies dans `config.py`.

### 2. Itération sur les groupes

On parcourt chaque groupe de `samples` (par ordre de priorité).

À l’intérieur de chaque groupe, les échantillons sont triés par nombre de ressources disponibles. On traite d’abord ceux qui ont le moins de choix de techniciens.

### 3. Assignation récursive

L’algorithme principal est récursif :

**Condition de sortie** : si la liste des samples est vide, la récursion s’arrête.

Cas récursif : sélectionner un échantillon, l’assigner, mettre à jour les ressources, et relancer l’assignation sur la liste réduite.

#### 3.1. Recherche des techniciens et équipements disponibles

Pour chaque sample :

- Un technicien est disponible si :

  - sa spécialité correspond au type d’analyse (sample.type) ou est GENERAL,
  - il dispose de temps restant suffisant (remaining_time ≥ analysis_time),
  - sa fenêtre de disponibilité couvre la date d’arrivée de l’échantillon.

- Un équipement est disponible si :
  - son type correspond au sample.type,
  - il est libre au moment où l’échantillon est prêt.

#### 3.2. Gestion des cas particuliers (conflits ?)

- Si aucun technicien n’est disponible → on passe l’échantillon (il sera réévalué plus tard dans la récursivité).

- Si un seul technicien est disponible → assignation directe.

- Si plusieurs techniciens sont disponibles :
  - Prioriser un spécialiste du type d’échantillon,
  - Sinon, choisir un technicien généraliste.

#### 3.3. Validation de l’assignation

Une fois qu’un couple (technicien, équipement) est trouvé pour un échantillon :

- on crée l'assignation (sample_id, technician_id, equipment_id, start_time, end_time).
- elle est ajoutée au schedule.

#### 3.4. Mise à jour des disponibilités

- Le technicien voit son remaining_time diminuer et sa nouvelle start_time avancée à la fin de l’analyse.

- L’équipement a une nouvelle start_time (créée si absente) avancée à la fin de l’analyse.

#### 3.5. Relance récursive

- On retire l'échantillon traité de la liste.
- L’algorithme se rappelle sur cette liste réduite.
