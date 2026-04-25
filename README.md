**🌐 Languages:** [Português (BR)](README.pt_BR.md) | [Español](README.es.md)

---

# 🎯 Soc Ops – Social Bingo for Real Connections

> **Break the ice, meet people, and win!** A dynamic bingo game that turns introductions into fun social moments. Perfect for conferences, team events, mixers, and icebreaker sessions.

Soc Ops transforms networking into an engaging game where players move around the room, connect with others, and mark off squares based on shared interests and experiences. It's networking reimagined—playful, inclusive, and genuinely fun.

---

## ✨ Why Soc Ops?

- **🤝 Genuine Connection** – Forces meaningful conversations instead of small talk
- **🎮 Gamified Fun** – Competitive yet collaborative; everyone has a chance to win
- **📱 Instant Setup** – No apps to download; works on any browser
- **🔧 Fully Customizable** – Control questions, themes, and game flow
- **⚡ Real-Time Gameplay** – HTMX-powered dynamic updates without page refreshes
- **📊 Inclusive Design** – Everyone plays at their own pace; no pressure

---

## 🎮 How It Works

1. **Start the Game** – A new 5×5 bingo card loads with randomized questions
2. **Get Around** – Move through the room and find people who match each square
3. **Mark & Match** – When you find someone, mark that square on your card
4. **Win!** – Get 5 in a row (horizontal, vertical, diagonal) and claim victory

**Example squares:**
- *"Has lived in another country"*
- *"Plays an instrument"*
- *"Has run a marathon"*
- *"Knows sign language"*
- *"Collects something unique"*
- ...and 20+ more!

---

## 🚀 Get Started in 60 Seconds

### Prerequisites
- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager

### Quick Start

```bash
# Clone the repository
git clone https://github.com/Nishan-Kumar-H-V/my-soc-ops-python.git
cd my-soc-ops-python

# Install dependencies
uv sync

# Run the dev server
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Open your browser to http://localhost:8000
```

That's it! The game is ready to play.

---

## 🛠️ Tech Stack

- **FastAPI** – Lightweight, high-performance Python web framework
- **Jinja2** – Server-side templating for dynamic HTML
- **HTMX** – Modern interactivity without writing JavaScript
- **Pydantic** – Type-safe data validation
- **Pytest** – Comprehensive test suite

---

## 📚 Learn by Building

This project is an **interactive lab** for AI-powered development. Explore how to build full-stack applications with modern tools and practices:

| Part | Title | Topics |
|------|-------|--------|
| [**00**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview) | Overview & Checklist | Project structure, prerequisites |
| [**01**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=01-setup) | Setup & Context Engineering | Environment, context instructions |
| [**02**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=02-design) | Design-First Frontend | Creative UI/UX with Jinja2 |
| [**03**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=03-quiz-master) | Custom Quiz Master | Custom AI agents |
| [**04**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=04-multi-agent) | Multi-Agent Development | Advanced agent workflows |

> 📝 **Offline access:** Lab guides are also available in the [`workshop/`](workshop/) folder.

---

## 🎨 Customization

Want to personalize your game?

- **Change Questions** – Edit `app/data.py` to add your own prompts
- **Customize Styling** – Modify CSS utilities in `app/static/css/app.css`
- **Adjust Game Logic** – Tweak scoring and win conditions in `app/game_logic.py`
- **Add Features** – Use the modular architecture to extend functionality

---

## 📋 Development

### Run Tests
```bash
uv run pytest
```

### Lint Code
```bash
uv run ruff check .
```

### Project Structure
```
app/
├── main.py          # FastAPI routes & HTMX endpoints
├── game_logic.py    # Bingo detection & board generation
├── game_service.py  # Session management
├── models.py        # Pydantic models
├── data.py          # Question bank
├── templates/       # Jinja2 templates (home, components)
└── static/          # CSS & assets
tests/               # Pytest test suite
```

---

## 🤝 Contribute

Found a bug or have an idea? We'd love your help! Check out [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📖 License & Code of Conduct

- **License:** [MIT](LICENSE)
- **Code of Conduct:** [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- **Security:** [SECURITY.md](SECURITY.md)

---

## 💡 Questions?

- 📚 See [SUPPORT.md](SUPPORT.md) for help
- 🐛 Found an issue? [Open a GitHub Issue](https://github.com/Nishan-Kumar-H-V/my-soc-ops-python/issues)
- 💬 Want to discuss? Start a [Discussion](https://github.com/Nishan-Kumar-H-V/my-soc-ops-python/discussions)

---

**Ready to break the ice? [Get started now!](#quick-start)** 🎉
