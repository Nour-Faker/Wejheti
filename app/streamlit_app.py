import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Wejheti — وجهتي",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
    <h1 style='text-align:center; color:#1a73e8;'>🎓 Wejheti — وجهتي</h1>
    <p style='text-align:center; color:#666;'>
        Trouve la meilleure orientation universitaire selon ton score
    </p>
    <hr/>
""", unsafe_allow_html=True)

# Input form
col1, col2 = st.columns(2)

with col1:
    bac_type = st.selectbox("Type de Bac", [
        "Mathematiques", "Sciences", "Technique",
        "Informatique", "Economie", "Lettres", "Sport"
    ])

with col2:
    score = st.number_input(
        "Ton score du Bac",
        min_value=60.0, max_value=220.0,
        value=140.0, step=0.5
    )

limit = st.slider("Nombre de résultats par catégorie", 5, 30, 10)

if st.button("🔍 Trouver mon orientation", use_container_width=True):
    with st.spinner("Analyse en cours..."):
        try:
            resp = requests.post(f"{API_URL}/orientation", json={
                "bac_type": bac_type,
                "score": score,
                "limit": limit
            })
            data = resp.json()
        except Exception as e:
            st.error(f"Erreur de connexion à l'API: {e}")
            st.stop()

    st.markdown(f"""
        <div style='background:#f0f7ff; padding:1rem; border-radius:8px; margin:1rem 0'>
            <b>Bac {bac_type}</b> · Score <b>{score}</b> · 
            {data['total_programs']} filières analysées
        </div>
    """, unsafe_allow_html=True)

    # REACH
    if data["reach"]:
        st.markdown("### 🚀 Filières Ambitieuses")
        st.caption("Score requis supérieur au tien — possible mais challengeant")
        for p in data["reach"]:
            with st.expander(f"{p['filiere_name']} — {p['universite']}"):
                c1, c2, c3 = st.columns(3)
                c1.metric("Score prédit 2026", f"{p['predicted_score_2026']:.1f}")
                c2.metric("Score 2025", f"{p['score_2025']:.1f}")
                c3.metric("Tendance", p['trend'])

    # MATCH
    if data["match"]:
        st.markdown("### 🎯 Dans tes cordes")
        st.caption("Score requis proche du tien — bonne chance d'admission")
        for p in data["match"]:
            with st.expander(f"{p['filiere_name']} — {p['universite']}"):
                c1, c2, c3 = st.columns(3)
                c1.metric("Score prédit 2026", f"{p['predicted_score_2026']:.1f}")
                c2.metric("Score 2025", f"{p['score_2025']:.1f}")
                c3.metric("Tendance", p['trend'])

    # SAFE
    if data["safe"]:
        st.markdown("### ✅ Filières Accessibles")
        st.caption("Score requis inférieur au tien — admission très probable")
        for p in data["safe"]:
            with st.expander(f"{p['filiere_name']} — {p['universite']}"):
                c1, c2, c3 = st.columns(3)
                c1.metric("Score prédit 2026", f"{p['predicted_score_2026']:.1f}")
                c2.metric("Score 2025", f"{p['score_2025']:.1f}")
                c3.metric("Tendance", p['trend'])

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#999; font-size:12px;'>"
    "Wejheti — وجهتي · Prédictions basées sur les données du Ministère de l'Enseignement Supérieur"
    "</p>",
    unsafe_allow_html=True
)