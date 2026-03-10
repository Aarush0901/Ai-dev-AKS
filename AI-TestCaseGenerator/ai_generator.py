from openai import OpenAI

client = OpenAI()

def generate_test_case(steps):

    step_text = "\n".join(steps)

    prompt = f"""
You are a QA automation expert.

Convert the following user steps into a professional test case.

User Steps:
{step_text}

Return the result in this format:

Title:
Preconditions:
Test Steps:
Expected Result:
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a QA automation expert"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content