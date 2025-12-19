import streamlit as st
import openai
import pdfplumber
import pandas as pd

st.set_page_config(page_title="CV Optimizer Pro", page_icon="🎯", layout="wide")

# --- STYLE CSS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #FF4B4B; color: white; }
    .status-box { padding: 20px; border-radius: 10px; border: 1px solid #e6e9ef; background-color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- INTERFACE ---
st.title("🎯 CV Optimizer Pro")
st.write("Analyse de matching IA pour le Staffing et le Recrutement")

# Barre latérale pour la configuration
with st.sidebar:
    st.title("⚙️ Configuration")
    api_key = st.text_input("Clé API OpenAI", type="password", help="Entre ta clé sk-...")
    st.info("Cette clé est nécessaire pour générer l'analyse.")

# --- ZONE DE SAISIE ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. L'Annonce")
    job_desc = st.text_area("Colle la description du poste ici :", height=300, placeholder="Recherche Business Developer avec 3 ans d'expérience...")

with col2:
    st.subheader("2. Le CV")
    uploaded_file = st.file_uploader("Upload le CV (format PDF uniquement)", type="pdf")

st.divider()

# --- TRAITEMENT ---
if st.button("🚀 Lancer l'Analyse du Matching"):
    if not api_key:
        st.error("❌ Erreur : Tu dois entrer ta clé API OpenAI dans la barre latérale.")
    elif not job_desc:
        st.warning("⚠️ Attention : Colle une description de poste.")
    elif not uploaded_file:
        st.warning("⚠️ Attention : Upload un fichier PDF.")
    else:
        with st.spinner("L'IA analyse le CV par rapport à l'annonce..."):
            try:
                # 1. Extraction du texte du PDF
                with pdfplumber.open(uploaded_file) as pdf:
                    resume_text = ""
                    for page in pdf.pages:
                        text = page.extract_text()
                        if text:
                            resume_text += text

                # 2. Préparation de la requête OpenAI
                client = openai.OpenAI(api_key=api_key)
                
                prompt = f"""
                Tu es un expert en recrutement (Talent Acquisition). 
                Analyse de manière critique le matching entre ce CV et cette annonce.
                
                DESCRIPTION DU POSTE:
                {job_desc}
                
                TEXTE DU CV:
                {resume_text}
                
                Fournis un rapport structuré avec :
                - SCORE DE MATCHING : Un score sur 100.
                - POINTS FORTS : Liste les 3 points clés où le candidat brille.
                - POINTS FAIBLES / MANQUANTS : Ce qui manque par rapport à l'annonce.
                - CONSEILS D'OPTIMISATION : 3 conseils concrets pour adapter ce CV au poste.
                """

                # 3. Appel à l'IA (Modèle GPT-4o pour la précision)
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "system", "content": "Tu es un assistant expert en recrutement."},
                              {"role": "user", "content": prompt}],
                    temperature=0.7
                )

                # 4. Affichage des résultats
                analysis = response.choices[0].message.content
                st.success("✅ Analyse terminée avec succès !")
                st.markdown("### 📊 Résultat de l'IA")
                st.markdown(analysis)
                
                # Option de téléchargement
                st.download_button("📥 Télécharger l'analyse", analysis, file_name="matching_cv.txt")

            except Exception as e:
                st.error(f"Une erreur est survenue lors de l'analyse : {str(e)}")

# --- PIED DE PAGE ---
st.divider()
st.caption("CV Optimizer Pro | Outil d'aide à la décision Staffing")
