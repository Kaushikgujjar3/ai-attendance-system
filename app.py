import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    
    st.set_page_config(
        page_title="SyncClass - Make Attendance faster using AI",
       page_icon = """<svg width="85" height="85" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <!-- Camera/Scan Brackets -->
    <path d="M4 9V5a2 2 0 0 1 2-2h4"></path>
    <path d="M14 3h4a2 2 0 0 1 2 2v4"></path>
    <path d="M20 15v4a2 2 0 0 1-2 2h-4"></path>
    <path d="M10 21H6a2 2 0 0 1-2-2v-4"></path>
    <!-- Person Silhouette -->
    <circle cx="12" cy="10" r="3"></circle>
    <path d="M7 21v-2a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v2"></path>
</svg>"""
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None
        
    match st.session_state["login_type"]:
        case 'teacher':
            teacher_screen()
            
        case 'student':
            student_screen()
            
        case None:
            home_screen()
            

    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
    
    
main()