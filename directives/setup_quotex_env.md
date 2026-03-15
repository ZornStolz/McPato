# Quotex API Environment Setup Directive

**Objective:** Create a Python environment capable of running the Quotex API, utilizing the `API-Quotex` repository.

## 1. Prerequisites
- Python 3.9+ (The repository requires a modern Python version due to asynchronous and typing features).

## 2. Setup Steps
1. **Repository:** Ensure the `API-Quotex` repository is cloned into the workspace.
   ```bash
   git clone https://github.com/A11ksa/API-Quotex
   ```
2. **Environment:** Create a virtual environment for the dependencies. 
   ```bash
   python -m venv venv
   ```
3. **Execution Policy (Windows):** If you encounter an `UnauthorizedAccess` error when activating the environment, you may need to bypass the execution policy or invoke python directly from the Scripts folder:
   ```bash
   # Option 1: Activate if policy allows
   .\venv\Scripts\activate  
   
   # Option 2: Run directly
   venv\Scripts\python.exe -m pip install -U pip
   ```
4. **Dependencies:** Install the API-Quotex project as a local editable package and install playwright alongside the required undocumented dependencies.
   ```bash
   venv\Scripts\python.exe -m pip install -e ./API-Quotex
   venv\Scripts\python.exe -m pip install python-dotenv pandas loguru cloudscraper beautifulsoup4 rich setuptools
   venv\Scripts\python.exe -m playwright install chromium
   ```

## 3. Configuration
The API uses Playwright to extract the SSID.
1. Create a `.env` file in the root of the project.
2. Add the your Quotex credentials:
   - `QUOTEX_EMAIL=your_email@example.com`
   - `QUOTEX_PASSWORD=your_password`

## 4. Execution
Scripts interacting with QuoteX must be executed using the python executable within the virtual environment (e.g. `venv\Scripts\python.exe execution/test_quotex_connection.py`).
