"""
CodeAlpha Internship — Tâche 2 : Suivi de Portefeuille Boursier
Auteur   : Stagiaire CodeAlpha
Objectif : Permettre à l'utilisateur de saisir des actions et des quantités,
           calculer la valeur totale du portefeuille, et sauvegarder le résultat.
Concepts : dictionnaire, entrées/sorties, arithmétique de base, gestion de fichiers
"""

import csv
import os
from datetime import datetime

# ── Prix des actions en dur (USD) ─────────────────────────────────────────────
PRIX_ACTIONS: dict[str, float] = {
    "AAPL":  180.00,   # Apple
    "TSLA":  250.00,   # Tesla
    "GOOGL": 140.00,   # Alphabet
    "AMZN":  185.00,   # Amazon
    "MSFT":  420.00,   # Microsoft
    "META":  500.00,   # Meta
    "NFLX":  630.00,   # Netflix
    "NVDA":  900.00,   # NVIDIA
}


def afficher_actions_disponibles() -> None:
    """Affiche la liste des actions disponibles et leurs prix."""
    print("\n📈 Actions disponibles :")
    print("-" * 32)
    print(f"{'Symbole':<10} {'Prix (USD)':>14}")
    print("-" * 32)
    for symbole, prix in PRIX_ACTIONS.items():
        print(f"{symbole:<10} ${prix:>13.2f}")
    print("-" * 32)


def saisir_portefeuille() -> dict[str, int]:
    """
    Demande à l'utilisateur les symboles et quantités d'actions.
    Retourne un dictionnaire du type {'AAPL': 5, 'TSLA': 2}.
    """
    portefeuille: dict[str, int] = {}
    print("\nEntrez les actions que vous possédez (tapez 'fin' pour terminer).")

    while True:
        symbole = input("\nSymbole de l'action (ou 'fin') : ").strip().upper()

        if symbole == "FIN":
            if not portefeuille:
                print("⚠  Vous n'avez encore ajouté aucune action.")
                continue
            break

        if symbole not in PRIX_ACTIONS:
            disponibles = ", ".join(PRIX_ACTIONS.keys())
            print(f"⚠  '{symbole}' n'est pas dans notre liste. Disponibles : {disponibles}")
            continue

        if symbole in portefeuille:
            print(f"⚠  '{symbole}' est déjà ajouté. Modifiez sa quantité ci-dessous.")

        while True:
            saisie = input(f"  Quantité de {symbole} : ").strip()
            if saisie.isdigit() and int(saisie) > 0:
                portefeuille[symbole] = int(saisie)
                break
            print("  ⚠  Veuillez entrer un nombre entier positif.")

    return portefeuille


def calculer_portefeuille(portefeuille: dict[str, int]) -> list[dict]:
    """
    Construit le détail de chaque ligne du portefeuille.
    Chaque élément : {symbole, quantite, prix_unitaire, valeur_totale}
    """
    lignes = []
    for symbole, qte in portefeuille.items():
        prix = PRIX_ACTIONS[symbole]
        lignes.append({
            "symbole":      symbole,
            "quantite":     qte,
            "prix_unitaire": prix,
            "valeur_totale": round(prix * qte, 2),
        })
    return lignes


def afficher_portefeuille(lignes: list[dict]) -> float:
    """Affiche un résumé formaté du portefeuille et retourne le total général."""
    print("\n" + "=" * 57)
    print("      📊 Résumé du Portefeuille — CodeAlpha Tracker")
    print("=" * 57)
    print(f"{'Symbole':<10} {'Qté':>5} {'Prix unitaire':>15} {'Valeur totale':>15}")
    print("-" * 57)

    total_general = 0.0
    for l in lignes:
        print(
            f"{l['symbole']:<10} {l['quantite']:>5} "
            f"${l['prix_unitaire']:>14.2f} "
            f"${l['valeur_totale']:>14.2f}"
        )
        total_general += l["valeur_totale"]

    print("-" * 57)
    print(f"{'TOTAL DE L\'INVESTISSEMENT':>43}  ${total_general:>12.2f}")
    print("=" * 57)
    return round(total_general, 2)


def sauvegarder_txt(lignes: list[dict], total: float, nom_fichier: str) -> None:
    """Sauvegarde les résultats dans un fichier texte (.txt)."""
    horodatage = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write("CodeAlpha — Suivi de Portefeuille Boursier\n")
        f.write(f"Généré le : {horodatage}\n")
        f.write("=" * 57 + "\n")
        f.write(f"{'Symbole':<10} {'Qté':>5} {'Prix unitaire':>15} {'Valeur totale':>15}\n")
        f.write("-" * 57 + "\n")
        for l in lignes:
            f.write(
                f"{l['symbole']:<10} {l['quantite']:>5} "
                f"${l['prix_unitaire']:>14.2f} "
                f"${l['valeur_totale']:>14.2f}\n"
            )
        f.write("-" * 57 + "\n")
        f.write(f"{'TOTAL DE L\'INVESTISSEMENT':>43}  ${total:>12.2f}\n")
    print(f"✅ Résultats sauvegardés dans '{nom_fichier}'.")


def sauvegarder_csv(lignes: list[dict], total: float, nom_fichier: str) -> None:
    """Sauvegarde les résultats dans un fichier CSV (.csv)."""
    with open(nom_fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["symbole", "quantite", "prix_unitaire", "valeur_totale"]
        )
        writer.writeheader()
        writer.writerows(lignes)
        # Ligne récapitulative du total
        writer.writerow({
            "symbole":       "TOTAL",
            "quantite":      "",
            "prix_unitaire": "",
            "valeur_totale": total,
        })
    print(f"✅ Résultats sauvegardés dans '{nom_fichier}'.")


def demander_sauvegarde(lignes: list[dict], total: float) -> None:
    """Propose à l'utilisateur de sauvegarder les résultats."""
    reponse = input("\nVoulez-vous sauvegarder les résultats ? (o/n) : ").strip().lower()
    if reponse != "o":
        return

    format_choix = input("Sauvegarder en (1) TXT  ou  (2) CSV ?  Entrez 1 ou 2 : ").strip()
    if format_choix == "1":
        sauvegarder_txt(lignes, total, "portefeuille_resultat.txt")
    elif format_choix == "2":
        sauvegarder_csv(lignes, total, "portefeuille_resultat.csv")
    else:
        print("⚠  Choix invalide — résultats non sauvegardés.")


def principal() -> None:
    """Point d'entrée du programme de suivi boursier."""
    print("\n" + "=" * 57)
    print("   💼 Suivi de Portefeuille Boursier — CodeAlpha")
    print("=" * 57)

    afficher_actions_disponibles()
    portefeuille = saisir_portefeuille()
    lignes = calculer_portefeuille(portefeuille)
    total = afficher_portefeuille(lignes)
    demander_sauvegarde(lignes, total)

    print("\nMerci d'avoir utilisé le Tracker CodeAlpha ! 📈")


if __name__ == "__main__":
    principal()