import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads OPENAI_API_KEY from .env
client = OpenAI()

# ============================================================
# DEMO 1: Testing the Flagship Model (gpt-4o)
# ============================================================
PROMPT = "how many 'a' in the word person ?"


response_flagship = client.chat.completions.create(
   model="gpt-4o",
   messages=[{"role": "user", "content": PROMPT}],
   max_tokens=200,
   temperature=0.0
)


gpt_output = response_flagship.choices[0].message.content
gpt_input_tokens = response_flagship.usage.prompt_tokens
gpt_output_tokens = response_flagship.usage.completion_tokens


# ============================================================
# DEMO 2: Testing the Efficiency Model (gpt-4o-mini)
# ============================================================
response_mini = client.chat.completions.create(
   model="gpt-4o-mini",
   messages=[{"role": "user", "content": PROMPT}],
   max_tokens=200,
   temperature=0.0
)


mini_output = response_mini.choices[0].message.content
mini_input_tokens = response_mini.usage.prompt_tokens
mini_output_tokens = response_mini.usage.completion_tokens


# ============================================================
# DEMO 3: Side-by-Side Calibration Dashboard
# ============================================================
print("============================================================")
print(f"GLOBAL INSTRUCTION: '{PROMPT}'")
print("============================================================\n")


print("FLAGSHIP SELECTION (gpt-4o)")
print("-" * 60)
print(gpt_output)
print(f"Tokens Used -> Input (Prompt): {gpt_input_tokens} | Output (Generated): {gpt_output_tokens}\n")


print("⚡ EFFICIENCY SELECTION (gpt-4o-mini)")
print("-" * 60)
print(mini_output)
print(f"Tokens Used -> Input (Prompt): {mini_input_tokens} | Output (Generated): {mini_output_tokens}\n")
