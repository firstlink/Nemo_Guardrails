from nemoguardrails import RailsConfig, LLMRails
import os

os.environ["OPENAI_API_KEY"] = "<OpenAI-API-Key>"
config = RailsConfig.from_path("./config")
llm_rail = LLMRails(config)

# Disallowed Topic
response = llm_rail.generate(messages=[{
    "role": "user",
    "content": "Top 5 vacation place in Europe?"
}])

# Allowed Topic
# response = llm_rail.generate(messages=[{
#     "role": "user",
#     "content": "How to play ping pong?"
# }])

print(response["content"])
