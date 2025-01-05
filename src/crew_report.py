from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ReportingCrew():
  agents_config = 'config/agents_report.yaml'
  tasks_config = 'config/tasks_report.yaml'
	
  @agent
  def reporter(self) -> Agent:
    return Agent(
      config=self.agents_config['reporter'],
      verbose=True
    )

  @task
  def report_task(self) -> Task:
    return Task(
      config=self.tasks_config['reporting_task'],
      output_file='expense_report.md'
    )

  @crew
  def crew(self) -> Crew:
    return Crew(
      agents=self.agents,
      tasks=self.tasks,
      process=Process.sequential,
      Verbose=True,
    )