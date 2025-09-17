"""
Demo utilities for the Nigerian Health Triage Advisor
"""

import streamlit as st
from datetime import datetime
import random

def load_demo_data():
    """Load sample demo data for testing the application"""
    
    demo_scenarios = [
        {
            "name": "Amina Ibrahim",
            "age": 28,
            "gender": "Female",
            "location": "Kano, Nigeria",
            "phone": "+234 803 123 4567",
            "medical_history": "No known allergies. Previous normal delivery 3 years ago.",
            "symptoms": {
                "fever": True,
                "headache": True,
                "fatigue": True,
                "joint_pain": True,
                "difficulty_breathing": False,
                "cough": False,
                "abdominal_pain": False,
                "vomiting": False,
                "diarrhea": False,
                "dizziness": False,
                "nausea": False,
                "skin_rash": False,
                "sleep_problems": True
            },
            "additional_symptoms": "Started with mild headache 3 days ago. Fever began yesterday evening (feels like 38-39°C). Body aches and joint pains, especially in knees and back. Feeling very tired and weak. No appetite. Symptoms seem to be getting worse.",
            "severity": "Moderate"
        },
        {
            "name": "Chidi Okafor",
            "age": 45,
            "gender": "Male",
            "location": "Lagos, Nigeria",
            "phone": "+234 701 987 6543",
            "medical_history": "Hypertension (managed with medication). Diabetes Type 2 diagnosed 2 years ago.",
            "symptoms": {
                "chest_pain": True,
                "difficulty_breathing": True,
                "dizziness": True,
                "fatigue": True,
                "fever": False,
                "headache": False,
                "cough": False,
                "abdominal_pain": False,
                "vomiting": False,
                "diarrhea": False,
                "joint_pain": False,
                "nausea": True,
                "skin_rash": False,
                "sleep_problems": True
            },
            "additional_symptoms": "Sharp chest pain started this morning, especially when taking deep breaths. Feeling short of breath even when sitting. Dizzy when standing up. Had similar but milder episode last week. Taking medication for blood pressure and diabetes regularly.",
            "severity": "Severe"
        },
        {
            "name": "Baby Kemi Adebayo",
            "age": 8,
            "gender": "Female",
            "location": "Ibadan, Nigeria",
            "phone": "+234 806 555 7890",
            "medical_history": "Up to date with immunizations. No known allergies. Normal birth weight and development.",
            "symptoms": {
                "fever": True,
                "cough": True,
                "vomiting": True,
                "diarrhea": True,
                "fatigue": True,
                "difficulty_breathing": False,
                "headache": False,
                "chest_pain": False,
                "abdominal_pain": True,
                "dizziness": False,
                "joint_pain": False,
                "nausea": True,
                "skin_rash": False,
                "sleep_problems": True
            },
            "additional_symptoms": "Child has been sick for 2 days. Started with stomach pain and loose stools (3-4 times per day). Vomited twice yesterday. Low-grade fever. Not eating well and seems very tired. Still drinking water but less than usual. No blood in stool.",
            "severity": "Moderate"
        }
    ]
    
    return random.choice(demo_scenarios)

def populate_demo_data():
    """Populate Streamlit session state with demo data"""
    demo_data = load_demo_data()
    
    # Store demo data in session state
    for key, value in demo_data.items():
        if key == "symptoms":
            # Handle symptoms separately
            for symptom, checked in value.items():
                st.session_state[f"symptom_{symptom}"] = checked
        else:
            st.session_state[key] = value
    
    return demo_data

def get_common_nigerian_locations():
    """Return a list of common Nigerian locations for autocomplete"""
    return [
        "Lagos, Nigeria",
        "Abuja, FCT, Nigeria",
        "Kano, Nigeria",
        "Ibadan, Oyo, Nigeria",
        "Port Harcourt, Rivers, Nigeria",
        "Benin City, Edo, Nigeria",
        "Kaduna, Nigeria",
        "Jos, Plateau, Nigeria",
        "Ilorin, Kwara, Nigeria",
        "Aba, Abia, Nigeria",
        "Onitsha, Anambra, Nigeria",
        "Warri, Delta, Nigeria",
        "Sokoto, Nigeria",
        "Calabar, Cross River, Nigeria",
        "Uyo, Akwa Ibom, Nigeria",
        "Maiduguri, Borno, Nigeria",
        "Enugu, Nigeria",
        "Bauchi, Nigeria",
        "Akure, Ondo, Nigeria",
        "Abeokuta, Ogun, Nigeria"
    ]

def format_phone_number(phone):
    """Format phone number to Nigerian standard"""
    if not phone:
        return ""
    
    # Remove any non-digit characters except +
    phone = ''.join(c for c in phone if c.isdigit() or c == '+')
    
    # If it starts with 0, replace with +234
    if phone.startswith('0'):
        phone = '+234' + phone[1:]
    elif not phone.startswith('+234') and phone.startswith('234'):
        phone = '+' + phone
    elif phone.startswith('8') or phone.startswith('7') or phone.startswith('9'):
        # Likely a Nigerian mobile number without country code
        phone = '+234' + phone
    
    return phone

def get_emergency_contacts():
    """Return emergency contact information for Nigeria"""
    return {
        "National Emergency": "112",
        "Police": "199", 
        "Fire Service": "112",
        "Lagos State Emergency": "767 / 199",
        "FCT Emergency Services": "112",
        "Nigerian Red Cross": "070 6433 7846",
        "NEMA (Emergency Management)": "0800 NEMA HELP"
    }

def validate_nigerian_phone(phone):
    """Validate if a phone number is a valid Nigerian format"""
    if not phone:
        return True  # Optional field
    
    # Remove spaces and special characters
    cleaned = ''.join(c for c in phone if c.isdigit() or c == '+')
    
    # Check for valid Nigerian formats
    valid_formats = [
        len(cleaned) == 14 and cleaned.startswith('+234'),  # +234XXXXXXXXXX
        len(cleaned) == 13 and cleaned.startswith('234'),   # 234XXXXXXXXXX  
        len(cleaned) == 11 and cleaned.startswith('0'),     # 0XXXXXXXXXX
        len(cleaned) == 10 and cleaned[0] in '789'          # XXXXXXXXXX (mobile)
    ]
    
    return any(valid_formats)

def get_health_tips():
    """Return health tips relevant to Nigerian context"""
    return [
        "Drink clean, treated water to prevent waterborne diseases",
        "Use insecticide-treated bed nets to prevent malaria",
        "Wash hands frequently with soap and clean water",
        "Ensure food is properly cooked and served hot",
        "Keep up with routine immunizations for you and your children",
        "Seek medical attention early for fever, especially during rainy season",
        "Practice safe food handling and storage in hot weather",
        "Stay hydrated, especially during harmattan season",
        "Regular exercise helps prevent diabetes and hypertension",
        "Visit your nearest PHC for free health screenings and services"
    ]