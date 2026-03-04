import json
import sys
import re

file_path = sys.argv[1]

with open(file_path, "r") as f:
    text = f.read()

memo = {
    "account_id": "account_001",
    "company_name": "",
    "business_hours": {
        "days": "",
        "start": "",
        "end": "",
        "timezone": ""
    },
    "services_supported": [],
    "emergency_definition": [],
    "emergency_routing_rules": "",
    "non_emergency_routing_rules": "",
    "call_transfer_rules": "",
    "integration_constraints": [],
    "after_hours_flow_summary": "",
    "office_hours_flow_summary": "",
    "questions_or_unknowns": [],
    "notes": ""
}

# extract company name
company_match = re.search(r'Company:\s*(.*)', text)
if company_match:
    memo["company_name"] = company_match.group(1)

# services
if "sprinkler" in text.lower():
    memo["services_supported"].append("sprinkler service")

if "fire alarm" in text.lower():
    memo["services_supported"].append("fire alarm service")

# emergency detection
if "emergency" in text.lower():
    memo["emergency_definition"].append("sprinkler leak or alarm trigger")

print(json.dumps(memo, indent=2))