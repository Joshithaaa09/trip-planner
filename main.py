from textwrap import dedent

from crewai import Crew, Process
from dotenv import load_dotenv

from trip_agents import TripAgents
from trip_tasks import TripTasks


load_dotenv()


class TripCrew:

    def __init__(
        self,
        origin,
        cities,
        date_range,
        interests
    ):

        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):

        agents = TripAgents()
        tasks = TripTasks()

        city_selector_agent = (
            agents.city_selection_agent()
        )

        local_expert_agent = (
            agents.local_expert()
        )

        travel_concierge_agent = (
            agents.travel_concierge()
        )

        identify_task = tasks.identify_task(
            city_selector_agent,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        gather_task = tasks.gather_task(
            local_expert_agent,
            self.origin,
            self.interests,
            self.date_range
        )

        plan_task = tasks.plan_task(
            travel_concierge_agent,
            self.origin,
            self.interests,
            self.date_range
        )

        crew = Crew(
            agents=[
                city_selector_agent,
                local_expert_agent,
                travel_concierge_agent
            ],

            tasks=[
                identify_task,
                gather_task,
                plan_task
            ],

            process=Process.sequential,

            verbose=True
        )

        return crew.kickoff()


if __name__ == "__main__":

    print()
    print("================================")
    print("       AI TRIP PLANNER")
    print("================================")
    print()

    origin = input(
        dedent(
            """
            From where will you be traveling from?
            """
        )
    )

    cities = input(
        dedent(
            """
            Which cities are you considering?
            """
        )
    )

    date_range = input(
        dedent(
            """
            What is your travel date or date range?
            """
        )
    )

    interests = input(
        dedent(
            """
            What are your interests and hobbies?
            """
        )
    )

    trip_crew = TripCrew(
        origin,
        cities,
        date_range,
        interests
    )

    result = trip_crew.run()

    print()
    print("================================")
    print("          TRIP PLAN")
    print("================================")
    print()

    print(result)
