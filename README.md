# Clean Graph

A minimal conversational AI agent built with LangGraph, designed for agent scaffolding and playground.

[中文版](README_CN.md)

## Project Showcase

This project builds a typical yet fully-featured graph-based agent that demonstrates the core capabilities of LangGraph, including state management, message flow, and extensible architecture design.

## Prerequisites

Before you begin, ensure your development environment has the following tools installed:

- **Python**: Programming language environment
- **pip**: Python package manager
- **Miniconda**: Lightweight conda environment manager
- **VSCode**: Recommended development environment

### Installation Guides

- [Python for MacOS](https://www.python.org/downloads/macos/)
- [Miniconda installation](https://www.anaconda.com/docs/getting-started/miniconda/install#macos-2)
- [pip Installation](https://pip.pypa.io/en/stable/installation/#)
- [Visual Studio Code on macOS](https://code.visualstudio.com/docs/setup/mac)

## Create Virtual Environment

It's recommended to create an isolated development environment using conda:

```bash
conda create -n clean_graph python=3.12
conda activate clean_graph
```

## Minimal Project Structure

This project adopts a minimal but complete engineering structure:

```
clean_graph/
├── langgraph.json    # LangGraph configuration file
├── requirements.txt  # Dependency management
├── .env             # Environment variables
└── src/
    ├── __init__.py
    ├── llms.py      # LLM configuration
    └── graph.py     # Graph definition
```

## Installation

### Install Dependencies

Install project dependencies using pip:

```bash
pip install -r requirements.txt
```

## LLM Configuration

This project supports multiple LLM providers, with LM Studio recommended for local development:

### LM Studio Setup

1. Download and install [LM Studio](https://lmstudio.ai/)
2. Select and download suitable models in LM Studio
3. Start the local server (typically at `http://localhost:1234`)

### Environment Variables Configuration

Edit `.env` file with your configuration:
```env
# Required: LLM API Configuration
LLM_API_BASE=http://localhost:1234/v1  # For LM Studio or your local LLM
LLM_MODEL=qwen/qwen3-next-80b          # Your model name
LLM_API_KEY=your-api-key-here          # API key for authentication

# Optional: LangSmith Tracing
LANGSMITH_TRACING=false                # Set to 'true' to enable
LANGSMITH_API_KEY=your-langsmith-key   # Your LangSmith API key
```

## LangGraph Studio Launch!

### LangGraph Studio Development

This project is specifically designed to be developed using **LangGraph Studio**, the official development tool for LangGraph applications that provides powerful visualization and debugging capabilities.

#### LangSmith Registration

For the best development experience, it's recommended to register for a LangSmith account:

1. Visit [LangSmith](https://smith.langchain.com/) and create an account
2. Get your API key
3. Configure `LANGSMITH_API_KEY` in your `.env` file

Note: Even when using local graphs with LangGraph Studio, you still need to register for a LangSmith Key (free) and have logged into LangSmith (as of November 2025).

#### Start Development Server

Start the development server with LangGraph Studio:

```bash
langgraph dev --no-reload
```

This will launch:
- **LangGraph Studio Interface**: Typically accessible at `http://localhost:2024`
- **Development Server**: Auto-reload disabled for stability
- **Real-time Monitoring**: Connected to LangSmith for performance tracing

## Project Structure

```
clean_graph/
├── src/
│   ├── __init__.py      # Package initialization
│   ├── graph.py         # Main LangGraph application logic
│   └── llms.py          # LLM configuration and setup
├── .env                 # Environment configuration
├── langgraph.json       # LangGraph application definition
├── requirements.txt     # Python dependencies
├── README.md           # English documentation
└── README_CN.md        # Chinese documentation
```

### Core Components

- **`graph.py`**: Defines the main conversation graph with state management
- **`llms.py`**: Configures the LLM client with streaming support
- **`langgraph.json`**: LangGraph application configuration

## Configuration

### Environment Variables

| Variable | Required | Description | Default |
|----------|----------|-------------|---------|
| `LLM_API_BASE` | Yes | Base URL for LLM API endpoint | - |
| `LLM_MODEL` | Yes | Model name to use | - |
| `LLM_API_KEY` | Yes | API key for authentication | - |
| `LANGSMITH_TRACING` | No | Enable LangSmith tracing | `false` |
| `LANGSMITH_API_KEY` | No | LangSmith API key | - |

### Supported LLM Providers

This project is compatible with any OpenAI-compatible API:

- **Local LLMs**: LM Studio, Ollama, LocalAI
- **Cloud Providers**: OpenAI, Together AI, Groq, etc.

## Dependencies

- `langchain~=1.0` - Core LangChain framework
- `langgraph~=1.0` - Graph-based AI application framework
- `langchain-core~=1.0` - Core LangChain components
- `langchain_openai` - OpenAI API client
- `python-dotenv~=1.0` - Environment variable management
- `langgraph-checkpoint>=2.1.0` - State checkpointing
- `langgraph-cli[inmem]` - Development tools (in-memory storage)
- `pydantic~=2.0` - Data validation and settings management

## References

### Related Tools and Documentation

- **Official Documentation**
  - [LangGraph Studio Doc](https://docs.langchain.com/oss/python/langgraph/studio)
  - [LangGraph Doc](https://docs.langchain.com/oss/python/langgraph/overview)

- **Development Tools**
  - [Python for MacOS](https://www.python.org/downloads/macos/)
  - [Miniconda installation](https://www.anaconda.com/docs/getting-started/miniconda/install#macos-2)
  - [pip Installation](https://pip.pypa.io/en/stable/installation/#)
  - [Visual Studio Code on macOS](https://code.visualstudio.com/docs/setup/mac)
  - [LM Studio - Local AI on your computer](https://lmstudio.ai/)

- **Related Projects**
  - [LangGraph](https://github.com/langchain-ai/langgraph) - The underlying graph framework
  - [LangChain](https://github.com/langchain-ai/langchain) - The LLM orchestration framework