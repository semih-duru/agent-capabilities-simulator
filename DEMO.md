# Demo Script 🎬

A guided walkthrough to demonstrate the Agentic Platform Simulation Game.

## Setup (2 minutes)

1. **Start the application**
```bash
./run.sh
```

2. **Open browser**
Navigate to: http://localhost:5000

## Demo Walkthrough (10-15 minutes)

### Part 1: Introduction (2 minutes)

**Show the welcome screen:**
- "You are building an enterprise multi-agent platform"
- Limited budget ($1M), time (52 weeks), resources (10 people)
- 5 critical capabilities to mature

**Click "Start New Game"**

### Part 2: Game Mechanics (5 minutes)

**Point out the dashboard:**
- Left sidebar shows current resources
- Budget, time, resources counters
- 5 maturity progress bars (all starting at 0)

**Explain the maturity capabilities:**
1. **Agent Development** - Building and coding agents
2. **Agent Operations** - Monitoring, maintenance, incidents
3. **Data Platforms** - Data infrastructure for agents
4. **Security** - Authentication, encryption, threats
5. **Governance** - Compliance, policies, risk management

**Show the decision area:**
- AI generates contextual decisions
- Each decision has multiple options
- Options show costs, time, resources, and impacts

### Part 3: Making Decisions (5 minutes)

**Decision 1: Agent Development Framework**
- Show the three options (basic, enterprise, custom)
- Highlight the trade-offs:
  - Basic: Quick but limited
  - Enterprise: Comprehensive but expensive
  - Custom: Flexible but time-consuming

**Select "Enterprise Framework"**
- Point out: $80K cost, 4 weeks, 3 resources
- Note the maturity impacts across multiple capabilities
- Click option to select it
- Click "Confirm Decision"

**Watch the updates:**
- Budget decreases
- Time advances
- Maturity bars increase
- Events appear

**Decision 2: Choose a contrasting approach**
Select a cheaper, quicker option for the next decision
- Show how this creates different maturity profile
- Explain the concept of "balanced maturity"

### Part 4: Production Launch (3 minutes)

**After a few decisions:**
- Show the maturity distribution
- Point out any weak areas

**Click "Launch to Production"**
- Alert shows risk level
- Explains potential issues based on low maturity areas

**Show the events:**
- Production issues appear based on maturity gaps
- Critical issues from capabilities below 40
- Major issues from capabilities below 60

### Part 5: Final Report (2 minutes)

**Click "End Game"**

**Review the final report:**
- Grade and overall score
- Summary of performance
- Strengths (high maturity areas)
- Weaknesses (low maturity areas)
- Key learnings
- Prescriptive guidance:
  - Short-term actions
  - Medium-term plans
  - Long-term strategy
- Best practices
- Specific recommendations

## Key Messages to Emphasize

### 1. Balance is Critical
"You can't just focus on development and ignore operations, security, or governance."

### 2. Technical Debt is Real
"Choosing quick, cheap options early creates expensive problems in production."

### 3. Security Can't Be an Afterthought
"Security breaches in production are 10x more expensive than building security in from the start."

### 4. Governance Matters
"Without governance, you'll face compliance issues, audit failures, and regulatory problems."

### 5. Operations Enable Success
"Good monitoring and operations capabilities mean faster incident response and less downtime."

## Demo Scenarios

### Scenario A: Speed Run (Shows Problems)
1. Always choose the cheapest, fastest options
2. Focus only on Agent Development
3. Ignore Security and Governance
4. Launch to production early
5. **Result**: Multiple critical production issues

**Teaching Point**: "Speed without stability leads to failure"

### Scenario B: Over-Engineering (Shows Trade-offs)
1. Always choose the most expensive, comprehensive options
2. Invest heavily in everything
3. Run out of time or budget before launch
4. **Result**: Miss deadline or go over budget

**Teaching Point**: "Perfection is the enemy of good; balance is key"

### Scenario C: Balanced Approach (Best Practice)
1. Identify weak areas from the maturity dashboard
2. Invest strategically to raise all capabilities above 60
3. Balance quick wins with long-term investments
4. Launch when all capabilities are mature enough
5. **Result**: Smooth production launch with minimal issues

**Teaching Point**: "Strategic, balanced investment leads to success"

## Live Demo Tips

### Before the Demo
- Have the app running and tested
- Clear browser cache
- Have backup slides in case of technical issues
- Know the fallback scenarios (if AI is unavailable)

### During the Demo
- Talk through your decision-making process
- Explain why you're choosing each option
- Point out the real-world parallels
- Ask audience what they would choose
- Show the cause-and-effect relationships

### Interactive Elements
- Ask audience: "What would you invest in first?"
- Poll: "Which capability is most important?"
- Discuss: "What happens if we ignore security?"

### Troubleshooting
If AI is slow:
- Use the time to explain the architecture
- Talk about Google's ADK and Gemini integration
- Discuss the fallback mechanisms

If something breaks:
- Show the code structure
- Explain the architecture
- Use slides or diagrams as backup

## Discussion Questions

After the demo:

1. **"What surprised you most about the simulation?"**
   - Usually: How interconnected everything is

2. **"Which capability would you prioritize first?"**
   - Discuss different strategies and their trade-offs

3. **"How does this relate to your real projects?"**
   - Connect simulation to actual enterprise challenges

4. **"What would you do differently in your organization?"**
   - Encourage reflection on current practices

## Follow-up Activities

### For Participants
1. Play the game themselves
2. Try different strategies
3. Compare results with colleagues
4. Discuss real-world applications

### For Organizations
1. Use for training new AI platform teams
2. Run workshops on platform maturity
3. Create custom scenarios for specific industry
4. Use reports as discussion starters

## Technical Demo (Optional)

For technical audiences:

### Show the Architecture
```python
# Open and explain:
- agents/decision_agent.py  # AI integration
- game_engine.py            # Game logic
- models/game_state.py      # Data models
- app.py                    # API endpoints
```

### Show AI Integration
```python
# Explain the DecisionAgent
- How it uses Gemini 2.0 Flash
- Prompt engineering for decisions
- Fallback mechanisms
```

### Show Extensibility
```bash
# Live add a custom scenario via API
curl -X POST http://localhost:5000/api/scenarios/add \
  -H "Content-Type: application/json" \
  -d @custom_scenario.json
```

### Show Test Suite
```bash
python test_api.py
```

## Presentation Slides (Suggested)

1. **Title**: Agentic Platform Simulation
2. **Problem**: Building enterprise AI platforms is complex
3. **Solution**: Interactive simulation to learn
4. **Architecture**: Google ADK + Gemini
5. **Demo**: Live walkthrough
6. **Results**: Sample final reports
7. **Learnings**: Key takeaways
8. **Q&A**: Discussion

## Success Metrics

A successful demo should:
- ✅ Show all 5 maturity capabilities
- ✅ Demonstrate 3-4 different decisions
- ✅ Launch to production
- ✅ Show impact of maturity gaps
- ✅ Display final report
- ✅ Generate discussion
- ✅ Inspire participants to try it

## Resources to Prepare

- Copy of this demo script
- Application running and tested
- Test scenarios pre-selected
- Backup slides
- Discussion questions
- Handouts with key learnings

---

**You're now ready to deliver an impactful demo! Good luck! 🎬**
