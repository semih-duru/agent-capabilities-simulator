"""Simple API test script to verify the application works."""
import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_new_game():
    """Test starting a new game."""
    print("Testing: Start new game...")
    response = requests.post(f"{BASE_URL}/api/game/new")
    data = response.json()
    
    if data['success']:
        print("✅ New game started successfully")
        print(f"   Budget: ${data['game_state']['budget']:,}")
        print(f"   Time: {data['game_state']['time_remaining_weeks']} weeks")
        print(f"   Resources: {data['game_state']['resources']}")
        return True
    else:
        print("❌ Failed to start new game")
        return False

def test_get_state():
    """Test getting game state."""
    print("\nTesting: Get game state...")
    response = requests.get(f"{BASE_URL}/api/game/state")
    data = response.json()
    
    if data['success']:
        print("✅ Game state retrieved successfully")
        print(f"   Current week: {data['game_state']['current_week']}")
        return True
    else:
        print("❌ Failed to get game state")
        return False

def test_get_decisions():
    """Test getting available decisions."""
    print("\nTesting: Get available decisions...")
    response = requests.get(f"{BASE_URL}/api/decisions/available")
    data = response.json()
    
    if data['success']:
        print(f"✅ Retrieved {len(data['decisions'])} decisions")
        if data['decisions']:
            print(f"   First decision: {data['decisions'][0]['title']}")
        return True
    else:
        print("❌ Failed to get decisions")
        return False

def test_make_decision():
    """Test making a decision."""
    print("\nTesting: Make a decision...")
    
    # First get available decisions
    response = requests.get(f"{BASE_URL}/api/decisions/available")
    data = response.json()
    
    if not data['success'] or not data['decisions']:
        print("❌ No decisions available")
        return False
    
    # Select first option of first decision
    decision = data['decisions'][0]
    option = decision['options'][0]
    
    print(f"   Choosing: {option['text']}")
    
    response = requests.post(
        f"{BASE_URL}/api/decision/make",
        json={"option": option}
    )
    result = response.json()
    
    if result['success']:
        print("✅ Decision made successfully")
        return True
    else:
        print(f"❌ Failed to make decision: {result.get('message', 'Unknown error')}")
        return False

def test_get_scenarios():
    """Test getting all scenarios."""
    print("\nTesting: Get all scenarios...")
    response = requests.get(f"{BASE_URL}/api/scenarios")
    data = response.json()
    
    if data['success']:
        print(f"✅ Retrieved {len(data['scenarios'])} scenarios")
        return True
    else:
        print("❌ Failed to get scenarios")
        return False

def test_add_scenario():
    """Test adding a custom scenario."""
    print("\nTesting: Add custom scenario...")
    
    scenario = {
        "id": "test_scenario_" + str(int(time.time())),
        "title": "Test Decision",
        "description": "This is a test scenario",
        "category": "development",
        "week_available": 1,
        "options": [
            {
                "id": "test_opt1",
                "text": "Test option 1",
                "cost": 10000,
                "time_weeks": 1,
                "resources_required": 1,
                "maturity_impact": {
                    "agent_development": 5,
                    "agent_operations": 0,
                    "data_platforms": 0,
                    "security": 0,
                    "governance": 0
                },
                "immediate_impact": True,
                "delayed_impact_weeks": 0,
                "consequences": "Test consequence"
            }
        ]
    }
    
    response = requests.post(
        f"{BASE_URL}/api/scenarios/add",
        json=scenario
    )
    data = response.json()
    
    if data['success']:
        print("✅ Scenario added successfully")
        return True
    else:
        print("❌ Failed to add scenario")
        return False

def run_all_tests():
    """Run all API tests."""
    print("=" * 50)
    print("🧪 Agentic Platform Simulation - API Tests")
    print("=" * 50)
    print()
    
    try:
        tests = [
            test_new_game,
            test_get_state,
            test_get_decisions,
            test_make_decision,
            test_get_scenarios,
            test_add_scenario
        ]
        
        passed = 0
        failed = 0
        
        for test in tests:
            try:
                if test():
                    passed += 1
                else:
                    failed += 1
            except Exception as e:
                print(f"❌ Test failed with exception: {e}")
                failed += 1
            
            time.sleep(0.5)  # Small delay between tests
        
        print("\n" + "=" * 50)
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print("=" * 50)
        
        if failed == 0:
            print("\n🎉 All tests passed! Application is working correctly.")
        else:
            print("\n⚠️  Some tests failed. Please check the errors above.")
            
    except requests.exceptions.ConnectionError:
        print("\n❌ Could not connect to the application.")
        print("   Make sure the Flask app is running on http://localhost:5000")
        print("   Run: python app.py")

if __name__ == "__main__":
    run_all_tests()
