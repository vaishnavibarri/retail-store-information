import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# -----------------------------------------------------------------------------
# 1. Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Retail Store Operations Dashboard",
    page_icon="🛍️",
    layout="wide"
)

# Custom Styling for Metric Cards & Badges
st.markdown("""
    <style>
    .metric-container {
        background-color: #FFFFFF;
        padding: 10px 15px;
        border-radius: 8px;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #475569;
        font-weight: 500;
        margin-bottom: 4px;
    }
    .metric-value {
        font-size: 2.1rem;
        font-weight: 700;
        color: #1E293B;
        line-height: 1.1;
    }
    .badge {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-top: 8px;
    }
    .badge-green { background-color: #DCFCE7; color: #166534; }
    .badge-red { background-color: #FEE2E2; color: #991B1B; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. Mock Data Setup (Matching Visualized Data Points)
# -----------------------------------------------------------------------------
products = ['Ergonomic Chair', 'Smartwatch', 'Wireless Headphones', 'Mechanical Keyboard', 'USB-C Hub']
revenue_by_prod = [240000, 190000, 144000, 65000, 16000]
stock_levels = [16, 12, 16, 8, 16]
reorder_points = [16, 14, 16, 10, 16]

months = ['Jan 2025', 'Feb 2025', 'Mar 2025', 'Apr 2025', 'May 2025', 'Jun 2025', 
          'Jul 2025', 'Aug 2025', 'Sep 2025', 'Oct 2025', 'Nov 2025', 'Dec 2025']
revenue_trend = [48000, 58000, 54000, 64000, 72000, 68000, 74000, 62000, 68000, 76000, 84000, 92000]
transferred_units = [320, 420, 390, 510, 480, 610, 550, 630, 500, 580, 690, 740]

# -----------------------------------------------------------------------------
# 3. Header Section
# -----------------------------------------------------------------------------
st.markdown("### 🛍️ Retail Store Operations Dashboard")
st.markdown("<p style='color: #64748B; margin-top: -15px;'>Academic Presentation | <i>Performance, Inventory, & CSAT Metrics</i></p>", unsafe_allow_html=True)

st.markdown("<hr style='margin: 15px 0 25px 0; border: none; border-top: 1px solid #E2E8F0;'>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. Key Performance Indicator (KPI) Row
# -----------------------------------------------------------------------------
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown("""
        <div class="metric-container">
            <div class="metric-label">Total Annual Revenue</div>
            <div class="metric-value">$889,000.00</div>
            <span class="badge badge-green">↑ +12.5% YoY</span>
        </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown("""
        <div class="metric-container">
            <div class="metric-label">Transferred Stock Units</div>
            <div class="metric-value">6,400</div>
            <span class="badge badge-red">↓ -3% MoM</span>
        </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown("""
        <div class="metric-container">
            <div class="metric-label">Low Stock Alerts</div>
            <div class="metric-value">2 Products</div>
            <span class="badge badge-red">↑ Action Needed</span>
        </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown("""
        <div class="metric-container">
            <div class="metric-label">Customer Satisfaction (CSAT)</div>
            <div class="metric-value">4.2 / 5.0</div>
            <span class="badge badge-green">↑ +0.3</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='margin: 25px 0; border: none; border-top: 1px solid #E2E8F0;'>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. Middle Charts: Monthly Trend Combo & CSAT Score Gauge
# -----------------------------------------------------------------------------
col_trend, col_gauge = st.columns([1.8, 1])

with col_trend:
    st.markdown("#### 📈 Monthly Revenue & Transferred Units")
    
    # Dual-axis Bar + Line Chart
    fig_combo = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig_combo.add_trace(
        go.Bar(
            x=months, 
            y=revenue_trend, 
            name="Revenue ($)", 
            marker_color="#1D70B8"
        ),
        secondary_y=False,
    )

    fig_combo.add_trace(
        go.Scatter(
            x=months, 
            y=transferred_units, 
            name="Transferred Units", 
            mode="lines+markers", 
            line=dict(color="#FF7F0E", width=3),
            marker=dict(size=6)
        ),
        secondary_y=True,
    )

    fig_combo.update_layout(
        template="plotly_white",
        height=380,
        margin=dict(l=10, r=10, t=20, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    fig_combo.update_xaxes(tickangle=-30)
    fig_combo.update_yaxes(title_text="Revenue ($)", secondary_y=False)
    fig_combo.update_yaxes(title_text="Transferred Units", secondary_y=True)

    st.plotly_chart(fig_combo, use_container_width=True)

with col_gauge:
    st.markdown("#### ⭐ CSAT Score Gauge")
    
    # Semi-Circle Gauge Chart
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=4.2,
        number={'suffix': "", 'font': {'size': 50}},
        gauge={
            'axis': {'range': [0, 5], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "rgba(0,0,0,0)"},
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
                {'range': [0, 2], 'color': '#F87171'},
                {'range': [2, 4], 'color': '#FBBF24'},
                {'range': [4, 5], 'color': '#4ADE80'}
            ],
            'threshold': {
                'line': {'color': "#1E293B", 'width': 4},
                'thickness': 0.75,
                'value': 4.2
            }
        }
    ))

    fig_gauge.update_layout(
        template="plotly_white",
        height=380,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig_gauge, use_container_width=True)

# -----------------------------------------------------------------------------
# 6. Bottom Charts: Revenue by Product & Inventory vs Targets
# -----------------------------------------------------------------------------
col_prod_rev, col_stock = st.columns([1.3, 1])

with col_prod_rev:
    st.markdown("#### 💰 Revenue by Product")
    
    # Horizontal Bar Chart
    df_prod = pd.DataFrame({'Product': products, 'Revenue': revenue_by_prod}).sort_values('Revenue', ascending=True)
    
    fig_prod_bar = px.bar(
        df_prod,
        y='Product',
        x='Revenue',
        orientation='h',
        text_auto='$,.0f',
        color_discrete_sequence=['#0066CC']
    )
    
    fig_prod_bar.update_traces(textposition='inside', textfont=dict(color='white', weight='bold'))
    fig_prod_bar.update_layout(
        template="plotly_white",
        xaxis_title="Revenue ($)",
        yaxis_title="Product",
        height=360,
        margin=dict(l=10, r=10, t=20, b=20)
    )
    
    st.plotly_chart(fig_prod_bar, use_container_width=True)

with col_stock:
    st.markdown("#### 📦 Stock vs Reorder Level")
    
    # Grouped Column Bar Chart for Stock Inventory
    fig_stock = go.Figure(data=[
        go.Bar(name='Stock Level', x=products, y=stock_levels, marker_color='#0066CC'),
        go.Bar(name='Reorder Point', x=products, y=reorder_points, marker_color='#7DD3FC')
    ])
    
    fig_stock.update_layout(
        barmode='group',
        template="plotly_white",
        yaxis_title="Units",
        xaxis_title="Product",
        height=360,
        margin=dict(l=10, r=10, t=20, b=20),
        legend=dict(orientation="v", yanchor="top", y=1, xanchor="left", x=1.02)
    )
    fig_stock.update_xaxes(tickangle=-30)

    st.plotly_chart(fig_stock, use_container_width=True)