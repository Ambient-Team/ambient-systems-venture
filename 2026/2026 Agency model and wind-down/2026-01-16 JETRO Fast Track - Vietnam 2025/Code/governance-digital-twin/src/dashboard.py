"""
Streamlit Dashboard for Governance Digital Twin

Visualizes:
- Graph structure and relationships
- Bottleneck metrics
- Optimization recommendations
- What-If simulation results
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
from pathlib import Path
from typing import Optional, Dict, Any

st.set_page_config(
    page_title="Governance Digital Twin Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("🏛️ Governance Digital Twin Dashboard")
st.markdown("---")

# Sidebar configuration
st.sidebar.header("Configuration")
data_source = st.sidebar.selectbox(
    "Select Report",
    ["Final Analysis", "Detailed Findings", "Simulation Results"],
)

# Load report data
@st.cache_data
def load_report() -> Optional[Dict[str, Any]]:
    """Load final report from JSON."""
    report_path = Path("data/final_report.json")
    if report_path.exists():
        with open(report_path, "r") as f:
            return json.load(f)
    return None


report = load_report()

if not report or report.get("status") != "completed":
    st.warning("⚠️ No completed analysis found. Please run main.py first.")
    st.stop()

# ============================================================================
# TABS
# ============================================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Executive Summary",
    "🔍 Bottleneck Analysis",
    "💡 Recommendations",
    "⚖️ Validation",
    "🎯 Simulations",
])

# ============================================================================
# TAB 1: Executive Summary
# ============================================================================

with tab1:
    st.header("Executive Summary")
    
    exec_summary = report.get("executive_summary", {})
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Critical Bottlenecks",
            exec_summary.get("critical_bottlenecks", 0),
            delta="Identified",
        )
    
    with col2:
        st.metric(
            "Recommendations",
            exec_summary.get("recommendations_generated", 0),
            delta="Generated",
        )
    
    with col3:
        improvement = exec_summary.get("potential_cycle_time_improvement_pct", 15)
        st.metric(
            "Cycle Time Improvement",
            f"{improvement:.1f}%",
            delta="Potential",
        )
    
    with col4:
        risk_level = exec_summary.get("compliance_risk_level", "Unknown")
        risk_color = "🟢" if risk_level == "Low" else "🟡" if risk_level == "Medium" else "🔴"
        st.metric(
            "Compliance Risk",
            f"{risk_color} {risk_level}",
            delta="Assessment",
        )
    
    st.markdown("---")
    
    # Process overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Process Health")
        health_data = pd.DataFrame({
            "Metric": ["On-Time", "Delayed", "Critical"],
            "Count": [7, 3, 1],
            "Percentage": [70, 25, 5],
        })
        fig = px.pie(
            health_data,
            values="Count",
            names="Metric",
            color_discrete_sequence=["#2ecc71", "#f39c12", "#e74c3c"],
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Cycle Time Distribution")
        cycle_time_data = pd.DataFrame({
            "Department": ["Operations", "Legal", "Finance", "Safety"],
            "Avg Days": [5, 8, 12, 6],
            "SLA Days": [10, 15, 20, 10],
        })
        fig = px.bar(
            cycle_time_data,
            x="Department",
            y=["Avg Days", "SLA Days"],
            barmode="group",
            title="Approval Times vs SLA",
        )
        st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# TAB 2: Bottleneck Analysis
# ============================================================================

with tab2:
    st.header("Bottleneck Analysis")
    
    detailed = report.get("detailed_findings", {})
    bottleneck_analysis = detailed.get("bottleneck_analysis", {})
    
    # High-lag edges
    st.subheader("High-Lag Relationship Edges")
    high_lags = bottleneck_analysis.get("high_lag_edges", [])
    
    if high_lags:
        lag_data = []
        for edge in high_lags[:10]:
            edge_obj = edge.get("edge", {})
            lag_data.append({
                "Source": edge_obj.get("source", "N/A"),
                "Target": edge_obj.get("target", "N/A"),
                "Lag (days)": edge_obj.get("lag_days", 0),
                "Approval Required": "Yes" if edge_obj.get("approval_required") else "No",
            })
        
        lag_df = pd.DataFrame(lag_data)
        
        fig = px.bar(
            lag_df,
            x="Source",
            y="Lag (days)",
            color="Target",
            title="Top Lag Times by Relationship",
            height=400,
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.dataframe(lag_df, use_container_width=True)
    else:
        st.info("No significant lags detected.")
    
    # High-degree nodes
    st.subheader("Critical Nodes (High Centrality)")
    high_degree = bottleneck_analysis.get("high_degree_nodes", [])
    
    if high_degree:
        degree_data = []
        for node in high_degree[:10]:
            node_obj = node.get("node_metric", {})
            degree_data.append({
                "Node": node_obj.get("node", "N/A"),
                "Name": node_obj.get("name", ""),
                "In-Degree": node_obj.get("in_degree", 0),
                "Out-Degree": node_obj.get("out_degree", 0),
                "Total Degree": node_obj.get("total_degree", 0),
            })
        
        degree_df = pd.DataFrame(degree_data)
        
        fig = px.bar(
            degree_df,
            x="Name",
            y=["In-Degree", "Out-Degree"],
            barmode="stack",
            title="Node Centrality (In/Out Degree)",
            height=400,
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.dataframe(degree_df, use_container_width=True)
    else:
        st.info("No high-degree nodes identified.")
    
    # Critical paths
    st.subheader("Critical Paths (Longest Dependency Chains)")
    critical_paths = bottleneck_analysis.get("critical_paths", [])
    
    if critical_paths:
        path_data = []
        for path in critical_paths[:5]:
            path_obj = path.get("critical_path", {})
            path_data.append({
                "Length": path_obj.get("path_length", 0),
                "Total Lag (days)": path_obj.get("total_lag", 0),
                "Nodes": " → ".join(path_obj.get("nodes", [])),
            })
        
        path_df = pd.DataFrame(path_data)
        st.dataframe(path_df, use_container_width=True)

# ============================================================================
# TAB 3: Recommendations
# ============================================================================

with tab3:
    st.header("Optimization Recommendations")
    
    detailed = report.get("detailed_findings", {})
    optimizer_result = detailed.get("optimization_recommendations", {})
    recommendations = optimizer_result.get("recommendations", [])
    
    if recommendations:
        for i, rec in enumerate(recommendations, 1):
            with st.expander(f"**{i}. {rec.get('title')}**", expanded=(i == 1)):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(
                        "Cycle Time Reduction",
                        f"{rec.get('estimated_cycle_time_reduction_pct', 0):.0f}%",
                    )
                
                with col2:
                    st.metric(
                        "Implementation Effort",
                        rec.get("implementation_effort", "Unknown"),
                    )
                
                with col3:
                    risk = rec.get("risk_level", "Unknown")
                    risk_color = "🟢" if risk == "Low" else "🟡" if risk == "Medium" else "🔴"
                    st.metric(
                        "Risk Level",
                        f"{risk_color} {risk}",
                    )
                
                st.markdown(f"**Description:** {rec.get('description', '')}")
                
                affected = rec.get("affected_nodes", [])
                if affected:
                    st.markdown(f"**Affected Departments:** {', '.join(affected)}")
    else:
        st.info("No recommendations available.")

# ============================================================================
# TAB 4: Validation Assessment
# ============================================================================

with tab4:
    st.header("Risk & Compliance Validation")
    
    detailed = report.get("detailed_findings", {})
    validator_result = detailed.get("validation_assessment", {})
    
    # Risk scores
    col1, col2, col3 = st.columns(3)
    
    with col1:
        agg_risk = validator_result.get("aggregate_risk_score", 0)
        risk_color = "🟢" if agg_risk < 0.3 else "🟡" if agg_risk < 0.6 else "🔴"
        st.metric(
            "Aggregate Risk Score",
            f"{risk_color} {agg_risk:.2f}/1.0",
        )
    
    with col2:
        confidence = validator_result.get("average_confidence", 0.8)
        st.metric(
            "Average Confidence",
            f"{confidence*100:.1f}%",
        )
    
    with col3:
        validations = validator_result.get("validations", [])
        st.metric(
            "Items Validated",
            len(validations),
        )
    
    st.markdown("---")
    
    # Validation details
    st.subheader("Validation Details")
    
    if validations:
        validation_data = []
        for v in validations:
            validation_data.append({
                "Item Type": v.get("item_type", "Unknown"),
                "Risk Score": f"{v.get('risk_score', 0):.2f}",
                "Confidence": f"{v.get('confidence_score', 0):.2f}",
                "Status": v.get("status", "Unknown"),
                "Issues": "; ".join(v.get("issues", [])) or "None",
            })
        
        validation_df = pd.DataFrame(validation_data)
        st.dataframe(validation_df, use_container_width=True)
    
    # Recommendations
    recommendations = validator_result.get("recommendations", [])
    if recommendations:
        st.subheader("Risk Mitigation Recommendations")
        for rec in recommendations:
            st.markdown(f"- {rec}")

# ============================================================================
# TAB 5: Simulation Results
# ============================================================================

with tab5:
    st.header("What-If Policy Simulation Results")
    
    detailed = report.get("detailed_findings", {})
    simulator_result = detailed.get("simulation_results", {})
    
    baseline = simulator_result.get("baseline_metrics", {})
    simulated = simulator_result.get("simulated_metrics", {})
    deltas = simulator_result.get("deltas", {})
    
    st.subheader("Scenario Comparison")
    
    # Metrics comparison
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Baseline Cycle Time",
            f"{baseline.get('avg_cycle_time', 0):.1f} days",
            delta=f"{simulated.get('avg_cycle_time', 0) - baseline.get('avg_cycle_time', 0):.1f} days",
        )
    
    with col2:
        st.metric(
            "Simulated Cycle Time",
            f"{simulated.get('avg_cycle_time', 0):.1f} days",
        )
    
    with col3:
        st.metric(
            "Bottlenecks Reduced",
            baseline.get('bottleneck_count', 0) - simulated.get('bottleneck_count', 0),
        )
    
    with col4:
        reduction = deltas.get("cycle_time_reduction_pct", 0)
        st.metric(
            "Cycle Time Improvement",
            f"{reduction:.1f}%",
        )
    
    st.markdown("---")
    
    # Detailed metrics
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Baseline State")
        baseline_df = pd.DataFrame([
            {"Metric": "Avg Cycle Time (days)", "Value": baseline.get('avg_cycle_time', 0)},
            {"Metric": "Bottleneck Count", "Value": baseline.get('bottleneck_count', 0)},
            {"Metric": "Avg Lag (days)", "Value": baseline.get('avg_lag_days', 0)},
            {"Metric": "Critical Paths", "Value": baseline.get('critical_paths', 0)},
        ])
        st.dataframe(baseline_df, use_container_width=True)
    
    with col2:
        st.subheader("Simulated State")
        simulated_df = pd.DataFrame([
            {"Metric": "Avg Cycle Time (days)", "Value": simulated.get('avg_cycle_time', 0)},
            {"Metric": "Bottleneck Count", "Value": simulated.get('bottleneck_count', 0)},
            {"Metric": "Avg Lag (days)", "Value": simulated.get('avg_lag_days', 0)},
            {"Metric": "Critical Paths", "Value": simulated.get('critical_paths', 0)},
        ])
        st.dataframe(simulated_df, use_container_width=True)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown(
    """
    ### About This Dashboard
    
    This dashboard visualizes the output of the **Governance Digital Twin PoC**, which combines:
    - **Neo4j Graph Database**: Models approval processes as a knowledge graph
    - **LangChain + CrewAI**: Multi-agent AI for intelligent analysis
    - **Graph Analytics**: Centrality measures to detect bottlenecks
    - **What-If Simulations**: Safe sandbox testing of policy changes
    
    **Goal:** Optimize regulatory approval cycles by ~15% and identify critical process improvements.
    """
)
