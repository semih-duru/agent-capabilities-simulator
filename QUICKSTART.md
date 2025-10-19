# Quick Start Guide 🚀

Get started with the Agentic Platform Simulation Game in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- (Optional) Google Cloud Project with Vertex AI enabled for AI-powered decisions

## Installation

### Option 1: Quick Start (Recommended)

**Linux/Mac:**
```bash
chmod +x run.sh
./run.sh
```

**Windows:**
```bash
run.bat
```

The script will:
1. Create a virtual environment
2. Install all dependencies
3. Create .env file from template
4. Start the application

### Option 2: Manual Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Run the application
python app.py
```

## Configuration (Optional)

If you have Google Cloud credentials:

1. Edit `.env` file:
```env
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_REGION=us-central1
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
```

2. Place your service account key file in the project directory

**Note**: The game works without Google Cloud credentials using fallback scenarios!

## Access the Game

Open your browser and navigate to:
```
http://localhost:5000
```

## How to Play

### 1. Start New Game
- Click "Start New Game" on the welcome screen
- You'll receive initial resources:
  - Budget: $1,000,000
  - Time: 52 weeks
  - Resources: 10 team members

### 2. Make Decisions
- Review available decision scenarios
- Each decision has multiple options with different trade-offs
- Consider:
  - 💰 Cost impact
  - ⏱️ Time required
  - 👥 Resources needed
  - 📊 Maturity impacts

### 3. Track Progress
Monitor your maturity levels in 5 capabilities:
- **Agent Development** (building agents)
- **Agent Operations** (monitoring, maintenance)
- **Data Platforms** (data infrastructure)
- **Security** (protection, compliance)
- **Governance** (policies, risk management)

### 4. Launch to Production
When ready (or when time runs out):
- Click "Launch to Production"
- See how your decisions impact production stability
- Low maturity areas will cause issues!

### 5. Review Final Report
- Comprehensive analysis of your performance
- Grade and score
- Strengths and weaknesses
- Key learnings
- Prescriptive guidance for improvement

## Tips for Success

1. **Balance Your Investments**: Don't neglect any capability
2. **Think Long-term**: Cheap shortcuts cause expensive problems later
3. **Security First**: Security breaches are costly
4. **Monitor Early**: Operations maturity prevents production chaos
5. **Governance Matters**: Compliance issues can halt everything

## Maturity Targets

- **Production Ready**: 60+ in all capabilities
- **Minimum Acceptable**: 40-59
- **Not Ready**: <40 (expect serious production issues)

## Common Scenarios

### Scenario 1: Fast Launch
- Focus on quick wins
- Minimal investment in operations/security
- **Result**: Fast to production but major incidents

### Scenario 2: Comprehensive Build
- Invest heavily in all capabilities
- Takes longer but more stable
- **Result**: Smooth production launch

### Scenario 3: Balanced Approach
- Strategic investments
- Address critical gaps early
- **Result**: Good balance of speed and stability

## Troubleshooting

### Port Already in Use
```bash
# Change port in app.py:
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Dependencies Won't Install
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

### AI Decisions Not Working
- Check .env file configuration
- Verify Google Cloud credentials
- The game will use fallback scenarios if AI is unavailable

### Browser Issues
- Clear cache and refresh
- Try a different browser
- Check browser console for errors

## Adding Custom Scenarios

Use the API to add your own scenarios:

```bash
curl -X POST http://localhost:5000/api/scenarios/add \
  -H "Content-Type: application/json" \
  -d '{
    "id": "my_scenario",
    "title": "My Custom Decision",
    "description": "Description here",
    "category": "development",
    "week_available": 5,
    "options": [
      {
        "id": "opt1",
        "text": "Option 1",
        "cost": 50000,
        "time_weeks": 3,
        "resources_required": 2,
        "maturity_impact": {
          "agent_development": 15,
          "agent_operations": 0,
          "data_platforms": 0,
          "security": 0,
          "governance": 0
        },
        "immediate_impact": true,
        "delayed_impact_weeks": 0,
        "consequences": "What happens"
      }
    ]
  }'
```

## Learning Objectives

After playing, you'll understand:
- ✅ Why balanced maturity matters
- ✅ Impact of technical debt
- ✅ Importance of security and governance
- ✅ Trade-offs in enterprise AI projects
- ✅ Production readiness requirements

## Next Steps

1. **Play Multiple Times**: Try different strategies
2. **Read ARCHITECTURE.md**: Understand the technical design
3. **Customize**: Add your own scenarios
4. **Share**: Use for training and education

## Support

For issues or questions:
1. Check the README.md
2. Review ARCHITECTURE.md
3. Check browser console for errors
4. Verify Python and dependency versions

## Have Fun! 🎮

Remember: This is a simulation to learn about multi-agent platform challenges. 
Real enterprise projects have even more complexity!

---

**Ready to become an AI platform expert? Start playing now!** 🚀
