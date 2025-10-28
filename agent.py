from google.adk.agents import Agent
from .k8s_utils import run_kubectl_command

root_agent = Agent(
    name="kube_agent",
    model="gemini-2.0-flash",
    description="An AI agent that manages Kubernetes resources using kubectl.",
    instruction="""
    You are a DevOps assistant that can run kubectl commands on an existing cluster.
    - If the user asks to create, list, or delete deployments/pods, generate the correct kubectl command.
    - Execute it using the run_kubectl_command() function and return the output.
    - Always confirm before deleting resources.
    """,
    tools=[run_kubectl_command],
)

