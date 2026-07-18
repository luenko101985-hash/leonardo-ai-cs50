import streamlit as st


CURRENT_CONCEPT = "current_concept"
CURRENT_CONCEPT_ID = "current_concept_id"
LEONARDO_ASSET = "leonardo_visual_asset"
BLUEPRINT_ASSET = "blueprint_visual_asset"
CURRENT_PAGE = "page"

_LEGACY_LOADED_CONCEPT = "loaded_concept"
_LEGACY_GENERATED_CONCEPT = "generated_concept"
_DEFAULT_PAGE = "app"


def initialize_session_state() -> None:
    if CURRENT_CONCEPT not in st.session_state:
        legacy_concept = st.session_state.get(_LEGACY_LOADED_CONCEPT)
        if legacy_concept is None:
            legacy_concept = st.session_state.get(_LEGACY_GENERATED_CONCEPT)
        st.session_state[CURRENT_CONCEPT] = legacy_concept

    if CURRENT_CONCEPT_ID not in st.session_state:
        st.session_state[CURRENT_CONCEPT_ID] = None

    if LEONARDO_ASSET not in st.session_state:
        st.session_state[LEONARDO_ASSET] = None

    if BLUEPRINT_ASSET not in st.session_state:
        st.session_state[BLUEPRINT_ASSET] = None

    if CURRENT_PAGE not in st.session_state:
        st.session_state[CURRENT_PAGE] = _DEFAULT_PAGE


def set_current_concept(concept_data, concept_id) -> None:
    st.session_state[CURRENT_CONCEPT] = concept_data
    st.session_state[CURRENT_CONCEPT_ID] = concept_id


def clear_current_concept() -> None:
    st.session_state[CURRENT_CONCEPT] = None
    st.session_state[CURRENT_CONCEPT_ID] = None
    st.session_state[LEONARDO_ASSET] = None
    st.session_state[BLUEPRINT_ASSET] = None


def clear_transient_visuals() -> None:
    st.session_state[LEONARDO_ASSET] = None
    st.session_state[BLUEPRINT_ASSET] = None


def get_current_concept() -> dict | None:
    return st.session_state.get(CURRENT_CONCEPT)


def get_current_concept_id() -> int | None:
    return st.session_state.get(CURRENT_CONCEPT_ID)


def get_current_page() -> str:
    return st.session_state.get(CURRENT_PAGE, _DEFAULT_PAGE)


def set_current_page(page: str) -> None:
    st.session_state[CURRENT_PAGE] = page
