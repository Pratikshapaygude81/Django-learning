# Django Installation Prerequisites
## Reference:-https://www.w3schools.com/django/django_getstarted.php

Django is a high-level Python web framework used to develop web applications. Before installing Django, we need to make sure that Python and PIP are installed and configured correctly.

## 1. Django Requires Python

Django is written in Python, so Python must be installed on your computer before installing Django.

### Check Python Installation

Open Command Prompt or PowerShell and execute the following command:

```bash
python --version
```

If Python is installed, the command displays the installed version.

Example:

```text
Python 3.12.5
```

On Windows, you can also use:

```bash
py --version
```

### Installing Python

If Python is not installed:

1. Visit the official Python website: https://www.python.org/downloads/
2. Download a Python version supported by your Django version.
3. Run the installer.
4. On Windows, select the **Add Python to PATH** option.
5. Complete the installation.
6. Open a new terminal and verify the installation using `python --version`.

**Note:** Always check the Django documentation to confirm which Python versions are supported by the Django version you want to install.

## 2. PIP (Python Package Installer)

PIP is the package manager for Python. It is used to install, update, and manage Python packages and libraries.

PIP is generally included with Python installations from Python 3.4 onwards.

### Check PIP Installation

Execute the following command:

```bash
python -m pip --version
```

If PIP is installed, the command displays its version and installation location.

Example:

```text
pip 24.x from ... (python 3.12)
```

You can also check using:

```bash
pip --version
```

### Installing or Updating PIP

If PIP is not available, try installing it using Python's built-in `ensurepip` module:

```bash
python -m ensurepip --upgrade
```

To upgrade PIP to the latest available version:

```bash
python -m pip install --upgrade pip
```

Official PIP documentation: https://pip.pypa.io/en/stable/installation/

## 3. Virtual Environment

A virtual environment is an isolated Python environment created for a particular project.

It allows us to install project-specific packages without affecting other Python projects on the same computer.

### Advantages of Virtual Environment

- Keeps project dependencies separate.
- Prevents conflicts between package versions.
- Makes project management easier.
- Helps maintain a consistent development environment.

### Creating a Virtual Environment

Navigate to your project directory and execute:

```bash
python -m venv .venv
```

This creates a virtual environment named `.venv`.

### Activating a Virtual Environment

**For Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**For Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

After successful activation, the environment name appears at the beginning of the terminal prompt.

Example:

```text
(.venv) PS C:\project>
```

### Deactivating a Virtual Environment

To deactivate the virtual environment, execute:

```bash
deactivate
```

## 4. Installing Django

After installing Python and PIP and activating the virtual environment, Django can be installed using PIP.

Execute:

```bash
python -m pip install Django
```

PIP downloads Django and installs it along with its required dependencies.

## 5. Verifying Django Installation

To check whether Django has been installed successfully, execute:

```bash
python -m django --version
```

The command displays the installed Django version.

You can also verify the installation using Python:

```python
import django

print(django.get_version())
```

## 6. Creating a Django Project

After installing Django, we can create a new Django project.

Execute the following command:

```bash
django-admin startproject myproject
```

Here, `myproject` is the name of the Django project.

Navigate into the project directory:

```bash
cd myproject
```

Django creates the initial project structure and configuration files.

## 7. Running the Django Development Server

Navigate to the directory containing the `manage.py` file.

Execute:

```bash
python manage.py runserver
```

Django starts its development server.

By default, the application runs at:

```text
http://127.0.0.1:8000/
```

Open this URL in your web browser to view the Django welcome page.

To stop the development server, press:

```text
Ctrl + C
```

**Note:** Django's built-in development server is intended for development and testing, not production deployment.

## 8. Common Django Installation Commands

| Purpose | Command |
|---|---|
| Check Python version | `python --version` |
| Check PIP version | `python -m pip --version` |
| Create virtual environment | `python -m venv .venv` |
| Activate virtual environment | `.\.venv\Scripts\Activate.ps1` |
| Deactivate virtual environment | `deactivate` |
| Install Django | `python -m pip install Django` |
| Upgrade PIP | `python -m pip install --upgrade pip` |
| Check Django version | `python -m django --version` |
| Create Django project | `django-admin startproject myproject` |
| Run Django server | `python manage.py runserver` |

## 9. Common Installation Errors

### 1. Python is not recognized

**Reason:** Python may not be installed or added to the system PATH.

**Solution:**
- Verify that Python is installed.
- Try `py --version`.
- Add Python to PATH if necessary.
- Restart the terminal.

### 2. PIP is not recognized

**Reason:** PIP may not be available through the system PATH.

**Solution:** Use:

```bash
python -m pip --version
```

If PIP is missing, try:

```bash
python -m ensurepip --upgrade
```

### 3. No module named Django

**Reason:** Django may not be installed in the currently active Python environment.

**Solution:**

```bash
python -m pip install Django
```

Make sure the correct virtual environment is activated.

### 4. Multiple Python Versions Installed

Sometimes multiple Python versions are installed on the same computer.

To check the Python executable paths on Windows, run:

```powershell
where.exe python
```

To list Python installations detected by the Python launcher, run:

```powershell
py -0p
```

Make sure the intended Python interpreter is used when creating the virtual environment and installing Django.

## 10. Important Points to Remember

- Django requires a compatible Python version.
- PIP is used to install and manage Python packages.
- A virtual environment isolates project dependencies.
- Django should preferably be installed inside the project's virtual environment.
- Use `python -m pip` to ensure PIP runs with the selected Python interpreter.
- Verify the Django installation before creating a project.
- Use the development server for local development and testing.

## Official Documentation

- Python Downloads: https://www.python.org/downloads/
- Django Installation Guide: https://docs.djangoproject.com/en/6.1/topics/install/
- Django Quick Install Guide: https://docs.djangoproject.com/en/6.1/intro/install/
- Django Windows Guide: https://docs.djangoproject.com/en/6.1/howto/windows/
- Python Virtual Environment: https://docs.python.org/3/library/venv.html
- PIP Installation Guide: https://pip.pypa.io/en/stable/installation/
