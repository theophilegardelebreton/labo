"""Génère la grille d'échantillons au format exact du bloc-notes GoodNotes de Théophile.

Papier : A4, fond crème, lignes tous les 17,5 pt à partir de y = 50 pt.
On écrit sur une ligne sur deux pour que les jambages ne se touchent pas.
La géométrie est enregistrée dans grille.json, qui sert ensuite au découpage.
"""
import json
from pathlib import Path

import pymupdf

ICI = Path(__file__).parent
W, H = 595.28, 841.89
PAS = 17.5            # interligne du modèle GoodNotes
Y0 = 50.0             # première ligne du modèle
FOND = (0.9725, 0.9687, 0.9136)
LIGNE = (0.8156, 0.8236, 0.8273)
GRIS = (0.55, 0.55, 0.55)
X_CASES, X_FIN = 50.0, 575.0
HAUT, BAS = 24.0, 11.0   # zone d'une case au-dessus / au-dessous de la ligne de base
POLICE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

FREQUENTS = (  # 10 échantillons chacun
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "éèêàçùâîôûëïœ"
    ".,;:!?'()-+=/"
    "αβγδεθλμπρστφωΔΣΩ"
    "∫√∞∂→⇒⇔≤≥≠≈×±∈∀∃"
)
RARES = (  # 5 échantillons chacun, deux par rangée
    "ÉÈÊÀÇÔŒæüÿ"
    "\"[]{}<>_%&@#*~^°€$|\\"
    "ζηκνξχψΓΘΛΠΦΨ∇"
    "∬∮∑∏⟨⟩←↔↦≡∝∓÷·∉⊂⊆∪∩∅ℝℕℤℚℂ′‖"
)
PHRASES = [
    "Portez ce vieux whisky au juge blond qui fume.",
    "D'après Taylor, f(x) = f(a) + (x − a)f′(a) + o(x − a).",
    "Or ΔU = W + Q, donc ∫ P dV ≤ 0 ⇒ le gaz se détend.",
    "Soit ε > 0, ∃ η > 0, ∀ x ∈ ℝ, |x − a| < η ⇒ |f(x) − f(a)| < ε.",
]


def rangees():
    """Liste de rangées ; chaque rangée = liste de (caractère, nb de cases)."""
    r = [[(c, 10)] for c in FREQUENTS]
    r += [[(c, 5) for c in RARES[i:i + 2]] for i in range(0, len(RARES), 2)]
    return r


def papier(page):
    page.draw_rect(pymupdf.Rect(0, 0, W, H), color=None, fill=FOND)
    y = Y0
    while y < H - 20:
        page.draw_rect(pymupdf.Rect(0, y, W, y + 0.5), color=None, fill=LIGNE)
        y += PAS
    for x, y in ((12, 12), (W - 12, 12), (12, H - 12), (W - 12, H - 12)):  # repères de calage
        page.draw_line((x - 5, y), (x + 5, y), color=GRIS, width=0.4)
        page.draw_line((x, y - 5), (x, y + 5), color=GRIS, width=0.4)


def texte(page, x, y, s, taille):
    page.insert_text((x, y), s, fontsize=taille, fontname="dv", fontfile=POLICE, color=GRIS)


def separateur(page, x, yb):
    page.draw_line((x, yb - HAUT), (x, yb + BAS), color=LIGNE, width=0.5, dashes="[2 2] 0")


def main():
    doc = pymupdf.open()
    geo = {"page": [W, H], "pas": PAS, "haut": HAUT, "bas": BAS, "cases": []}
    bases = [Y0 + PAS * (2 * k + 2) for k in range(30)]
    bases = [y for y in bases if y + BAS < H - 20]
    rs = rangees()
    while rs:
        num = len(doc)
        page = doc.new_page(width=W, height=H)
        papier(page)
        texte(page, 50, 38, f"Page {num + 1}. Un caractère par case, posé sur la ligne, à ta taille normale.", 8)
        for yb in bases[:len(rs)]:
            rangee = rs.pop(0)
            larg = (X_FIN - X_CASES) / sum(k for _, k in rangee)
            x = X_CASES
            for car, k in rangee:
                if x == X_CASES:
                    texte(page, 22, yb, car, 11)            # modèle dans la marge
                else:  # second caractère de la rangée : trait plein et modèle dans la case
                    page.draw_line((x, yb - HAUT), (x, yb + BAS), color=GRIS, width=1)
                    texte(page, x + 3, yb - HAUT + 10, car, 10)
                for _ in range(k):
                    separateur(page, x, yb)
                    geo["cases"].append({"page": num, "car": car, "x0": round(x, 2),
                                         "x1": round(x + larg, 2), "base": yb})
                    x += larg
            separateur(page, x, yb)
    # dernière page : phrases libres pour l'espacement, les liaisons et la vérification
    num = len(doc)
    page = doc.new_page(width=W, height=H)
    papier(page)
    texte(page, 50, 38, f"Page {num + 1}. Recopie chaque phrase sur la ligne du dessous, avec ton écriture normale.", 8)
    lignes = []
    for i, p in enumerate(PHRASES):
        texte(page, 50, Y0 + PAS * (4 * i + 1) - 4, p, 9)
        lignes.append(Y0 + PAS * (4 * i + 2))
    geo["phrases"] = {"page": num, "lignes": lignes, "textes": PHRASES}
    doc.save(ICI / "grille.pdf")
    (ICI / "grille.json").write_text(json.dumps(geo, ensure_ascii=False, indent=1))
    print(len(doc), "pages,", len(geo["cases"]), "cases")


if __name__ == "__main__":
    main()
