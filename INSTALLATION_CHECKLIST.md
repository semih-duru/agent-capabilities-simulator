# Installation & Verification Checklist ✅

Use this checklist to verify your installation and setup.

## Pre-Installation

- [ ] Python 3.8+ installed
  ```bash
  python3 --version
  ```

- [ ] pip installed
  ```bash
  pip --version
  ```

- [ ] (Optional) Google Cloud credentials ready
  - Project ID
  - Service account key file
  - Vertex AI API enabled

## Installation Steps

- [ ] Navigate to project directory
  ```bash
  cd /workspace
  ```

- [ ] Create virtual environment
  ```bash
  python3 -m venv venv
  ```

- [ ] Activate virtual environment
  ```bash
  # Linux/Mac:
  source venv/bin/activate
  
  # Windows:
  venv\Scripts\activate
  ```

- [ ] Install dependencies
  ```bash
  pip install -r requirements.txt
  ```

- [ ] Verify installation
  ```bash
  pip list | grep -E "flask|vertexai|google-cloud-aiplatform"
  ```

## Configuration

- [ ] Copy environment template
  ```bash
  cp .env.example .env
  ```

- [ ] Edit .env file (if using Vertex AI)
  ```bash
  # Add your values:
  GOOGLE_GENAI_USE_VERTEXAI=1
  GOOGLE_CLOUD_PROJECT=your-project-id
  GOOGLE_CLOUD_LOCATION=us-central1
  ```

## File Structure Verification

- [ ] Core Python files exist
  ```bash
  ls -1 *.py
  # Should show: app.py, config.py, game_engine.py, scenario_manager.py, test_api.py
  ```

- [ ] Agents module exists
  ```bash
  ls -1 agents/
  # Should show: __init__.py, decision_agent.py
  ```

- [ ] Models module exists
  ```bash
  ls -1 models/
  # Should show: __init__.py, game_state.py
  ```

- [ ] Templates exist
  ```bash
  ls -1 templates/
  # Should show: index.html
  ```

- [ ] Documentation exists
  ```bash
  ls -1 *.md
  # Should show: README.md, QUICKSTART.md, ARCHITECTURE.md, DEMO.md, etc.
  ```

## Python Syntax Validation

- [ ] Validate main files
  ```bash
  python3 -m py_compile app.py game_engine.py scenario_manager.py config.py
  echo $?  # Should output: 0
  ```

- [ ] Validate agent files
  ```bash
  python3 -m py_compile agents/*.py
  echo $?  # Should output: 0
  ```

- [ ] Validate model files
  ```bash
  python3 -m py_compile models/*.py
  echo $?  # Should output: 0
  ```

## Application Startup

- [ ] Start the application
  ```bash
  python3 app.py
  ```

- [ ] Look for success message
  ```
  * Running on http://0.0.0.0:5000
  ```

- [ ] Check for errors in console
  - No error messages should appear
  - Warnings about debug mode are okay

## Browser Verification

- [ ] Open browser
  ```
  http://localhost:5000
  ```

- [ ] Welcome screen loads
  - Should see purple gradient background
  - "Agentic Platform Simulation" title
  - "Start New Game" button

- [ ] Click "Start New Game"
  - Game screen should appear
  - Dashboard shows initial values:
    - Budget: $1,000,000
    - Time: 52 weeks
    - Resources: 10
    - All maturity bars at 0

## Functionality Tests

- [ ] Decisions load
  - Either AI-generated or fallback scenarios appear
  - Each decision has multiple options

- [ ] Make a decision
  - Select an option
  - Click "Confirm Decision"
  - Dashboard updates
  - Budget decreases
  - Time advances
  - Maturity increases

- [ ] Multiple decisions work
  - Make 2-3 more decisions
  - Values update correctly

- [ ] Launch to production
  - Click "Launch to Production"
  - Confirmation dialog appears
  - Analysis shows risk level
  - Events appear

- [ ] End game
  - Click "End Game"
  - Final report appears
  - Shows grade and score
  - Shows guidance

## API Tests (Optional)

- [ ] Keep app running in one terminal

- [ ] Run API tests in another terminal
  ```bash
  # Activate venv first
  python3 test_api.py
  ```

- [ ] All tests should pass
  ```
  ✅ Passed: 6
  ❌ Failed: 0
  ```

## AI Integration Tests (If Configured)

- [ ] AI generates decisions
  - Decisions should be contextually relevant
  - Different from predefined scenarios

- [ ] Production analysis works
  - Shows detailed risk assessment
  - Identifies specific weak areas

- [ ] Final report is comprehensive
  - Detailed prescriptive guidance
  - Specific recommendations

## Common Issues & Solutions

### Issue: Port 5000 already in use
```bash
# Solution: Use a different port
# Edit app.py, change last line to:
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Issue: ModuleNotFoundError
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Issue: Permission denied on run.sh
```bash
# Solution: Make executable
chmod +x run.sh
```

### Issue: AI not working
```bash
# Check:
- Is .env configured?
- Is Vertex AI API enabled?
- Are you properly authenticated to GCP?
- Is GOOGLE_GENAI_USE_VERTEXAI set to 1?

# Workaround: App works without AI using fallback scenarios
```

### Issue: Blank page in browser
```bash
# Check:
- Is Flask app running?
- Any errors in terminal?
- Try clearing browser cache
- Try different browser
- Check browser console (F12)
```

## Performance Verification

- [ ] Initial load < 2 seconds
- [ ] Decision generation < 10 seconds
- [ ] UI updates instant
- [ ] No visible lag

## Cross-Browser Testing

Test in multiple browsers:
- [ ] Chrome/Chromium
- [ ] Firefox
- [ ] Safari (Mac)
- [ ] Edge (Windows)

## Security Checklist

- [ ] .env file not committed to git
  ```bash
  cat .gitignore | grep .env
  ```

- [ ] Virtual environment not committed
  ```bash
  cat .gitignore | grep venv
  ```

## Documentation Review

- [ ] README.md is clear
- [ ] QUICKSTART.md helps get started
- [ ] ARCHITECTURE.md explains design
- [ ] DEMO.md provides demo script

## Final Checks

- [ ] Application runs without errors
- [ ] All game features work
- [ ] Documentation is complete
- [ ] Code is clean and commented
- [ ] Git repository is clean
  ```bash
  git status
  ```

## Success Criteria

✅ **Installation Successful** if:
1. App starts without errors
2. Browser loads game interface
3. Can start and play a game
4. Can complete a full game cycle
5. Final report generates

## Next Steps After Successful Installation

1. **Play a full game** to understand mechanics
2. **Read DEMO.md** for presentation tips
3. **Review ARCHITECTURE.md** for technical details
4. **Try adding custom scenarios**
5. **Share with your team**

## Getting Help

If you encounter issues:

1. Check error messages in terminal
2. Check browser console (F12)
3. Review documentation
4. Verify all checklist items
5. Check Python and package versions

## Maintenance

Regular checks:
- [ ] Update dependencies periodically
  ```bash
  pip install --upgrade -r requirements.txt
  ```

- [ ] Check for Python updates
- [ ] Review and update scenarios
- [ ] Backup custom scenarios

---

**Once all items are checked, you're ready to use the application!** 🎉

**Happy Simulating!** 🤖
