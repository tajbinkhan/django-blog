import os
import sys
import subprocess

# Get the path to the Python interpreter in the virtual environment
venv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".venv")
python_path = os.path.join(venv_path, "Scripts", "python.exe")

# Install the package using the Python interpreter in the virtual environment
subprocess.run([python_path, "-m", "pip", "uninstall"] + sys.argv[1:])

# Update the requirements.txt file using the Python interpreter in the virtual environment
print("Updating requirements.txt...")
subprocess.run(
	[python_path, "-m", "pip", "freeze"], stdout=subprocess.PIPE, text=True, check=True
)
with open("requirements.txt", "w", encoding="utf-8") as f:
	f.write(
		subprocess.run(
			[python_path, "-m", "pip", "freeze"],
			stdout=subprocess.PIPE,
			text=True,
			check=True,
		).stdout
	)

print("Successfully updated requirements.txt")
