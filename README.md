Investment Calculator
Cette application calcule et affiche la croissance d'un investissement basé sur des contributions mensuelles et annuelles, avec un graphique interactif et un tableau récapitulatif.

Prérequis
Python 3.7 ou supérieur (pour le backend Flask).
PHP (pour lancer le frontend localement).
Un navigateur web moderne.

1. Installation du Backend (Flask)
Étape 1 : Cloner le dépôt
bash
Copier le code
git clone https://github.com/votre-utilisateur/investment-calculator.git
cd investment-calculator/backend
Étape 2 : Créer un environnement virtuel
bash
Copier le code
python -m venv venv
Étape 3 : Activer l'environnement virtuel
Windows :
bash
Copier le code
venv\Scripts\activate
Mac/Linux :
bash
Copier le code
source venv/bin/activate
Étape 4 : Installer les dépendances Python
bash
Copier le code
pip install -r requirements.txt
Le fichier requirements.txt doit contenir les dépendances suivantes :

makefile
Copier le code
Flask==2.2.3
Flask-Cors==3.0.10
Étape 5 : Lancer le backend Flask
bash
Copier le code
python app.py
Le backend sera accessible à l’adresse suivante :

arduino
Copier le code
http://127.0.0.1:5000

2. Lancement du Frontend
Étape 1 : Aller dans le dossier frontend
bash
Copier le code
cd ../frontend
Étape 2 : Lancer un serveur local avec PHP
bash
Copier le code
php -S localhost:8000
Le frontend sera accessible à l’adresse suivante :

arduino
Copier le code
http://localhost:8000

3. Utilisation de l'application
Accédez à http://localhost:8000 dans votre navigateur.
Remplissez les champs du formulaire avec vos paramètres d'investissement :
Initial Balance (€) : La balance initiale.
Annual Rate (%) : Le taux d'intérêt annuel.
Investment Period (Years) : La durée de l'investissement.
Monthly Contribution (€) : Contribution mensuelle (valeur fixe chaque mois).
Annual Lump Sum (€) : Contribution annuelle unique (valeur fixe chaque année).
Cliquez sur "Calculate".
Les résultats apparaîtront sous forme de tableau et de graphique.

4. Structure du projet
bash
Copier le code
investment-calculator/
├── backend/
│   ├── app.py                # Code du backend Flask
│   ├── requirements.txt      # Dépendances Python
├── frontend/
│   ├── index.html            # Interface utilisateur
│   ├── style.css             # Styles CSS (optionnel)

5. Problèmes connus
Erreur CORS dans la console du navigateur :
Assurez-vous que le backend Flask est lancé avec Flask-CORS correctement configuré.
Le frontend ne se charge pas :
Vérifiez que vous avez lancé le serveur PHP avec la commande php -S localhost:8000.

6. Contributions
Les contributions sont les bienvenues ! Pour signaler un bug ou demander une fonctionnalité, ouvrez une issue dans ce dépôt.