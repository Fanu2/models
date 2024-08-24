import os
import subprocess
import sys

# Define paths
project_path = '/home/jasvir/PycharmProjects/HuggingFaceInteractions'
venv_path = os.path.join(project_path, 'venv')
requirements_path = os.path.join(project_path, 'requirements.txt')

# Create a requirements file with the needed packages
requirements = """
transformers
torch
"""

with open(requirements_path, 'w') as f:
    f.write(requirements)

# Ensure the virtual environment is created
if not os.path.exists(os.path.join(venv_path, 'bin', 'python')):
    subprocess.check_call([sys.executable, '-m', 'venv', venv_path])

# Install the packages
try:
    subprocess.check_call([os.path.join(venv_path, 'bin', 'pip'), 'install', '-r', requirements_path])
except subprocess.CalledProcessError as e:
    print(f"Error installing packages: {e}")
    sys.exit(1)

print("Project setup complete.")
