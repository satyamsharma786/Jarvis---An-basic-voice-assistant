# 🤖 Jarvis — Voice Controlled Python Assistant

A beginner-friendly voice-controlled desktop assistant built with Python.

This project was created while learning Python and exploring how voice recognition, text-to-speech, APIs, browser automation, and external Python libraries can be combined to build a practical application.

> **Note:** This is a learning project inspired by the Jarvis project demonstrated in CodeWithHarry's Python course. The project was built using freely available tools and resources, with the goal of understanding how different components work together.

---

## ✨ Features

* 🎙️ Voice-based command recognition
* 🗣️ Text-to-speech responses
* 🌐 Open websites using voice commands
* 🎵 Play songs using a custom music library
* 📰 Fetch news using an API
* 🤖 AI integration structure
* 🔐 Environment-variable based API configuration
* ⚡ Simple voice-command processing system

---

## 🛠️ Technologies Used

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* Requests
* python-dotenv
* OpenAI API
* Python Web Browser module

---

## 📂 Project Structure

```text
Jarvis/
│
├── main.py
├── musicLibrary.py
├── client.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

The basic workflow of Jarvis is:

```text
User speaks
     ↓
Speech Recognition
     ↓
Command Processing
     ↓
Identify the requested action
     ↓
Execute the command
     ↓
Text-to-Speech Response
```

For example:

```text
User → "Jarvis, open Google"
             ↓
       Voice Recognition
             ↓
       Command Processing
             ↓
         Web Browser
             ↓
          Google
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Jarvis
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project directory and add the required API credentials.

Example:

```env
NEWS_API_KEY=your_api_key_here
```

> Never upload your `.env` file or expose API keys publicly.

### 5. Run Jarvis

```bash
python main.py
```

---

## 🎵 Music Library

Songs can be configured through `musicLibrary.py`.

The project uses a dictionary-based structure to associate commands with URLs.

Example:

```python
music = {
    "song_name": "song_url"
}
```

You can add your own songs and links to the library.

---

## 🧠 What I Learned From This Project

This project helped me understand how different Python concepts can work together in a real application.

### Python Concepts

* Functions
* Conditional statements
* Loops
* Dictionaries
* Modules
* Exception handling
* Environment variables
* Working with external libraries

### Practical Concepts

* Voice recognition
* Text-to-speech
* API requests
* API authentication
* Browser automation
* Project structure
* Dependency management
* Git & GitHub workflow

---

## 🔮 Future Improvements

* [ ] Better natural-language command processing
* [ ] More reliable voice recognition
* [ ] Modular command architecture
* [ ] Better error handling
* [ ] Weather integration
* [ ] System controls
* [ ] Reminder and task management
* [ ] Improved AI integration
* [ ] Conversation memory
* [ ] GUI interface
* [ ] Completely redesigned version built from scratch

---

## 📚 Learning Resources

The initial project structure and concept were inspired by the CodeWithHarry Python course.

Additional documentation and freely available resources were used while working with Python libraries and APIs.

---

## ⚠️ Project Status

**Learning / Experimental Project**

This project was created primarily for learning and experimentation rather than production use.

The current version represents an early exploration of Python application development. Future versions will focus on independently designing the architecture and implementing features from scratch.

---

## 👨‍💻 Author

**Satyam Sharma**

Learning Python • Building Projects • Exploring AI/ML

---

## ⭐ Learning Philosophy

This project is a stepping stone toward building larger projects independently.

**Learn → Build → Break → Debug → Rebuild → Improve**
