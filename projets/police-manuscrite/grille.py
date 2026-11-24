"""Génère la grille d'échantillons au format exact du bloc-notes GoodNotes de Théophile.

Papier : A4, fond crème, lignes tous les 17,5 pt à partir de y = 50 pt.
Trois sortes de rangées :
  - normale : caractères posés sur une ligne de base (une ligne sur deux) ;
  - grande  : grands délimiteurs, intégrales, sommes, hauts de k interlignes, entre deux lignes ;
  - trait   : traits et flèches de longueur imposée (fractions, soulignements, encadrés, vecteurs).
La géométrie de chaque case est enregistrée dans grille.json pour le découpage.
"""
import json
from pathlib import Path

import pymupdf

ICI = Path(__file__).parent
W, H = 595.28, 841.89
PAS, Y0, N_LIGNES = 17.5, 50.0, 45      # modèle GoodNotes : 45 lignes de y = 50 à y = 820
FOND = (0.9725, 0.9687, 0.9136)
LIGNE = (0.8156, 0.8236, 0.8273)
GRIS = (0.55, 0.55, 0.55)
LARG = 500.0                             # largeur du bloc de cases, centré sur la page
X0 = (W - LARG) / 2
HAUT, BAS = 24.0, 11.0                   # case normale : au-dessus / au-dessous de la ligne de base
N = 10                                   # échantillons par élément
CM = 72 / 2.54
POLICE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SYMB = "/usr/share/fonts/truetype/freefont/FreeSerif.ttf"   # couvre ⟦ ⟧ 𝒜 𝟙 ⩽ …

MINUSCULES = "abcdefghijklmnopqrstuvwxyz"
MAJUSCULES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHIFFRES = "0123456789"
ACCENTS = "éèêëàâäîïôöùûüçÿœæŒÆ"
MARQUES = "´`^¨¸"                        # accents seuls, pour composer les majuscules accentuées
PONCTUATION = ".,;:!?'\"«»()[]{}-–_/\\|*&@#%°€$§~"
GREC = "αβγδεζηθϑικλμνξπρστυφχψωΓΔΘΛΞΠΣΥΦΨΩ"
CALLI = "𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"
DOUBLES = "ℕℤℚℝℂ𝕂𝟙ℙ𝔼"
MATHS = (
    "+−=≠<>⩽⩾≪≫±∓×÷·∗∘≈≃∼≡∝∞∂∇ℏℓ′″"
    "∀∃∄¬∧∨⇒⇐⇔∈∉∋⊂⊄⊆⊃∪∩∅∁∖"
    "→←↔↦⟶↗↘⊥∥∠⊙⊗⊕"
    "∑∏∫∬∭∮√⟦⟧⟨⟩⌊⌋‖"
)
# accents mathématiques posés au-dessus d'une lettre : on les dessine au-dessus d'un « x » modèle
ACCENTS_MATHS = [("x⃗", "flèche de vecteur"), ("x̄", "barre (conjugué)"), ("ẋ", "point (dérivée)"),
                 ("ẍ", "deux points"), ("x̂", "chapeau"), ("x̃", "tilde")]
GRANDS = "()[]{}|‖⟦⟧⟨⟩⌊⌋"                # délimiteurs en 2, 3 et 4 interlignes
GRANDS_OPS = "∫∬∮∑∏⋃⋂√"                  # opérateurs « display », 2 interlignes ; √ aussi en 3 et 4
TRAITS = [(1, "trait 1 cm"), (3, "trait 3 cm"), (8, "trait 8 cm"), (16, "trait 16 cm"),
          (1, "flèche 1 cm"), (3, "flèche 3 cm"), (6, "flèche 6 cm")]
PHRASES = [
    "Portez ce vieux whisky au juge blond qui fume.",
    "Le cœur déçu mais l'âme plutôt naïve, Louÿs rêva de crapaüter en canoë.",
    "D'après Taylor, f(x) = f(a) + (x − a)f′(a) + o(x − a).",
    "Or ΔU = W + Q, donc ∫ P dV ⩽ 0, de ce fait le gaz se détend.",
    "Soit ε > 0, ∃ η > 0, ∀ x ∈ ℝ, |x − a| < η ⇒ |f(x) − f(a)| < ε.",
    "On projette le principe fondamental sur la base (e⃗r, e⃗θ, e⃗z) du repère.",
    "La tension aux bornes de la résistance vaut U = R I, soit 12 V.",
    "Je n'écris pas toujours de la même façon, et c'est très bien comme ça.",
]


def y(i):
    return Y0 + PAS * i


def elements():
    """Suite de rangées : (type, [(clé, étiquette, nb_cases)], paramètre)."""
    r = []
    for c in (MINUSCULES + MAJUSCULES + CHIFFRES + ACCENTS + MARQUES + PONCTUATION
              + GREC + CALLI + DOUBLES + MATHS):
        r.append(("normale", [(c, c, N)], None))
    for c, nom in ACCENTS_MATHS:
        r.append(("normale", [(c, c, N)], nom))
    for k in (2, 3, 4):
        r += [("grande", [(f"{c}@{k}", c, N)], k) for c in GRANDS]
    r += [("grande", [(f"{c}@2", c, N)], 2) for c in GRANDS_OPS]
    r += [("grande", [(f"√@{k}", "√", N)], k) for k in (3, 4)]
    for cm, nom in TRAITS:
        par_rangee = max(1, int(LARG // (cm * CM + 12)))
        reste = N
        while reste:
            n = min(par_rangee, reste)
            r.append(("trait", [(nom, nom, n)], cm))
            reste -= n
    return r


def hauteur(rangee):
    """Nombre d'interlignes consommés par une rangée."""
    return rangee[2] + 1 if rangee[0] == "grande" else 2


def papier(page, num, consigne):
    page.draw_rect(pymupdf.Rect(0, 0, W, H), color=None, fill=FOND)
    for i in range(N_LIGNES):
        page.draw_rect(pymupdf.Rect(0, y(i), W, y(i) + 0.5), color=None, fill=LIGNE)
    for cx, cy in ((12, 12), (W - 12, 12), (12, H - 12), (W - 12, H - 12)):  # repères de calage
        page.draw_line((cx - 5, cy), (cx + 5, cy), color=GRIS, width=0.4)
        page.draw_line((cx, cy - 5), (cx, cy + 5), color=GRIS, width=0.4)
    texte(page, X0, 38, f"Page {num + 1}. {consigne}", 8)


def texte(page, x, yb, s, taille, police=POLICE):
    if any(ord(ch) > 0x2000 for ch in s):
        police = SYMB
    page.insert_text((x, yb), s, fontsize=taille, fontname=Path(police).stem, fontfile=police, color=GRIS)


def pointille(page, x, y_haut, y_bas):
    page.draw_line((x, y_haut), (x, y_bas), color=LIGNE, width=0.5, dashes="[2 2] 0")


def dessiner(page, num, curseur, rangee, cases):
    sorte, items, param = rangee
    (cle, etiquette, n), = items
    if sorte == "normale":
        yb = y(curseur + 2)
        larg = LARG / n
        texte(page, X0 - 26, yb, etiquette, 12)
        if param:  # accent mathématique : x gris modèle, on dessine seulement l'accent au-dessus
            texte(page, X0 - 26, yb + 8, param, 5)
            for k in range(n):
                texte(page, X0 + k * larg + larg / 2 - 3, yb, "x", 11)
        for k in range(n + 1):
            pointille(page, X0 + k * larg, yb - HAUT, yb + BAS)
        cases += [{"page": num, "cle": cle, "type": sorte, "x0": round(X0 + k * larg, 2),
                   "x1": round(X0 + (k + 1) * larg, 2), "base": yb} for k in range(n)]
    elif sorte == "grande":
        haut, bas = y(curseur + 1), y(curseur + 1 + param)
        larg = LARG / n
        texte(page, X0 - 26, (haut + bas) / 2 + 4, etiquette, 12)
        texte(page, X0 - 26, bas - 2, f"{param}×", 6)
        for k in range(n + 1):
            pointille(page, X0 + k * larg, haut, bas)
        for k in range(n):  # petites butées : le caractère va d'une butée à l'autre
            for yy in (haut, bas):
                page.draw_line((X0 + k * larg + 18, yy), (X0 + k * larg + larg - 18, yy), color=GRIS, width=1.2)
        cases += [{"page": num, "cle": cle, "type": sorte, "x0": round(X0 + k * larg, 2),
                   "x1": round(X0 + (k + 1) * larg, 2), "haut": haut, "bas": bas} for k in range(n)]
    else:  # trait : segment imposé, matérialisé par deux butées
        yb = y(curseur + 2) - 6
        longueur = param * CM
        pas = LARG / n
        texte(page, X0, y(curseur + 1) + 6, etiquette, 6)
        for k in range(n):
            xa = X0 + k * pas + (pas - longueur) / 2
            for xx in (xa, xa + longueur):
                page.draw_line((xx, yb - 5), (xx, yb + 5), color=GRIS, width=0.8)
            page.draw_line((xa, yb + 4), (xa + longueur, yb + 4), color=LIGNE, width=0.6, dashes="[1 2] 0")
            cases.append({"page": num, "cle": cle, "type": sorte, "x0": round(xa - 6, 2),
                          "x1": round(xa + longueur + 6, 2), "base": yb})


def main():
    doc = pymupdf.open()
    cases = []
    rs = elements()
    consigne = "Un caractère par case, à ta taille normale. Grandes cases et traits : d'une butée à l'autre."
    while rs:
        num = len(doc)
        page = doc.new_page(width=W, height=H)
        papier(page, num, consigne)
        curseur = 0
        while rs and curseur + hauteur(rs[0]) <= N_LIGNES - 2:
            dessiner(page, num, curseur, rs[0], cases)
            curseur += hauteur(rs.pop(0))
    # phrases libres : espacement, liaisons, vérification
    num = len(doc)
    page = doc.new_page(width=W, height=H)
    papier(page, num, "Recopie chaque phrase sur la ligne du dessous, avec ton écriture normale, liaisons comprises.")
    lignes = []
    for i, p in enumerate(PHRASES):
        texte(page, X0, y(5 * i + 1) - 4, p, 9)
        lignes.append(y(5 * i + 3))
    doc.save(ICI / "grille.pdf")
    geo = {"page": [W, H], "pas": PAS, "haut": HAUT, "bas": BAS, "cases": cases,
           "phrases": {"page": num, "lignes": lignes, "textes": PHRASES}}
    (ICI / "grille.json").write_text(json.dumps(geo, ensure_ascii=False, indent=1))
    print(len(doc), "pages,", len(cases), "cases")


if __name__ == "__main__":
    main()
