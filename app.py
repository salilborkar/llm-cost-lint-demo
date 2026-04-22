import boto3

client = boto3.client("bedrock-runtime")

def summarize(text: str) -> str:
    response = client.invoke_model(
        modelId="anthropic.claude-3-haiku-20240307-v1:0",
        body='{"prompt": "' + text + '", "max_tokens": 500}'
    )
    return response["body"].read().decode()
