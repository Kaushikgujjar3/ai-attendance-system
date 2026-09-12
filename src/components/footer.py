import streamlit as st

def footer_home():
    st.markdown("""
        <!-- Subtle divider line -->
        <hr style="border: none; border-top: 1px solid rgba(255, 255, 255, 0.1); margin: 4rem 0 1.5rem 0;">
        
        <div style="display:flex; justify-content:center; align-items:center;">
            <p style="font-family: 'Inter', sans-serif; font-size: 0.9rem; color: #a1a1aa; margin: 0;">
                Created with by <span style="color: #bb86fc; font-weight: 600; letter-spacing: 0.5px;">SyncCLASS</span>
            </p> 
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():
    st.markdown("""
        <!-- Subtle divider line -->
        <hr style="border: none; border-top: 1px solid rgba(255, 255, 255, 0.1); margin: 4rem 0 1.5rem 0;">
        
        <div style="display:flex; justify-content:center; align-items:center;">
            <p style="font-family: 'Inter', sans-serif; font-size: 0.85rem; color: #a1a1aa; margin: 0;">
                Created with by <span style="color: #5865F2; font-weight: 600; letter-spacing: 0.5px;">SyncCLASS</span>
            </p> 
        </div>
    """, unsafe_allow_html=True)