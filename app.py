import os
import streamlit as st
import pandas as pd
import random
import re
from datetime import datetime, timedelta

# --- 1. CONFIG & ROBUST PATHING ---
st.set_page_config(page_title="CTI & Awareness Dashboard", page_icon="🛡️", layout="wide")

# This forces the app to look in the exact absolute directory of your project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_PATH = os.path.join(DATA_DIR, "synthetic_threats.csv")

# --- 2. SYNTHETIC DATA GENERATOR ---
def generate_synthetic_data():
    os.makedirs(DATA_DIR, exist_ok=True)
    
    categories = ["PHISHING", "MALWARE", "RANSOMWARE", "CREDENTIAL THREATS", "NETWORK THREATS"]
    indicator_types = ["IP ADDRESS", "DOMAIN", "URL", "FILE HASH", "CVE ID"]
    statuses = ["NEW", "UNDER_REVIEW", "MONITORING", "CLOSED", "FALSE_POSITIVE"]
    
    data = []
    for i in range(200):
        category = random.choice(categories)
        itype = random.choice(indicator_types)
        
        if itype == "IP ADDRESS": val = f"198.51.100.{random.randint(1, 255)}"
        elif itype == "DOMAIN": val = f"malicious-demo-{i}.example.com"
        elif itype == "URL": val = f"http://example.com/safe-demo-path-{i}"
        elif itype == "FILE HASH": val = f"demo-hash-sha256-{random.randint(1000, 9999)}"
        else: val = f"CVE-2026-{random.randint(1000, 9999)}"
            
        risk = random.randint(10, 100)
        confidence = random.randint(10, 100)
        
        if risk < 20: severity = "INFORMATIONAL"
        elif risk < 40: severity = "LOW"
        elif risk < 60: severity = "MEDIUM"
        elif risk < 80: severity = "HIGH"
        else: severity = "CRITICAL"

        data.append({
            "threat_id": f"THR-2026-{i:04d}",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d"),
            "category": category,
            "indicator_type": itype,
            "indicator_value": val,
            "severity": severity,
            "risk_score": risk,
            "confidence_score": confidence,
            "status": random.choice(statuses)
        })
    
    df = pd.DataFrame(data)
    df.to_csv(DATA_PATH, index=False)
    return df

@st.cache_data
def load_data():
    # If the file doesn't exist or is 0 bytes, generate new data
    if not os.path.exists(DATA_PATH) or os.path.getsize(DATA_PATH) == 0:
        return generate_synthetic_data()
    return pd.read_csv(DATA_PATH)

# --- 3. IOC VALIDATION ENGINE ---
def validate_indicator(indicator):
    if re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", indicator):
        return "IP ADDRESS", True
    elif re.match(r"^CVE-\d{4}-\d{4,}$", indicator, re.IGNORECASE):
        return "CVE ID", True
    elif "example.com" in indicator or "example.org" in indicator:
        return "DOMAIN", True
    return "UNKNOWN", False

# --- 4. UI ROUTING ---
df = load_data()

st.sidebar.title("🛡️ CTI Dashboard")
menu = st.sidebar.radio("Navigation", ["SOC Dashboard", "IOC Search", "Awareness Center"])

# --- 5. SOC DASHBOARD ---
if menu == "SOC Dashboard":
    st.header("SOC Threat Intelligence Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Threat Records", len(df))
    col2.metric("Critical Threats", len(df[df['severity'] == 'CRITICAL']))
    col3.metric("Active Investigations", len(df[df['status'] == 'UNDER_REVIEW']))
    col4.metric("Average Risk Score", f"{df['risk_score'].mean():.1f}/100")
    
    st.subheader("Recent Threat Activity")
    st.dataframe(df.sort_values(by="timestamp", ascending=False).head(15), use_container_width=True)

# --- 6. IOC SEARCH ---
elif menu == "IOC Search":
    st.header("IOC Lookup & Validation Engine")
    st.write("Search the synthetic database for known defensive indicators.")
    
    search_val = st.text_input("Enter Indicator (IP, Domain, Hash, CVE):")
    if search_val:
        itype, is_valid = validate_indicator(search_val)
        if not is_valid:
            st.warning(f"Indicator '{search_val}' format is not recognized or is not a safe demo domain.")
        else:
            match = df[df['indicator_value'] == search_val]
            if not match.empty:
                st.success(f"Indicator Found! Type: {itype}")
                st.dataframe(match, use_container_width=True)
            else:
                st.info(f"Syntactically valid {itype}, but no historical records found in local telemetry.")

# --- 7. AWARENESS CENTER ---
elif menu == "Awareness Center":
    st.header("Cybersecurity Awareness Center")
    st.write("Human defense combined with technical threat intelligence.")
    
    st.subheader("Phishing Awareness Quiz")
    st.write("You receive an unexpected message asking you to urgently verify your password. What should you do?")
    ans = st.radio("Select action:", ["Click immediately", "Reply with password", "Verify through an official trusted channel", "Forward credentials"], index=None)
    
    if st.button("Submit Answer"):
        if ans == "Verify through an official trusted channel":
            st.success("Correct! Always verify urgent requests independently. Phishing relies on artificial urgency.")
        elif ans:
            st.error("Incorrect. Never click links or reply with passwords to unexpected, urgent requests.")