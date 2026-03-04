import json
import sys

memo_file = sys.argv[1]

with open(memo_file) as f:
    memo = json.load(f)

company = memo.get("company_name", "Service Company")

# detect version from memo
version = memo.get("version", "v1")

agent = {
    "agent_name": f"{company} AI Assistant",
    "version": version,
    "voice_style": "professional calm",

    "variables": {
        "company_name": company,
        "business_hours": memo["business_hours"]
    },

    "system_prompt": f"""
You are Clara, the AI call assistant for {company}.

BUSINESS HOURS FLOW
1. Greet caller professionally
2. Ask reason for call
3. Collect caller name and phone number
4. Route or transfer the call
5. If transfer fails apologize and note follow-up
6. Ask if they need anything else
7. End call politely

AFTER HOURS FLOW
1. Greet caller
2. Ask purpose of call
3. Determine if emergency
4. If emergency collect name, phone, and address
5. Attempt transfer to dispatch
6. If transfer fails assure quick follow-up
7. Ask if anything else is needed
8. Close the call
"""
}

print(json.dumps(agent, indent=2))