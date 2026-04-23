import boto3

client = boto3.client("bedrock-runtime")

def summarize(text: str) -> str:
    response = client.invoke_model(
        modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
        body='{"prompt": "' + text + '", "max_tokens": 2000}'
    )
    return response["body"].read().decode()
#dogfooding2
