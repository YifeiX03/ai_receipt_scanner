#!/usr/bin/env python
import sys
import warnings

from crewai.flow.flow import Flow, listen, start

from crew import AiReceiptScanner
from crew_report import ReportingCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

class ExpensesPipeline(Flow):
    @start()
    def fetch_receipts(self):
        receipts = [
            {'image_path_url': 'receipt-pics/receipt-1.jpg'},
            {'image_path_url': 'receipt-pics/receipt-2.png'}   
        ]
        return receipts

    @listen(fetch_receipts)
    def decide_expenses(self, receipts):
        decisions = AiReceiptScanner().crew().kickoff_for_each(receipts)
        self.state['decisions'] = decisions
        return decisions

    @listen(decide_expenses)
    def submit_expenses(self, decisions):
        for decision in decisions:
            print(f"Decision: {decision['decision']}")
            print(f"Reason: {decision['reason']}")

    @listen(decide_expenses)
    def write_expense_report(self, decisions):
        ReportingCrew().crew().kickoff({'decisions': decisions})

def run_flow():
    ExpensesPipeline().kickoff() 

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'image_path_url': 'receipt-pics/receipt-1.jpg',
    }
    # AiReceiptScanner().crew().kickoff(inputs=inputs)
    crew = AiReceiptScanner().crew()
    crew.kickoff(inputs=inputs)
    tokens_used = crew.usage_metrics.prompt_tokens + crew.usage_metrics.completion_tokens
    costs = 0.150 * (tokens_used) / 1_000_000
    print("Tokens used: ", tokens_used)
    print(f"Costs: ${costs:.2f}")

if __name__ == "__main__":
    # run()
    run_flow()
    # ReportingCrew().crew().kickoff({
    #     'decisions': [
    #         {
    #             'decision': 'approve',
    #             'reason': '"The total amount spent at Sweetfish Sushi is $22.12, which is below the $50 threshold set by the policy for food purchases. Therefore, this expense is allowed.'
    #         }
    #     ]
    # })

# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         AiReceiptScanner().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         AiReceiptScanner().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         AiReceiptScanner().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

