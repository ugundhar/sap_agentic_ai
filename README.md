# sap_agentic_ai
example for agentic ai code in google colba
ramana chanla bagundau


generative_ai_project/
│
├── config/
│   ├── __init__.py
│   ├── model_config.yaml
│   ├── prompt_templates.yaml
│   └── logging_config.yaml
│
├── src/
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── claude_client.py
│   │   ├── gpt_client.py
│   │   └── utils.py
│   │
│   ├── prompt_engineering/
│   │   ├── __init__.py
│   │   ├── templates.py
│   │   ├── few_shot.py
│   │   └── chainer.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── rate_limiter.py
│   │   ├── token_counter.py
│   │   ├── cache.py
│   │   └── logger.py
│   │
│   └── handlers/
│       ├── __init__.py
│       └── error_handler.py
│
├── data/
│   ├── cache/
│   ├── prompts/
│   ├── outputs/
│   └── embeddings/
│
├── examples/
│   ├── basic_completion.py
│   ├── chat_session.py
│   └── chain_prompts.py
│
├── notebooks/
│   ├── prompt_testing.ipynb
│   ├── response_analysis.ipynb
│   └── model_experimentation.ipynb
│
├── requirements.txt
├── setup.py
├── README.md
└── Dockerfile
