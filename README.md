# Startup

## Step 1: First, download the requirements using

```bash
    pip install -r requirements.txt
```

## Step 2: Pull llama3 or any other open-source model from Ollama

```bash
    ollama pull llama3
```

It will download around 4-5 GB of the model onto your local system.

## Step 3: Confirm Ollama is Running

```bash
    ollama run llama3
```

It should load the model and give you an interactive prompt. Once confirmed, stop it with Ctrl+d

Then, test the API directly:

```bash
    curl http://localhost:11434
```

If Ollama is running, you will see:
"Ollama is running"

## Step 4: Run the server in a cmd terminal

```bash
    python -m uvicorn main:app --reload
```

## Step 5: In another cmd terminal, send a POST request with your desired prompt

```bash
    curl -X POST http://127.0.0.1:8000/process -H "Content-Type: application/json" -d "{\"prompt\": \"John Doe lives in Dublin, CA.\"}"
```
