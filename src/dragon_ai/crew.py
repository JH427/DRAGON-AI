from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from dragon_ai.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class DragonAiCrew():
	"""DragonAi crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def leader(self) -> Agent:
		return Agent(
			config=self.agents_config['leader'],
			# tools=[], # No tools initially
			verbose=True
		)

	@task
	def initial_communication_task(self) -> Task:
		return Task(
			config=self.tasks_config['initial_communication_task'],
			agent=self.leader()
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the DRAGON AI crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)