from litellm import completion
import string
import random
import os
import dspy
lm = dspy.LM("openai/gpt-4o-mini")
response = completion(
  model="gpt-4o-mini",
  messages=[{ "content": f"{random.choices(string.digits,k=1)}Hello, how are you?","role": "user"}]
)
print(response)

