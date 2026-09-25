# Kunskapskontroll i AI – teori och tillämpning, del 1

Detta repository innehåller min lösning på kunskapskontrollen i kursen **AI – teori och tillämpning, del 1**.

Projektet består av både teoretiska frågor och praktiska koduppgifter inom Machine Learning med Python. Arbetet följer kursens övningsuppgifter och kursboken och är uppdelat kapitelvis för att göra materialet enkelt att följa och navigera.

## Syfte

Syftet med projektet är att visa förståelse för centrala begrepp och arbetsmetoder inom Machine Learning samt att tillämpa dessa i praktiska koduppgifter.

Projektet behandlar bland annat maskininlärningens grunder, ML-arbetsflöden, regression, klassificering, dimensionalitetsreduktion och klustring.

## Innehåll

Projektet omfattar följande kapitel och uppgifter:

| Kapitel | Uppgifter |
|---|---|
| **Kapitel 1 – Introduktion till maskininlärning** | Fråga 1–9, 11 |
| **Kapitel 2 – Ett ML-projekt från början till slut** | Fråga 1–6, 8–12 |
| **Kapitel 3 – Regression** | Fråga 1–11, 13, 16 |
| **Kapitel 4 – Classification** | Fråga 1–9, 11, 13, 15 |
| **Kapitel 5 – Dimensionalitetsreduktion** | Fråga 1–3, 5–6, 8–9 |
| **Kapitel 6 – Klustring** | Fråga 1–2, 3–5, 7, 9 |

## Projekt- och notebookstruktur

Projektet är organiserat kapitelvis. För varje kapitel är de teoretiska frågorna och de praktiska koduppgifterna uppdelade i separata notebooks.

- `kapitelX.ipynb` – innehåller fakta- och resonemangsfrågor.
- `koduppgifterX.ipynb` – innehåller de praktiska koduppgifterna.

Numreringen följer respektive kapitel, exempelvis `kapitel3.ipynb` och `koduppgifter3.ipynb` för kapitel 3.

Dataset och övriga filer som behövs för respektive uppgift ligger i den aktuella kapitelmappen.

```
kunskapskontroll_del1/
│
├── Kapitel 1/
│   ├── kapitel1.ipynb
│   └── koduppgifter1.ipynb
│
├── Kapitel 2/
│   ├── dataset/
│   ├── kapitel2.ipynb
│   ├── koduppgifter2.ipynb
│   └── linear_model.joblib
│
├── Kapitel 3/
│   ├── dataset/
│   ├── kapitel3.ipynb
│   └── koduppgifter3.ipynb
│
├── Kapitel 4/
│   ├── bilder/
│   ├── dataset/
│   ├── app.py
│   ├── extra_trees_mnist.joblib
│   ├── mnist_scaler.joblib
│   ├── kapitel4.ipynb
│   └── koduppgifter4.ipynb
│
├── Kapitel 5/
│   ├── dataset/
│   ├── kapitel5.ipynb
│   └── koduppgifter5.ipynb
│
├── Kapitel 6/
│   ├── bilder/
│   ├── dataset/
│   ├── kapitel6.ipynb
│   └── koduppgifter6.ipynb
│
└── README.md
```

## Tekniker och bibliotek

Projektet använder huvudsakligen:

- **Python**
- **pandas**
- **NumPy**
- **scikit-learn**
- **Matplotlib**
- **Seaborn**
- **Jupyter Notebook**
- **Streamlit**
- **Joblib**

## Streamlit-applikation

I Kapitel 4 finns en Streamlit-applikation som kan användas för att testa MNIST-modellen på externa bilder.

För att starta applikationen, öppna terminalen i projektets rotmapp och kör:

```bash
cd "Kapitel 4"
streamlit run app.py
```

Bilderna som används för testning finns i:

```text
Kapitel 4/bilder/
```

## Referenser

- **Kursens övningsuppgifter:** Antonio Prgomets GitHub-repository
- **Kursbok:** *Lär dig AI från grunden – Tillämpad maskininlärning med Python* av Antonio Prgomet, Terese Johnson, Amanda Solberg och Linus Rundberg Streuli
- **scikit-learn Documentation**
- **scikit-learn Getting Started**

### Länkar

- [Antonio Prgomets GitHub-repository](https://github.com/AntonioPrgomet/ai_tillaempad_ml)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [scikit-learn Getting Started](https://scikit-learn.org/stable/getting_started.html)