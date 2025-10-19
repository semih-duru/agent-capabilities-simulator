"""Agent for generating decisions and analyzing impacts using Gemini."""
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig
from typing import Dict, List
import json
import config


class DecisionAgent:
    """Agent that uses Gemini to generate decisions and analyze game scenarios."""
    
    def __init__(self):
        """Initialize the Decision Agent with Vertex AI."""
        if config.PROJECT_ID:
            vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)
        self.model = GenerativeModel(config.MODEL_NAME)
        self.generation_config = GenerationConfig(
            temperature=0.7,
            top_p=0.9,
            max_output_tokens=2048,
        )
    
    def generate_decision_scenarios(self, game_state: Dict, week: int) -> List[Dict]:
        """Generate decision scenarios based on current game state."""
        prompt = f"""You are an AI advisor for an enterprise multi-agent platform development simulation.

Current Game State (Week {week}):
- Budget: ${game_state['budget']:,}
- Time Remaining: {game_state['time_remaining_weeks']} weeks
- Resources: {game_state['resources']} team members
- Maturity Levels:
  * Agent Development: {game_state['maturity']['agent_development']}/100
  * Agent Operations: {game_state['maturity']['agent_operations']}/100
  * Data Platforms: {game_state['maturity']['data_platforms']}/100
  * Security: {game_state['maturity']['security']}/100
  * Governance: {game_state['maturity']['governance']}/100

Generate 2-3 realistic decision scenarios that the player must choose from. Each decision should:
1. Be relevant to the current maturity levels (focus on weaker areas)
2. Have trade-offs between cost, time, and maturity improvements
3. Include both immediate and potential delayed impacts
4. Reflect real enterprise challenges in building agentic platforms

Return your response as a JSON array with this structure:
[
  {{
    "id": "unique_id",
    "title": "Decision Title",
    "description": "Detailed description of the situation",
    "category": "development|operations|data|security|governance|strategic",
    "options": [
      {{
        "id": "option_id",
        "text": "Option description",
        "cost": 50000,
        "time_weeks": 4,
        "resources_required": 2,
        "maturity_impact": {{
          "agent_development": 10,
          "agent_operations": 5,
          "data_platforms": 0,
          "security": 0,
          "governance": 0
        }},
        "immediate_impact": true,
        "delayed_impact_weeks": 0,
        "consequences": "What happens if you choose this"
      }}
    ]
  }}
]

Only return valid JSON, no additional text."""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config
            )
            
            # Parse JSON response
            response_text = response.text.strip()
            # Remove markdown code blocks if present
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.startswith("```"):
                response_text = response_text[3:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            
            decisions = json.loads(response_text.strip())
            return decisions
        except Exception as e:
            print(f"Error generating decisions: {e}")
            return self._get_fallback_decisions(game_state)
    
    def analyze_production_readiness(self, maturity: Dict[str, int]) -> Dict:
        """Analyze if the platform is ready for production."""
        prompt = f"""Analyze the production readiness of a multi-agent platform with these maturity levels:

- Agent Development: {maturity['agent_development']}/100
- Agent Operations: {maturity['agent_operations']}/100
- Data Platforms: {maturity['data_platforms']}/100
- Security: {maturity['security']}/100
- Governance: {maturity['governance']}/100

Thresholds:
- Production Ready: 60+
- Minimum Acceptable: 40-59
- Not Ready: <40

Provide analysis as JSON:
{{
  "ready_for_production": true/false,
  "risk_level": "low|medium|high|critical",
  "weak_areas": ["list of capabilities below 60"],
  "critical_gaps": ["list of capabilities below 40"],
  "potential_issues": ["list of 3-5 specific issues that may occur in production"],
  "recommendations": ["list of 3-5 recommendations to improve readiness"]
}}

Only return valid JSON."""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config
            )
            
            response_text = response.text.strip()
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.startswith("```"):
                response_text = response_text[3:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            
            analysis = json.loads(response_text.strip())
            return analysis
        except Exception as e:
            print(f"Error analyzing production readiness: {e}")
            return self._get_fallback_analysis(maturity)
    
    def generate_final_report(self, game_state: Dict) -> Dict:
        """Generate final game report with analysis and prescriptive guidance."""
        prompt = f"""Generate a comprehensive final report for an enterprise multi-agent platform development simulation.

Final Game State:
- Budget Used: ${config.INITIAL_BUDGET - game_state['budget']:,} of ${config.INITIAL_BUDGET:,}
- Time Taken: {game_state['current_week']} weeks
- Decisions Made: {len(game_state['decisions_made'])}
- Production Launch: Week {game_state.get('production_week', 'N/A')}

Final Maturity Levels:
- Agent Development: {game_state['maturity']['agent_development']}/100
- Agent Operations: {game_state['maturity']['agent_operations']}/100
- Data Platforms: {game_state['maturity']['data_platforms']}/100
- Security: {game_state['maturity']['security']}/100
- Governance: {game_state['maturity']['governance']}/100

Production Issues Encountered: {len(game_state.get('production_issues', []))}

Provide a detailed report as JSON:
{{
  "overall_score": 0-100,
  "grade": "A+|A|B|C|D|F",
  "summary": "Brief summary of performance",
  "strengths": ["list of 3-5 strengths"],
  "weaknesses": ["list of 3-5 weaknesses"],
  "key_learnings": ["list of 5-7 key lessons learned"],
  "prescriptive_guidance": {{
    "short_term": ["3-5 immediate actions to take"],
    "medium_term": ["3-5 actions for next 6 months"],
    "long_term": ["3-5 strategic initiatives"]
  }},
  "best_practices": ["5-7 best practices for multi-agent platform development"],
  "recommendations": ["5-7 specific recommendations based on the gameplay"]
}}

Only return valid JSON."""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=GenerationConfig(
                    temperature=0.5,
                    top_p=0.9,
                    max_output_tokens=3072,
                )
            )
            
            response_text = response.text.strip()
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.startswith("```"):
                response_text = response_text[3:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            
            report = json.loads(response_text.strip())
            return report
        except Exception as e:
            print(f"Error generating final report: {e}")
            return self._get_fallback_report(game_state)
    
    def _get_fallback_decisions(self, game_state: Dict) -> List[Dict]:
        """Provide fallback decisions if AI generation fails."""
        return [
            {
                "id": "invest_dev_tools",
                "title": "Invest in Agent Development Tools",
                "description": "Invest in modern development frameworks and tools for building agents",
                "category": "development",
                "options": [
                    {
                        "id": "basic_tools",
                        "text": "Basic open-source tools",
                        "cost": 20000,
                        "time_weeks": 2,
                        "resources_required": 1,
                        "maturity_impact": {
                            "agent_development": 10,
                            "agent_operations": 0,
                            "data_platforms": 0,
                            "security": 0,
                            "governance": 0
                        },
                        "immediate_impact": True,
                        "delayed_impact_weeks": 0,
                        "consequences": "Quick start but limited capabilities"
                    },
                    {
                        "id": "enterprise_tools",
                        "text": "Enterprise-grade platform",
                        "cost": 100000,
                        "time_weeks": 6,
                        "resources_required": 3,
                        "maturity_impact": {
                            "agent_development": 25,
                            "agent_operations": 10,
                            "data_platforms": 5,
                            "security": 5,
                            "governance": 5
                        },
                        "immediate_impact": False,
                        "delayed_impact_weeks": 4,
                        "consequences": "Comprehensive solution with better long-term benefits"
                    }
                ]
            }
        ]
    
    def _get_fallback_analysis(self, maturity: Dict[str, int]) -> Dict:
        """Provide fallback analysis if AI analysis fails."""
        avg = sum(maturity.values()) / len(maturity)
        weak_areas = [k for k, v in maturity.items() if v < 60]
        critical_gaps = [k for k, v in maturity.items() if v < 40]
        
        return {
            "ready_for_production": avg >= 60 and len(critical_gaps) == 0,
            "risk_level": "low" if avg >= 70 else "medium" if avg >= 50 else "high",
            "weak_areas": weak_areas,
            "critical_gaps": critical_gaps,
            "potential_issues": ["System may experience performance issues"],
            "recommendations": ["Focus on improving weak areas before production launch"]
        }
    
    def _get_fallback_report(self, game_state: Dict) -> Dict:
        """Provide fallback report if AI generation fails."""
        avg_maturity = sum(game_state['maturity'].values()) / len(game_state['maturity'])
        
        return {
            "overall_score": int(avg_maturity),
            "grade": "B" if avg_maturity >= 70 else "C",
            "summary": "Simulation completed",
            "strengths": ["Completed the simulation"],
            "weaknesses": ["Some areas need improvement"],
            "key_learnings": ["Multi-agent platforms require balanced investment"],
            "prescriptive_guidance": {
                "short_term": ["Address critical gaps"],
                "medium_term": ["Build operational maturity"],
                "long_term": ["Establish governance framework"]
            },
            "best_practices": ["Invest in all capabilities equally"],
            "recommendations": ["Continue improving maturity levels"]
        }
