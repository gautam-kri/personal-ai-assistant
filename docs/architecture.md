# System Architecture

## Overview
This project is a personal AI assistant designed to act as a privacy-first, local system for conversation, planning, and task execution. The assistant translates natural language into structured intent, executes actions through dedicated tools, and maintains long-term context through memory.

The system is designed to be modular, extensible, and safe, with clear separation between reasoning, execution, and data storage.

---

## Core Design Principles
- Local-first processing for privacy and data protection
- Clear separation between AI reasoning and system execution
- Deterministic tool execution with validation
- Extensible architecture for future capabilities

---

## High-Level Architecture

User input flows through the following stages:

1. Input Layer  
   Accepts user interaction through a text-based interface (CLI in V1).

2. Local LLM Layer  
   A locally hosted language model handles:
   - Conversational responses
   - Intent extraction
   - Planning and summarization

   The LLM does not execute actions directly.

3. Intent Router  
   Interprets structured output from the LLM and determines which tool or system component should handle the request.

4. Tool Layer  
   Responsible for executing concrete actions such as:
   - Google Calendar scheduling
   - Email handling
   - System-level actions

   Each tool is isolated and independently testable.

5. Memory Layer  
   Stores:
   - User preferences
   - Long-term goals
   - Past interactions and context

6. Response Layer  
   Converts system results into clear, human-readable responses.

---

## V1 Scope

### Included
- Text-based conversational interface
- Local LLM for intent parsing and dialogue
- Google Calendar event creation and conflict detection
- Goal tracking via a local file
- Guardrails to warn about scheduling conflicts
- Modular, documented architecture

### Excluded
- Voice input/output
- Visual UI
- Phone calling
- App search and control
- Autonomous decision-making without user confirmation

---

## Local LLM Constraint

All language processing is performed using a locally hosted LLM. This design choice ensures that sensitive personal data such as conversations, schedules, and goals do not leave the user’s machine.

Tradeoffs include reduced model size and performance compared to cloud-based models, which are accepted in exchange for privacy, control, and offline capability.

The architecture allows the LLM to be swapped or upgraded without affecting other system components.

---

## Current Status
- Repository initialized
- Architecture defined
- V1 scope finalized
