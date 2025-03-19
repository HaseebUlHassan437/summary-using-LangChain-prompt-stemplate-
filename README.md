
# Research Tool (Gemini + LangChain + Streamlit)

A lightweight Streamlit‑powered web app that uses LangChain’s Google Gemini integration to generate custom summaries of research papers. Input a paper title, select explanation style & length, then click **Summarize** to see AI‑powered results in your browser.

---

## 📁 Repository Structure

| File | Description |
|-------|-------------|
| `prompt_ui.py` | Main Streamlit application — handles user inputs and displays Gemini’s output |
| `prompt_template.py` | Duplicate of the Streamlit UI (can be removed) |
| `prompt_generator.py` | Generates and saves the JSON prompt template used by the app |
| `template.json` | Prompt template definition |
| `requirements.txt` | All Python dependencies |

---

## 🚀 Quick Start

### 1️⃣ Clone & Enter Folder
```bash
git clone <your-repo-url>
cd <repository-folder>
```

### 2️⃣ (Recommended) Create & Activate Virtual Environment
- **Windows**
  ```powershell
  python -m venv venv
  venv\Scripts\activate
  ```
- **macOS/Linux**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure `.env`
Create a file named `.env` in the project root containing your Google AI API key:
```env
GOOGLE_API_KEY=your_google_api_key_here
```
> You can generate a free key at https://aistudio.google.com/prompts/new_chat

### 5️⃣ Run the Streamlit App
```bash
streamlit run prompt_ui.py
```
Open http://localhost:8501 in your browser to interact with the tool.

---

## 🔧 Tech Stack

- **LangChain Google Generative AI** (`langchain-google-genai`)  
- **Streamlit** — easy interactive UI  
- **dotenv** — secure environment variable management  

---

## 📄 License

MIT © 2025
## Contact

For questions, feedback, or support, feel free to reach out at **haseebulhassan1172003@gmail.com**.


