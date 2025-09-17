"""
crew file for the Public Health Triage Advisor project
"""

import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from dotenv import load_dotenv
from .tools.health_tools import create_health_tools
from .tools.emergency_tools import create_emergency_tools

# Load environment variables
load_dotenv()

# Configure Gemini (model can be read at import-time; API key check is deferred)
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")


@CrewBase
class PublicHealthTriageCrew():
    """Public Health Triage Advisor crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self):
        """Initialize the crew with Gemini LLM"""
        # Ensure latest env vars are loaded and validate API key at runtime (not import-time)
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key or api_key == "your_gemini_api_key_here":
            raise ValueError(
                "GEMINI_API_KEY not found. Please set it in your .env file or environment variables. "
                "You can get one from https://makersuite.google.com/app/apikey"
            )

        # Use CrewAI's LLM class with improved configuration
        self.llm = LLM(
            model=f"gemini/{GEMINI_MODEL}",
            api_key=api_key,
            temperature=0.7,
            max_tokens=4000  # Ensure comprehensive responses
        )

    @agent
    def public_health_triage(self) -> Agent:
        return Agent(
            config=self.agents_config['public_health_triage'],
            llm=self.llm,
            tools=create_emergency_tools() + create_health_tools(),
            verbose=True,
            max_iter=2,  # Reduce iterations to avoid complexity
            memory=False  # Disable memory to avoid embedder issues
        )

    @agent
    def maternal_child_health(self) -> Agent:
        return Agent(
            config=self.agents_config['maternal_child_health'],
            llm=self.llm,
            verbose=True,
            max_iter=2,
            memory=False
        )

    @agent
    def medicine_availability_locator(self) -> Agent:
        return Agent(
            config=self.agents_config['medicine_availability_locator'],
            llm=self.llm,
            verbose=True,
            max_iter=2,
            memory=False
        )

    @agent
    def health_finance_coach(self) -> Agent:
        return Agent(
            config=self.agents_config['health_finance_coach'],
            llm=self.llm,
            verbose=True,
            max_iter=2,
            memory=False
        )

    @agent
    def public_health_aggregator(self) -> Agent:
        return Agent(
            config=self.agents_config['public_health_aggregator'],
            llm=self.llm,
            verbose=True,
            max_iter=2,
            memory=False
        )

    @task
    def public_health_triage_task(self) -> Task:
        task_config = self.tasks_config['public_health_triage_task'].copy()
        
        # Enhanced task description with input handling
        task_config['description'] = """
        Assess the patient's reported symptoms and provide guidance on next steps for care within the Nigerian healthcare system.
        
        You will receive the following patient information:
        - patient_name: The patient's full name
        - age: Patient's age in years
        - gender: Patient's gender (Male/Female/Other)
        - location: Patient's location within Nigeria
        - symptoms: Detailed description of symptoms
        - symptom_severity: Overall severity level (Mild/Moderate/Severe/Very Severe)
        - selected_symptoms: List of specific symptoms selected by the patient
        - medical_history: Any existing medical conditions or relevant history
        
        Based on this information, classify urgency as:
        - Home Care: Mild symptoms manageable with rest and basic care
        - Primary Health Centre (PHC): Moderate symptoms requiring basic medical attention
        - General Hospital: Serious symptoms requiring specialized care
        - Teaching Hospital: Critical/complex cases requiring advanced medical intervention
        
        Consider Nigerian healthcare context, common diseases, and local healthcare capacity.
        Provide specific, actionable recommendations.
        """
        
        return Task(config=task_config)

    @task
    def maternal_child_health_task(self) -> Task:
        task_config = self.tasks_config['maternal_child_health_task'].copy()
        
        # Enhanced description for maternal and child health
        task_config['description'] = """
        Provide specialized guidance for pregnancy, childbirth, and newborn/child health within Nigeria's healthcare system.
        
        Focus on:
        - Free antenatal care services available in Nigerian PHCs and hospitals
        - Essential supplements (folic acid, iron, calcium) and nutrition guidance
        - Nigeria's routine immunization schedule for children
        - Maternal health programs and support services
        - Child development milestones and health screening schedules
        - Emergency signs during pregnancy, delivery, and postpartum
        
        Tailor advice based on patient's age, gender, location, and specific symptoms if related to maternal or child health.
        Reference Nigerian health policies and available free services.
        """
        
        return Task(config=task_config)

    @task
    def medicine_availability_locator_task(self) -> Task:
        task_config = self.tasks_config['medicine_availability_locator_task'].copy()
        
        # Enhanced medicine locator description
        task_config['description'] = """
        Provide Nigerian patients with comprehensive medicine availability and cost information.
        
        Based on the patient's symptoms and recommended treatments, provide:
        - Common generic medicine names available in Nigeria
        - Nigerian brand equivalents where applicable
        - Approximate costs in Nigerian Naira (₦)
        - Availability locations: PHCs (free/subsidized), general hospitals, private pharmacies
        - Over-the-counter vs. prescription requirements
        - Alternative medicines if primary options are unavailable
        
        Consider the patient's location to suggest regional availability and pricing variations.
        Highlight cost-effective options and government subsidy programs.
        """
        
        return Task(config=task_config)

    @task
    def health_finance_coach_task(self) -> Task:
        task_config = self.tasks_config['health_finance_coach_task'].copy()
        
        # Enhanced finance coaching description
        task_config['description'] = """
        Recommend Nigerian health financing options and cost-saving strategies.
        
        Provide guidance on:
        - National Health Insurance Scheme (NHIS) enrollment and benefits
        - State-specific health insurance programs
        - Free services available at PHCs (immunization, antenatal care, basic consultations)
        - NGO and community health programs offering free/subsidized care
        - Government health initiatives and subsidy programs
        - Payment plans and financial assistance options at hospitals
        - Cost comparison between different facility types
        
        Based on patient location and symptoms, suggest the most cost-effective care pathway.
        Include eligibility requirements and application processes for insurance/assistance programs.
        """
        
        return Task(config=task_config)

    @task
    def public_health_aggregator_task(self) -> Task:
        task_config = self.tasks_config['public_health_aggregator_task'].copy()
        
        # Enhanced aggregator description
        task_config['description'] = """
        Combine all Nigerian-specific health guidance into a comprehensive, well-structured Markdown report.
        
        Create a professional health assessment report with these sections:
        
        # Nigerian Health Assessment Report for [Patient Name]
        
        ## Patient Information Summary
        - Demographics and basic information
        - Symptoms overview and severity assessment
        
        ## 🏥 Symptom Triage & Urgency Classification
        - Detailed symptom analysis
        - Recommended facility type and urgency level
        - When to seek immediate care
        
        ## 👶 Maternal & Child Health Guidance
        - Age-specific health recommendations
        - Immunization schedules if applicable
        - Specialized care recommendations
        
        ## 💊 Medicine Availability & Costs
        - Recommended medications with Nigerian availability
        - Cost estimates in Naira
        - Where to find medications (PHC/hospital/pharmacy)
        
        ## 💰 Healthcare Financing Options
        - Insurance and subsidy programs
        - Cost-saving recommendations
        - Free services available
        
        ## 🎯 Next Steps & Action Plan
        - Immediate actions to take
        - Follow-up care recommendations
        - Emergency contact information
        
        ## ⚠️ Important Disclaimers
        - This is for guidance only
        - When to seek immediate medical attention
        
        Ensure all recommendations are specific to Nigeria's healthcare system and the patient's location.
        Use clear, non-medical language that patients can understand.
        Include specific facility names, contact information, and cost estimates where possible.
        """
        
        return Task(
            config=task_config,
            output_file='nigerian_health_assessment_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Public Health Triage Advisor crew with improved configuration"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=False,  # Disable memory to avoid embedder issues
            max_rpm=10,  # Rate limiting for API calls
        )