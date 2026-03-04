import os
import subprocess

demo_folder = "dataset/demo_calls"

for file in os.listdir(demo_folder):
    if file.endswith(".txt"):
        account_id = file.split(".")[0]

        print(f"Processing {file}")

        # create account folders
        v1_path = f"outputs/accounts/{account_id}/v1"
        os.makedirs(v1_path, exist_ok=True)

        transcript_path = f"{demo_folder}/{file}"

        memo_path = f"{v1_path}/memo.json"
        agent_path = f"{v1_path}/agent.json"

        # run extraction
        subprocess.run(
            f"python scripts/extract_data.py {transcript_path} > {memo_path}",
            shell=True
        )

        # generate agent
        subprocess.run(
            f"python scripts/generate_agent.py {memo_path} > {agent_path}",
            shell=True
        )

print("Batch processing completed.")