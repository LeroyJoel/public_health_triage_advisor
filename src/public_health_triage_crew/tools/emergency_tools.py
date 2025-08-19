"""
Emergency response tools for critical health situations
"""

import json
from typing import Dict, List
from crewai.tools import tool

class EmergencyTools:
    """Emergency response and critical care tools"""
    
    @staticmethod
    def emergency_triage_assessment(symptoms: str, vital_signs: str = "") -> str:
        """Perform emergency triage assessment"""
        try:
            critical_keywords = [
                "chest pain", "heart attack", "stroke", "unconscious", 
                "severe bleeding", "difficulty breathing", "seizure",
                "head injury", "poisoning", "anaphylaxis"
            ]
            
            symptoms_lower = symptoms.lower()
            critical_found = [kw for kw in critical_keywords if kw in symptoms_lower]
            
            if critical_found:
                return f"🚨 CRITICAL EMERGENCY DETECTED! Symptoms: {', '.join(critical_found)}. IMMEDIATE ACTION REQUIRED: Call 112 or go to nearest hospital immediately!"
            else:
                return "No critical emergency detected, but continue monitoring symptoms."
                
        except Exception as e:
            return f"Error in emergency assessment: {str(e)}"
    
    @staticmethod
    def get_emergency_contacts(location: str) -> str:
        """Get emergency contact numbers for a location"""
        try:
            contacts = {
                "Lagos": {
                    "Emergency": "112",
                    "Police": "100",
                    "Ambulance": "112",
                    "Fire": "112",
                    "Lagos Emergency": "0800-123-4567"
                },
                "Kano": {
                    "Emergency": "112",
                    "Police": "100",
                    "Ambulance": "112",
                    "Kano Emergency": "0800-987-6543"
                },
                "Port Harcourt": {
                    "Emergency": "112",
                    "Police": "100",
                    "Ambulance": "112",
                    "Port Harcourt Emergency": "0800-555-1234"
                }
            }
            
            if location in contacts:
                result = f"Emergency contacts for {location}:\n"
                for service, number in contacts[location].items():
                    result += f"- {service}: {number}\n"
                return result
            else:
                return f"National Emergency: 112\nPolice: 100\nAmbulance: 112"
                
        except Exception as e:
            return f"Error getting emergency contacts: {str(e)}"
    
    @staticmethod
    def first_aid_instructions(injury_type: str) -> str:
        """Provide first aid instructions for common injuries"""
        try:
            first_aid_guide = {
                "bleeding": "Apply direct pressure with clean cloth, elevate if possible, call emergency services",
                "burn": "Cool with running water for 10-20 minutes, cover with sterile bandage, seek medical help",
                "choking": "Perform Heimlich maneuver, call emergency services immediately",
                "head injury": "Keep person still, monitor consciousness, call emergency services",
                "fracture": "Immobilize the area, apply ice, seek medical attention",
                "heart attack": "Call emergency services immediately, have person sit down, give aspirin if available",
                "stroke": "Remember FAST: Face drooping, Arm weakness, Speech difficulty, Time to call emergency"
            }
            
            if injury_type.lower() in first_aid_guide:
                return f"First aid for {injury_type}: {first_aid_guide[injury_type.lower()]}"
            else:
                return f"First aid instructions for {injury_type} not available. Call emergency services."
                
        except Exception as e:
            return f"Error providing first aid instructions: {str(e)}"
    
    @staticmethod
    def nearest_hospital_finder(location: str, emergency_type: str = "general") -> str:
        """Find nearest hospitals based on emergency type"""
        try:
            hospitals = {
                "Lagos": {
                    "general": ["Lagos University Teaching Hospital", "General Hospital Lagos"],
                    "cardiac": ["Cardiac Centre Lagos", "Heart Foundation Hospital"],
                    "pediatric": ["Lagos Children Hospital", "Mother and Child Centre"]
                },
                "Kano": {
                    "general": ["Aminu Kano Teaching Hospital", "Murtala Mohammed Specialist Hospital"],
                    "cardiac": ["Kano Cardiac Centre"],
                    "pediatric": ["Kano Children Hospital"]
                }
            }
            
            if location in hospitals:
                if emergency_type in hospitals[location]:
                    result = f"Nearest {emergency_type} hospitals in {location}:\n"
                    for hospital in hospitals[location][emergency_type]:
                        result += f"- {hospital}\n"
                    return result
                else:
                    result = f"General hospitals in {location}:\n"
                    for hospital in hospitals[location]["general"]:
                        result += f"- {hospital}\n"
                    return result
            else:
                return f"Contact local emergency services for hospital locations in {location}"
                
        except Exception as e:
            return f"Error finding hospitals: {str(e)}"

@tool("emergency_triage_assessment")
def emergency_triage_assessment(symptoms: str, vital_signs: str = "") -> str:
    """Assess if symptoms indicate a critical emergency requiring immediate attention"""
    return EmergencyTools.emergency_triage_assessment(symptoms, vital_signs)


@tool("get_emergency_contacts")
def get_emergency_contacts(location: str) -> str:
    """Get emergency contact numbers for a specific location"""
    return EmergencyTools.get_emergency_contacts(location)


@tool("first_aid_instructions")
def first_aid_instructions(injury_type: str) -> str:
    """Provide first aid instructions for common injuries and emergencies"""
    return EmergencyTools.first_aid_instructions(injury_type)


@tool("nearest_hospital_finder")
def nearest_hospital_finder(location: str, emergency_type: str = "general") -> str:
    """Find nearest hospitals based on location and emergency type"""
    return EmergencyTools.nearest_hospital_finder(location, emergency_type)


def create_emergency_tools():
    """Create and return emergency response tools"""
    return [
        emergency_triage_assessment,
        get_emergency_contacts,
        first_aid_instructions,
        nearest_hospital_finder,
    ]

