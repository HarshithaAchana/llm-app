import subprocess


def ask_ollama(question, model="tinyllama"):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=question.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )
        stdout = result.stdout.decode("utf-8").strip()
        stderr = result.stderr.decode("utf-8").strip()

        if stdout:
            return stdout
        elif stderr:
            return f"⚠️ Ollama error:\n{stderr}"
        else:
            return "⚠️ No response from Ollama."
    except Exception as e:
        return f"❌ Exception while calling Ollama:\n{str(e)}"
