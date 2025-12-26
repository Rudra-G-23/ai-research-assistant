from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os


@CrewBase
class AiResearchAssistant:
    """Sequential AI Research Assistant Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # ======================== AGENTS ========================

    @agent
    def topic_decomposer(self) -> Agent:
        return Agent(
            config=self.agents_config
        )

    @agent
    def question_generator(self) -> Agent:
        return Agent(
            config=self.agents_config
        )

    @agent
    def learning_path_planner(self) -> Agent:
        return Agent(
            config=self.agents_config
        )

    @agent
    def human_explainer(self) -> Agent:
        return Agent(
            config=self.agents_config
        )

    # ======================== TASKS ========================

    @task
    def topic_decomposition_task(self) -> Task:
        """Break raw topic into structured subtopics"""
        return Task(
            config=self.tasks_config
        )

    @task
    def question_generation_task(self) -> Task:
        """Generate deep questions for each subtopic"""
        return Task(
            config=self.tasks_config
        )

    @task
    def learning_path_planning_task(self) -> Task:
        """Create a staged learning roadmap"""
        return Task(
            config=self.tasks_config
        )

    @task
    def human_explanation_task(self) -> Task:
        """Convert roadmap into human-friendly explanation"""
        os.makedirs("study-plans", exist_ok=True)

        return Task(
            config=self.tasks_config,
            output_file="study-plans/planning.md"
        )

    # ======================== CREW ========================

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
