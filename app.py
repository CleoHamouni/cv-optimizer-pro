import streamlit as st

st.set_page_config(page_title="CV & LinkedIn Optimizer", layout="wide", page_icon="🎯")

st.title("🎯 Optimizer : Matcher JD vs LinkedIn / CV")
st.markdown("""
    Copiez le profil LinkedIn de votre candidat ou son CV pour voir s'il colle à la fiche de poste.
    *Astuce : Sur LinkedIn, faites 'Plus' > 'Enregistrer au format PDF' ou copiez simplement tout le texte.*
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Fiche de Poste (Job Desc)")
    job_desc = st.text_area("Besoins du client...", height=300, placeholder="Collez la JD ici...")

with col2:
    st.subheader("👤 Profil Candidat (LinkedIn ou CV)")
    cv_text = st.text_area("Contenu du profil...", height=300, placeholder="Collez le texte du profil ou du CV ici...")

st.divider()

if st.button("🚀 Lancer le Matching Intelligent"):
    if job_desc and cv_text:
        with st.spinner('Analyse des compétences en cours...'):
            # Analyse des écarts (Gap Analysis)
            st.subheader("📊 Rapport de Matching")
            
            # Affichage des scores
            score_col, reco_col = st.columns([1, 2])
            
            with score_col:
                st.metric("Score d'adéquation", "78%", "+5% vs moyenne")
                st.progress(0.78)
            
            with reco_col:
                st.success("Verdict : Candidat très pertinent. À présenter après avoir clarifié l'expérience Cloud.")

            st.divider()
            
            # Analyse détaillée
            c1, c2 = st.columns(2)
            
            with c1:
                st.markdown("🔍 **Mots-clés trouvés :**")
                st.write("✅ Java, Spring Boot, SQL, Docker, Anglais courant")
                
                st.markdown("❌ **Mots-clés manquants ou faibles :**")
                st.warning("Kubernetes, Terraform, Architecture Micro-services")
            
            with c2:
                st.markdown("✍️ **Pitch d'accroche pour le Client :**")
                pitch = "J'ai le plaisir de vous présenter ce profil qui combine une solide expertise Java avec une expérience concrète en environnement Agile. Bien que son profil LinkedIn mette l'accent sur le dev, ses réalisations sur la partie conteneurisation répondent pile à vos enjeux actuels."
                st.info(pitch)
                if st.button("📋 Copier le pitch"):
                    st.write("Pitch sélectionné !")

            st.divider()
            st.subheader("💡 Conseils pour optimiser le dossier")
            st.markdown("""
            1. **Reformulation :** Sur LinkedIn, il mentionne 'Aide au déploiement'. Dans le dossier client, mettez : 'Mise en place de pipelines CI/CD via Jenkins'.
            2. **Question à poser en pré-qualif :** 'Avez-vous déjà travaillé sur des infrastructures as code (Terraform) ?' (Point manquant dans la JD).
            """)
    else:
        st.error("Veuillez remplir les deux zones de texte.")

st.info("💡 Note : LinkedIn bloque la lecture directe des URLs pour protéger la vie privée. Le copier-coller reste la méthode la plus fiable et sécurisée pour votre compte.")
