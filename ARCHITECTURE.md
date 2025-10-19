# Architecture Documentation

## Google ADK Alignment

This application follows Google's Agent Development Kit (ADK) best practices:

### 1. Agent-Based Architecture

The application uses specialized agents for different tasks:

#### DecisionAgent (`agents/decision_agent.py`)
- **Purpose**: Generate contextual decisions using Gemini AI
- **Capabilities**:
  - Generate decision scenarios based on game state
  - Analyze production readiness
  - Generate comprehensive final reports with prescriptive guidance
- **AI Model**: Gemini 2.0 Flash via Vertex AI
- **Design Pattern**: Single Responsibility - handles all AI-related tasks

### 2. State Management

Clean separation between game state and business logic:

#### Models (`models/game_state.py`)
- `GameState`: Main game state container
- `MaturityMetrics`: Tracks maturity across 5 capabilities
- `Decision` & `DecisionOption`: Decision modeling
- `GameEvent`: Event tracking system

### 3. Game Engine (`game_engine.py`)

Core business logic separate from presentation:
- State transitions
- Decision processing
- Time advancement
- Event generation
- Production simulation

### 4. Scenario Management (`scenario_manager.py`)

Extensible scenario system:
- JSON-based storage
- Dynamic scenario addition
- Week-based availability
- Default scenarios included

### 5. API Layer (`app.py`)

RESTful API design:
- Clean endpoint structure
- Proper error handling
- CORS enabled for flexibility
- JSON request/response

### 6. Presentation Layer (`templates/index.html`)

Modern, responsive UI:
- Single-page application
- Real-time updates
- Interactive visualizations
- Engaging user experience

## Data Flow

```
User Action → API Endpoint → Game Engine → Decision Agent (AI)
                                    ↓
                              Update State
                                    ↓
                              Return to UI
```

## AI Integration Points

### 1. Decision Generation
```python
DecisionAgent.generate_decision_scenarios(game_state, week)
```
- Analyzes current maturity levels
- Focuses on weak areas
- Generates realistic enterprise scenarios
- Returns structured JSON decisions

### 2. Production Readiness Analysis
```python
DecisionAgent.analyze_production_readiness(maturity)
```
- Evaluates all capability maturity levels
- Identifies weak areas and critical gaps
- Predicts potential production issues
- Provides risk assessment

### 3. Final Report Generation
```python
DecisionAgent.generate_final_report(game_state)
```
- Comprehensive performance analysis
- Strengths and weaknesses identification
- Key learnings extraction
- Prescriptive guidance (short/medium/long-term)
- Best practices recommendations

## Maturity Capabilities

### 1. Agent Development (0-100)
- Development frameworks and tools
- Agent design patterns
- Testing and quality assurance
- Development velocity

**Impact if Low**:
- Frequent agent errors
- Poor reliability
- Difficult maintenance
- Slow feature delivery

### 2. Agent Operations (0-100)
- Monitoring and observability
- Incident response
- Performance optimization
- Capacity planning

**Impact if Low**:
- Downtime and outages
- Slow incident resolution
- Performance problems
- Poor visibility

### 3. Data Platforms (0-100)
- Data infrastructure
- Data quality and governance
- API design
- Data access patterns

**Impact if Low**:
- Data quality issues
- Agent failures
- Inconsistent behavior
- Security vulnerabilities

### 4. Security (0-100)
- Authentication and authorization
- Encryption
- Threat protection
- Security monitoring

**Impact if Low**:
- Security breaches
- Data exposure
- Compliance violations
- Reputation damage

### 5. Governance (0-100)
- Policies and procedures
- Compliance frameworks
- Audit capabilities
- Risk management

**Impact if Low**:
- Compliance failures
- Audit issues
- Regulatory problems
- Operational chaos

## Decision Impact System

### Immediate Impact
```python
immediate_impact: true
```
Effects applied immediately when decision is made.

### Delayed Impact
```python
immediate_impact: false
delayed_impact_weeks: 4
```
Effects applied after specified weeks - simulates real project timelines.

### Combined Impact
Decisions can affect multiple capabilities simultaneously, reflecting real-world interconnections.

## Event System

### Random Events
- Triggered based on low maturity levels
- 10% chance per week
- Realistic enterprise scenarios
- Negative impacts to emphasize importance of maturity

### Production Events
- Generated when launching to production
- Based on maturity gaps
- Severity levels: Critical, Major
- Financial and reputational impacts

## Extensibility

### Adding New Capabilities
1. Update `MaturityMetrics` in `models/game_state.py`
2. Add UI elements in `templates/index.html`
3. Update AI prompts in `agents/decision_agent.py`
4. Add decision scenarios affecting new capability

### Adding New Scenarios
1. Use API: `POST /api/scenarios/add`
2. Or add to `scenario_manager.py` defaults
3. Follow JSON schema for decisions

### Customizing AI Behavior
1. Modify prompts in `DecisionAgent`
2. Adjust generation config parameters
3. Add new analysis methods

## Performance Considerations

### AI Response Times
- Decisions: 2-5 seconds (Gemini generation)
- Production analysis: 1-3 seconds
- Final report: 3-7 seconds

### Fallback Mechanisms
- Predefined scenarios if AI fails
- Template-based reports
- Basic analysis algorithms

### Scalability
- Stateless API design
- Could add database for persistence
- Could support multiple concurrent games
- Redis for session management (future)

## Security Considerations

### API Security
- CORS configured
- Input validation needed
- Rate limiting recommended (future)

### Credential Management
- Environment variables for secrets
- .env file excluded from git
- Service account best practices

### Data Privacy
- No personal data collected
- Game state ephemeral
- No data persistence currently

## Testing Strategy

### Unit Tests (Future)
- Game engine logic
- Decision processing
- Maturity calculations
- Event generation

### Integration Tests (Future)
- API endpoints
- AI agent integration
- State management

### UI Tests (Future)
- User interactions
- State updates
- Error handling

## Deployment

### Local Development
```bash
./run.sh  # or run.bat on Windows
```

### Production Deployment
Recommendations:
1. Use gunicorn for WSGI server
2. Add nginx reverse proxy
3. Enable HTTPS
4. Set up monitoring
5. Configure Cloud Run or App Engine

### Environment Variables
Required:
- `GOOGLE_CLOUD_PROJECT`
- `GOOGLE_CLOUD_REGION`
- `GOOGLE_APPLICATION_CREDENTIALS`

Optional:
- `FLASK_ENV`
- `FLASK_DEBUG`
- `PORT`

## Future Enhancements

### Multiplayer
- Compare decisions with others
- Leaderboards
- Collaborative mode

### Persistence
- Save/load games
- Historical analytics
- Progress tracking

### Advanced AI
- Multi-turn conversations
- Personalized recommendations
- Adaptive difficulty

### Additional Features
- More scenario categories
- Industry-specific scenarios
- Custom maturity models
- Export reports as PDF

## Conclusion

This architecture provides:
- ✅ Clean separation of concerns
- ✅ Extensible design
- ✅ AI-powered intelligence
- ✅ Engaging user experience
- ✅ Educational value
- ✅ Production-ready patterns

The simulation effectively demonstrates the complexity and importance of balanced maturity in enterprise AI platforms.
