prompt_generate_questions = """
You are an expert at creating insightful, theory-based questions from any text. Given the following document, generate a list of 10 to 15 relevant, clear, and self-contained questions that could be asked about its content.

### Instructions:
- Carefully read and understand the provided text.
- Generate 10 to 15 diverse, meaningful questions that test understanding of the document's key concepts, facts, or arguments.
- Do NOT include answers, explanations, or commentary.
- Each question should be on a new line, with no numbering, bullets, or extra formatting.
- Questions must be self-contained and clearly phrased.

### Input Text:
{text}

### Output:
A list of 10 to 15 relevant, theory-based questions, each on a separate line (no answers, no extra formatting).
"""