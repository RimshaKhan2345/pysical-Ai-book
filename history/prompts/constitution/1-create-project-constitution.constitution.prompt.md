---
id: 1
title: Create Project Constitution
stage: constitution
date: 2025-06-13
surface: agent
model: gpt-4
feature: none
branch: main
user: USER
command: /sp.constitution
labels: [constitution, documentation, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/spec-template.md
  - .specify/templates/tasks-template.md
tests:
  - none
---

## Prompt

```
/sp.constitution

Project: AI/Spec-Driven Book with Embedded RAG Chatbot

Core principles:
- Technical accuracy and best practices
- Clear documentation for developers
- Full reproducibility of code and deployment
- Strict adherence to specified tools and stack

Key standards:
- Use only Spec-Kit Plus, Claude Code, OpenAI Agents/ChatKit, FastAPI, Neon Serverless Postgres, Qdrant Cloud Free Tier
- Markdown-based Docusaurus structure
- Functional RAG chatbot supporting full content and selected-text queries
- Clean, tested, linted code

Constraints:
- Docusaurus site with ≥5 sections/chapters
- Embedded, fully working RAG chatbot
- Deployed to GitHub Pages (public repo)
- Free tiers only for Neon and Qdrant

Success criteria:
- Live GitHub Pages site accessible
- RAG chatbot accurately answers book and selected-text queries
- Zero deployment or runtime errors
- All deliverables functional and verified
```

## Response snapshot

I've successfully created and updated the project constitution for the AI/Spec-Driven Book with Embedded RAG Chatbot project. The constitution now includes specific principles around technical accuracy, clear documentation, reproducibility, strict tool adherence, functional RAG chatbot implementation, and clean, tested code standards. The dependent templates have also been updated to ensure consistency with the new constitution.

## Outcome

- ✅ Impact: Created comprehensive project constitution with 6 core principles and aligned dependent templates
- 🧪 Tests: No tests required for documentation update
- 📁 Files: Updated 4 files including the main constitution and 3 template files
- 🔁 Next prompts: Ready to proceed with feature specifications based on this constitution
- 🧠 Reflection: The constitution effectively captures the project requirements and provides clear governance guidelines

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A for documentation task
- Prompt variant (if applicable): Original prompt
- Next experiment (smallest change to try): Begin feature specification using the new constitution
