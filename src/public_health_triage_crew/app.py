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
    .emergency-alert {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #f5c6cb;
        margin: 1rem 0;
    }
    .stForm {
        border: 1px solid #e6e6e6;
        border-radius: 10px;
        padding: 20px;
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
        
        st.markdown("---")
        st.markdown("### 📊 Quick Stats")
        st.metric("Agents", "5")
        st.metric("Tasks", "5")
        st.metric("Coverage", "Full Healthcare")
        
        st.markdown("---")
        st.markdown("### 📞 Emergency Numbers")
        st.markdown("""
        - **National Emergency:** 112
        - **Police:** 199
        - **Fire Service:** 112
        - **Lagos State Emergency:** 767/199
        """)
        
        st.markdown("---")
        st.markdown("### ⚠️ Disclaimer")
        st.warning("This tool is for educational purposes only. Always consult healthcare professionals for medical advice.")
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h2 class="sub-header">🚀 Start Your Health Assessment</h2>', unsafe_allow_html=True)
        
        # Patient information form
        with st.form("patient_assessment_form", clear_on_submit=False):
            # Patient Information Section
            st.subheader("📝 Patient Information")
            
            col_a, col_b = st.columns(2)
            with col_a:
                patient_name = st.text_input(
                    "Patient Name *", 
                    placeholder="Enter patient name",
                    help="This field is required"
                )
                age = st.number_input("Age", min_value=0, max_value=120, value=25)
                gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            
            with col_b:
                location = st.text_input(
                    "Location (State/City)", 
                    placeholder="e.g., Lagos, Nigeria"
                )
                phone = st.text_input(
                    "Phone Number (Optional)", 
                    placeholder="+234..."
                )
                medical_history = st.text_area(
                    "Medical History (Optional)", 
                    placeholder="Any existing conditions, medications, allergies...",
                    height=100
                )
            
            st.markdown("---")
            
            # Emergency Section
            st.subheader("🚨 Emergency Assessment")
            is_emergency = st.checkbox(
                "This is a medical emergency requiring immediate attention",
                help="Check this if you need immediate medical care"
            )
            
            if is_emergency:
                st.error("🚨 If this is truly an emergency, please call 112 or go to the nearest hospital immediately!")
            
            st.markdown("---")
            
            # Symptoms Section
            st.subheader("🔍 Symptoms Assessment")
            
            # Main symptoms description (this is the key field)
            symptoms_description = st.text_area(
                "Describe Your Symptoms *",
                placeholder="Please describe your symptoms in detail including:\n• What symptoms you're experiencing\n• How long you've had them\n• How severe they are (mild, moderate, severe)\n• What makes them better or worse\n• Any other relevant details...",
                height=150,
                help="This field is required. Please provide as much detail as possible."
            )
            
            # Common symptoms checklist (optional, to supplement the description)
            st.markdown("**Optional: Check any symptoms that apply (to supplement your description above):**")
            
            col_s1, col_s2, col_s3 = st.columns(3)
            
            # Create checkboxes but store them in variables immediately
            with col_s1:
                fever_check = st.checkbox("Fever")
                headache_check = st.checkbox("Headache") 
                fatigue_check = st.checkbox("Fatigue")
                dizziness_check = st.checkbox("Dizziness")
            
            with col_s2:
                cough_check = st.checkbox("Cough")
                difficulty_breathing_check = st.checkbox("Difficulty Breathing")
                chest_pain_check = st.checkbox("Chest Pain")
                joint_pain_check = st.checkbox("Joint Pain")
            
            with col_s3:
                abdominal_pain_check = st.checkbox("Abdominal Pain")
                vomiting_check = st.checkbox("Vomiting")
                diarrhea_check = st.checkbox("Diarrhea")
                nausea_check = st.checkbox("Nausea")
            
            # Symptom severity
            severity = st.select_slider(
                "Overall symptom severity",
                options=["Mild", "Moderate", "Severe", "Very Severe"],
                value="Moderate",
                help="How would you rate your overall symptoms?"
            )
            
            st.markdown("---")
            
            # Submit button
            submitted = st.form_submit_button(
                "🔍 Generate Health Assessment",
                type="primary",
                use_container_width=True
            )
    
    with col2:
        st.markdown('<h3 class="sub-header">📋 Quick Actions</h3>', unsafe_allow_html=True)
        
        if st.button("🎬 Load Demo Data", type="secondary", use_container_width=True):
            st.success("✅ Demo feature - would populate form with sample patient data")
        
        if st.button("🏥 Find Nearest PHC", type="secondary", use_container_width=True):
            st.info("🔍 Feature: Would integrate with maps to find nearest Primary Health Centres")
        
        if st.button("💊 Medicine Prices", type="secondary", use_container_width=True):
            st.info("💰 Feature: Would show medicine prices from local pharmacies")
        
        st.markdown("---")
        st.markdown("### 💡 Health Tips")
        st.markdown("""
        - Stay hydrated with clean water
        - Use insecticide-treated nets
        - Wash hands frequently
        - Eat well-cooked food
        - Keep up with immunizations
        """)
    
    # Process form submission
    if submitted:
        # Simple validation
        if not patient_name or not patient_name.strip():
            st.error("❌ Please enter the patient's name.")
            return
        
        if not symptoms_description or not symptoms_description.strip():
            st.error("❌ Please describe the symptoms in the text area above.")
            return
        
        # Handle emergency cases
        if is_emergency:
            st.error("🚨 EMERGENCY ALERT: Please call emergency services immediately!")
            st.markdown("""
            <div class="emergency-alert">
                <h3>🚨 IMMEDIATE ACTION REQUIRED</h3>
                <p><strong>Emergency Numbers:</strong></p>
                <ul>
                    <li><strong>National Emergency:</strong> 112</li>
                    <li><strong>Police:</strong> 199</li>
                    <li><strong>Lagos State Emergency:</strong> 767/199</li>
                </ul>
                <p><strong>Go to the nearest hospital immediately!</strong></p>
            </div>
            """, unsafe_allow_html=True)
            return
        
        # Collect selected symptoms
        selected_symptoms_list = []
        if fever_check: selected_symptoms_list.append("Fever")
        if headache_check: selected_symptoms_list.append("Headache")
        if fatigue_check: selected_symptoms_list.append("Fatigue")
        if dizziness_check: selected_symptoms_list.append("Dizziness")
        if cough_check: selected_symptoms_list.append("Cough")
        if difficulty_breathing_check: selected_symptoms_list.append("Difficulty Breathing")
        if chest_pain_check: selected_symptoms_list.append("Chest Pain")
        if joint_pain_check: selected_symptoms_list.append("Joint Pain")
        if abdominal_pain_check: selected_symptoms_list.append("Abdominal Pain")
        if vomiting_check: selected_symptoms_list.append("Vomiting")
        if diarrhea_check: selected_symptoms_list.append("Diarrhea")
        if nausea_check: selected_symptoms_list.append("Nausea")
        
        # Format comprehensive symptoms
        comprehensive_symptoms = symptoms_description.strip()
        if selected_symptoms_list:
            comprehensive_symptoms += f"\n\nAdditional symptoms checked: {', '.join(selected_symptoms_list)}"
        
        # Show what we collected (for debugging)
        with st.expander("Debug Info - Form Data Collected"):
            st.write(f"Patient Name: '{patient_name}'")
            st.write(f"Symptoms Description: '{symptoms_description}'")
            st.write(f"Selected Symptoms: {selected_symptoms_list}")
            st.write(f"Comprehensive Symptoms: '{comprehensive_symptoms}'")
        
        # Show processing
        with st.spinner("🤖 AI Agents are analyzing your health information..."):
            try:
                # Create crew instance
                crew = PublicHealthTriageCrew()
                
                # Prepare inputs for the crew
                inputs = {
                    # Patient information
                    'patient_name': patient_name.strip(),
                    'age': str(age),
                    'gender': gender,
                    'location': location.strip() if location else "Nigeria",
                    'phone': phone.strip() if phone else "Not provided",
                    'medical_history': medical_history.strip() if medical_history else "None reported",
                    
                    # Symptoms information - the key data
                    'symptoms': comprehensive_symptoms,
                    'symptom_severity': severity,
                    'selected_symptoms': selected_symptoms_list,
                    
                    # System information
                    'topic': 'Nigerian Public Health Triage Assessment',
                    'current_year': str(datetime.now().year),
                    'assessment_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    
                    # Additional context
                    'country': 'Nigeria',
                    'healthcare_system': 'Nigerian Healthcare System'
                }
                
                # Show inputs for debugging
                with st.expander("Debug Info - Inputs to CrewAI"):
                    st.json(inputs)
                
                # Run the crew
                result = crew.crew().kickoff(inputs=inputs)
                
                # Display results
                st.success("✅ Health Assessment Complete!")
                
                # Create tabs for results
                tab1, tab2, tab3 = st.tabs(["📋 Full Report", "📊 Summary", "📥 Download"])
                
                with tab1:
                    st.markdown("## 📋 Your Health Assessment Report")
                    st.markdown(result)
                
                with tab2:
                    st.markdown("## 📊 Assessment Summary")
                    col_sum1, col_sum2 = st.columns(2)
                    
                    with col_sum1:
                        st.metric("Patient", patient_name)
                        st.metric("Age", f"{age} years")
                        st.metric("Severity", severity)
                    
                    with col_sum2:
                        st.metric("Location", location if location else "Not specified")
                        st.metric("Symptoms", f"{len(selected_symptoms_list)} checked")
                        st.metric("Date", datetime.now().strftime('%Y-%m-%d'))
                
                with tab3:
                    # Prepare download content
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    filename = f"health_assessment_{patient_name.replace(' ', '_')}_{timestamp}"
                    
                    download_content = f"""# Nigerian Health Assessment Report

**Patient:** {patient_name}
**Age:** {age}
**Gender:** {gender}
**Location:** {location if location else 'Not specified'}
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

**Symptoms:**
{comprehensive_symptoms}

**Severity:** {severity}

---

{result}

---
*Generated by Nigerian Health Triage Advisor*
*This is for educational purposes only. Always consult healthcare professionals.*
"""
                    
                    st.download_button(
                        label="📄 Download Report (Markdown)",
                        data=download_content,
                        file_name=f"{filename}.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
                    
                    st.download_button(
                        label="📋 Download Report (Text)",
                        data=download_content,
                        file_name=f"{filename}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                # Success message
                st.markdown("---")
                st.info("""
                **Important Reminders:**
                - This assessment is for guidance only
                - Always consult healthcare professionals for serious symptoms
                - Seek immediate medical attention if symptoms worsen
                - Keep this report for your medical records
                """)
                
            except Exception as e:
                st.error(f"❌ Error during assessment: {str(e)}")
                st.markdown("""
                **Possible solutions:**
                - Check your internet connection
                - Verify your API key is set correctly
                - Try refreshing the page and submitting again
                """)
                
                with st.expander("🔧 Technical Error Details"):
                    st.code(str(e))
                    st.write("If this error persists, please check:")
                    st.write("1. GEMINI_API_KEY is set in your .env file")
                    st.write("2. You have internet connectivity")
                    st.write("3. The CrewAI agents are configured correctly")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🏥 <strong>Nigerian Health Triage Advisor</strong></p>
        <p>⚠️ <em>For educational purposes only. Always consult healthcare professionals for medical advice.</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()