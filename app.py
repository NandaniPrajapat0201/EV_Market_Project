from flask import Flask, render_template

app = Flask(__name__)

# After you publish the dashboard on Tableau Public, paste its embed link here.
# Example format:
# "https://public.tableau.com/views/YourDashboardName/YourViewName?:language=en-US&:display_count=n&:origin=viz_share_link"
# TABLEAU_URL = "https://public.tableau.com/app/profile/nandini.prajapat/viz/EV_Market_17936073090410/Dashboard1??:showVizHome=no&:embed=true"

# ✅ Correct — /views/ path
TABLEAU_URL = "https://public.tableau.com/views/EV_Market_17936073090410/Dashboard1?:showVizHome=no&:embed=true"   
KPIS = [
    {"label": "Total Annual Sales", "value": "1.55B units"},
    {"label": "Average Range", "value": "324.5 km"},
    {"label": "Average Customer Rating", "value": "4.09"},
]

INSIGHTS = [
    "All seven market regions sell roughly 217M to 222M units each, so no single region dominates.",
    "Two-Wheeler Scooters are the top-selling category in every region (about 23.7M to 26.2M units per region).",
    "Hatchbacks, Compact SUVs and Sedans follow, while Electric Trucks, Pickup Trucks and Electric Buses sell far fewer units.",
    "NMC (33.8%) and LFP (32.0%) batteries make up about two-thirds of sales, followed by NCA (17.2%), Sodium-Ion (9.9%) and Solid-State (7.1%).",
    "Annual sales stay in a fairly narrow band across the years shown, which suggests a stable market rather than rapid growth.",
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        title="Electric Vehicle Market Performance & Insights",
        kpis=KPIS,
        insights=INSIGHTS,
        tableau_url=TABLEAU_URL,
    )


if __name__ == "__main__":
    app.run(debug=True)
