# Clean Graph

一个基于 LangGraph 构建的极简对话式AI智能体，用于智能体脚手架和游乐场，为学习，构建和实验高级智能体技术提供了实用的起点。

## 快速开始

### 1. 环境设置

创建 conda 环境：

```bash
conda create -n clean_graph python=3.12
conda activate clean_graph
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 环境配置

编辑 `.env` 文件，填入你的配置：

```env
# 必需: LLM API 配置 (支持任何 OpenAI 兼容的 API)
LLM_API_BASE=http://localhost:1234/v1  # LM Studio、Ollama 或其他 OpenAI 兼容 API 地址
LLM_MODEL=qwen/qwen3-next-80b          # 你的模型名称
LLM_API_KEY=your-api-key-here          # 身份验证的 API 密钥

# 可选: LangSmith 追踪
LANGSMITH_TRACING=false                # 设置为 'true' 启用
LANGSMITH_API_KEY=your-langsmith-key   # 你的 LangSmith API 密钥
```

### 4. 启动 LangGraph Studio

```bash
langgraph dev --no-reload
```

在 `http://localhost:2024` 访问 LangGraph Studio 界面。

## 前置要求

### 必需工具

- **Python**: 编程语言环境
- **pip**: Python 包管理器
- **Miniconda**: 轻量级 conda 环境管理器
- **VSCode**: 推荐的开发环境

### 安装指南

- [Python for MacOS](https://www.python.org/downloads/macos/)
- [Miniconda installation](https://www.anaconda.com/docs/getting-started/miniconda/install#macos-2)
- [pip Installation](https://pip.pypa.io/en/stable/installation/#)
- [Visual Studio Code on macOS](https://code.visualstudio.com/docs/setup/mac)

## 配置

### LLM 设置

本项目支持多种 LLM 提供商，推荐使用 LM Studio 进行本地开发：

#### LM Studio 设置

1. 下载并安装 [LM Studio](https://lmstudio.ai/)
2. 在 LM Studio 中选择并下载合适的模型
3. 启动本地服务器（通常在 `http://localhost:1234`）

#### LangSmith 注册

为了获得最佳的开发体验，建议注册 LangSmith 账户：

1. 访问 [LangSmith](https://smith.langchain.com/) 并注册账户
2. 获取你的 API 密钥
3. 在 `.env` 文件中配置 `LANGSMITH_API_KEY`

注：即使 LangGraph Studio 使用的是本地 graph，依然需要注册 LangSmith Key（免费），并且登录过 LangSmith （截止 2025-11）

### 环境变量

| 变量 | 必需 | 描述 | 默认值 |
|------|------|------|--------|
| `LLM_API_BASE` | 是 | LLM API 端点的基础URL | - |
| `LLM_MODEL` | 是 | 要使用的模型名称 | - |
| `LLM_API_KEY` | 是 | 身份验证的 API 密钥 | - |
| `LANGSMITH_TRACING` | 否 | 启用 LangSmith 追踪 | `false` |
| `LANGSMITH_API_KEY` | 是 | LangSmith API 密钥 | - |

### 支持的 LLM 提供商

此项目兼容任何 OpenAI 兼容的 API：

- **本地LLM**: LM Studio、Ollama、LocalAI
- **云服务提供商**: OpenAI、Together AI、Groq 等

## 项目结构

```
clean_graph/
├── src/
│   ├── __init__.py      # 包初始化
│   ├── graph.py         # 主要的 LangGraph 应用逻辑
│   └── llms.py          # LLM 配置和设置
├── .env                 # 环境配置
├── langgraph.json       # LangGraph 应用定义
├── requirements.txt     # Python 依赖
├── README.md           # 英文版说明文档
└── README_CN.md        # 中文版说明文档
```

### 核心组件

- **`graph.py`**: 定义主要的对话图，包含状态管理
- **`llms.py`**: 配置支持流式传输的 LLM 客户端
- **`langgraph.json`**: LangGraph 应用配置

## 开发

### LangGraph Studio 开发

此项目专门设计为使用 **LangGraph Studio** 进行开发，这是 LangGraph 应用的官方开发工具，提供了强大的可视化和调试功能。

启动开发服务器：

```bash
langgraph dev --no-reload
```

这将启动：
- **LangGraph Studio 界面**: 通常可在 `http://localhost:2024` 访问
- **开发服务器**: 禁用自动重载以确保稳定性
- **实时监控**: 连接到 LangSmith 进行性能追踪

## 依赖项

- `langchain~=1.0` - 核心 LangChain 框架
- `langgraph~=1.0` - 基于图的 AI 应用框架
- `langchain-core~=1.0` - 核心 LangChain 组件
- `langchain_openai` - OpenAI API 客户端
- `python-dotenv~=1.0` - 环境变量管理
- `langgraph-checkpoint>=2.1.0` - 状态检查点
- `langgraph-cli[inmem]` - 开发工具（内存存储）
- `pydantic~=2.0` - 数据验证和设置管理

## 引用

### 相关工具和文档

- **官方文档**
  - [LangGraph Studio Doc](https://docs.langchain.com/oss/python/langgraph/studio)
  - [LangGraph Doc](https://docs.langchain.com/oss/python/langgraph/overview)

- **开发工具**
  - [Python for MacOS](https://www.python.org/downloads/macos/)
  - [Miniconda installation](https://www.anaconda.com/docs/getting-started/miniconda/install#macos-2)
  - [pip Installation](https://pip.pypa.io/en/stable/installation/#)
  - [Visual Studio Code on macOS](https://code.visualstudio.com/docs/setup/mac)
  - [LM Studio - Local AI on your computer](https://lmstudio.ai/)

- **相关项目**
  - [LangGraph](https://github.com/langchain-ai/langgraph) - 底层的图框架
  - [LangChain](https://github.com/langchain-ai/langchain) - LLM 编排框架