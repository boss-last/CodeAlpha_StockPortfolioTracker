# 📈 Suivi de Portefeuille Boursier — Stock Portfolio Tracker

> Projet réalisé dans le cadre du stage Python chez **CodeAlpha**

---

## 📌 Description

Un outil de suivi d'investissement boursier en **mode terminal**, développé en Python pur.  
L'utilisateur saisit les actions qu'il possède et leurs quantités.  
Le programme calcule automatiquement la valeur totale de son portefeuille et peut sauvegarder les résultats en `.txt` ou `.csv`.

---

## 🖥️ Démonstration

```
=========================================================
   💼 Suivi de Portefeuille Boursier — CodeAlpha
=========================================================

📈 Actions disponibles :
--------------------------------
Symbole       Prix (USD)
--------------------------------
AAPL           $     180.00
TSLA           $     250.00
GOOGL          $     140.00
...
--------------------------------

Entrez les actions que vous possédez (tapez 'fin' pour terminer).

Symbole de l'action (ou 'fin') : AAPL
  Quantité de AAPL : 5

Symbole de l'action (ou 'fin') : TSLA
  Quantité de TSLA : 2

Symbole de l'action (ou 'fin') : fin

=========================================================
      📊 Résumé du Portefeuille — CodeAlpha Tracker
=========================================================
Symbole      Qté    Prix unitaire    Valeur totale
---------------------------------------------------------
AAPL           5 $        180.00 $         900.00
TSLA           2 $        250.00 $         500.00
---------------------------------------------------------
                   TOTAL DE L'INVESTISSEMENT  $     1400.00
=========================================================

Voulez-vous sauvegarder les résultats ? (o/n) : o
Sauvegarder en (1) TXT  ou  (2) CSV ?  Entrez 1 ou 2 : 2
✅ Résultats sauvegardés dans 'portefeuille_resultat.csv'.
```

---

## 🚀 Lancement

### Prérequis

- Python 3.10 ou supérieur
- Aucune bibliothèque externe nécessaire (`csv`, `os`, `datetime` sont des modules standard)

### Installation & Exécution

```bash
# Cloner le dépôt
git clone https://github.com/<votre-username>/CodeAlpha_StockPortfolioTracker.git

# Accéder au dossier
cd CodeAlpha_StockPortfolioTracker

# Lancer le programme
python task2_portefeuille.py
```

---

## 🗂️ Structure du projet

```
CodeAlpha_StockPortfolioTracker/
│
├── task2_portefeuille.py      # Code source principal
├── portefeuille_resultat.txt  # Exemple de fichier de sortie TXT (généré à l'exécution)
├── portefeuille_resultat.csv  # Exemple de fichier de sortie CSV (généré à l'exécution)
└── README.md                  # Documentation du projet
```

---

## ⚙️ Fonctionnement

| Étape | Description |
|-------|-------------|
| 1 | Affichage de la liste des 8 actions disponibles avec leurs prix |
| 2 | L'utilisateur saisit un symbole boursier (ex: `AAPL`) |
| 3 | L'utilisateur saisit la quantité détenue |
| 4 | Répétition jusqu'à la saisie de `fin` |
| 5 | Calcul et affichage du résumé du portefeuille |
| 6 | Sauvegarde optionnelle en `.txt` ou `.csv` |

---

## 📊 Actions disponibles

| Symbole | Entreprise | Prix unitaire |
|---------|-----------|--------------|
| AAPL | Apple | $180.00 |
| TSLA | Tesla | $250.00 |
| GOOGL | Alphabet (Google) | $140.00 |
| AMZN | Amazon | $185.00 |
| MSFT | Microsoft | $420.00 |
| META | Meta | $500.00 |
| NFLX | Netflix | $630.00 |
| NVDA | NVIDIA | $900.00 |

---

## 🧠 Concepts Python utilisés

- **`dict`** — stockage des prix des actions et du portefeuille utilisateur
- **`input / print`** — interface utilisateur en mode terminal
- **Arithmétique** — calcul de la valeur totale (`prix × quantité`)
- **Gestion de fichiers** — sauvegarde avec `open()`, `write()`, module `csv`
- **`datetime`** — horodatage des fichiers de résultats
- **Validation des entrées** — vérification du symbole et de la quantité
- **Fonctions** — architecture modulaire et lisible

---

## 📁 Exemple de fichier CSV généré

```csv
symbole,quantite,prix_unitaire,valeur_totale
AAPL,5,180.0,900.0
TSLA,2,250.0,500.0
TOTAL,,,1400.0
```

---

## 📋 Règles de saisie

- ✅ Les symboles sont insensibles à la casse (`aapl` = `AAPL`)
- ✅ La quantité doit être un entier positif
- ✅ Un symbole déjà ajouté peut être mis à jour
- ❌ Les symboles hors liste sont refusés avec un message d'erreur

---

## 👤 Auteur

**Stagiaire CodeAlpha — Module 3**  
Stage Python Development — CodeAlpha  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-CodeAlpha-blue?logo=linkedin)](https://www.linkedin.com/company/codealpha/)
[![GitHub](https://img.shields.io/badge/GitHub-CodeAlpha__StockPortfolioTracker-black?logo=github)](https://github.com/<votre-username>/CodeAlpha_StockPortfolioTracker)

---

## 🏢 À propos de CodeAlpha

CodeAlpha est une entreprise leader en développement logiciel, axée sur la création de solutions scalables et efficaces. Ce stage permet aux étudiants de maîtriser les fondamentaux Python, les structures de données, la gestion de fichiers et la POO.
