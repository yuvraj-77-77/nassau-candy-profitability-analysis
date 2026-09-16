# 🍬 Nassau Candy — Product Line Profitability & Margin Performance Analysis

> **A professional data analytics and business intelligence solution for evaluating product profitability, margin performance, division efficiency, cost structure, profit concentration, and factory-level performance.**

---

## 👤 Project Owner

**YUVRAJ SINGH**

**Project:** Product Line Profitability & Margin Performance Analysis  
**Organization / Business Context:** Nassau Candy Distributor  
**Application:** Interactive Streamlit Analytics Dashboard  
**Primary Language:** Python  
**Project Type:** Data Analytics & Business Intelligence

---

# 📌 Project Overview

The **Nassau Candy Product Line Profitability & Margin Performance Analysis** project is an interactive analytics solution designed to transform transactional sales and cost data into meaningful business intelligence.

Traditional sales reporting often focuses heavily on revenue and sales volume. However, high sales volume does not necessarily mean high profitability.

A product may:

- Generate significant sales but produce relatively low profit.
- Have high manufacturing costs.
- Contribute little to overall profitability.
- Generate strong revenue while maintaining weak margins.
- Create margin risk within a particular product division.
- Depend heavily on a particular manufacturing facility.

This project addresses these challenges by analyzing **sales, cost, gross profit, units, product divisions, regions, factories, and time-based performance** through an interactive Streamlit dashboard.

The system provides decision-makers with a centralized view of:

- Product profitability
- Gross margin performance
- Revenue contribution
- Profit contribution
- Division-level performance
- Cost efficiency
- Profit concentration
- Factory performance
- Product–factory relationships
- Margin risk

---

# 🎯 Project Objective

The primary objective of this project is to develop a **data-driven profitability intelligence platform** that enables users to understand where revenue and profit are being generated and where potential margin problems exist.

The dashboard helps answer questions such as:

1. Which products generate the highest gross profit?
2. Which products have the highest gross margins?
3. Are high-sales products actually profitable?
4. Which products represent margin risk?
5. How does profitability vary across divisions?
6. Which divisions contribute most to overall profit?
7. Which products have high costs relative to their sales?
8. How concentrated is the company's profit across products?
9. Which factories are associated with different product categories?
10. How does profitability change over time?

---

# 🏢 Business Context

For a distributor such as Nassau Candy, analyzing sales volume alone can provide an incomplete picture of business performance.

A product can have:

**High Sales + Low Margin = Potential Profitability Risk**

while another product can have:

**Moderate Sales + High Margin = Strong Profit Contribution**

Therefore, this project focuses on **profitability rather than revenue alone**.

The analysis combines sales and cost information to calculate meaningful profitability metrics and provides interactive visualizations for deeper investigation.

---

# ❗ Problem Statement

The organization requires better visibility into product and division profitability.

Without detailed profitability analysis, management may have difficulty determining:

- Which product lines generate sustainable profit.
- Which high-volume products have weak margins.
- Which divisions are financially efficient.
- Which products require pricing review.
- Where manufacturing costs may be excessive.
- Whether profit is concentrated among a small number of products.
- Which factories are associated with particular product categories.

The proposed solution is an interactive dashboard that converts raw transactional information into actionable analytical views.

---

# 💡 Proposed Solution

The project implements a **Streamlit-based Business Intelligence Dashboard**.

The application provides:

### Product Profitability Analysis
Evaluates products based on:

- Sales
- Gross Profit
- Gross Margin
- Units
- Profit per Unit
- Revenue Contribution
- Profit Contribution

### Division Performance Analysis
Compares divisions based on:

- Revenue
- Gross Profit
- Average Margin
- Product count
- Profit contribution

### Cost & Margin Diagnostics
Identifies products where:

- Cost is high relative to sales.
- Margins are below the selected threshold.
- Profitability is weak.
- Pricing or cost optimization may require further investigation.

### Profit Concentration Analysis
Uses Pareto-style analysis to understand:

- Profit concentration
- Revenue concentration
- Dependence on a limited number of products

### Factory Intelligence
Analyzes:

- Factory profitability
- Factory geographic coordinates
- Product–factory relationships
- Factory-level contribution

---

# 📊 Key Performance Indicators (KPIs)

The dashboard calculates the following KPIs.

| KPI | Formula | Purpose |
|---|---|---|
| **Gross Margin (%)** | Gross Profit ÷ Sales × 100 | Measures profitability relative to revenue |
| **Profit per Unit** | Gross Profit ÷ Units | Measures profit generated per unit |
| **Revenue Contribution** | Product Sales ÷ Total Sales × 100 | Measures product share of total revenue |
| **Profit Contribution** | Product Profit ÷ Total Profit × 100 | Measures product share of total profit |
| **Gross Profit** | Sales − Cost | Measures absolute product profitability |
| **Margin Volatility** | Change in margin over time | Identifies unstable profitability |

---

# 📁 Dataset Structure

The application uses structured transactional data containing the following fields:

| Field | Description |
|---|---|
| Row ID | Unique row identifier |
| Order ID | Unique order identifier |
| Order Date | Date on which the order was placed |
| Ship Date | Date on which the order was shipped |
| Ship Mode | Shipping method |
| Customer ID | Unique customer identifier |
| Country/Region | Customer country or region |
| City | Customer city |
| State/Province | Customer state or province |
| Postal Code | Customer postal/ZIP code |
| Division | Product division |
| Region | Customer region |
| Product ID | Unique product identifier |
| Product Name | Product name |
| Sales | Total sales value |
| Units | Number of units sold |
| Gross Profit | Sales minus cost |
| Cost | Manufacturing cost |

---

# 🧮 Analytical Methodology

The project follows a structured analytical workflow.

## 1. Data Cleaning & Validation

The data processing layer validates:

- Sales values
- Cost values
- Gross profit values
- Unit values
- Product names
- Division names
- Missing values
- Invalid records

The application uses defensive processing so data issues can be displayed clearly rather than causing an uncontrolled application failure.

---

## 2. Profitability Metric Calculation

For every product, the system calculates:
**© YUVRAJ SINGH**

```text
Gross Margin (%) = Gross Profit / Sales × 100
