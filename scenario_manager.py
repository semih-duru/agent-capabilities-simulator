"""Scenario manager for adding and managing game scenarios."""
from typing import Dict, List
import json
import os


class ScenarioManager:
    """Manages game scenarios and decision templates."""
    
    def __init__(self, scenarios_file: str = "scenarios.json"):
        """Initialize the scenario manager."""
        self.scenarios_file = scenarios_file
        self.scenarios = self._load_scenarios()
    
    def _load_scenarios(self) -> List[Dict]:
        """Load scenarios from file."""
        if os.path.exists(self.scenarios_file):
            try:
                with open(self.scenarios_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading scenarios: {e}")
        return self._get_default_scenarios()
    
    def _get_default_scenarios(self) -> List[Dict]:
        """Get default scenarios."""
        return [
            {
                "id": "dev_framework_choice",
                "title": "Choose Agent Development Framework",
                "description": "You need to select a framework for building your agents. This decision will impact how quickly you can develop agents and their capabilities.",
                "category": "development",
                "week_available": 1,
                "options": [
                    {
                        "id": "opensource_basic",
                        "text": "Use basic open-source framework (Quick start, limited features)",
                        "cost": 10000,
                        "time_weeks": 1,
                        "resources_required": 1,
                        "maturity_impact": {
                            "agent_development": 8,
                            "agent_operations": 0,
                            "data_platforms": 0,
                            "security": 0,
                            "governance": 0
                        },
                        "immediate_impact": True,
                        "delayed_impact_weeks": 0,
                        "consequences": "Fast to implement but may need rework later as complexity grows"
                    },
                    {
                        "id": "enterprise_framework",
                        "text": "Invest in enterprise-grade framework (Comprehensive, battle-tested)",
                        "cost": 80000,
                        "time_weeks": 4,
                        "resources_required": 3,
                        "maturity_impact": {
                            "agent_development": 20,
                            "agent_operations": 8,
                            "data_platforms": 5,
                            "security": 5,
                            "governance": 5
                        },
                        "immediate_impact": False,
                        "delayed_impact_weeks": 3,
                        "consequences": "Higher upfront cost but better long-term scalability and security"
                    },
                    {
                        "id": "custom_framework",
                        "text": "Build custom framework (Maximum flexibility, high effort)",
                        "cost": 150000,
                        "time_weeks": 8,
                        "resources_required": 5,
                        "maturity_impact": {
                            "agent_development": 30,
                            "agent_operations": 5,
                            "data_platforms": 3,
                            "security": 2,
                            "governance": 0
                        },
                        "immediate_impact": False,
                        "delayed_impact_weeks": 6,
                        "consequences": "Most flexible but requires significant investment and may delay other initiatives"
                    }
                ]
            },
            {
                "id": "observability_setup",
                "title": "Establish Observability and Monitoring",
                "description": "Your agents need monitoring and observability. How much should you invest in operations?",
                "category": "operations",
                "week_available": 5,
                "options": [
                    {
                        "id": "basic_logging",
                        "text": "Basic logging only (Minimal cost, limited visibility)",
                        "cost": 5000,
                        "time_weeks": 1,
                        "resources_required": 1,
                        "maturity_impact": {
                            "agent_development": 0,
                            "agent_operations": 8,
                            "data_platforms": 0,
                            "security": 0,
                            "governance": 2
                        },
                        "immediate_impact": True,
                        "delayed_impact_weeks": 0,
                        "consequences": "Will struggle to debug issues in production"
                    },
                    {
                        "id": "full_observability",
                        "text": "Comprehensive observability platform (Metrics, logs, traces, alerts)",
                        "cost": 60000,
                        "time_weeks": 3,
                        "resources_required": 2,
                        "maturity_impact": {
                            "agent_development": 5,
                            "agent_operations": 25,
                            "data_platforms": 5,
                            "security": 5,
                            "governance": 8
                        },
                        "immediate_impact": True,
                        "delayed_impact_weeks": 0,
                        "consequences": "Better visibility and faster incident response in production"
                    }
                ]
            },
            {
                "id": "data_infrastructure",
                "title": "Data Platform Strategy",
                "description": "Agents need access to enterprise data. How will you architect the data layer?",
                "category": "data",
                "week_available": 8,
                "options": [
                    {
                        "id": "direct_access",
                        "text": "Direct database access (Fast to implement, security risks)",
                        "cost": 20000,
                        "time_weeks": 2,
                        "resources_required": 2,
                        "maturity_impact": {
                            "agent_development": 10,
                            "agent_operations": 0,
                            "data_platforms": 15,
                            "security": -10,
                            "governance": -5
                        },
                        "immediate_impact": True,
                        "delayed_impact_weeks": 0,
                        "consequences": "Security vulnerabilities and governance issues will emerge"
                    },
                    {
                        "id": "api_layer",
                        "text": "Build API abstraction layer (Secure, governed access)",
                        "cost": 80000,
                        "time_weeks": 6,
                        "resources_required": 4,
                        "maturity_impact": {
                            "agent_development": 8,
                            "agent_operations": 10,
                            "data_platforms": 30,
                            "security": 15,
                            "governance": 15
                        },
                        "immediate_impact": False,
                        "delayed_impact_weeks": 4,
                        "consequences": "Better security and governance, enables safer production deployment"
                    },
                    {
                        "id": "data_mesh",
                        "text": "Implement data mesh architecture (Future-proof, complex)",
                        "cost": 200000,
                        "time_weeks": 12,
                        "resources_required": 6,
                        "maturity_impact": {
                            "agent_development": 5,
                            "agent_operations": 15,
                            "data_platforms": 40,
                            "security": 20,
                            "governance": 25
                        },
                        "immediate_impact": False,
                        "delayed_impact_weeks": 8,
                        "consequences": "Most scalable approach but may delay production launch"
                    }
                ]
            },
            {
                "id": "security_implementation",
                "title": "Security Posture Decision",
                "description": "How will you secure your multi-agent platform?",
                "category": "security",
                "week_available": 12,
                "options": [
                    {
                        "id": "basic_auth",
                        "text": "Basic authentication only (Quick, minimal security)",
                        "cost": 15000,
                        "time_weeks": 2,
                        "resources_required": 1,
                        "maturity_impact": {
                            "agent_development": 0,
                            "agent_operations": 0,
                            "data_platforms": 0,
                            "security": 12,
                            "governance": 0
                        },
                        "immediate_impact": True,
                        "delayed_impact_weeks": 0,
                        "consequences": "High risk of security incidents in production"
                    },
                    {
                        "id": "comprehensive_security",
                        "text": "Comprehensive security framework (Zero-trust, encryption, IAM)",
                        "cost": 120000,
                        "time_weeks": 8,
                        "resources_required": 4,
                        "maturity_impact": {
                            "agent_development": 5,
                            "agent_operations": 10,
                            "data_platforms": 8,
                            "security": 35,
                            "governance": 12
                        },
                        "immediate_impact": False,
                        "delayed_impact_weeks": 4,
                        "consequences": "Strong security posture, reduced risk of breaches"
                    }
                ]
            },
            {
                "id": "governance_framework",
                "title": "Establish Governance Framework",
                "description": "How will you govern agent behavior and ensure compliance?",
                "category": "governance",
                "week_available": 15,
                "options": [
                    {
                        "id": "minimal_governance",
                        "text": "Minimal governance (Fast deployment, compliance risks)",
                        "cost": 10000,
                        "time_weeks": 1,
                        "resources_required": 1,
                        "maturity_impact": {
                            "agent_development": 0,
                            "agent_operations": 0,
                            "data_platforms": 0,
                            "security": 0,
                            "governance": 10
                        },
                        "immediate_impact": True,
                        "delayed_impact_weeks": 0,
                        "consequences": "Will face compliance and audit issues post-production"
                    },
                    {
                        "id": "comprehensive_governance",
                        "text": "Comprehensive governance (Policies, auditing, compliance)",
                        "cost": 100000,
                        "time_weeks": 6,
                        "resources_required": 3,
                        "maturity_impact": {
                            "agent_development": 8,
                            "agent_operations": 12,
                            "data_platforms": 10,
                            "security": 12,
                            "governance": 35
                        },
                        "immediate_impact": False,
                        "delayed_impact_weeks": 3,
                        "consequences": "Strong compliance posture, better risk management"
                    }
                ]
            }
        ]
    
    def save_scenarios(self) -> bool:
        """Save scenarios to file."""
        try:
            with open(self.scenarios_file, 'w') as f:
                json.dump(self.scenarios, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving scenarios: {e}")
            return False
    
    def add_scenario(self, scenario: Dict) -> bool:
        """Add a new scenario."""
        try:
            self.scenarios.append(scenario)
            return self.save_scenarios()
        except Exception as e:
            print(f"Error adding scenario: {e}")
            return False
    
    def get_scenario(self, scenario_id: str) -> Dict:
        """Get a specific scenario by ID."""
        for scenario in self.scenarios:
            if scenario['id'] == scenario_id:
                return scenario
        return None
    
    def get_all_scenarios(self) -> List[Dict]:
        """Get all scenarios."""
        return self.scenarios
    
    def get_scenarios_for_week(self, week: int) -> List[Dict]:
        """Get scenarios available for a specific week."""
        return [s for s in self.scenarios if s.get('week_available', 0) <= week]
