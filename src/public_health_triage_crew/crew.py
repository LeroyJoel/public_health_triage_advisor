"""
Main crew file for the Public Health Triage Advisor project
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

        # Use CrewAI's LLM class
        self.llm = LLM(
            model=f"gemini/{GEMINI_MODEL}",
            api_key=api_key,
            temperature=0.7
        )

    @agent
    def public_health_triage(self) -> Agent:
        return Agent(
            config=self.agents_config['public_health_triage'],
            llm=self.llm,
            tools=create_emergency_tools() + create_health_tools(),
            verbose=True
        )

    @agent
    def maternal_child_health(self) -> Agent:
        return Agent(
            config=self.agents_config['maternal_child_health'],
            llm=self.llm,
            verbose=True
        )

    @agent
    def medicine_availability_locator(self) -> Agent:
        return Agent(
            config=self.agents_config['medicine_availability_locator'],
            llm=self.llm,
            verbose=True
        )

    @agent
    def health_finance_coach(self) -> Agent:
        return Agent(
            config=self.agents_config['health_finance_coach'],
            llm=self.llm,
            verbose=True
        )

    @agent
    def public_health_aggregator(self) -> Agent:
        return Agent(
            config=self.agents_config['public_health_aggregator'],
            llm=self.llm,
            verbose=True
        )

    @task
    def public_health_triage_task(self) -> Task:
        return Task(
            config=self.tasks_config['public_health_triage_task']
        )

    @task
    def maternal_child_health_task(self) -> Task:
        return Task(
            config=self.tasks_config['maternal_child_health_task']
        )

    @task
    def medicine_availability_locator_task(self) -> Task:
        return Task(
            config=self.tasks_config['medicine_availability_locator_task']
        )

    @task
    def health_finance_coach_task(self) -> Task:
        return Task(
            config=self.tasks_config['health_finance_coach_task']
        )

    @task
    def public_health_aggregator_task(self) -> Task:
        return Task(
            config=self.tasks_config['public_health_aggregator_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Public Health Triage Advisor crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
