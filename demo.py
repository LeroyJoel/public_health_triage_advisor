#!/usr/bin/env python3
"""
Demo script for Public Health Triage Advisor - Hackathon Presentation
"""

import time
import sys
from datetime import datetime
from public_health_triage_crew.crew import PublicHealthTriageCrew

def print_banner():
    """Print a cool banner for the demo"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    🏥 NIGERIAN HEALTH TRIAGE ADVISOR 🏥      ║
    ║                                                              ║
    ║              AI-Powered Healthcare Guidance System           ║
    ║                    Built with CrewAI & Gemini               ║
    ║                                                              ║
    ║                    🚀 HACKATHON DEMO 🚀                     ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def demo_scenario_1():
    """Demo Scenario 1: Emergency Case"""
    print("\n" + "="*60)
    print("🎬 DEMO SCENARIO 1: EMERGENCY CASE")
    print("="*60)
    
    scenario = {
        'patient_name': 'Aisha Mohammed',
        'age': 45,
        'location': 'Lagos',
        'symptoms': 'Severe chest pain, difficulty breathing, sweating, and pain radiating to left arm for the past 30 minutes',
        'topic': 'Public Health Triage Advisor',
        'current_year': str(datetime.now().year)
    }
    
    print(f"👤 Patient: {scenario['patient_name']} ({scenario['age']} years old)")
    print(f"📍 Location: {scenario['location']}")
    print(f"🏥 Symptoms: {scenario['symptoms']}")
    print("\n🤖 AI Agents are analyzing...")
    
    return scenario

def demo_scenario_2():
    """Demo Scenario 2: Maternal Health"""
    print("\n" + "="*60)
    print("🎬 DEMO SCENARIO 2: MATERNAL HEALTH")
    print("="*60)
    
    scenario = {
        'patient_name': 'Fatima Yusuf',
        'age': 28,
        'location': 'Kano',
        'symptoms': 'Pregnant woman in third trimester seeking antenatal care information, immunization schedule for her 2-year-old child, and guidance on nutrition during pregnancy',
        'topic': 'Public Health Triage Advisor',
        'current_year': str(datetime.now().year)
    }
    
    print(f"👤 Patient: {scenario['patient_name']} ({scenario['age']} years old)")
    print(f"📍 Location: {scenario['location']}")
    print(f"🏥 Symptoms: {scenario['symptoms']}")
    print("\n🤖 AI Agents are analyzing...")
    
    return scenario

def demo_scenario_3():
    """Demo Scenario 3: Medicine Availability"""
    print("\n" + "="*60)
    print("🎬 DEMO SCENARIO 3: MEDICINE AVAILABILITY")
    print("="*60)
    
    scenario = {
        'patient_name': 'Chukwudi Okonkwo',
        'age': 35,
        'location': 'Port Harcourt',
        'symptoms': 'Patient with malaria symptoms seeking information about ACT medications, their availability, pricing, and where to find them locally',
        'topic': 'Public Health Triage Advisor',
        'current_year': str(datetime.now().year)
    }
    
    print(f"👤 Patient: {scenario['patient_name']} ({scenario['age']} years old)")
    print(f"📍 Location: {scenario['location']}")
    print(f"🏥 Symptoms: {scenario['symptoms']}")
    print("\n🤖 AI Agents are analyzing...")
    
    return scenario

def run_demo():
    """Run the complete demo"""
    print_banner()
    
    print("\n🎯 Welcome to the Nigerian Health Triage Advisor Demo!")
    print("This system uses 5 AI agents to provide comprehensive healthcare guidance.")
    print("\n📋 Agent Overview:")
    print("   🔍 Public Health Triage Advisor - Symptom assessment & urgency classification")
    print("   👶 Maternal & Child Health Helper - Pregnancy & child care guidance")
    print("   💊 Medicine Availability Advisor - Medicine prices & availability")
    print("   💰 Health Finance Coach - Insurance & cost-saving options")
    print("   📋 Public Health Aggregator - Comprehensive report compilation")
    
    input("\n⏸️  Press Enter to start the demo scenarios...")
    
    scenarios = [demo_scenario_1, demo_scenario_2, demo_scenario_3]
    
    for i, scenario_func in enumerate(scenarios, 1):
        try:
            scenario = scenario_func()
            
            # Initialize crew
            crew = PublicHealthTriageCrew()
            
            # Run the scenario
            print(f"\n🔄 Running Scenario {i}...")
            start_time = time.time()
            
            result = crew.crew().kickoff(inputs=scenario)
            
            end_time = time.time()
            duration = end_time - start_time
            
            print(f"\n✅ Scenario {i} completed in {duration:.2f} seconds!")
            print("\n📋 COMPREHENSIVE HEALTH REPORT:")
            print("="*60)
            print(result)
            print("="*60)
            
            if i < len(scenarios):
                input(f"\n⏸️  Press Enter to continue to Scenario {i+1}...")
                
        except Exception as e:
            print(f"❌ Error in scenario {i}: {str(e)}")
            continue
    
    print("\n🎉 Demo completed successfully!")
    print("\n🚀 Key Features Demonstrated:")
    print("   ✅ Multi-agent AI collaboration")
    print("   ✅ Real-time health assessment")
    print("   ✅ Location-specific guidance")
    print("   ✅ Emergency response capabilities")
    print("   ✅ Comprehensive health reporting")
    print("   ✅ Nigerian healthcare system integration")
    
    print("\n💡 Potential Applications:")
    print("   🏥 Primary Health Centres")
    print("   📱 Mobile health apps")
    print("   🚑 Emergency response systems")
    print("   🏢 Health insurance companies")
    print("   📚 Medical training institutions")

if __name__ == "__main__":
    run_demo()

