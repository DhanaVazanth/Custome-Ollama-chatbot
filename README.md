# 🤖 Ollama-Based AI Avatar Customizer

Create, customize, and interact with your own AI avatars using [Ollama](https://ollama.com/) and a Streamlit-powered UI. This project allows you to define personalities, system prompts, and generation parameters, and deploy custom LLM-based avatars with ease.

![Ollama Avatar Creator Demo](https://crosslabcollab.wordpress.com/wp-content/uploads/2014/03/tumblr_n2mbj6nw821qkjjfoo1_400.gif)

---

## 🚀 Features

- 🔧 Create custom avatars by setting a system prompt and temperature.
- 📁 Auto-generate a `modelfile` compatible with Ollama.
- 🧠 Store avatar metadata in a local SQLite database.
- ⚙️ Launch and run models using Ollama CLI.
- 💬 Stream responses in real-time through a sleek Streamlit UI.

---

## 📂 Project Structure

```
├── main.py               # Streamlit app entry point
├── function.py           # Core logic: DB, API, modelfile generation, Ollama integration
├── avatars.db            # Auto-generated SQLite DB (after first run)
├── modelfile2            # Auto-generated model file for Ollama
```

---

## 🧱 How It Works

1. **User Input**: Enter avatar name, prompt, and temperature via Streamlit sidebar.
2. **Database Save**: Avatar configuration is saved to a local SQLite DB.
3. **Model File Creation**: A `modelfile2` is dynamically generated for the avatar.
4. **Model Build & Run**:
   - Uses `ollama create` to build the model.
   - Uses `ollama run` to start the model in the background.
5. **Interaction**: Prompts sent via the chat input box stream the model’s responses in real-time.

---

## 🛠️ Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and available via CLI
- Docker (Ollama requires Docker in the backend)
- Required Python packages:

```bash
pip install streamlit requests
```

---

## ▶️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/DhanaVazanth/Custome-Ollama-chatbot.git
cd ollama-avatar-creator
```

### 2. Launch the Streamlit app
```bash
streamlit run main.py
```

### 3. Use the UI
- Enter a name and prompt for your AI Avatar.
- Set a generation temperature (controls creativity).
- Hit **Create..🧺** to generate and run the model.
- Use the chat box to start a conversation with your avatar.

---

## 📆 Example `modelfile` Output

```Dockerfile
FROM llama3.1:latest

PARAMETER temperature 0.8

SYSTEM """Your name is Luna and you are a futuristic AI assistant that loves science fiction."""
```

---

## 📌 Notes

- The model name must be unique. If you reuse an existing name, the DB will prevent duplication.
- Ensure `ollama` is installed and accessible from your terminal/command prompt.
- This setup assumes Ollama is running locally on `http://localhost:11434`.

---

## 🧠 Tech Stack

| Tool         | Purpose                           |
|--------------|-----------------------------------|
| Streamlit    | Web-based UI                      |
| Ollama       | LLM execution engine              |
| SQLite       | Lightweight avatar storage        |
| Docker       | Backend runtime for Ollama models |
| Python       | Backend logic and orchestration   |

---

## 🧃 Future Enhancements

- [ ] Add delete/update functionality for avatars
- [ ] View past prompts and responses
- [ ] Model selection (beyond `llama3.1`)
- [ ] Deploy to cloud with Ollama remote hosting

---

## 💡 Credits

Built with ❤️ using [Ollama](https://ollama.com), [Streamlit](https://streamlit.io), and Python.

---

## 📬 Contact

Have questions or want to contribute? Open an issue.

