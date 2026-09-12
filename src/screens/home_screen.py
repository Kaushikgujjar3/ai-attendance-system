import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout


def home_screen():
    header_home()
    style_base_layout()

    # Dark gradient background + polish to match the purple/pink accent palette
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #1a1425 0%, #14151f 45%, #1f1420 75%, #23142a 100%) !important;
                background-attachment: fixed !important;
            }

            /* Soft glow accents echoing the purple/pink icon colors */
            .stApp::before {
                content: "";
                position: fixed;
                top: -180px;
                left: -140px;
                width: 480px;
                height: 480px;
                background: radial-gradient(circle, rgba(187,134,252,0.16) 0%, rgba(187,134,252,0) 70%);
                pointer-events: none;
                z-index: 0;
            }
            .stApp::after {
                content: "";
                position: fixed;
                bottom: -180px;
                right: -140px;
                width: 480px;
                height: 480px;
                background: radial-gradient(circle, rgba(255,121,198,0.14) 0%, rgba(255,121,198,0) 70%);
                pointer-events: none;
                z-index: 0;
            }

            /* Glass card panels around each portal option */
            div[data-testid="column"] > div[data-testid="stVerticalBlock"] {
                background: rgba(255,255,255,0.035);
                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 1.75rem;
                padding: 2.5rem 1.75rem 2rem 1.75rem;
                backdrop-filter: blur(6px);
                box-shadow: 0 12px 32px rgba(0,0,0,0.35);
                transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
                position: relative;
                z-index: 1;
            }
            div[data-testid="column"]:nth-of-type(1) > div[data-testid="stVerticalBlock"]:hover {
                transform: translateY(-6px);
                border-color: rgba(187,134,252,0.4);
                box-shadow: 0 18px 42px rgba(187,134,252,0.18);
            }
            div[data-testid="column"]:nth-of-type(2) > div[data-testid="stVerticalBlock"]:hover {
                transform: translateY(-6px);
                border-color: rgba(255,121,198,0.4);
                box-shadow: 0 18px 42px rgba(255,121,198,0.18);
            }

            /* Subtle glow behind each SVG icon */
            .icon-glow {
                display: flex;
                justify-content: center;
                margin: 25px 0;
                position: relative;
            }
            .icon-glow::before {
                content: "";
                position: absolute;
                width: 110px;
                height: 110px;
                border-radius: 50%;
                background: radial-gradient(circle, var(--glow-color) 0%, transparent 70%);
                z-index: 0;
            }
            .icon-glow svg {
                position: relative;
                z-index: 1;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    # --- STUDENT HUB ACCESS ---
    with col1:
        st.markdown("""
            <div style="text-align: center;">
                <h2 style="color: #bb86fc; font-weight: 700; text-transform: uppercase; letter-spacing: 7px;">
                    Student Portal
                </h2>
                <!-- Minimal Modern Student SVG Icon -->
                <div class="icon-glow" style="--glow-color: rgba(187,134,252,0.35);">
                    <svg width="90" height="90" viewBox="0 0 24 24" fill="none" stroke="#bb86fc" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M22 10v6M2 10l10-5 10 5-10 5z"></path>
                        <path d="M6 12v5c3 3 9 3 12 0v-5"></path>
                    </svg>
                </div>
                <p style="color: #aeb9cc; font-size: 0.95rem; margin-bottom: 30px;">
                    Seamlessly check in and track your daily attendance.
                </p>
            </div>
        """, unsafe_allow_html=True)

        if st.button('Log In As Student', type='primary', use_container_width=True):
            st.session_state['login_type'] = 'student'
            st.rerun()

    # --- TEACHER CONTROL TERMINAL ---
    with col2:
        st.markdown("""
            <div style="text-align: center;">
                <h2 style="color: #ff79c6; font-weight: 700; text-transform: uppercase; letter-spacing: 7px;">
                    Teacher Portal
                </h2>
                <!-- Minimal Modern Instructor SVG Icon -->
                <div class="icon-glow" style="--glow-color: rgba(255,121,198,0.35);">
                    <svg width="90" height="90" viewBox="0 0 24 24" fill="none" stroke="#ff79c6" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
                        <circle cx="9" cy="7" r="4"></circle>
                        <path d="M22 21v-2a4 4 0 0 0-3-3.87"></path>
                        <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                    </svg>
                </div>
                <p style="color: #aeb9cc; font-size: 0.95rem; margin-bottom: 30px;">
                    Automate roll calls, manage rosters, and generate reports.
                </p>
            </div>
        """, unsafe_allow_html=True)

        if st.button('Log In As Teacher', type='secondary', use_container_width=True):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()