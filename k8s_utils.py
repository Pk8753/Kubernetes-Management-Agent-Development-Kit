import subprocess

def run_kubectl_command(command: str):
    """
    Run a kubectl command and return the output or error.
    Example command: 'get pods' or 'create deployment nginx --image=nginx'
    """
    try:
        full_command = f"kubectl {command}"
        result = subprocess.run(
            full_command, shell=True, capture_output=True, text=True
        )
        if result.returncode == 0:
            return f"Command executed successfully:\n{result.stdout}"
        else:
            return f"Error executing command:\n{result.stderr}"
    except Exception as e:
        return f" Exception: {str(e)}"

