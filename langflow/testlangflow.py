from langflow import load_flow_from_json

flow = load_flow_from_json("New_flow.json")
# Now you can use it like any chain
flow("Hey, have you heard of LangFlow?")