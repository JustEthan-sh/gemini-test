# PROJECT: ECOCHEF [CLI / WEB EDITION]
# TYPE: Python Web Application (Streamlit)
# ARCHITECTURE: Monolithic Script / Micro-Frontend

[CORE_IDENTITY]
Name: EcoChef Lite
Tagline: The Terminal-Grade Kitchen OS.
Primary_Goal: Text-based & Image-based inventory management + Generative Cooking.

[TECH_STACK]
Language: Python 3.9+
UI_Framework: Streamlit (allows GUI rendering via simple Python scripts)
AI_Integration: `google-generativeai` (Python SDK)
Data_Store: Simple JSON (local) or SQLite (embedded)

[FUNCTIONAL_MODULES]
1. MODULE_INGEST (vision.py)
   - Input: `st.file_uploader` (Upload fridge photo).
   - Logic: Pass image stream to Gemini Pro Vision.
   - Prompt: "Identify ingredients in JSON format. Estimate remaining shelf life."

2. MODULE_PANTRY_DB (db.py)
   - Structure: SQLite DB.
   - Schema: `id | item_name | quantity | days_until_expiry | category`
   - Feature: "Quick Add" command line interface for manual entry.

3. MODULE_CHEF_LOGIC (chef.py)
   - Input: Current JSON inventory state.
   - Logic: Gemini 1.5 Flash.
   - Temperature: 0.7 (Creative but structured).
   - Output: Markdown-formatted recipe card.

[USER_FLOW]
1. User runs `streamlit run app.py`.
2. UI loads in browser (localhost).
3. User uploads image -> AI populates "Virtual Pantry" sidebar.
4. User clicks "Generate Dinner" -> AI reads Pantry -> Output Recipe.

[ADVANTAGE_OVER_MOBILE]
- Zero compilation time.
- Single file deployment (`app.py`).
- Extremely low latency (Direct API calls, no middleware).
- Highly hackable (User can edit the prompt logic directly in the script).

[MONETIZATION_PIVOT]
- Open Source Core (GitHub).
- Enterprise API: Sell the "Food Vision" JSON parser API to grocery chains.