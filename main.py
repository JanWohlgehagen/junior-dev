import autogen
from autogen.coding import LocalCommandLineCodeExecutor

# Define the LLM configuration
llm_config = {
    "model": "llama3.2:3b",
    "client_host": "127.0.0.1:11434",
    "api_type": "ollama",
    "num_predict": -2,
    "repeat_penalty": 1.1,
    "stream": False,
    "seed": 42,
    "temperature": 0,
    "top_k": 50,
    "top_p": 0.8,
    "native_tool_calls": False,
    "cache_seed": None,
}

# Create an AssistantAgent named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
)

# Create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "executor": LocalCommandLineCodeExecutor(work_dir="coding"),
    },
)

# Define the task for the assistant
chat_res = user_proxy.initiate_chat(
    assistant,
    message="""
Write a Python function `calculate_average` that:
1. Takes a list of integers as input.
2. Returns the average of the integers, or 0 if the list is empty.

Additionally, write test cases to verify the function works as expected. 
Do not use assertions to validate the results with example inputs and outputs.
""",
    summary_method="reflection_with_llm",
)

