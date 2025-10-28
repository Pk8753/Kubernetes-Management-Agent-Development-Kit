# Kubernetes-Management-Agent-Development-Kit
This project uses Google’s Agent Development Kit (ADK) to build a conversational agent (or set of agents) that can help **manage a Kubernetes cluster** We are using Rancher instance, e.g., on Google Kubernetes Engine (GKE).

# What is Agent Development Kit?

Agent Development Kit (ADK) is a flexible and modular framework for developing and deploying AI agents. While optimized for Gemini and the Google ecosystem, ADK is model-agnostic, deployment-agnostic, and is built for compatibility with other frameworks. ADK was designed to make agent development feel more like software development, to make it easier for developers to create, deploy, and orchestrate agentic architectures that range from simple tasks to complex workflows.


##  What You'll Learn

- Setting up the **Google ADK** environment  
- Creating your **first conversational agent**  
- Implementing **Natural Language Understanding (NLU)**  
- Integrating with **Google services**  
- **Testing** and **deploying** agents  


## What You'll Build

- A **simple greeting agent**  
- A **weather information agent**  
- A **task management agent**  
- Integration with **Google Assistant**  


## Prerequisites

- Python 3.8+ installed  
- A Google Cloud Platform (GCP) project with GKE, Vertex AI API and AI Studio enabled  
- `kubectl` configured for your GKE cluster or Rancher Instance 
- Basic familiarity with REST APIs, JSON, and Kubernetes  
- (Optional) Docker / containerization tools if deploying the agent 


## ⚙️ Install and Set Up ADK

### 1. Create a Virtual Environment

First, create and activate a virtual environment to manage dependencies:

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# macOS/Linux:
source .venv/bin/activate
# Windows CMD:
.venv\Scripts\activate.bat
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Install ADK
pip install google-adk



```

### 2. Install Google ADK

Install the Google ADK directly from the GitHub repository:

```bash
# Install ADK from GitHub
pip install git+https://github.com/google/adk-python.git@main

# Install additional dependencies
pip install requests python-dotenv
```

### 3. Create an .env file in parent directory to pass environment variables.

```bash
# For Google AI Studio
GOOGLE_API_KEY=<AI Studio KEY>

GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=<GCP Project>
GOOGLE_CLOUD_LOCATION=us-central1
```
### 4. Run the Agent Locally for Testing
```bash
adk web
```
### 4. 

