import boto3
# AWS Software Development Kit (SDK) for Python

def check_guardrail(text: str):

    client = boto3.client(
        "bedrock-runtime",
        region_name="eu-north-1"
    )

    response = client.apply_guardrail(
        guardrailIdentifier="sf8n1nsion1v",
        guardrailVersion="1",
        source="INPUT",
        content=[
            {
                "text": {
                    "text": text
                }
            }
        ]
    )

    action = response.get("action")

    print("Guardrail action:", action)

    # Only block when guardrail intervenes
    if action == "GUARDRAIL_INTERVENED" or action == "BLOCK":
        return False

    return True