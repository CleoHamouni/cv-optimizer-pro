import streamlit as st

st.set_page_config(page_title="CV Optimizer Pro", layout="wide", page_icon="📝")

st.title("📝 CV Optimizer : Matcher vs Fiche de Poste")
st.markdown("Optimisez la présentation de vos consultants pour maximiser les chances de closing.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Besoins du Client")
    job_desc = st.text_area("Collez ici la Fiche de Poste (Job Desc)", height=250, placeholder="Ex: Recherche expert Java avec expérience Cloud AWS...")

with col2:
    st.subheader("📄 CV du Consultant")
    cv_text = st.text_area("Collez ici le contenu du CV", height=250, placeholder="Expériences, diplômes, compétences...")

st.divider()

if st.button("🚀 Analyser & Optimiser"):
    if job_desc and cv_text:
        with st.spinner('L\'IA analyse les correspondances...'):
            # Simulation de l'analyse IA (On peut connecter une vraie API plus tard)
            st.subheader("💡 Recommandations d'optimisation")
            
            c1, c2, c3 = st.columns(3)
            
            with c1:
                st.info("✅ Points Forts")
                st.write("- Stack technique alignée")
                st.write("- Années d'expérience suffisantes")
            
            with c2:
                st.warning("⚠️ Mots-clés manquants")
                st.write("- CI/CD (Jenkins/GitLab)")
                st.write("- Méthodologie Agile / Scrum")
                st.write("- Tests unitaires")
            
            with c3:
                st.success("✍️ Accroche suggérée")
                st.write("Consultant expert avec une solide maîtrise de la stack demandée, ayant déjà évolué dans des contextes similaires...")
            
            st.divider()
            st.subheader("🛠️ Bullet points à reformuler")
            st.markdown("""
            | Avant | Après (Optimisé) |
            | :--- | :--- |
            | "J'ai fait du développement Java" | "Développement de modules critiques sous Java 17 avec une réduction de 20% du temps de traitement." |
            | "Utilisation de Docker" | "Conteneurisation d'architectures micro-services via Docker pour fluidifier les déploiements." |
            """)
    else:
        st.error("Veuillez remplir les deux champs pour lancer l'analyse.")

st.info("💡 Conseil IA : Ne modifiez pas le fond des expériences, valorisez simplement la forme pour parler le langage du client.")
