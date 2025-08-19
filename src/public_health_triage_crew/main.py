#!/usr/bin/env python
"""
Main entry point for the Public Health Triage Advisor project
"""

import sys
import warnings
from datetime import datetime

from public_health_triage_crew.crew import PublicHealthTriageCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Public Health Triage Advisor',
        'current_year': str(datetime.now().year)
    }
    
    try:
        PublicHealthTriageCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Public Health Triage Advisor",
        'current_year': str(datetime.now().year)
    }
    try:
        n_iterations = int(sys.argv[1])
        filename = sys.argv[2]
        PublicHealthTriageCrew().crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        task_id = sys.argv[1]
        PublicHealthTriageCrew().crew().replay(task_id=task_id)
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "Public Health Triage Advisor",
        "current_year": str(datetime.now().year)
    }
    
    try:
        n_iterations = int(sys.argv[1])
        eval_llm = sys.argv[2]
        PublicHealthTriageCrew().crew().test(n_iterations=n_iterations, eval_llm=eval_llm, inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    run()
