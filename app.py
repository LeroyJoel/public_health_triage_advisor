import streamlit as st
from datetime import datetime
from public_health_triage_crew.crew import PublicHealthTriageCrew

st.set_page_config(page_title="Nigerian Health Triage Advisor", page_icon="🏥", layout="wide")

def main():
    st.title("🏥 Nigerian Health Triage Advisor")
    st.markdown("AI-Powered Healthcare Guidance for Nigeria")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        model = st.selectbox("AI Model", ["gemini-1.5-flash", "gemini-1.5-pro"])
        temperature = st.slider("Creativity", 0.1, 1.0, 0.7)
        
        st.markdown("### 🎯 Features")
        st.markdown("- Symptom Triage 🔍")
        st.markdown("- Maternal Health 👶")
        st.markdown("- Medicine Locator 💊")
        st.markdown("- Finance Coach 💰")
    
    # Main form
    with st.form("health_assessment"):
        st.subheader("Patient Information")
        
        col1, col2 = st.columns(2)
        with col1:
            patient_name = st.text_input("Patient Name")
            age = st.number_input("Age", min_value=0, max_value=120, value=25)
        
        with col2:
            location = st.text_input("Location", placeholder="Lagos, Nigeria")
            phone = st.text_input("Phone")
        
        st.subheader("Symptoms")
        symptoms = st.text_area("Describe your symptoms in detail")
        
        emergency = st.checkbox("🚨 This is a medical emergency")
        
        submitted = st.form_submit_button("🔍 Get Assessment")
    
    if submitted:
        if emergency:
            st.error("🚨 EMERGENCY: Call 112 or go to nearest hospital!")
            return
        
        if not patient_name or not symptoms:
            st.warning("Please fill in name and symptoms.")
            return
        
        with st.spinner("🤖 AI Agents analyzing..."):
            try:
                crew = PublicHealthTriageCrew()
                inputs = {
                    'patient_name': patient_name,
                    'age': age,
                    'location': location,
                    'symptoms': symptoms,
                    'topic': 'Public Health Triage Advisor',
                    'current_year': str(datetime.now().year)
                }
                
                result = crew.crew().kickoff(inputs=inputs)
                
                st.success("✅ Assessment Complete!")
                st.markdown("## 📋 Health Report")
                st.markdown(result)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

