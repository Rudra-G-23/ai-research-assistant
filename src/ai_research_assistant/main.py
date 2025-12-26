import warnings
from ai_research_assistant.crew import AiResearchAssistant

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': "Open Source Project for Data Science"
    }

    try:
        AiResearchAssistant().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
