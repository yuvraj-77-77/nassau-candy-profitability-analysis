import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import zipfile
import io
from datetime import date


# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Nassau Candy | Profitability Intelligence",
    page_icon="🍬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PROFESSIONAL THEME
# ============================================================
st.markdown(
    """
    <style>
        :root {
            --navy: #10213F;
            --navy-2: #17335F;
            --blue: #1769E0;
            --blue-2: #2F7CF6;
            --ink: #15213A;
            --muted: #687791;
            --line: #E5EAF2;
            --surface: #FFFFFF;
            --bg: #F4F7FB;
            --green: #19A66A;
            --red: #D9534F;
            --orange: #F0A33A;
        }

        html, body, [class*="css"] {
            font-family: Arial, Helvetica, sans-serif;
        }

        .stApp {
            background: var(--bg);
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0D1B33 0%, #102747 100%);
            border-right: 1px solid rgba(255,255,255,.08);
        }

        [data-testid="stSidebar"] * {
            color: #EEF4FF;
        }

        [data-testid="stSidebar"] .stRadio label {
            padding: 7px 4px;
        }

        .brand {
            padding: 6px 0 20px 0;
            border-bottom: 1px solid rgba(255,255,255,.12);
            margin-bottom: 17px;
        }

        .brand-name {
            color: #FFFFFF;
            font-size: 20px;
            font-weight: 800;
            letter-spacing: -.4px;
        }

        .brand-sub {
            color: #AABBD7;
            font-size: 11px;
            margin-top: 4px;
            letter-spacing: .4px;
        }

        .nav-caption {
            color: #90A6C8;
            font-size: 10px;
            font-weight: 800;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            margin: 18px 0 7px;
        }

        .topbar {
            background: #FFFFFF;
            border: 1px solid var(--line);
            border-radius: 14px;
            padding: 14px 18px;
            margin-bottom: 16px;
            box-shadow: 0 5px 18px rgba(18, 36, 66, .035);
        }

        .top-title {
            color: var(--ink);
            font-size: 25px;
            font-weight: 800;
            letter-spacing: -.6px;
        }

        .top-sub {
            color: var(--muted);
            font-size: 12px;
            margin-top: 3px;
        }

        .eyebrow {
            color: var(--blue);
            font-size: 10px;
            font-weight: 800;
            letter-spacing: 1.35px;
            text-transform: uppercase;
            margin: 8px 0 4px;
        }

        .hero {
            background: linear-gradient(105deg, #EAF2FF 0%, #F8FAFE 68%, #E9F2FF 100%);
            border: 1px solid #DCE7FA;
            border-radius: 15px;
            padding: 23px 25px;
            margin-bottom: 15px;
        }

        .hero-title {
            color: #101A2F !important;
            font-size: 29px;
            font-weight: 800;
            letter-spacing: -.9px;
            line-height: 1.12;
        }

        .hero-text {
            color: #405572 !important;
            font-size: 13px;
            line-height: 1.55;
            max-width: 760px;
            margin-top: 7px;
        }

        .filter-shell {
            background: #FFFFFF;
            border: 1px solid var(--line);
            border-radius: 13px;
            padding: 10px 14px 1px;
            margin-bottom: 15px;
            box-shadow: 0 4px 15px rgba(18, 36, 66, .03);
        }

        .filter-label {
            color: #50627F;
            font-size: 10px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: .7px;
            margin-bottom: 2px;
        }

        .kpi {
            background: #FFFFFF;
            border: 1px solid var(--line);
            border-radius: 13px;
            padding: 15px 16px 13px;
            min-height: 112px;
            box-shadow: 0 5px 18px rgba(18, 36, 66, .035);
        }

        .kpi-head {
            display: flex;
            align-items: center;
            gap: 8px;
            color: #566883;
            font-size: 10px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: .65px;
        }

        .kpi-icon {
            width: 27px;
            height: 27px;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: #EDF4FF;
            color: var(--blue);
            font-size: 14px;
        }

        .kpi-value {
            color: var(--ink);
            font-size: 24px;
            font-weight: 800;
            margin-top: 9px;
            letter-spacing: -.5px;
        }

        .kpi-note {
            color: #8190A8;
            font-size: 10px;
            margin-top: 4px;
        }

        .section-title {
            color: #101A2F !important;
            font-size: 18px;
            font-weight: 800;
            letter-spacing: -.2px;
            margin: 18px 0 3px;
        }

        .section-sub {
            color: #536581 !important;
            font-size: 12px;
            font-weight: 500;
            margin-bottom: 9px;
        }

        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #101A2F !important;
        }

        [data-testid="stDataFrame"] * {
            color: #1B2A44;
        }

        [data-testid="stMetricValue"] {
            color: #101A2F !important;
        }

        /* Explicit dark typography for every custom executive card.
           This prevents browser/theme inheritance from making text invisible. */
        .insight-grid,
        .insight-grid *,
        .quality-strip,
        .quality-strip *,
        .hero-badges,
        .hero-badges * {
            color: #14213B !important;
            opacity: 1 !important;
            text-shadow: none !important;
        }

        .insight-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin: 12px 0 5px;
        }

        .insight-card {
            background: #FFFFFF !important;
            border: 1px solid #D9E2F0;
            border-radius: 12px;
            padding: 14px 15px;
            min-height: 92px;
            box-shadow: 0 4px 14px rgba(16, 33, 63, .045);
        }

        .insight-label {
            color: #50627F !important;
            font-size: 10px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: .7px;
        }

        .insight-value {
            color: #10213F !important;
            font-size: 19px;
            font-weight: 800;
            margin-top: 5px;
        }

        .insight-note {
            color: #64748B !important;
            font-size: 10px;
            line-height: 1.4;
            margin-top: 3px;
        }

        .quality-strip {
            background: #FFFFFF !important;
            border: 1px solid #D9E2F0;
            border-radius: 10px;
            padding: 10px 13px;
            margin: 10px 0 15px;
            color: #405572 !important;
            font-size: 11px;
            box-shadow: 0 3px 12px rgba(16, 33, 63, .025);
        }

        .quality-strip b {
            color: #10213F !important;
        }

        .hero-badges {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-top: 13px;
        }

        .hero-badge {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 999px;
            background: #FFFFFF !important;
            border: 1px solid #C9D9F2;
            color: #2459A6 !important;
            font-size: 9px;
            font-weight: 800;
            letter-spacing: .25px;
        }

        @media (max-width: 900px) {
            .insight-grid {
                grid-template-columns: 1fr;
            }
        }

        .stCaption {
            color: #536581 !important;
        }

        .insight {
            background: #F0F5FF;
            border: 1px solid #DDE8FB;
            border-radius: 11px;
            padding: 12px 14px;
            color: #304563;
            font-size: 11px;
            line-height: 1.55;
        }

        .warning {
            background: #FFF7EC;
            border: 1px solid #F1DFC2;
            border-radius: 11px;
            padding: 12px 14px;
            color: #654A27;
            font-size: 11px;
            line-height: 1.55;
        }

        .footer {
            color: #8A96A9;
            font-size: 10px;
            text-align: center;
            padding: 25px 0 3px;
        }

        .pill {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 20px;
            background: #EEF4FF;
            color: #2569C7;
            font-size: 9px;
            font-weight: 700;
        }

        .stButton button, .stDownloadButton button {
            border-radius: 9px !important;
            font-weight: 700 !important;
        }

        div[data-testid="stDataFrame"] {
            border: 1px solid var(--line);
            border-radius: 11px;
            overflow: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SYNTHETIC DATA — FULLY SELF-CONTAINED
# ============================================================
@st.cache_data
def make_data():
    products = [
        ("Wonka Bar - Nutty Crunch Surprise", "Chocolate", 18.50, 10.20, "Lot's O' Nuts"),
        ("Wonka Bar - Fudge Mallows", "Chocolate", 16.80, 9.80, "Lot's O' Nuts"),
        ("Wonka Bar - Scrumdiddlyumptious", "Chocolate", 21.20, 11.30, "Lot's O' Nuts"),
        ("Wonka Bar - Milk Chocolate", "Chocolate", 15.50, 9.70, "Wicked Choccy's"),
        ("Wonka Bar - Triple Dazzle Caramel", "Chocolate", 22.40, 11.10, "Wicked Choccy's"),
        ("Laffy Taffy", "Sugar", 8.80, 4.10, "Sugar Shack"),
        ("SweeTARTS", "Sugar", 10.40, 4.90, "Sugar Shack"),
        ("Nerds", "Sugar", 12.20, 5.80, "Sugar Shack"),
        ("Fun Dip", "Sugar", 7.60, 3.70, "Sugar Shack"),
        ("Fizzy Lifting Drinks", "Other", 14.80, 8.20, "Sugar Shack"),
        ("Everlasting Gobstopper", "Sugar", 19.50, 8.90, "Secret Factory"),
        ("Hair Toffee", "Sugar", 11.30, 7.30, "The Other Factory"),
        ("Lickable Wallpaper", "Other", 17.20, 8.20, "Secret Factory"),
        ("Wonka Gum", "Other", 13.60, 6.40, "Secret Factory"),
        ("Kazookles", "Other", 20.80, 9.70, "The Other Factory"),
    ]

    coords = {
        "Lot's O' Nuts": (32.881893, -111.768036),
        "Wicked Choccy's": (32.076176, -81.088371),
        "Sugar Shack": (48.119140, -96.181150),
        "Secret Factory": (41.446333, -90.565487),
        "The Other Factory": (35.117500, -89.971107),
    }

    regions = ["East", "West", "Central", "South"]
    cities = ["New York", "Chicago", "Dallas", "Phoenix", "Atlanta", "Denver", "Seattle"]
    states = ["NY", "IL", "TX", "AZ", "GA", "CO", "WA"]
    ship_modes = ["Standard Class", "Second Class", "First Class"]

    rows = []
    start = pd.Timestamp("2022-01-01")

    # Deterministic synthetic transactions. No randomness and no external dependency.
    for i in range(1, 1801):
        p_idx = (i * 7 + i // 13) % len(products)
        name, division, price, unit_cost, factory = products[p_idx]

        units = 18 + ((i * 17) % 145)
        order_date = start + pd.Timedelta(days=(i * 3) % 365)
        ship_date = order_date + pd.Timedelta(days=1 + (i % 5))

        price_factor = 0.92 + ((i % 9) * 0.012)
        cost_factor = 0.96 + ((i % 7) * 0.009)

        sales = round(units * price * price_factor, 2)
        cost = round(units * unit_cost * cost_factor, 2)
        profit = round(sales - cost, 2)

        lat, lon = coords[factory]

        rows.append(
            {
                "Row ID": i,
                "Order ID": f"ORD-{100000 + i}",
                "Order Date": order_date,
                "Ship Date": ship_date,
                "Ship Mode": ship_modes[(i * 3) % len(ship_modes)],
                "Customer ID": f"CUST-{1000 + ((i * 19) % 450)}",
                "Country/Region": "United States",
                "City": cities[(i * 5) % len(cities)],
                "State/Province": states[(i * 11) % len(states)],
                "Postal Code": 10000 + ((i * 37) % 80000),
                "Division": division,
                "Region": regions[(i * 5) % len(regions)],
                "Product ID": f"P-{100 + p_idx}",
                "Product Name": name,
                "Sales": sales,
                "Units": units,
                "Gross Profit": profit,
                "Cost": cost,
                "Factory": factory,
                "Factory Latitude": lat,
                "Factory Longitude": lon,
            }
        )

    result = pd.DataFrame(rows)

    result["Gross Margin %"] = (
        result["Gross Profit"]
        .div(result["Sales"].replace(0, pd.NA))
        .fillna(0)
        * 100
    )

    result["Profit per Unit"] = (
        result["Gross Profit"]
        .div(result["Units"].replace(0, pd.NA))
        .fillna(0)
    )

    return result


# ============================================================
# HELPERS
# ============================================================
def money(value):
    try:
        return f"${float(value):,.2f}"
    except (TypeError, ValueError):
        return "$0.00"


def compact_money(value):
    try:
        value = float(value)
        if abs(value) >= 1_000_000:
            return f"${value / 1_000_000:.2f}M"
        if abs(value) >= 1_000:
            return f"${value / 1_000:.1f}K"
        return f"${value:,.0f}"
    except (TypeError, ValueError):
        return "$0"


def pct(value):
    try:
        return f"{float(value):.1f}%"
    except (TypeError, ValueError):
        return "0.0%"


def kpi_card(label, value, note, icon):
    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-head">
                <span class="kpi-icon">{icon}</span>
                {label}
            </div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_plot(fig, height=370):
    try:
        fig.update_layout(
            height=height,
            margin=dict(l=10, r=10, t=50, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="#FFFFFF",
            font=dict(family="Arial, sans-serif", color="#18243D", size=12),
            title_font=dict(size=17, color="#101A2F", family="Arial, sans-serif"),
            title_x=0.02,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.01,
                xanchor="right",
                x=1,
            ),
            hoverlabel=dict(bgcolor="white"),
        )
        fig.update_xaxes(
            showgrid=False,
            linecolor="#C8D0DE",
            tickfont=dict(color="#34445F", size=11),
            title_font=dict(color="#18243D", size=12),
        )
        fig.update_yaxes(
            gridcolor="#E5EAF2",
            zeroline=False,
            tickfont=dict(color="#34445F", size=11),
            title_font=dict(color="#18243D", size=12),
        )
        st.plotly_chart(fig, use_container_width=True)
    except Exception as exc:
        st.error(f"Chart rendering failed: {exc}")


def trend_percent(current, previous):
    try:
        if float(previous) == 0:
            return None
        return (float(current) - float(previous)) / abs(float(previous)) * 100
    except (TypeError, ValueError, ZeroDivisionError):
        return None


def trend_label(value):
    try:
        if value is None:
            return "No prior-month comparison"
        sign = "+" if value >= 0 else ""
        return f"{sign}{value:.1f}% vs prior month"


    except (TypeError, ValueError):
        return "Comparison unavailable"


def safe_filter(data, start, end, divisions, regions, factory, product_query):
    try:
        output = data.copy()
        output["Order Date"] = pd.to_datetime(output["Order Date"], errors="coerce")

        # Explicit type casting for widget values.
        start_ts = pd.Timestamp(start)
        end_ts = pd.Timestamp(end) + pd.Timedelta(days=1)

        output = output[
            (output["Order Date"] >= start_ts)
            & (output["Order Date"] < end_ts)
        ]

        if divisions:
            output = output[output["Division"].astype(str).isin(divisions)]

        if regions:
            output = output[output["Region"].astype(str).isin(regions)]

        if factory != "All":
            output = output[output["Factory"].astype(str) == str(factory)]

        if product_query.strip():
            output = output[
                output["Product Name"]
                .astype(str)
                .str.contains(product_query.strip(), case=False, na=False)
            ]

        return output

    except Exception as exc:
        st.error(f"Filtering failed: {exc}")
        return data.iloc[0:0].copy()


# ============================================================
# INITIALIZE
# ============================================================
try:
    df = make_data()
    if df.empty:
        st.error("The synthetic dataset is empty.")
        st.stop()
except Exception as exc:
    st.error(f"Dataset initialization failed: {exc}")
    st.stop()


# ============================================================
# SIDEBAR
# ============================================================
try:
    with st.sidebar:
        st.markdown(
            """
            <div class="brand">
                <div class="brand-name">🍬 NASSAU CANDY</div>
                <div class="brand-sub">A SWEETER TOMORROW • PROFITABILITY INTELLIGENCE</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="nav-caption">Analytics Workspace</div>', unsafe_allow_html=True)

        page = st.radio(
            "Navigation",
            [
                "Dashboard",
                "Product Analysis",
                "Division Analysis",
                "Cost & Margin Analysis",
                "Pareto Analysis",
                "Factory Analysis",
                "Product–Factory Map",
                "Data Explorer",
                "About Project",
            ],
            label_visibility="collapsed",
        )

        st.markdown("---")
        st.markdown('<div class="nav-caption">Filters</div>', unsafe_allow_html=True)

        min_date = df["Order Date"].min().date()
        max_date = df["Order Date"].max().date()

        selected_dates = st.date_input(
            "Date range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
        )

        if isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 2:
            start_date = pd.Timestamp(selected_dates[0]).date()
            end_date = pd.Timestamp(selected_dates[1]).date()
        else:
            start_date = min_date
            end_date = max_date

        division_options = sorted(df["Division"].astype(str).unique().tolist())
        selected_divisions = st.multiselect(
            "Division",
            division_options,
            default=division_options,
        )

        region_options = sorted(df["Region"].astype(str).unique().tolist())
        selected_regions = st.multiselect(
            "Region",
            region_options,
            default=region_options,
        )

        factory_options = ["All"] + sorted(df["Factory"].astype(str).unique().tolist())
        selected_factory = st.selectbox(
            "Factory",
            factory_options,
            index=0,
        )

        margin_threshold = int(
            st.slider(
                "Margin threshold",
                min_value=0,
                max_value=100,
                value=60,
                step=1,
            )
        )

        product_search = st.text_input(
            "Product search",
            value="",
            placeholder="Search product...",
        )

except Exception as exc:
    st.error(f"Sidebar initialization failed: {exc}")
    st.stop()


# ============================================================
# FILTER DATA
# ============================================================
filtered = safe_filter(
    df,
    start_date,
    end_date,
    selected_divisions,
    selected_regions,
    selected_factory,
    product_search,
)


# ============================================================
# GLOBAL HEADER
# ============================================================
st.markdown(
    """
    <div class="topbar">
        <div class="top-title">Product Line Profitability & Margin Performance Analysis</div>
        <div class="top-sub">Nassau Candy Distributor • Executive Business Intelligence Dashboard</div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# DASHBOARD
# ============================================================
if page == "Dashboard":
    try:
        st.markdown('<div class="hero">', unsafe_allow_html=True)
        st.markdown('<div class="eyebrow">WELCOME TO THE ANALYTICS DASHBOARD</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="hero-title">Data-Driven Insights for a Sweeter Tomorrow</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="hero-text">Explore product profitability, division performance, cost efficiency, factory intelligence and profit concentration to support informed business decisions.</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="hero-badges">'
            '<span class="hero-badge">EXECUTIVE VIEW</span>'
            '<span class="hero-badge">PRODUCT ECONOMICS</span>'
            '<span class="hero-badge">MARGIN INTELLIGENCE</span>'
            '<span class="hero-badge">FACTORY ANALYTICS</span>'
            '</div>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="filter-shell">', unsafe_allow_html=True)
        st.markdown('<div class="filter-label">Current analysis scope</div>', unsafe_allow_html=True)
        st.caption(
            f"{start_date.strftime('%Y-%m-%d')} → {end_date.strftime('%Y-%m-%d')}  •  "
            f"{len(filtered):,} transactions  •  "
            f"{filtered['Product Name'].nunique():,} products"
        )
        st.markdown("</div>", unsafe_allow_html=True)

        sales = float(filtered["Sales"].sum())
        cost = float(filtered["Cost"].sum())
        profit = float(filtered["Gross Profit"].sum())
        units = float(filtered["Units"].sum())
        margin = profit / sales * 100 if sales else 0
        ppu = profit / units if units else 0

        c1, c2, c3, c4, c5 = st.columns(5)
        with c1:
            kpi_card("Total Sales", compact_money(sales), "Selected period", "▥")
        with c2:
            kpi_card("Total Cost", compact_money(cost), "Manufacturing cost", "▤")
        with c3:
            kpi_card("Total Profit", compact_money(profit), "Gross profit", "$")
        with c4:
            kpi_card("Overall Margin", pct(margin), "Gross profit ÷ sales", "%")
        with c5:
            kpi_card("Total Units Sold", f"{units:,.0f}", f"{money(ppu)} profit / unit", "□")

        monthly = (
            filtered.assign(
                Month=filtered["Order Date"].dt.to_period("M").dt.to_timestamp()
            )
            .groupby("Month", as_index=False)
            .agg(
                Sales=("Sales", "sum"),
                Gross_Profit=("Gross Profit", "sum"),
            )
        )

        try:
            if len(monthly) >= 2:
                last_month = monthly.iloc[-1]
                prior_month = monthly.iloc[-2]
                sales_change = trend_percent(last_month["Sales"], prior_month["Sales"])
                profit_change = trend_percent(last_month["Gross_Profit"], prior_month["Gross_Profit"])
            else:
                sales_change = None
                profit_change = None

            margin_health = "Healthy" if margin >= margin_threshold else "Margin watch"

            st.markdown(
                f'<div class="insight-grid">'
                f'<div class="insight-card"><div class="insight-label">Margin Health</div>'
                f'<div class="insight-value">{margin_health}</div>'
                f'<div class="insight-note">{pct(margin)} overall margin vs {margin_threshold}% threshold</div></div>'
                f'<div class="insight-card"><div class="insight-label">Latest Sales Momentum</div>'
                f'<div class="insight-value">{trend_label(sales_change)}</div>'
                f'<div class="insight-note">Latest month compared with preceding month</div></div>'
                f'<div class="insight-card"><div class="insight-label">Latest Profit Momentum</div>'
                f'<div class="insight-value">{trend_label(profit_change)}</div>'
                f'<div class="insight-note">Latest month compared with preceding month</div></div>'
                f'</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<div class="quality-strip"><b>Analysis scope:</b> {len(filtered):,} transactions • '
                f'{filtered["Product Name"].nunique():,} products • '
                f'{filtered["Division"].nunique():,} divisions • '
                f'{filtered["Factory"].nunique():,} factories • '
                f'<b>Data quality:</b> {int(filtered.isna().sum().sum()):,} missing values.</div>',
                unsafe_allow_html=True,
            )
        except Exception as exc:
            st.error(f"Executive summary processing failed: {exc}")

        product_summary = (
            filtered.groupby("Product Name", as_index=False)
            .agg(
                Sales=("Sales", "sum"),
                Gross_Profit=("Gross Profit", "sum"),
                Units=("Units", "sum"),
            )
        )

        product_summary["Gross Margin %"] = (
            product_summary["Gross_Profit"]
            .div(product_summary["Sales"].replace(0, pd.NA))
            .fillna(0)
            * 100
        )

        left, middle, right = st.columns([1.55, 1, 1])

        with left:
            st.markdown('<div class="section-title">Monthly Sales vs Profit Trend</div>', unsafe_allow_html=True)
            st.markdown('<div class="section-sub">Revenue and gross profit across the selected analysis period.</div>', unsafe_allow_html=True)

            fig = go.Figure()
            fig.add_trace(
                go.Scatter(
                    x=monthly["Month"],
                    y=monthly["Sales"],
                    mode="lines+markers",
                    name="Sales",
                    line=dict(width=3),
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=monthly["Month"],
                    y=monthly["Gross_Profit"],
                    mode="lines+markers",
                    name="Gross Profit",
                    line=dict(width=3),
                )
            )
            fig.update_layout(
                title="Sales and Gross Profit",
                xaxis_title="Month",
                yaxis_title="Value ($)",
            )
            render_plot(fig, 380)

        with middle:
            st.markdown('<div class="section-title">Top 10 Products by Profit</div>', unsafe_allow_html=True)
            top10 = product_summary.nlargest(10, "Gross_Profit").sort_values("Gross_Profit")
            fig = px.bar(
                top10,
                x="Gross_Profit",
                y="Product Name",
                orientation="h",
                text="Gross_Profit",
                title="Top 10 Products by Gross Profit",
            )
            fig.update_traces(
                texttemplate="$%{text:,.0f}",
                textposition="outside",
                textfont=dict(size=10, color="#18243D"),
            )
            fig.update_layout(
                xaxis_title="Gross Profit ($)",
                yaxis_title="Product",
                yaxis=dict(automargin=True),
            )
            render_plot(fig, 430)

        with right:
            st.markdown('<div class="section-title">Profit Contribution</div>', unsafe_allow_html=True)
            if not product_summary.empty and profit > 0:
                pareto = product_summary.sort_values(
                    "Gross_Profit", ascending=False
                ).reset_index(drop=True)
                pareto["Share"] = pareto["Gross_Profit"] / profit * 100

                top20_n = max(1, int(round(len(pareto) * .20)))
                next20_n = max(1, int(round(len(pareto) * .20)))

                labels = []
                values = []

                top20 = pareto.iloc[:top20_n]["Gross_Profit"].sum()
                next20 = pareto.iloc[top20_n:top20_n + next20_n]["Gross_Profit"].sum()
                next20b = pareto.iloc[top20_n + next20_n:top20_n + 2 * next20_n]["Gross_Profit"].sum()
                bottom = pareto.iloc[top20_n + 2 * next20_n:]["Gross_Profit"].sum()

                for label, value in [
                    ("Top 20% Products", top20),
                    ("Next 20% Products", next20),
                    ("Next 20% Products", next20b),
                    ("Bottom 40% Products", bottom),
                ]:
                    if value > 0:
                        labels.append(label)
                        values.append(value)

                fig = px.pie(
                    values=values,
                    names=labels,
                    hole=.42,
                    title="",
                )
                fig.update_traces(textinfo="percent", hovertemplate="%{label}<br>%{percent}<extra></extra>")
                render_plot(fig, 380)
            else:
                st.info("No positive profit is available for the current filter selection.")

        try:
            if not product_summary.empty:
                best_idx = product_summary["Gross_Profit"].idxmax()
                top_product = str(product_summary.loc[best_idx, "Product Name"])
                top_profit = float(product_summary.loc[best_idx, "Gross_Profit"])
                watch_count = int((product_summary["Gross Margin %"] < margin_threshold).sum())
                st.markdown(
                    f'<div class="insight"><b>Executive readout:</b> {top_product} '
                    f'has the highest gross-profit contribution in the current view '
                    f'({money(top_profit)}). {watch_count} of {len(product_summary)} '
                    f'products are below the selected {margin_threshold}% margin threshold. '
                    f'Use the Product Analysis and Cost & Margin Analysis pages for deeper diagnosis.</div>',
                    unsafe_allow_html=True,
                )
        except Exception as exc:
            st.error(f"Executive readout failed: {exc}")

        st.markdown('<div class="section-title">Performance Summary</div>', unsafe_allow_html=True)

        div_summary = (
            filtered.groupby("Division", as_index=False)
            .agg(
                Sales=("Sales", "sum"),
                Gross_Profit=("Gross Profit", "sum"),
                Units=("Units", "sum"),
            )
        )
        div_summary["Gross Margin %"] = div_summary["Gross_Profit"] / div_summary["Sales"] * 100

        factory_summary = (
            filtered.groupby("Factory", as_index=False)
            .agg(
                Sales=("Sales", "sum"),
                Gross_Profit=("Gross Profit", "sum"),
            )
        )
        factory_summary["Gross Margin %"] = factory_summary["Gross_Profit"] / factory_summary["Sales"] * 100

        c1, c2 = st.columns(2)

        with c1:
            fig = px.bar(
                div_summary.sort_values("Gross_Profit"),
                x="Gross_Profit",
                y="Division",
                orientation="h",
                color="Division",
                title="Division Performance",
            )
            fig.update_layout(
                xaxis_title="Gross Profit ($)",
                yaxis_title="Division",
                yaxis=dict(automargin=True),
            )
            render_plot(fig, 330)

        with c2:
            fig = px.bar(
                factory_summary.sort_values("Gross_Profit"),
                x="Gross_Profit",
                y="Factory",
                orientation="h",
                color="Gross Margin %",
                color_continuous_scale="Blues",
                title="Factory Performance",
            )
            fig.update_layout(
                xaxis_title="Gross Profit ($)",
                yaxis_title="Factory",
                yaxis=dict(automargin=True),
            )
            render_plot(fig, 330)

        st.markdown('<div class="section-title">Recent Orders (Sample)</div>', unsafe_allow_html=True)
        recent = filtered.sort_values("Order Date", ascending=False).head(8)[
            [
                "Order ID",
                "Order Date",
                "Division",
                "Product Name",
                "Region",
                "Units",
                "Sales",
                "Gross Profit",
            ]
        ].copy()

        st.dataframe(
            recent.style.format(
                {
                    "Sales": "${:,.2f}",
                    "Gross Profit": "${:,.2f}",
                    "Order Date": lambda x: x.strftime("%d %b %Y"),
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

    except Exception as exc:
        st.error(f"Dashboard processing failed: {exc}")


# ============================================================
# PRODUCT ANALYSIS
# ============================================================
elif page == "Product Analysis":
    try:
        st.markdown('<div class="section-title">Product Profitability Analysis</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-sub">Rank products by profitability, margin efficiency and unit economics.</div>',
            unsafe_allow_html=True,
        )

        ps = (
            filtered.groupby(["Division", "Product Name", "Factory"], as_index=False)
            .agg(
                Sales=("Sales", "sum"),
                Units=("Units", "sum"),
                Gross_Profit=("Gross Profit", "sum"),
                Cost=("Cost", "sum"),
            )
        )
        ps["Gross Margin %"] = ps["Gross_Profit"] / ps["Sales"].replace(0, pd.NA) * 100
        ps["Profit per Unit"] = ps["Gross_Profit"] / ps["Units"].replace(0, pd.NA)

        metric = st.selectbox(
            "Leaderboard metric",
            ["Gross_Profit", "Gross Margin %", "Sales", "Profit per Unit", "Units"],
            format_func=lambda x: {
                "Gross_Profit": "Gross Profit",
                "Gross Margin %": "Gross Margin %",
                "Sales": "Sales",
                "Profit per Unit": "Profit per Unit",
                "Units": "Units",
            }[x],
        )

        left, right = st.columns([1.25, 1])

        with left:
            chart = ps.nlargest(12, metric).sort_values(metric)
            fig = px.bar(
                chart,
                x=metric,
                y="Product Name",
                color="Division",
                orientation="h",
                title="Product Profitability Leaderboard",
            )
            fig.update_layout(
                xaxis_title=metric,
                yaxis_title="Product",
                yaxis=dict(automargin=True),
            )
            render_plot(fig, 540)

        with right:
            fig = px.scatter(
                ps,
                x="Sales",
                y="Gross Margin %",
                size="Gross_Profit",
                color="Division",
                hover_name="Product Name",
                title="Sales vs Gross Margin",
            )
            fig.update_layout(
                xaxis_title="Sales ($)",
                yaxis_title="Gross Margin (%)",
            )
            fig.add_hline(
                y=margin_threshold,
                line_dash="dash",
                annotation_text=f"{margin_threshold}% threshold",
            )
            render_plot(fig, 500)

        table = ps.rename(
            columns={
                "Product Name": "Product",
                "Gross_Profit": "Gross Profit",
                "Profit per Unit": "Profit / Unit",
            }
        )

        st.dataframe(
            table.style.format(
                {
                    "Sales": "${:,.2f}",
                    "Gross Profit": "${:,.2f}",
                    "Cost": "${:,.2f}",
                    "Gross Margin %": "{:.1f}%",
                    "Profit / Unit": "${:.2f}",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

    except Exception as exc:
        st.error(f"Product analysis failed: {exc}")


# ============================================================
# DIVISION ANALYSIS
# ============================================================
elif page == "Division Analysis":
    try:
        st.markdown('<div class="section-title">Division Performance</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-sub">Compare revenue, profit, unit economics and margin across product divisions.</div>',
            unsafe_allow_html=True,
        )

        ds = (
            filtered.groupby("Division", as_index=False)
            .agg(
                Sales=("Sales", "sum"),
                Cost=("Cost", "sum"),
                Gross_Profit=("Gross Profit", "sum"),
                Units=("Units", "sum"),
                Products=("Product Name", "nunique"),
            )
        )
        ds["Gross Margin %"] = ds["Gross_Profit"] / ds["Sales"].replace(0, pd.NA) * 100
        ds["Profit per Unit"] = ds["Gross_Profit"] / ds["Units"].replace(0, pd.NA)

        c1, c2 = st.columns(2)

        with c1:
            fig = px.bar(
                ds,
                x="Division",
                y="Sales",
                color="Division",
                title="Revenue by Division",
            )
            fig.update_layout(
                xaxis_title="Division",
                yaxis_title="Sales ($)",
            )
            render_plot(fig, 390)

        with c2:
            fig = px.bar(
                ds.sort_values("Gross Margin %"),
                x="Gross Margin %",
                y="Division",
                orientation="h",
                color="Division",
                title="Gross Margin by Division",
                text="Gross Margin %",
            )
            fig.update_layout(
                xaxis_title="Gross Margin (%)",
                yaxis_title="Division",
            )
            fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
            render_plot(fig, 390)

        st.dataframe(
            ds.style.format(
                {
                    "Sales": "${:,.2f}",
                    "Cost": "${:,.2f}",
                    "Gross_Profit": "${:,.2f}",
                    "Gross Margin %": "{:.1f}%",
                    "Profit per Unit": "${:.2f}",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

        mix = ds.melt(
            id_vars="Division",
            value_vars=["Sales", "Gross_Profit"],
            var_name="Metric",
            value_name="Value",
        )
        mix["Metric"] = mix["Metric"].replace({"Gross_Profit": "Gross Profit"})

        fig = px.bar(
            mix,
            x="Division",
            y="Value",
            color="Metric",
            barmode="group",
            title="Revenue vs Gross Profit",
        )
        fig.update_layout(
            xaxis_title="Division",
            yaxis_title="Value ($)",
        )
        render_plot(fig, 350)

    except Exception as exc:
        st.error(f"Division analysis failed: {exc}")


# ============================================================
# COST & MARGIN ANALYSIS
# ============================================================
elif page == "Cost & Margin Analysis":
    try:
        st.markdown('<div class="section-title">Cost & Margin Diagnostics</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-sub">Identify cost-heavy products, margin pressure and potential pricing or sourcing review areas.</div>',
            unsafe_allow_html=True,
        )

        cm = (
            filtered.groupby(["Division", "Product Name"], as_index=False)
            .agg(
                Sales=("Sales", "sum"),
                Cost=("Cost", "sum"),
                Gross_Profit=("Gross Profit", "sum"),
            )
        )
        cm["Gross Margin %"] = cm["Gross_Profit"] / cm["Sales"].replace(0, pd.NA) * 100
        cm["Cost / Sales %"] = cm["Cost"] / cm["Sales"].replace(0, pd.NA) * 100
        cm["Status"] = cm["Gross Margin %"].apply(
            lambda x: "Margin Watch" if x < margin_threshold else "Monitor"
        )

        left, right = st.columns([1.3, 1])

        with left:
            fig = px.scatter(
                cm,
                x="Cost",
                y="Gross Margin %",
                size="Sales",
                color="Division",
                hover_name="Product Name",
                title="Cost vs Gross Margin Diagnostics",
            )
            fig.update_layout(
                xaxis_title="Cost ($)",
                yaxis_title="Gross Margin (%)",
            )
            fig.add_hline(
                y=margin_threshold,
                line_dash="dash",
                annotation_text=f"{margin_threshold}% threshold",
            )
            render_plot(fig, 450)

        with right:
            risks = cm[cm["Gross Margin %"] < margin_threshold].sort_values("Gross Margin %")
            if risks.empty:
                st.markdown(
                    f'<div class="insight">No products are below the selected {margin_threshold}% margin threshold.</div>',
                    unsafe_allow_html=True,
                )
            else:
                fig = px.bar(
                    risks,
                    x="Gross Margin %",
                    y="Product Name",
                    color="Division",
                    orientation="h",
                    title="Products Below Margin Threshold",
                )
                fig.update_layout(
                    xaxis_title="Gross Margin (%)",
                    yaxis_title="Product",
                    yaxis=dict(automargin=True),
                )
                render_plot(fig, 480)

        st.dataframe(
            cm.rename(
                columns={
                    "Product Name": "Product",
                    "Gross_Profit": "Gross Profit",
                }
            ).style.format(
                {
                    "Sales": "${:,.2f}",
                    "Cost": "${:,.2f}",
                    "Gross Profit": "${:,.2f}",
                    "Gross Margin %": "{:.1f}%",
                    "Cost / Sales %": "{:.1f}%",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

    except Exception as exc:
        st.error(f"Cost and margin analysis failed: {exc}")


# ============================================================
# PARETO ANALYSIS
# ============================================================
elif page == "Pareto Analysis":
    try:
        st.markdown('<div class="section-title">Profit Concentration (Pareto) Analysis</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-sub">Determine how much of total gross profit is concentrated in the leading products.</div>',
            unsafe_allow_html=True,
        )

        pp = (
            filtered.groupby("Product Name", as_index=False)
            .agg(
                Sales=("Sales", "sum"),
                Gross_Profit=("Gross Profit", "sum"),
            )
            .sort_values("Gross_Profit", ascending=False)
            .reset_index(drop=True)
        )

        total = pp["Gross_Profit"].sum()

        if pp.empty or total <= 0:
            st.warning("There is insufficient positive profit for Pareto analysis.")
        else:
            pp["Cumulative Profit %"] = pp["Gross_Profit"].cumsum() / total * 100
            pp["Rank"] = range(1, len(pp) + 1)

            fig = go.Figure()
            fig.add_trace(
                go.Bar(
                    x=pp["Product Name"],
                    y=pp["Gross_Profit"],
                    name="Gross Profit",
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=pp["Product Name"],
                    y=pp["Cumulative Profit %"],
                    name="Cumulative %",
                    yaxis="y2",
                    mode="lines+markers",
                    line=dict(width=3),
                )
            )
            fig.update_layout(
                title="Product Profit Pareto Analysis",
                yaxis=dict(
                    title="Gross Profit ($)",
                    tickfont=dict(color="#34445F", size=11),
                ),
                yaxis2=dict(
                    title="Cumulative Profit (%)",
                    overlaying="y",
                    side="right",
                    range=[0, 105],
                    tickfont=dict(color="#34445F", size=11),
                ),
                xaxis=dict(
                    title="Product",
                    tickangle=0,
                    tickfont=dict(color="#34445F", size=10),
                    automargin=True,
                ),
            )
            render_plot(fig, 500)

            n80 = int((pp["Cumulative Profit %"] < 80).sum()) + 1
            top5_share = pp.head(5)["Gross_Profit"].sum() / total * 100

            c1, c2, c3 = st.columns(3)
            with c1:
                kpi_card("Products to ~80%", str(n80), "Products needed to cross 80%", "80")
            with c2:
                kpi_card("Top Product Share", pct(pp.iloc[0]["Gross_Profit"] / total * 100), "Share of gross profit", "1")
            with c3:
                kpi_card("Top 5 Share", pct(top5_share), "Share of gross profit", "5")

            st.dataframe(
                pp.style.format(
                    {
                        "Sales": "${:,.2f}",
                        "Gross_Profit": "${:,.2f}",
                        "Cumulative Profit %": "{:.1f}%",
                    }
                ),
                use_container_width=True,
                hide_index=True,
            )

    except Exception as exc:
        st.error(f"Pareto analysis failed: {exc}")


# ============================================================
# FACTORY ANALYSIS
# ============================================================
elif page == "Factory Analysis":
    try:
        st.markdown('<div class="section-title">Factory Performance</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-sub">Connect product economics to the project-specified manufacturing facilities.</div>',
            unsafe_allow_html=True,
        )

        fs = (
            filtered.groupby("Factory", as_index=False)
            .agg(
                Sales=("Sales", "sum"),
                Cost=("Cost", "sum"),
                Gross_Profit=("Gross Profit", "sum"),
                Units=("Units", "sum"),
                Products=("Product Name", "nunique"),
            )
        )
        fs["Gross Margin %"] = fs["Gross_Profit"] / fs["Sales"].replace(0, pd.NA) * 100
        fs["Profit per Unit"] = fs["Gross_Profit"] / fs["Units"].replace(0, pd.NA)

        left, right = st.columns(2)

        with left:
            fig = px.bar(
                fs.sort_values("Gross_Profit"),
                x="Gross_Profit",
                y="Factory",
                orientation="h",
                color="Gross Margin %",
                color_continuous_scale="Blues",
                title="Gross Profit by Factory",
            )
            fig.update_layout(
                xaxis_title="Gross Profit ($)",
                yaxis_title="Factory",
                yaxis=dict(automargin=True),
            )
            render_plot(fig, 450)

        with right:
            fig = px.scatter(
                fs,
                x="Sales",
                y="Gross Margin %",
                size="Gross_Profit",
                text="Factory",
                title="Factory Revenue vs Margin",
            )
            fig.update_traces(
                textposition="top center",
                textfont=dict(size=13, color="#101A2F"),
            )
            fig.update_layout(
                xaxis_title="Sales ($)",
                yaxis_title="Gross Margin (%)",
            )
            render_plot(fig, 450)

        st.dataframe(
            fs.style.format(
                {
                    "Sales": "${:,.2f}",
                    "Cost": "${:,.2f}",
                    "Gross_Profit": "${:,.2f}",
                    "Gross Margin %": "{:.1f}%",
                    "Profit per Unit": "${:.2f}",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

    except Exception as exc:
        st.error(f"Factory analysis failed: {exc}")


# ============================================================
# PRODUCT–FACTORY MAP / CORRELATION
# ============================================================
elif page == "Product–Factory Map":
    try:
        st.markdown('<div class="section-title">Products & Factories Correlation</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-sub">Product-to-factory relationships and the geographic footprint defined by the project specification.</div>',
            unsafe_allow_html=True,
        )

        mapping = (
            filtered[
                [
                    "Division",
                    "Product Name",
                    "Factory",
                    "Factory Latitude",
                    "Factory Longitude",
                ]
            ]
            .drop_duplicates()
            .sort_values(["Factory", "Division", "Product Name"])
        )

        left, right = st.columns([1.05, 1.45])

        with left:
            st.markdown('<div class="section-title">Factory Coordinates</div>', unsafe_allow_html=True)
            st.markdown('<div class="section-sub">Latitude and longitude for every project-defined factory.</div>', unsafe_allow_html=True)
            coords = mapping[
                ["Factory", "Factory Latitude", "Factory Longitude"]
            ].drop_duplicates()
            st.dataframe(
                coords.style.format(
                    {
                        "Factory Latitude": "{:.6f}",
                        "Factory Longitude": "{:.6f}",
                    }
                ),
                use_container_width=True,
                hide_index=True,
            )

        with right:
            st.markdown('<div class="section-title">Factory Footprint</div>', unsafe_allow_html=True)
            factory_plot = (
                filtered.groupby(
                    ["Factory", "Factory Latitude", "Factory Longitude"],
                    as_index=False,
                )
                .agg(
                    Sales=("Sales", "sum"),
                    Gross_Profit=("Gross Profit", "sum"),
                    Products=("Product Name", "nunique"),
                )
            )

            fig = px.scatter(
                factory_plot,
                x="Factory Longitude",
                y="Factory Latitude",
                size="Gross_Profit",
                color="Gross_Profit",
                hover_name="Factory",
                hover_data=["Sales", "Products"],
                text="Factory",
                title="Factory Geographic Footprint",
                color_continuous_scale="Blues",
            )
            fig.update_traces(
                textposition="top center",
                textfont=dict(
                    family="Arial, sans-serif",
                    size=13,
                    color="#101A2F",
                ),
                marker=dict(line=dict(width=2, color="#FFFFFF")),
            )
            fig.update_layout(
                xaxis_title="Longitude",
                yaxis_title="Latitude",
                margin=dict(l=55, r=70, t=65, b=55),
            )
            render_plot(fig, 500)

        st.markdown('<div class="section-title">Product–Factory Correlation</div>', unsafe_allow_html=True)
        st.dataframe(mapping, use_container_width=True, hide_index=True)

    except Exception as exc:
        st.error(f"Product-factory analysis failed: {exc}")


# ============================================================
# DATA EXPLORER
# ============================================================
elif page == "Data Explorer":
    try:
        st.markdown('<div class="section-title">Data Explorer</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-sub">Inspect the synthetic transaction-level dataset used by this application.</div>',
            unsafe_allow_html=True,
        )

        columns = [
            "Order ID",
            "Order Date",
            "Ship Date",
            "Division",
            "Region",
            "Product Name",
            "Factory",
            "Sales",
            "Units",
            "Gross Profit",
            "Cost",
            "Gross Margin %",
            "Profit per Unit",
        ]

        selected_columns = st.multiselect(
            "Columns",
            options=[c for c in columns if c in filtered.columns],
            default=columns,
        )

        if selected_columns:
            display = filtered[selected_columns].sort_values(
                "Order Date",
                ascending=False,
            )
            st.dataframe(
                display.style.format(
                    {
                        "Sales": "${:,.2f}",
                        "Gross Profit": "${:,.2f}",
                        "Cost": "${:,.2f}",
                        "Gross Margin %": "{:.1f}%",
                        "Profit per Unit": "${:.2f}",
                    }
                ),
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.info("Select at least one column.")

        try:
            st.markdown('<div class="section-title">Data Quality Checks</div>', unsafe_allow_html=True)
            quality_df = pd.DataFrame({
                "Check": [
                    "Missing values",
                    "Zero / negative sales",
                    "Zero / negative cost",
                    "Zero units",
                    "Duplicate Order IDs",
                ],
                "Count": [
                    int(filtered.isna().sum().sum()),
                    int((filtered["Sales"] <= 0).sum()),
                    int((filtered["Cost"] <= 0).sum()),
                    int((filtered["Units"] <= 0).sum()),
                    int(filtered["Order ID"].duplicated().sum()),
                ],
                "Status": [
                    "PASS" if int(filtered.isna().sum().sum()) == 0 else "REVIEW",
                    "PASS" if int((filtered["Sales"] <= 0).sum()) == 0 else "REVIEW",
                    "PASS" if int((filtered["Cost"] <= 0).sum()) == 0 else "REVIEW",
                    "PASS" if int((filtered["Units"] <= 0).sum()) == 0 else "REVIEW",
                    "PASS" if int(filtered["Order ID"].duplicated().sum()) == 0 else "REVIEW",
                ],
            })
            st.dataframe(quality_df, use_container_width=True, hide_index=True)
        except Exception as exc:
            st.error(f"Data quality checks failed: {exc}")

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            kpi_card("Rows", f"{len(filtered):,}", "Current filtered rows", "▦")
        with c2:
            kpi_card("Orders", f"{filtered['Order ID'].nunique():,}", "Unique orders", "□")
        with c3:
            kpi_card("Products", f"{filtered['Product Name'].nunique():,}", "Unique products", "◇")
        with c4:
            kpi_card("Missing Values", f"{int(filtered.isna().sum().sum()):,}", "Filtered dataset", "✓")

    except Exception as exc:
        st.error(f"Data explorer failed: {exc}")


# ============================================================
# ABOUT PROJECT
# ============================================================
elif page == "About Project":
    try:
        st.markdown('<div class="section-title">About the Project</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-sub">Professional implementation of the requested Product Line Profitability & Margin Performance analysis.</div>',
            unsafe_allow_html=True,
        )

        a, b = st.columns(2)

        with a:
            st.markdown(
                """
                <div class="insight">
                    <b>Business objective</b><br>
                    Sales volume alone can be misleading. The dashboard is designed to reveal
                    which products generate gross profit, where margins are under pressure,
                    how profitability varies by division, and how profit is concentrated.
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <div class="section-title">Core KPIs</div>
                <div class="section-sub">Metrics used throughout the application.</div>
                """,
                unsafe_allow_html=True,
            )

            st.dataframe(
                pd.DataFrame(
                    {
                        "KPI": [
                            "Gross Margin (%)",
                            "Profit per Unit",
                            "Revenue Contribution",
                            "Profit Contribution",
                            "Margin Volatility",
                        ],
                        "Definition": [
                            "Gross Profit ÷ Sales",
                            "Gross Profit ÷ Units",
                            "Product Sales ÷ Total Sales",
                            "Product Profit ÷ Total Profit",
                            "Variation of margin over time",
                        ],
                    }
                ),
                use_container_width=True,
                hide_index=True,
            )

        with b:
            st.markdown(
                """
                <div class="warning">
                    <b>Data mode</b><br>
                    This version intentionally uses deterministic synthetic data generated
                    inside the Python application. It does not depend on a CSV, external
                    API, database, website, network service, or cloud credential.
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <div class="section-title">Application modules</div>
                <div class="section-sub">All requested analytical areas are included.</div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                - Product Profitability Overview
                - Product-level margin leaderboard
                - Profit contribution charts
                - Division Performance Dashboard
                - Revenue vs Profit comparison
                - Margin distribution by division
                - Cost vs Margin Diagnostics
                - Cost-sales scatter analysis
                - Margin risk flags
                - Profit Concentration / Pareto
                - Factory Performance
                - Product–Factory Correlation
                - Factory coordinate analysis
                - Interactive date, division, region, factory and product filters
                - Margin threshold control
                """,
            )

    except Exception as exc:
        st.error(f"About page failed: {exc}")


# ============================================================
# FOOTER — NO EXPORT / DOWNLOAD SECTION
# ============================================================
st.markdown(
    """
    <div class="footer">
        Nassau Candy Profitability Intelligence • Professional Streamlit Application<br>
        Self-contained synthetic demonstration data • No external APIs • No external databases
    </div>
    """,
    unsafe_allow_html=True,
)
