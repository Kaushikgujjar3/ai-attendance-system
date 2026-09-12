import streamlit as st
import time
from PIL import Image
import numpy as np

from src.ui.base_layout import (
    style_background_dashboard,
    style_base_layout
)

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card

from src.pipelines.face_pipeline import (
    predict_attendance,
    get_face_embeddings,
    train_classifier
)

from src.pipelines.voice_pipeline import get_voice_embedding

from src.database.db import (
    get_all_students,
    create_student,
    get_student_subjects,
    get_student_attendance,
    unenroll_student_to_subject
)


def student_dashboard():

    student_data = st.session_state.student_data
    student_id = student_data["student_id"]

    # -----------------------------
    # Header
    # -----------------------------

    c1, c2 = st.columns(
        2,
        vertical_alignment="center",
        gap="xxlarge"
    )

    with c1:
        header_dashboard()

    with c2:

        st.subheader(
            f"Welcome, {student_data['name']}"
        )

        if st.button(
            "Logout",
            type="secondary",
            key="student_logout",
            shortcut="control+backspace"
        ):

            st.session_state["is_logged_in"] = False

            if "student_data" in st.session_state:
                del st.session_state["student_data"]

            st.rerun()

    st.space()

    # -----------------------------
    # Subjects Header
    # -----------------------------

    c1, c2 = st.columns(2)

    with c1:
        st.header("Your Enrolled Subjects")

    with c2:

        if st.button(
            "Enroll in Subject",
            type="primary",
            width="stretch"
        ):
            enroll_dialog()

    st.divider()

    # -----------------------------
    # Load Data
    # -----------------------------

    with st.spinner("Loading your enrolled subjects.."):

        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    # -----------------------------
    # Calculate Attendance
    # -----------------------------

    stats_map = {}

    for log in logs:

        subject_id = log["subject_id"]

        if subject_id not in stats_map:

            stats_map[subject_id] = {
                "total": 0,
                "attended": 0
            }

        stats_map[subject_id]["total"] += 1

        if log.get("is_present"):
            stats_map[subject_id]["attended"] += 1

    # -----------------------------
    # Display Subjects
    # -----------------------------

    cols = st.columns(2)

    for i, sub_node in enumerate(subjects):

        sub = sub_node["subjects"]

        subject_id = sub["subject_id"]

        stats = stats_map.get(
            subject_id,
            {
                "total": 0,
                "attended": 0
            }
        )

        def unenroll_button(
            student_id=student_id,
            subject_id=subject_id,
            subject_name=sub["name"]
        ):

            if st.button(
                "Unenroll from this course",
                type="tertiary",
                width="stretch",
                icon=":material/delete_forever:",
                key=f"unenroll_{student_id}_{subject_id}"
            ):

                unenroll_student_to_subject(
                    student_id,
                    subject_id
                )

                st.toast(
                    f"Unenrolled from {subject_name} successfully!"
                )

                st.rerun()

        with cols[i % 2]:

            subject_card(
                name=sub["name"],
                code=sub["subject_code"],
                section=sub["section"],

                stats=[
                    (
                        "📅",
                        "Total",
                        stats["total"]
                    ),
                    (
                        "✅",
                        "Attended",
                        stats["attended"]
                    )
                ],

                footer_callback=unenroll_button
            )

    footer_dashboard()


def student_screen():

    # -----------------------------
    # Page Styling
    # -----------------------------

    style_background_dashboard()
    style_base_layout()

    # -----------------------------
    # Already Logged In
    # -----------------------------

    if "student_data" in st.session_state:

        student_dashboard()

        return

    # -----------------------------
    # Header
    # -----------------------------

    c1, c2 = st.columns(
        2,
        vertical_alignment="center",
        gap="xxlarge"
    )

    with c1:
        header_dashboard()

    with c2:

        if st.button(
            "Go back to Home",
            type="secondary",
            key="student_back",
            shortcut="control+backspace"
        ):

            st.session_state["login_type"] = None

            st.rerun()

    # -----------------------------
    # Face Login
    # -----------------------------

    st.header(
        "Login using FaceID",
        text_alignment="center"
    )

    st.space()
    st.space()

    show_registration = False

    photo_source = st.camera_input(
        "Position your face in the center"
    )

    # -----------------------------
    # Scan Face
    # -----------------------------

    if photo_source:

        img = np.array(
            Image.open(photo_source)
        )

        with st.spinner("AI is scanning.."):

            detected, all_ids, num_faces = predict_attendance(img)

        # No face
        if num_faces == 0:

            st.warning(
                "Face not found!"
            )

        # Multiple faces
        elif num_faces > 1:

            st.warning(
                "Multiple faces found"
            )

        # Exactly one face
        else:

            # -------------------------
            # Recognized Student
            # -------------------------

            if detected:

                student_id = list(
                    detected.keys()
                )[0]

                all_students = get_all_students()

                student = next(
                    (
                        s
                        for s in all_students
                        if s["student_id"] == student_id
                    ),
                    None
                )

                if student:

                    st.session_state["is_logged_in"] = True
                    st.session_state["user_role"] = "student"
                    st.session_state["student_data"] = student

                    st.toast(
                        f"Welcome Back {student['name']}"
                    )

                    time.sleep(1)

                    st.rerun()

            # -------------------------
            # New Student
            # -------------------------

            else:

                st.info(
                    "Face not recognized! "
                    "You might be a new student!"
                )

                show_registration = True

    # -----------------------------
    # Student Registration
    # -----------------------------

    if show_registration:

        with st.container(border=True):

            st.header(
                "Register new Profile"
            )

            new_name = st.text_input(
                "Enter your name",
                placeholder="E.g. Hamza Rizvi"
            )

            st.subheader(
                "Optional: Voice Enrollment"
            )

            st.info(
                "Enroll your voice for voice-only attendance"
            )

            audio_data = None

            try:

                audio_data = st.audio_input(
                    "Record a short phrase like "
                    "'I am present' or "
                    "'My name is Akash'."
                )

            except Exception:

                st.error(
                    "Audio Data failed!"
                )

            # -------------------------
            # Create Account
            # -------------------------

            if st.button(
                "Create Account",
                type="primary"
            ):

                if not new_name:

                    st.warning(
                        "Please enter your name!"
                    )

                else:

                    with st.spinner(
                        "Creating profile.."
                    ):

                        # Face embedding
                        img = np.array(
                            Image.open(photo_source)
                        )

                        encodings = get_face_embeddings(
                            img
                        )

                        if encodings:

                            face_emb = encodings[0].tolist()

                            # Voice embedding
                            voice_emb = None

                            if audio_data:

                                voice_emb = get_voice_embedding(
                                    audio_data.read()
                                )

                            # Save student
                            response_data = create_student(
                                new_name,
                                face_embedding=face_emb,
                                voice_embedding=voice_emb
                            )

                            if response_data:

                                # Retrain classifier
                                train_classifier()

                                # Login student
                                st.session_state[
                                    "is_logged_in"
                                ] = True

                                st.session_state[
                                    "user_role"
                                ] = "student"

                                st.session_state[
                                    "student_data"
                                ] = response_data[0]

                                st.toast(
                                    f"Profile Created! Hi {new_name}!"
                                )

                                time.sleep(1)

                                st.rerun()

                        else:

                            st.error(
                                "Couldn't capture your "
                                "facial features for registration"
                            )

    # -----------------------------
    # Footer
    # -----------------------------

    footer_dashboard()