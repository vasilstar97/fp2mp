# FP2MP

This repository contains the experimental evidence and serves as the entry point for our paper:

> **From Prompt 2 Master Plan: Towards Solving Ill-Defined Problems with LLM-MAS**

## About

The main goals of this repository are:

- Provide the implementation of the instruments used in the study.
- Provide the main experimental setup and data.

### Related Repositories

The FP2MP project is organized across several repositories:

- **[fp2mp-core](https://github.com/Eynor-Systems/FP2MP_system)** – The core MAS-LLM approach for solving ill-defined problems.
- **[fp2mp-eval](https://github.com/vasilstar97/fp2mp-eval)** – Evaluation framework for assessing solution quality for ill-defined tasks.
- **[fp2mp-baselines](https://github.com/Mvin8/fp2mp-baselines)** – Implementation of the baselines used in the experiments.

## Quickstart

One can reproduce experimental results using the following setup pipeline:

- `git clone https://github.com/vasilstar97/fp2mp` - cloning the repository
- `python3 -m venv .venv` - create venv
- `source .venv/bin/activate` - activate venv
- `pip install -r requirements.txt` - installing requirements

## Environment Variables

To work with this repository and the related ones, you need to define certain variables in a `.env` file. Use [.env.example](.env.example) as a reference:

- `FP2MP_CHAT_URL` – OpenAI-compatible API URL.
- `FP2MP_API_KEY` – API key for the above endpoint.

## Dataset

The experimental dataset consists of **8 ill-defined questions** combined with **4 distinct locations**, resulting in a total of `8 × 4 = 32` ill-defined problems. Each problem is constructed using the following template:

```python
TEMPLATE = "{location}. {question}"

problems = []

for question in questions:
    for location in locations:
        problem = TEMPLATE.format(location=location, question=question)
        problems.append(input)
```

The following resources are available in the repository:

- [questions.json](./examples/data/questions.json) - list of ill-defined questions.
- [locations.json](./examples/data/locations.json) - list of distinct locations.
- [problems.json](./examples/data/problems.json) - list of resulting ill-defined problems.

## Baselines

...

## Evaluation framework

...

## Experimental results

...
