# Nassau Candy — Product Line Profitability & Margin Performance

Professional Streamlit analytics dashboard for product, division, cost, margin, Pareto, factory and product–factory analysis.

## Included
- Executive dashboard and KPI cards
- Sales / profit trend
- Product profitability leaderboard
- Division performance
- Factory performance and geographic footprint
- Cost vs margin diagnostics
- Margin risk identification
- Pareto profit concentration
- Product–factory correlation
- Data explorer and quality checks
- Date, division, region, factory, product and margin filters
- Deterministic synthetic data — no external API, database or CSV required

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

The `.streamlit/config.toml` file forces a clean light theme so dashboard text remains readable across Streamlit environments.

## Deployment

Upload the ZIP contents to a Streamlit deployment or GitHub repository and use:

```text
streamlit run app.py
```
