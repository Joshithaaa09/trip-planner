from crewai import Agent

from browser_tools import BrowserTools, SearchTools
from calculator_tools import CalculatorTools


class TripAgents:

    def city_selection_agent(self):
        return Agent(
            role="City Selection Expert",
            goal=(
                "Select the best destination based on weather, season, "
                "travel costs, and the traveler's interests."
            ),
            backstory=(
                "An experienced travel researcher who compares destinations "
                "using current information from the web."
            ),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            verbose=True,
        )

    def local_expert(self):
        return Agent(
            role="Local Expert",
            goal=(
                "Provide useful and practical information about the selected "
                "destination, including attractions, culture, food, and travel tips."
            ),
            backstory=(
                "A knowledgeable local guide with extensive knowledge of "
                "destinations, attractions, customs, and hidden gems."
            ),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            verbose=True,
        )

    def travel_concierge(self):
        return Agent(
            role="Travel Concierge",
            goal=(
                "Create a detailed and practical itinerary including activities, "
                "hotels, restaurants, transportation, packing suggestions, and budget."
            ),
            backstory=(
                "A professional travel planner who turns research into "
                "realistic day-by-day travel plans."
            ),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
                CalculatorTools.calculate,
            ],
            verbose=True,
        )
