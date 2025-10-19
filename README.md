# Agentic Platform Simulation Game 🤖

An interactive simulation game that helps enterprise leaders understand the complexities and critical decisions involved in building a production-ready multi-agent platform. Built with Google's Agent Development Kit (ADK) principles and powered by Gemini 2.0 Flash via Vertex AI.

## 🎯 Overview

This simulation game puts you in the role of a Chief AI Officer tasked with building an enterprise multi-agent platform. You'll manage a budget, timeline, and resources while making strategic decisions that impact five critical maturity capabilities:

- **Agent Development** - Building and deploying agents
- **Agent Operations** - Monitoring, maintenance, and incident response
- **Data Platforms for Agents** - Data infrastructure and quality
- **Security for Agents** - Authentication, authorization, and threat protection
- **Governance for Agents** - Compliance, policies, and risk management

## 🎮 Game Mechanics

### Starting Resources
- **Budget**: $1,000,000
- **Time**: 52 weeks (1 year)
- **Resources**: 10 team members

### Gameplay
1. **Make Decisions**: Choose from AI-generated and predefined scenarios
2. **Manage Trade-offs**: Balance cost, time, and maturity improvements
3. **Track Progress**: Monitor your maturity levels across all capabilities
4. **Face Events**: Random events based on your maturity levels
5. **Launch to Production**: Deploy when ready (or when time runs out)
6. **Learn from Results**: Receive detailed analysis and prescriptive guidance

### Maturity Thresholds
- **Production Ready**: 60+ in all capabilities
- **Minimum Acceptable**: 40-59
- **Not Ready**: <40 (expect production issues)

## 🏗️ Architecture

This application follows Google's ADK best practices:

```
.
├── agents/                 # AI agents powered by Gemini
│   ├── decision_agent.py  # Generates decisions and analysis
│   └── __init__.py
├── models/                 # Data models
│   ├── game_state.py      # Game state and decision models
│   └── __init__.py
├── templates/             # UI templates
│   └── index.html         # Main game interface
├── app.py                 # Flask application
├── config.py              # Configuration settings
├── game_engine.py         # Core game logic
├── scenario_manager.py    # Scenario management
├── requirements.txt       # Python dependencies
└── .env.example          # Environment variables template

```

## 🚀 Setup and Installation

### Prerequisites
- Python 3.8+
- Google Cloud Project with Vertex AI API enabled
- Service account credentials with Vertex AI permissions

### Installation Steps

1. **Clone the repository**
```bash
cd /workspace
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**
```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_REGION=us-central1
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
```

4. **Run the application**
```bash
python app.py
```

5. **Open in browser**
```
http://localhost:5000
```

## 🎨 Features

### AI-Powered Decision Generation
- Uses Gemini 2.0 Flash to generate contextual decisions based on current game state
- Analyzes production readiness with AI
- Generates comprehensive end-game reports with prescriptive guidance

### Dynamic Game Engine
- Real-time maturity tracking
- Delayed impact system for strategic decisions
- Random events based on maturity gaps
- Production simulation with realistic consequences

### Engaging UI
- Modern, responsive design
- Real-time progress visualization
- Interactive decision-making interface
- Comprehensive final reports

### Scenario Management
- Add custom scenarios via API
- Predefined decision templates
- JSON-based scenario storage
- Week-based scenario availability

## 📊 API Endpoints

### Game Management
- `POST /api/game/new` - Start a new game
- `GET /api/game/state` - Get current game state
- `POST /api/game/end` - End game and get report

### Decision Making
- `GET /api/decisions/available` - Get available decisions (AI + predefined)
- `POST /api/decision/make` - Process a decision

### Production
- `POST /api/production/launch` - Launch to production

### Scenario Management
- `GET /api/scenarios` - Get all scenarios
- `POST /api/scenarios/add` - Add a new scenario

## 🎓 Learning Objectives

This simulation teaches:

1. **Balanced Investment**: All capabilities need attention
2. **Technical Debt**: Quick shortcuts create future problems
3. **Security First**: Security gaps are expensive in production
4. **Operational Maturity**: Monitoring and operations are critical
5. **Governance Importance**: Compliance issues can halt operations
6. **Trade-off Analysis**: Cost vs. time vs. quality decisions
7. **Production Readiness**: What "ready" really means

## 🔧 Customization

### Adding Custom Scenarios

POST to `/api/scenarios/add`:
```json
{
  "id": "custom_scenario",
  "title": "Your Decision Title",
  "description": "Scenario description",
  "category": "development|operations|data|security|governance|strategic",
  "week_available": 10,
  "options": [
    {
      "id": "option1",
      "text": "Option description",
      "cost": 50000,
      "time_weeks": 4,
      "resources_required": 2,
      "maturity_impact": {
        "agent_development": 10,
        "agent_operations": 5,
        "data_platforms": 0,
        "security": 0,
        "governance": 0
      },
      "immediate_impact": true,
      "delayed_impact_weeks": 0,
      "consequences": "What happens if chosen"
    }
  ]
}
```

### Modifying Game Parameters

Edit `config.py`:
```python
INITIAL_BUDGET = 1000000
INITIAL_TIME_WEEKS = 52
INITIAL_RESOURCES = 10
PRODUCTION_READY_THRESHOLD = 60
MINIMUM_ACCEPTABLE_THRESHOLD = 40
```

## 🧪 Testing Without Vertex AI

If you don't have Vertex AI credentials, the application includes fallback mechanisms:
- Predefined decision scenarios
- Basic production readiness analysis
- Template-based final reports

## 📈 Best Practices Demonstrated

This application showcases:
- **Agent-Based Architecture**: Separation of concerns with specialized agents
- **AI Integration**: Gemini for dynamic content generation
- **State Management**: Clean game state handling
- **API Design**: RESTful API with clear endpoints
- **UI/UX**: Engaging, intuitive interface
- **Error Handling**: Graceful fallbacks and error messages

## 🤝 Contributing

To extend the game:
1. Add more scenarios in `scenario_manager.py`
2. Enhance AI prompts in `decision_agent.py`
3. Add new maturity capabilities in `models/game_state.py`
4. Implement additional random events in `game_engine.py`

## 📝 License

This project is built for educational purposes to demonstrate multi-agent platform development challenges.

## 🙏 Acknowledgments

- Built with Google's Agent Development Kit principles
- Powered by Gemini 2.0 Flash via Vertex AI
- Inspired by real enterprise challenges in AI adoption

---

**Ready to test your skills in building enterprise AI platforms? Start the game and see if you can achieve production readiness!** 🚀
