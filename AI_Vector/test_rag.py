from rag_generator import generate_testcase

steps = """
1 Click search
2 Drag STUDENT table
3 Add to task chain
4 Save
"""

result = generate_testcase(steps)

print(result)