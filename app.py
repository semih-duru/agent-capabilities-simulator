"""Flask application for the Agentic Platform Simulation Game."""
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from game_engine import GameEngine
from scenario_manager import ScenarioManager
import traceback

app = Flask(__name__)
CORS(app)

# Initialize game engine and scenario manager
game_engine = GameEngine()
scenario_manager = ScenarioManager()


@app.route('/')
def index():
    """Render the main game interface."""
    return render_template('index.html')


@app.route('/api/game/new', methods=['POST'])
def new_game():
    """Start a new game."""
    try:
        game_state = game_engine.start_new_game()
        return jsonify({
            'success': True,
            'game_state': game_state.to_dict()
        })
    except Exception as e:
        print(f"Error starting new game: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/game/state', methods=['GET'])
def get_game_state():
    """Get the current game state."""
    try:
        state = game_engine.get_current_state()
        if state:
            return jsonify({
                'success': True,
                'game_state': state
            })
        return jsonify({
            'success': False,
            'error': 'No active game'
        }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/decisions/available', methods=['GET'])
def get_available_decisions():
    """Get available decisions using AI."""
    try:
        # Get decisions from both AI and predefined scenarios
        ai_decisions = game_engine.get_available_decisions()
        
        # Also get predefined scenarios
        state = game_engine.get_current_state()
        if state:
            week = state['current_week']
            predefined = scenario_manager.get_scenarios_for_week(week)
            
            # Combine and limit to 3 decisions
            all_decisions = ai_decisions + predefined
            # Remove duplicates and limit
            decisions = all_decisions[:3]
        else:
            decisions = ai_decisions
        
        return jsonify({
            'success': True,
            'decisions': decisions
        })
    except Exception as e:
        print(f"Error getting decisions: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/decision/make', methods=['POST'])
def make_decision():
    """Process a decision."""
    try:
        data = request.json
        option = data.get('option')
        
        if not option:
            return jsonify({
                'success': False,
                'error': 'Option data required'
            }), 400
        
        result = game_engine.process_decision_impact(option)
        return jsonify(result)
    except Exception as e:
        print(f"Error making decision: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/production/launch', methods=['POST'])
def launch_production():
    """Launch to production."""
    try:
        result = game_engine.launch_to_production()
        return jsonify(result)
    except Exception as e:
        print(f"Error launching production: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/game/end', methods=['POST'])
def end_game():
    """End the game and get final report."""
    try:
        result = game_engine.end_game()
        return jsonify({
            'success': True,
            'result': result
        })
    except Exception as e:
        print(f"Error ending game: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/scenarios', methods=['GET'])
def get_scenarios():
    """Get all scenarios."""
    try:
        scenarios = scenario_manager.get_all_scenarios()
        return jsonify({
            'success': True,
            'scenarios': scenarios
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/scenarios/add', methods=['POST'])
def add_scenario():
    """Add a new scenario."""
    try:
        scenario = request.json
        success = scenario_manager.add_scenario(scenario)
        
        if success:
            return jsonify({
                'success': True,
                'message': 'Scenario added successfully'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to add scenario'
            }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
