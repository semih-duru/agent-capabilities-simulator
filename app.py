"""Flask application for the Agentic Platform Simulation Game."""
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from game_engine import GameEngine
from scenario_manager import ScenarioManager
from pdf_scenario_parser import PDFScenarioParser
import traceback
import os
from datetime import datetime
from werkzeug.utils import secure_filename
import config

app = Flask(__name__)
CORS(app)

# Configure upload folder
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize game engine, scenario manager, and PDF parser
game_engine = GameEngine()
scenario_manager = ScenarioManager()
pdf_parser = PDFScenarioParser()


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


@app.route('/api/scenarios/add-from-pdf', methods=['POST'])
def add_scenarios_from_pdf():
    """
    Add scenarios from a PDF document.
    Upload a PDF file and AI will extract/generate scenarios from it.
    """
    try:
        # Check if file is present
        if 'pdf_file' not in request.files:
            return jsonify({
                'success': False,
                'error': 'No PDF file provided. Please upload a file with key "pdf_file"'
            }), 400
        
        pdf_file = request.files['pdf_file']
        
        # Check if file is actually selected
        if pdf_file.filename == '':
            return jsonify({
                'success': False,
                'error': 'No file selected'
            }), 400
        
        # Check file extension
        if not pdf_file.filename.lower().endswith('.pdf'):
            return jsonify({
                'success': False,
                'error': 'File must be a PDF'
            }), 400
        
        # Generate safe filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        original_filename = secure_filename(pdf_file.filename)
        filename = f"{timestamp}_{original_filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save the PDF file
        pdf_file.save(filepath)
        print(f"PDF saved to: {filepath}")
        
        # Parse PDF and generate scenarios (read from saved file)
        with open(filepath, 'rb') as f:
            scenarios = pdf_parser.parse_pdf_to_scenarios(f)
        
        # Add all scenarios to the scenario manager
        added_count = 0
        for scenario in scenarios:
            if scenario_manager.add_scenario(scenario):
                added_count += 1
        
        return jsonify({
            'success': True,
            'message': f'Successfully added {added_count} scenarios from PDF',
            'scenarios_added': added_count,
            'scenarios': scenarios,
            'pdf_saved_as': filename
        })
        
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': f'PDF parsing error: {str(e)}'
        }), 400
    except Exception as e:
        print(f"Error processing PDF: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': f'Failed to process PDF: {str(e)}'
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
