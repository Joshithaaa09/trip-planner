# AI Trip Planner

An AI-powered multi-agent travel planning system built with Python, CrewAI, and Ollama. The application researches destinations, gathers local information, and generates personalized travel itineraries based on the user's preferences.

## Overview

AI Trip Planner uses a multi-agent architecture where each agent has a specialized responsibility in the travel-planning process.

The user provides:

- Starting location
- Destination options
- Travel dates
- Interests and preferences

The system then processes this information through a sequence of specialized agents to produce a detailed travel plan.

The project uses Ollama to run the language model locally, allowing the application to operate without relying on paid OpenAI API credits.

## Features

- Multi-agent travel planning using CrewAI
- Destination comparison and selection
- Internet-based travel research
- Local destination information
- Attraction and activity recommendations
- Restaurant recommendations
- Hotel recommendations
- Transportation suggestions
- Weather and seasonal considerations
- Packing recommendations
- Budget estimation
- Day-by-day itinerary generation
- Safe mathematical calculations
- Local LLM execution using Ollama

## Architecture

The application follows a sequential multi-agent workflow:

```text
User Input
    |
    v
City Selection Agent
    |
    v
Destination Research
    |
    v
Local Expert Agent
    |
    v
Local Destination Research
    |
    v
Travel Concierge Agent
    |
    v
Itinerary Generation
    |
    v
Final Travel Plan


```
## Tech Stack

### Languages
- Python

### AI & Agent Framework
- CrewAI
- Ollama
- Llama 3.2 1B

### Web & Data Retrieval
- DuckDuckGo Search
- Python `urllib`
- HTML parsing and text extraction

### Libraries & Tools
- python-dotenv
- Unstructured
- Python AST
- Operator

### Development Tools
- Git
- GitHub
- Visual Studio Code
