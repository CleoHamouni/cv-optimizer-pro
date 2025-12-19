import streamlit as st
import openai
import pdfplumber

st.set_page_config(page_title="CV Optimizer Pro", page_icon="🎯")

# --- INTERFACE ---
st.title("🎯 CV Optimizer Pro")
st.subheader("Analyse de matching IA pour Staffing & Recrutement")

# Configuration de la clé API (à mettre dans tes Secrets Streamlit)
api_key = st.sidebar.text_input("Clé API OpenAI", type="password")

with st.expander("ℹ️ Instructions"):
    st.write("1. Entre ta clé OpenAI. 2. Colle l'annonce. 3. Upload le CV (PDF).")

# --- INPUTS ---
col1, col2 = st.columns(2)
with col1:
    job_desc = st.text_area("📄 Description du Poste", height=250, placeholder="Colle l'annonce ici...")

with col2:
    uploaded_file = st.file_uploader("📂 Upload CV (PDF)", type="pdf")

# --- LOGIQUE D'ANALYSE ---
if st.button("🚀 Lancer l'Optimisation"):
    if not api_key:
        st.error("L'IA a besoin de ta clé API pour travailler !")
    elif not job_desc or not uploaded_file:
        st.warning("Merci de fournir une annonce ET un CV.")
    else:
        with st.spinner("L'IA analyse le matching..."):
            try:
                # 1. Lecture du PDF
                with pdfplumber.open(uploaded_file) as pdf:
                    resume_text = ""
                    for page in pdf.pages:
                        resume_text += page.extract_text()

                # 2. Appel OpenAI (Sans cache persistant pour éviter les bugs)
                client = openai.OpenAI(api_key=api_key)
                
                prompt = f"""
                Tu es un expert en recrutement et staffing. 
                Analyse le matching entre ce CV et cette annonce.
                
                ANNONCE: {job_desc}
                CV: {resume_text}
                
                Donne une réponse structurée :
                1. Score de matching (X/100)
                2. Points forts du candidat pour ce poste
                3. Compétences ou mots-clés manquants
                4. Recommandations pour adapter le CV (Staffing)
                """

                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )

                # 3. Affichage du résultat
                result = response.choices[0].message.content
                st.success("✅ Analyse terminée !")
                st.markdown("---")
                st.markdown(result)
                
                # Bouton pour télécharger le compte-rendu
                st.download_button("📥 Télécharger l'analyse", result, file_name="analyse_matching.txt")

            except Exception as e:
                st.error(f"Une erreur est survenue : {e}")

st.divider()
st.caption("Propulsé par GPT-4o - Spécial Staffing & Recrutement")
