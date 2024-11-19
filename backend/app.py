from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Activer CORS pour autoriser les requêtes cross-origin

@app.route('/calculate-investment', methods=['POST'])
def calculate_investment():
    try:
        # Récupérer les données de la requête
        data = request.json
        initial_balance = data.get("initial_balance", 0)
        monthly_contribution = data.get("monthly_contribution", 0)  # Contribution mensuelle unique
        annual_lump_sum = data.get("annual_lump_sum", 0)  # Contribution annuelle unique
        annual_rate = data.get("annual_rate", 0.08)
        years = data.get("years", 30)

        # Validation de base
        if not isinstance(years, int) or years <= 0:
            return jsonify({"error": "Invalid 'years' value. Must be a positive integer"}), 400

        # Calcul de l'investissement
        balance = initial_balance
        results = []
        for year in range(years):
            annual_contribution = monthly_contribution * 12  # Contribution mensuelle sur l'année
            total_contribution = annual_contribution + annual_lump_sum  # Contribution totale annuelle

            start_balance = balance
            balance = (start_balance + total_contribution) * (1 + annual_rate)

            results.append({
                "Year": year + 1,
                "Start Balance (€)": round(start_balance, 2),
                "Monthly Contributions (€)": round(annual_contribution, 2),
                "Lump Sum Contributions (€)": round(annual_lump_sum, 2),
                "Total Contributions (€)": round(total_contribution, 2),
                "End Balance (€)": round(balance, 2)
            })

        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
