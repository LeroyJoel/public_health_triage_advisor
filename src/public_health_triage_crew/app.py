import streamlit as st
import sys
import os
from datetime import datetime
from public_health_triage_crew.crew import PublicHealthTriageCrew

# Page configuration
st.set_page_config(
    page_title="Nigerian Health Triage Advisor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #28a745;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ffc107;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🏥 Nigerian Health Triage Advisor</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">AI-Powered Healthcare Guidance for Nigeria</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Model selection
        model = st.selectbox(
            "Select AI Model",
            ["gemini-1.5-flash", "gemini-1.5-pro"],
            index=0
        )
        
        # Temperature slider
        temperature = st.slider("AI Creativity Level", 0.1, 1.0, 0.7, 0.1)
        
        st.markdown("---")
        st.markdown("### 📊 Quick Stats")
        st.metric("Agents", "5")
        st.metric("Tasks", "5")
        st.metric("Coverage", "Full Healthcare")
        
        st.markdown("---")
        st.markdown("### 🎯 Features")
        st.markdown("""
        - **Symptom Triage** 🔍
        - **Maternal Health** 👶
        - **Medicine Locator** 💊
        - **Finance Coach** 💰
        - **Health Aggregator** 📋
        """)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h2 class="sub-header">🚀 Start Your Health Assessment</h2>', unsafe_allow_html=True)
        
        # Patient information form
        with st.form("patient_info"):
            st.subheader("Patient Information")
            
            col_a, col_b = st.columns(2)
            with col_a:
                patient_name = st.text_input("Patient Name", placeholder="Enter patient name")
                age = st.number_input("Age", min_value=0, max_value=120, value=25)
                gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            
            with col_b:
                location = st.text_input("Location (State/City)", placeholder="e.g., Lagos, Nigeria")
                phone = st.text_input("Phone Number", placeholder="+234...")
            
            # Symptoms section
            st.subheader("Symptoms Assessment")
            
            # Common symptoms checklist
            st.markdown("**Select all applicable symptoms:**")
            col_s1, col_s2 = st.columns(2)
            
            with col_s1:
                fever = st.checkbox("Fever")
                headache = st.checkbox("Headache")
                cough = st.checkbox("Cough")
                chest_pain = st.checkbox("Chest Pain")
                difficulty_breathing = st.checkbox("Difficulty Breathing")
            
            with col_s2:
                abdominal_pain = st.checkbox("Abdominal Pain")
                vomiting = st.checkbox("Vomiting")
                diarrhea = st.checkbox("Diarrhea")
                fatigue = st.checkbox("Fatigue")
                dizziness = st.checkbox("Dizziness")
            
            # Additional symptoms
            additional_symptoms = st.text_area(
                "Additional Symptoms (Describe in detail)",
                placeholder="Please describe any other symptoms, their severity, duration, and any relevant medical history..."
            )
            
            # Emergency checkbox
            is_emergency = st.checkbox("🚨 This is a medical emergency requiring immediate attention")
            
            # Submit button
            submitted = st.form_submit_button("🔍 Get Health Assessment", type="primary")
    
    with col2:
        st.markdown('<h3 class="sub-header">📋 Quick Actions</h3>', unsafe_allow_html=True)
        
        # Quick action buttons
        if st.button("🏥 Find Nearest PHC", type="secondary"):
            st.info("Feature: Would integrate with Google Maps API to find nearest Primary Health Centres")
        
        if st.button("💊 Medicine Price Check", type="secondary"):
            st.info("Feature: Would show real-time medicine prices from local pharmacies")
        
        if st.button("💰 Insurance Checker", type="secondary"):
            st.info("Feature: Would verify NHIS coverage and benefits")
        
        if st.button("📞 Emergency Contacts", type="secondary"):
            st.info("Feature: Would display emergency numbers for the selected location")
        
        st.markdown("---")
        st.markdown("### 🎯 Demo Mode")
        if st.button("🎬 Run Demo Assessment", type="secondary"):
            st.success("Would run a pre-configured demo with sample patient data")
    
    # Process form submission
    if submitted:
        if is_emergency:
            st.error("🚨 EMERGENCY ALERT: Please call emergency services immediately or go to the nearest hospital!")
            st.markdown("""
            **Emergency Numbers:**
            - National Emergency: 112
            - Police: 100
            - Ambulance: 112
            """)
            return
        
        if not patient_name or not additional_symptoms:
            st.warning("Please fill in patient name and describe symptoms for a proper assessment.")
            return
        
        # Show processing
        with st.spinner("🤖 AI Agents are analyzing your health information..."):
            try:
                # Create crew instance
                crew = PublicHealthTriageCrew()
                
                # Prepare inputs
                inputs = {
                    'patient_name': patient_name,
                    'age': age,
                    'gender': gender,
                    'location': location,
                    'symptoms': additional_symptoms,
                    'selected_symptoms': {
                        'fever': fever,
                        'headache': headache,
                        'cough': cough,
                        'chest_pain': chest_pain,
                        'difficulty_breathing': difficulty_breathing,
                        'abdominal_pain': abdominal_pain,
                        'vomiting': vomiting,
                        'diarrhea': diarrhea,
                        'fatigue': fatigue,
                        'dizziness': dizziness
                    },
                    'topic': 'Public Health Triage Advisor',
                    'current_year': str(datetime.now().year)
                }
                
                # Run the crew
                result = crew.crew().kickoff(inputs=inputs)
                
                # Display results
                st.success("✅ Health Assessment Complete!")
                
                # Display the result in a nice format
                st.markdown("## 📋 Comprehensive Health Report")
                st.markdown(result)
                
                # Add download button
                st.download_button(
                    label="📥 Download Report as PDF",
                    data=result,
                    file_name=f"health_assessment_{patient_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown"
                )
                
            except Exception as e:
                st.error(f"❌ Error during assessment: {str(e)}")
                st.info("Please check your API key and try again.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🏥 Built with CrewAI & Gemini for Nigerian Healthcare | Hackathon Project</p>
        <p>⚠️ This is for educational purposes only. Always consult healthcare professionals for medical advice.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

