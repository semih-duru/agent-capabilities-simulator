"""Game engine for the multi-agent platform simulation."""
from typing import Dict, List, Optional
from models import GameState, MaturityMetrics, GameEvent, Decision, DecisionOption, DecisionCategory
from agents import DecisionAgent
import config
import random


class GameEngine:
    """Main game engine that manages game state and logic."""
    
    def __init__(self):
        """Initialize the game engine."""
        self.game_state: Optional[GameState] = None
        self.decision_agent = DecisionAgent()
        self.pending_impacts: List[Dict] = []
    
    def start_new_game(self) -> GameState:
        """Start a new game with initial state."""
        self.game_state = GameState(
            budget=config.INITIAL_BUDGET,
            time_remaining_weeks=config.INITIAL_TIME_WEEKS,
            resources=config.INITIAL_RESOURCES,
            current_week=0,
            maturity=MaturityMetrics()
        )
        self.pending_impacts = []
        
        # Add initial welcome event
        self.game_state.events.append(GameEvent(
            week=0,
            title="Welcome to Agentic Platform Simulation",
            description="You have been appointed to lead the development of a multi-agent platform. "
                       "You must make strategic decisions to build a production-ready platform within the given budget and timeline.",
            impact={}
        ))
        
        return self.game_state
    
    def get_current_state(self) -> Optional[Dict]:
        """Get the current game state as a dictionary."""
        if self.game_state:
            return self.game_state.to_dict()
        return None
    
    def make_decision(self, decision_id: str, option_id: str) -> Dict:
        """Process a decision made by the player."""
        if not self.game_state:
            raise ValueError("No active game")
        
        # Find the decision and option (would come from scenario manager in full implementation)
        # For now, we'll process the impacts directly
        
        result = {
            "success": True,
            "message": "Decision processed",
            "impacts": {}
        }
        
        # This would be populated from the actual decision/option data
        # For demonstration, we'll return the result
        return result
    
    def process_decision_impact(self, option: Dict) -> Dict:
        """Process the impact of a decision option."""
        if not self.game_state:
            raise ValueError("No active game")
        
        # Deduct costs
        self.game_state.budget -= option.get('cost', 0)
        
        # Allocate resources
        resources_required = option.get('resources_required', 0)
        if resources_required > self.game_state.resources:
            return {
                "success": False,
                "message": "Insufficient resources"
            }
        
        # Process maturity impacts
        maturity_impact = option.get('maturity_impact', {})
        
        if option.get('immediate_impact', True):
            # Apply immediate impacts
            self._apply_maturity_changes(maturity_impact)
        else:
            # Schedule delayed impact
            delayed_weeks = option.get('delayed_impact_weeks', 0)
            self.pending_impacts.append({
                'week': self.game_state.current_week + delayed_weeks,
                'impact': maturity_impact,
                'description': option.get('text', '')
            })
        
        # Advance time
        time_weeks = option.get('time_weeks', 1)
        self._advance_time(time_weeks)
        
        # Record decision
        self.game_state.decisions_made.append({
            'week': self.game_state.current_week,
            'option_id': option.get('id'),
            'text': option.get('text', ''),
            'cost': option.get('cost', 0),
            'maturity_impact': maturity_impact
        })
        
        return {
            "success": True,
            "message": "Decision processed successfully",
            "new_state": self.game_state.to_dict()
        }
    
    def _apply_maturity_changes(self, changes: Dict[str, int]):
        """Apply maturity changes to the game state."""
        for key, value in changes.items():
            current = getattr(self.game_state.maturity, key, 0)
            new_value = max(0, min(100, current + value))
            setattr(self.game_state.maturity, key, new_value)
    
    def _advance_time(self, weeks: int):
        """Advance game time and process pending impacts."""
        for _ in range(weeks):
            self.game_state.current_week += 1
            self.game_state.time_remaining_weeks -= 1
            
            # Process pending impacts
            impacts_to_remove = []
            for pending in self.pending_impacts:
                if pending['week'] == self.game_state.current_week:
                    self._apply_maturity_changes(pending['impact'])
                    self.game_state.events.append(GameEvent(
                        week=self.game_state.current_week,
                        title="Delayed Impact Realized",
                        description=f"Previous investment in '{pending['description']}' is now showing results",
                        impact=pending['impact']
                    ))
                    impacts_to_remove.append(pending)
            
            for impact in impacts_to_remove:
                self.pending_impacts.remove(impact)
            
            # Generate random events based on maturity levels
            if random.random() < 0.1:  # 10% chance per week
                self._generate_random_event()
    
    def _generate_random_event(self):
        """Generate a random event based on current maturity levels."""
        events = [
            {
                "title": "Security Audit Required",
                "description": "A security audit has revealed potential vulnerabilities. Additional security measures needed.",
                "condition": lambda m: m.security < 40,
                "impact": {"budget": -20000}
            },
            {
                "title": "Data Quality Issues",
                "description": "Poor data quality is affecting agent performance.",
                "condition": lambda m: m.data_platforms < 40,
                "impact": {"maturity": {"agent_operations": -5}}
            },
            {
                "title": "Compliance Review",
                "description": "Regulatory compliance review identified gaps in governance.",
                "condition": lambda m: m.governance < 50,
                "impact": {"budget": -30000, "time": 2}
            },
        ]
        
        for event_template in events:
            if event_template["condition"](self.game_state.maturity):
                impact = event_template["impact"]
                
                if "budget" in impact:
                    self.game_state.budget += impact["budget"]
                if "maturity" in impact:
                    self._apply_maturity_changes(impact["maturity"])
                if "time" in impact:
                    self.game_state.time_remaining_weeks -= impact["time"]
                
                self.game_state.events.append(GameEvent(
                    week=self.game_state.current_week,
                    title=event_template["title"],
                    description=event_template["description"],
                    impact=impact
                ))
                break
    
    def launch_to_production(self) -> Dict:
        """Launch the platform to production and analyze results."""
        if not self.game_state:
            raise ValueError("No active game")
        
        if self.game_state.is_production:
            return {
                "success": False,
                "message": "Already in production"
            }
        
        # Analyze production readiness
        analysis = self.decision_agent.analyze_production_readiness(
            self.game_state.maturity.to_dict()
        )
        
        self.game_state.is_production = True
        self.game_state.production_week = self.game_state.current_week
        
        # Generate production issues based on maturity gaps
        self.game_state.production_issues = analysis.get('potential_issues', [])
        
        # Add production launch event
        self.game_state.events.append(GameEvent(
            week=self.game_state.current_week,
            title="Production Launch",
            description=f"Platform launched to production. Risk Level: {analysis.get('risk_level', 'unknown').upper()}",
            impact={"production": True}
        ))
        
        # Simulate production impacts over the remaining weeks
        self._simulate_production_period()
        
        return {
            "success": True,
            "analysis": analysis,
            "production_issues": self.game_state.production_issues
        }
    
    def _simulate_production_period(self):
        """Simulate production period and generate issues based on maturity."""
        maturity = self.game_state.maturity
        
        # Generate issues for each low maturity area
        if maturity.agent_development < config.PRODUCTION_READY_THRESHOLD:
            severity = "Critical" if maturity.agent_development < config.MINIMUM_ACCEPTABLE_THRESHOLD else "Major"
            self.game_state.events.append(GameEvent(
                week=self.game_state.current_week + random.randint(1, 4),
                title=f"{severity}: Agent Development Issues",
                description="Agents are experiencing frequent errors due to inadequate development practices.",
                impact={"cost": -50000, "reputation": -10}
            ))
        
        if maturity.agent_operations < config.PRODUCTION_READY_THRESHOLD:
            severity = "Critical" if maturity.agent_operations < config.MINIMUM_ACCEPTABLE_THRESHOLD else "Major"
            self.game_state.events.append(GameEvent(
                week=self.game_state.current_week + random.randint(1, 4),
                title=f"{severity}: Operational Issues",
                description="Poor monitoring and operations leading to downtime and performance problems.",
                impact={"cost": -75000, "reputation": -15}
            ))
        
        if maturity.data_platforms < config.PRODUCTION_READY_THRESHOLD:
            severity = "Critical" if maturity.data_platforms < config.MINIMUM_ACCEPTABLE_THRESHOLD else "Major"
            self.game_state.events.append(GameEvent(
                week=self.game_state.current_week + random.randint(1, 4),
                title=f"{severity}: Data Platform Issues",
                description="Data quality and availability issues causing agent failures.",
                impact={"cost": -60000, "reputation": -12}
            ))
        
        if maturity.security < config.PRODUCTION_READY_THRESHOLD:
            severity = "Critical" if maturity.security < config.MINIMUM_ACCEPTABLE_THRESHOLD else "Major"
            self.game_state.events.append(GameEvent(
                week=self.game_state.current_week + random.randint(1, 4),
                title=f"{severity}: Security Breach",
                description="Security vulnerabilities exploited, requiring immediate response.",
                impact={"cost": -150000, "reputation": -25}
            ))
        
        if maturity.governance < config.PRODUCTION_READY_THRESHOLD:
            severity = "Critical" if maturity.governance < config.MINIMUM_ACCEPTABLE_THRESHOLD else "Major"
            self.game_state.events.append(GameEvent(
                week=self.game_state.current_week + random.randint(1, 4),
                title=f"{severity}: Governance and Compliance Issues",
                description="Lack of governance causing compliance violations and audit failures.",
                impact={"cost": -100000, "reputation": -20}
            ))
    
    def end_game(self) -> Dict:
        """End the game and generate final report."""
        if not self.game_state:
            raise ValueError("No active game")
        
        self.game_state.game_over = True
        
        # Generate final report using AI agent
        report = self.decision_agent.generate_final_report(
            self.game_state.to_dict()
        )
        
        return {
            "game_state": self.game_state.to_dict(),
            "report": report
        }
    
    def get_available_decisions(self) -> List[Dict]:
        """Get available decisions for current week using AI agent."""
        if not self.game_state or self.game_state.game_over:
            return []
        
        decisions = self.decision_agent.generate_decision_scenarios(
            self.game_state.to_dict(),
            self.game_state.current_week
        )
        
        return decisions
