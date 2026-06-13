# Large Language Models (LLMs)

## 1. What is an LLM?

**LLM (Large Language Model)** is an AI model trained on massive amounts of text data to understand and generate human language.

### Capabilities

* Answer questions
* Generate text
* Summarize documents
* Translate languages
* Write code
* Explain concepts

### Examples

* GPT
* Gemini
* Claude
* Llama

---

## 2. Why is it Called "Large"?

Because it is trained using:

* Huge datasets
* Billions of parameters
* Massive computational resources

### Example

| Model       | Parameters  |
| ----------- | ----------- |
| GPT-2       | 1.5 Billion |
| Llama 2 70B | 70 Billion  |

---

## 3. Parameters

### Definition

Parameters are the learned weights of a neural network.

### Think of Them As

The model's stored knowledge and learned patterns.

### More Parameters Usually Mean

* Better language understanding
* Better generation quality
* Better reasoning

---

## 4. Transformer Architecture

Most modern LLMs use the Transformer architecture.

### Introduced In

"Attention Is All You Need" (2017)

### Main Idea

Use Attention Mechanisms to determine which words are important.

### Example

Sentence:

The cat sat on the mat because it was tired.

The model learns:

it → cat

---

## 5. Attention Mechanism

### Purpose

Allows the model to focus on relevant words.

### Example

Neha went to college because she had an exam.

The model learns:

she → Neha

### Why Important?

Attention is the foundation of modern LLMs.

---

## 6. Training Process

### Stage 1: Pretraining

The model learns by predicting the next token.

Example:

Input:

I love drinking ___

Prediction:

* Tea
* Coffee
* Water

### Goal

Learn:

* Grammar
* Facts
* Language patterns
* Relationships

---

### Stage 2: Fine-Tuning

The pretrained model is specialized for specific tasks.

Examples:

* Chatbots
* Coding assistants
* Medical assistants
* Customer support systems

---

## 7. Tokens

### Definition

The smallest units processed by an LLM.

### Example

Sentence:

Machine Learning is awesome

Tokens may be:

* Machine
* Learning
* is
* awesome

### Important

LLMs think in tokens, not words.

---

## 8. Context Window

### Definition

The amount of text the model can remember at one time.

### Examples

* 8K tokens
* 32K tokens
* 128K tokens
* 1M+ tokens

### Larger Context Helps With

* Long documents
* Research papers
* Books
* Large codebases

---

## 9. Embeddings

### Definition

Numerical vector representations of text.

### Purpose

Convert text into numbers that machines can understand.

### Used In

* Search
* Recommendations
* Semantic similarity
* RAG systems

---

## 10. Prompt Engineering

### Definition

The process of designing effective prompts.

### Weak Prompt

Explain DBMS.

### Better Prompt

Explain DBMS in 5 exam-friendly points with examples.

### Rule

Better prompts → Better outputs.

---

## 11. Hallucinations

### Definition

When an LLM generates incorrect information confidently.

### Examples

* Fake facts
* Fake citations
* Incorrect references

### Solution

Always verify important information.

---

## 12. RAG (Retrieval-Augmented Generation)

### Definition

A technique where the model retrieves information before generating an answer.

### Workflow

User Query
↓
Retriever
↓
Relevant Documents
↓
LLM
↓
Final Answer

### Benefits

* More accurate
* More up-to-date
* Fewer hallucinations

---

## 13. Fine-Tuning

### Definition

Training an existing LLM on specialized data.

### Example

Hospital Dataset
↓
Fine-Tuning
↓
Medical Assistant

### Benefits

* Domain expertise
* Better task performance

---

## 14. AI Agents

### Definition

An LLM capable of taking actions using tools.

### Capabilities

* Search the web
* Use APIs
* Read files
* Execute tasks

### Example

User:
Book a flight.

Agent:

1. Searches flights
2. Compares prices
3. Selects best option
4. Completes booking process

---

## 15. Limitations of LLMs

### Problems

* Hallucinations
* Bias
* High computational cost
* Limited reasoning
* Limited real-time knowledge

---

## 16. Important Terms

| Term           | Meaning                         |
| -------------- | ------------------------------- |
| LLM            | Large Language Model            |
| Token          | Basic unit of text              |
| Parameter      | Learned weight                  |
| Transformer    | Core architecture               |
| Attention      | Focus mechanism                 |
| Prompt         | User instruction                |
| Context Window | Memory size                     |
| Embedding      | Numerical text representation   |
| Fine-Tuning    | Specialized training            |
| RAG            | Retrieval + Generation          |
| Hallucination  | Incorrect generated information |
| Agent          | LLM capable of taking actions   |

---

# key points

1. Transformer Architecture
2. Attention Mechanism
3. Tokens
4. Parameters
5. Context Window
6. Embeddings
7. Prompt Engineering
8. Fine-Tuning
9. RAG
10. Hallucinations
11. AI Agents



