import streamlit as st

def header_home():
    st.markdown("""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <!-- AI Biometric Scan Logo -->
            <svg width="85" height="85" viewBox="0 0 24 24" fill="none" stroke="#E0E3FF" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <!-- Camera/Scan Brackets -->
                <path d="M4 9V5a2 2 0 0 1 2-2h4"></path>
                <path d="M14 3h4a2 2 0 0 1 2 2v4"></path>
                <path d="M20 15v4a2 2 0 0 1-2 2h-4"></path>
                <path d="M10 21H6a2 2 0 0 1-2-2v-4"></path>
                <!-- Person Silhouette -->
                <circle cx="12" cy="10" r="3"></circle>
                <path d="M7 21v-2a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v2"></path>
            </svg>
            <h1 style='text-align:center; color:#E0E3FF; margin-top: 15px;'>SyncClass</h1>
        </div>   
    """, unsafe_allow_html=True)

def header_dashboard():
    st.markdown("""
        <div style="display:flex; align-items:center; justify-content:center; gap:15px; margin-bottom: 20px;">
            <!-- AI Biometric Scan Logo (Dashboard Version) -->
            <svg width="55" height="55" viewBox="0 0 24 24" fill="none" stroke="#5865F2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 9V5a2 2 0 0 1 2-2h4"></path>
                <path d="M14 3h4a2 2 0 0 1 2 2v4"></path>
                <path d="M20 15v4a2 2 0 0 1-2 2h-4"></path>
                <path d="M10 21H6a2 2 0 0 1-2-2v-4"></path>
                <circle cx="12" cy="10" r="3"></circle>
                <path d="M7 21v-2a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v2"></path>
            </svg>
            <h2 style='text-align:left; color:#5865F2; margin: 0;'>SyncClass</h2>
        </div>   
    """, unsafe_allow_html=True)