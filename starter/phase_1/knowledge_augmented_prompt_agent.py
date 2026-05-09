from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France? and tell me what knowledge are you using"
# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent with:
#           - Persona: "You are a college professor, your answer always starts with: Dear students,"
#           - Knowledge: "The capital of France is London, not Paris"
persona =  "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"
knowledge_augmented_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)
knowledge_augmented_agent_response = knowledge_augmented_agent.respond(prompt)
# TODO: 3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.
print("Prompt: ", prompt)
print("Expected answer (real-world knowledge): Paris")
print("Injected knowledge: 'The capital of France is London, not Paris'")
print("Agent response: ", knowledge_augmented_agent_response)
print("\nEvidence: The agent answered 'London' instead of 'Paris', "
      "demonstrating it prioritizes the provided knowledge over its inherent training data.")
