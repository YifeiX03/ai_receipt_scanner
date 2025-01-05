from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import VisionTool, SerperDevTool
from tools.reporting_tool import ReportingTool
# from crewai.knowledge.source import CrewDoclingSource
from pydantic import BaseModel

vision_tool = VisionTool(image_path_url="receipt-pics/receipt-1.jpg")
serper_dev_tool = SerperDevTool()
reporting_tool = ReportingTool()

# text_source = CrewDoclingSource(
# 	file_paths=["../knowledge/policy.txt"]
# )
# knowledge = Knowledge(
	# collection_name="text_knowledge",
	# sources=[text_source]
# )

class ExpenseForm(BaseModel):
	decision: str
	reason: str

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class AiReceiptScanner():
	"""AiReceiptScanner crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def scanner(self) -> Agent:
		return Agent(
			config=self.agents_config['scanner'],
			verbose=True,
			max_iter=1,
			tools=[vision_tool]
		)

	@agent
	def merchant_finder(self) -> Agent:
		return Agent(
			config=self.agents_config['merchant_finder'],
			verbose=True,
			tools=[serper_dev_tool]
		)

	@agent
	def policy_decider(self) -> Agent:
		return Agent(
			config=self.agents_config['policy_decider'],
			verbose=True,
			# knowledge_sources=[text_source],
			# tools=[reporting_tool]
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def scanning_task(self) -> Task:
		return Task(
			config=self.tasks_config['scanning_task'],
		)

	@task
	def find_merchant_task(self) -> Task:
		return Task(
			config=self.tasks_config['find_merchant_task'],
		)

	@task 
	def decide_policy_task(self) -> Task:
		return Task(
			config=self.tasks_config['decide_policy_task'],
			output_json=ExpenseForm,
			output_file='expense_report.json'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AiReceiptScanner crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
