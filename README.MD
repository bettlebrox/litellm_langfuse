relates to https://github.com/langfuse/langfuse/issues/3757

steps to reproduce:
1. pip install requirements.txt
2. python test.py

result:
exception trace

mitigation:
pip uninstall langfuse
OR
comment dspy import and configure
