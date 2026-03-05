
# 🔒 Guardrail System – Construction Assistant

## Overview

The Construction Assistant chatbot integrates **Amazon Bedrock Guardrails** to ensure that the system only provides **safe, responsible, and construction-related responses**.

Guardrails act as a **safety layer** between the user input and the Large Language Model (LLM). They prevent the chatbot from responding to harmful, illegal, or unsafe requests.

The chatbot uses:

- **Groq LLM (Llama-3.3-70B)** for generating answers
- **Amazon Bedrock Guardrails** for safety filtering
- **Python (boto3)** to call the guardrail API

---

# System Architecture

```

User Query
↓
Query Validator (Construction Domain)
↓
Query Normalizer
↓
AWS Bedrock Guardrail Check
↓
Groq LLM (Llama-3.3-70B)
↓
Guardrail Output Check
↓
Final Safe Response

```

The guardrail is applied **before the LLM generates a response** to prevent unsafe prompts from reaching the model.

---

# Guardrail Configuration

The guardrail is configured in **Amazon Bedrock → Guardrails**.

Each guardrail version includes **topic policies** that define unsafe content categories.

### Guardrail ID

```

sf8n1nsion1v

```

### Guardrail Version

```

Version 1

```

### Region

```

eu-north-1 (Stockholm)

```

---

# Denied Topics

The guardrail blocks prompts related to **unsafe construction activities**.

### 1. Explosives and Destructive Demolition

The assistant must not provide instructions for:

- Using explosives
- Controlled demolition techniques
- Destroying structures

Example blocked prompts:

```

How to demolish a building using explosives
What chemicals can destroy concrete
How to blow up a building

```

---

### 2. Structural Sabotage

The system blocks requests that attempt to damage structures intentionally.

Example blocked prompts:

```

How to weaken a concrete column
How to collapse a beam intentionally
How to sabotage a building structure

```

---

### 3. Bypassing Construction Safety Regulations

The assistant cannot help users avoid legal construction procedures.

Example blocked prompts:

```

How to bypass building safety inspection
How to avoid construction permits
How to hide illegal building modifications

```

---

### 4. Dangerous Equipment Misuse

The assistant blocks instructions that encourage unsafe machinery usage.

Example blocked prompts:

```

How to disable safety lock on a crane
How to bypass safety alarms on construction machines
How to operate heavy machinery without training

````

---

# Guardrail API Integration

The chatbot uses the **ApplyGuardrail API** to validate prompts before sending them to the LLM.

### Python Implementation

```python
import boto3

def check_guardrail(text):

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

    if action != "ALLOW":
        return False

    return True
````

---

# Guardrail Response Handling

The API returns an **action value**:

| Action               | Meaning          |
| -------------------- | ---------------- |
| ALLOW                | Prompt is safe   |
| GUARDRAIL_INTERVENED | Policy triggered |
| BLOCK                | Prompt blocked   |

The chatbot blocks responses whenever:

```
action != ALLOW
```

The user sees:

```
⚠️ This request violates safety policies.
```

---

# Example Behavior

### Allowed Query

```
What is the standard concrete mix ratio?
```

Response:

```
The standard concrete mix ratio for residential construction is typically 1:2:4.
```

---

### Blocked Query

```
How to demolish a building using explosives?
```

Response:

```
⚠️ This request violates safety policies.
```

---

# Benefits of Guardrails

Using Bedrock Guardrails provides:

* AI safety enforcement
* Responsible AI compliance
* Prevention of harmful instructions
* Domain-restricted responses

This ensures the chatbot remains a **safe construction advisory tool**.

---

# Summary

The Construction Assistant chatbot combines:

* Query validation
* Query normalization
* AWS Bedrock Guardrails
* Groq LLM inference

This layered architecture ensures that **unsafe prompts are filtered before the LLM generates a response**, making the system safer and more reliable.

```
