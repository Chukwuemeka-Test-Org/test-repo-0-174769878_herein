import subprocess

GIHUB_TOKEN="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"
def run_cmd(cmd):
    subprocess.call(cmd, shell=True)  # ⚠️ CodeQL flags this as risky
