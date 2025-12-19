import streamlit as st

st.set_page_config(page_title="CV & LinkedIn Optimizer", layout="wide", page_icon="🎯")

st.title("🎯 Optimizer : Matcher JD vs LinkedIn / CV")

# --- STYLE POUR NETTOYER L'INTERFACE ---
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 14px; }
    .status-box { padding: 20px; border-radius: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.info("💡 Méthode Infaillible : Allez sur le profil LinkedIn, faites Ctrl+A (Tout sélectionner), Ctrl+C (Copier) et collez tout ici. L'IA s'occupe de trier les infos.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Fiche de Poste (Job Desc)")
    job_desc = st.text_area("Besoins du client...", height=300, placeholder="Collez la JD ici...")

with col2:
    st.subheader("👤 Profil (Copier-coller LinkedIn direct)")
    cv_text = st.text_area("Texte brut du profil...", height=300, placeholder="Collez tout le texte LinkedIn ici (même le désordre)...")

st.divider()

if st.button("🚀 Lancer l'Analyse"):
    if job_desc and cv_text:
        with st.spinner('Nettoyage du profil et analyse en cours...'):
            
            # Ici, on simule le moteur qui sépare le nom, les titres et les expériences
            st.success("✅ Profil analysé avec succès !")
            
            # --- RESULTATS ---
            res_col1, res_col2 = st.columns([1, 2])
            
            with res_col1:
                st.metric("Score d'adéquation", "82%")
                st.write("**Stack technique détectée :**")
                st.write("- Java / Spring Boot")
                st.write("- Docker & CI/CD")
                st.write("- PostgreSQL")
            
            with res_col2:
                st.markdown("### ✍️ Pitch pour votre client")
                pitch = f"J'ai analysé le profil de ce consultant par rapport à votre besoin '{job_desc[:30]}...'. Il possède 82% des compétences critiques, notamment sur la partie backend. Son expérience chez son dernier client matche parfaitement avec votre environnement agile."
                st.info(pitch)
                
                st.markdown("### 🚩 Points à vérifier en entretien")
                st.warning("Le profil LinkedIn ne mentionne pas explicitement la maîtrise de Kubernetes. À valider lors de votre call de pré-qualification.")

    else:
        st.error("Veuillez remplir les deux champs.")

st.divider()
st.caption("Note : Cette version simule l'analyse. Pour une analyse réelle, nous connecterons l'API OpenAI/Gemini à l'étape du Cockpit.")
