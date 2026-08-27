# Claude API Tutorial

Using the Anthropic Claude API.

## Setting up local environment

We'll use `uv` to manage local Python environment. 

### Step 1: Install uv

If you don't have `uv` yet, install it.

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify it landed correctly:

```bash
uv --version
```

You want `0.5.0` or newer. `uv` handles both your Python version and your dependencies, so you don't need a separate pyenv or conda setup.

### Step 2: Create the project

We'll create all the code under a parent `claude_api_tutorial` folder. Let's call this the `root foder` of the project

Start a new terminal and create the `claude_api_tutorial` folder anywhere in your folder hierarchy. Run the following commands from _inside_ the `claude_api_tutorial` folder.

```bash
uv init . --python 3.12
uv venv
```

The first command gives you a `pyproject.toml` file, a `.python-version` file pinned to 3.12, and a placeholder `main.py` in the `claude_api_tutorial` folder - you can delete the `main.py` file, we don't need it. 

The `uv venv` command creates an empty virtual environment explicitly inside a `.venv` sub-directory (i.e. `claude_api_tutorial/.venv`) without installing dependencies.

Activate the local environment you just created. From inside the same `claude_api_tutorial` folder run one of the following commands depending on your OS.

```bash
# on a Mac/Linux 
source .venv/bin/activate
# on Windows git-bash shell (it's Scripts not bin!)
source .venv/Scripts/activate
# on a Windows CMD shell run
.venv\Scripts\activate.bat
# on a Windows Powershell run
.venv\Scripts\Activate.ps1
```

> 📌**NOTE:** you should always activate the local environment before installing any new modules or running any code we create.

I switch between a Manjaro Linux and Windows 11 machine. I have setup my Windows 11 machine with the `git-bash` shell, that helps me run the same Linux commands on Windows. I use VS Code as my IDE and my default terminal is also the `git-bash` shell. You'll get the `git bash` shell _for free_ on Windows 11 once you install Git for Windows. I highly recommend you get `git bash` on Windows too.

Throughout this series you'll notice that I use the Linux/Mac version of the commands (such as `source .venv/bin/activate`. Replace it with the appropriate command for your shell.)

Confirm the interpreter version:

```bash
uv run python --version
```

You should see `Python 3.12.x`. ADK 2.x requires Python 3.10 or newer.

### Step 3: Add the dependencies

**Once your local environment is activated** (this is important!!), run the following commands to add the required modules.

```bash
uv add anthropic python-dotenv ipykernel
```

For using the Claude API, we actually need just the first 2 modules. `ipykernel` is needed to run Python Notebooks.


### Step 4: Get the Anthropic API Key

To access the Claude API, you'll need an Anthropic API key. Navigate to [Claude Console](https://platform.claude.com/dashboard) to generate a new API Key.

Save the API Key to a local `.env` file as:

`ANTHROPIC_API_KEY=your_api_key`

### Step 5: Test the Claude API

In the `claude_api_tutorial` folder, create a new Notebook file.