import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

QUESTION = """
Your manager, Nancy, would like a status update describing your progress on developing the microprocessor simulation.  Write an email message to Nancy that provides a high-level description of how the program functions, and outlines the portion of the work that you found most challenging and how you overcame that challenge.  Remember that Nancy is busy!  She is managing a team of 15 people and will be reviewing everyone's status update each week.  Nancy is a technical manager, so she understands software development; however, she probably doesn't need a line-by-line explanation of your code. It's important that your message is clearly and concisely addresses the above two points as efficiently as possible.   
"""


RUBRIC = """
| Criteria    | Proficient (3)     | Competent (2)     | Developing (1)   |
|-------------|--------------------|-------------------|------------------|
| Clarity     | The email is exceptionally clear and easy to understand, utilizing straightforward language tailored for Nancy. | The email is clear, though minor instances of unnecessary complexity or ambiguity may be present. | The email lacks clarity, with convoluted language that might hinder Nancy's understanding. |
| Conciseness | The email efficiently addresses both points, providing a high-level description of the program's function and addressing the challenging portion succinctly. | The email is mostly concise, though some areas could be more succinct while still covering the required information. | The email tends to be wordy, potentially overwhelming Nancy with unnecessary details. |
| Concreteness| The email includes specific examples or details to illustrate the program's function and the challenging portion, aiding Nancy's comprehension. | The email provides some concrete details, but further elaboration and examples could enhance clarity. | The email lacks specific examples or specifics, making it challenging for Nancy to visualize the content. |
| Correctness | The email is accurate and error-free, maintaining a professional tone and polished language. | The email contains minor errors that do not significantly affect the overall accuracy and professionalism. | The email has noticeable errors in grammar, spelling, or tone that detract from the message's credibility. |
| Coherence   | The email is well-organized, presenting information in a logical sequence that aligns with the task's requirements. | The email is structured logically, though some areas might benefit from improved organization. | The email lacks a clear structure, making it challenging for Nancy to follow the flow of information. |
| Completeness| The email fully addresses both points, offering a comprehensive high-level description and explanation of the challenging portion. | The email covers both points but might lack depth in either the program's function or the explanation of the challenge. | The email omits significant aspects of either the program's function or the challenge, impacting Nancy's understanding. |
| Courtesy    | The email demonstrates consideration for Nancy's busy schedule and technical understanding, using a respectful and considerate tone. | The email acknowledges Nancy's role and technical understanding, though some sections might be overly casual or unintentionally insensitive. | The email lacks consideration for Nancy's perspective, potentially coming across as dismissive or inconsiderate. |

"""

with open('./ProjectSummary.txt') as f:
    STUDENT_ANSWER = f.readlines()

PROMPT = """
Evaluate the student's answer to the question using the provided rubric. Use specific examples from the student's work to justify the evaluation. Your evaluation should be no more than 1000 words and should provide a recommended score for each performance indicator.  Format the output in JSON such that each of the performance indicators is contained within an array called 'tests', which has a 'name' field with the performance indicator, a 'score' field with the performance indicator's score, and an `output` field with the justification for that indicator's score.
"""

messages=[
    {"role": "system", "content": "You are an instructor evaluating student work using a provided rubric."},
    {"role": "user", "content": f"The question posed to the student is:\n {QUESTION}"},
    {"role": "user", "content": f"The rubric is:\n {RUBRIC}"},
    {"role": "user", "content": f"The student's answer is:\n {STUDENT_ANSWER}"},
    {"role": "user", "content": PROMPT}
]

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

# Do a little manual cleanup for now so that the scores aren't actually included in the overall score.
results = json.loads(chat_completion.choices[0].message.content)
results['execution_time'] = 0.0

results['score'] = 0
results['output'] = "These assessments are informational only and will not be directly included in your grade for this project without review by your instructors."

for test in results['tests']:
    test['output'] += f" [Recommended Score: {test['score']}/3]"
    test['name'] = f"Project Summary - {test['name']}"
    test['score'] = 0


with open("project_summary_results.json", 'w') as f:
    json.dump(results, f, indent=4)
