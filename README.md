# Investment Calculator

Cette application calcule et affiche la croissance d'un investissement basé sur des contributions mensuelles et annuelles, avec un graphique interactif et un tableau récapitulatif.

### Prérequis
- Python 3.7 ou supérieur (pour le backend Flask).
- PHP (pour lancer le frontend localement).
- Un navigateur web moderne.

---

### 1. Installation du Backend (Flask)

#### Étape 1 : Cloner le dépôt
```bash
git clone https://github.com/votre-utilisateur/investment-calculator.git
cd investment-calculator/backend
```

#### Étape 2 : Créer un environnement virtuel
```bash
python -m venv venv
```

#### Étape 3 : Activer l'environnement virtuel
- **Windows** :
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux** :
  ```bash
  source venv/bin/activate
  ```

#### Étape 4 : Installer les dépendances Python
```bash
pip install -r requirements.txt
```

Le fichier `requirements.txt` doit contenir les dépendances suivantes :
```
Flask==2.2.3
Flask-Cors==3.0.10
```

#### Étape 5 : Lancer le backend Flask
```bash
python app.py
```

Le backend sera accessible à l’adresse suivante :
```
http://127.0.0.1:5000
```

---

### 2. Lancement du Frontend

#### Étape 1 : Aller dans le dossier `frontend`
```bash
cd ../frontend
```

#### Étape 2 : Lancer un serveur local avec PHP
```bash
php -S localhost:8000
```

Le frontend sera accessible à l’adresse suivante :
```
http://localhost:8000
```

---

### 3. Utilisation de l'application
1. Accédez à `http://localhost:8000` dans votre navigateur.
2. Remplissez les champs du formulaire avec vos paramètres d'investissement :
   - **Initial Balance (€)** : La balance initiale.
   - **Annual Rate (%)** : Le taux d'intérêt annuel.
   - **Investment Period (Years)** : La durée de l'investissement.
   - **Monthly Contribution (€)** : Contribution mensuelle (valeur fixe chaque mois).
   - **Annual Lump Sum (€)** : Contribution annuelle unique (valeur fixe chaque année).
3. Cliquez sur "Calculate".
4. Les résultats apparaîtront sous forme de tableau et de graphique.

---

### 4. Structure du projet

```
investment-calculator/
├── backend/
│   ├── app.py                # Code du backend Flask
│   ├── requirements.txt      # Dépendances Python
├── frontend/
│   ├── index.html            # Interface utilisateur
│   ├── style.css             # Styles CSS (optionnel)
│   ├── script.js             # Logique frontend
```

---

### 5. Problèmes connus

- **Erreur `CORS` dans la console du navigateur** :
  - Assurez-vous que le backend Flask est lancé avec `Flask-CORS` correctement configuré.
- **Le frontend ne se charge pas** :
  - Vérifiez que vous avez lancé le serveur PHP avec la commande `php -S localhost:8000`.

---

### 6. Contributions

Les contributions sont les bienvenues ! Pour signaler un bug ou demander une fonctionnalité, ouvrez une issue dans ce dépôt.
```
