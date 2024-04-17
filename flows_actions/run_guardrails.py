from nemoguardrails import RailsConfig, LLMRails
import os


def main():
    os.environ["openai_api_key"] = "<OpenAI-API-Key>"
    config = RailsConfig.from_path("./config")
    rails = LLMRails(config)
    response = rails.generate(messages=[
        {"role": "context", "content": {"name": "John"}},
        {"role": "user", "content": "Hey there!"}
    ])
    print(response["content"])


if __name__ == "__main__":
    main()