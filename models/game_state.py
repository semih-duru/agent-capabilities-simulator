"""Game state models for the simulation."""
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum


class DecisionCategory(Enum):
    DEVELOPMENT = "development"
    OPERATIONS = "operations"
    DATA = "data"
    SECURITY = "security"
    GOVERNANCE = "governance"
    STRATEGIC = "strategic"


@dataclass
class MaturityMetrics:
    """Tracks maturity levels across all capabilities."""
    agent_development: int = 0
    agent_operations: int = 0
    data_platforms: int = 0
    security: int = 0
    governance: int = 0
    
    def get_average(self) -> float:
        """Calculate average maturity across all capabilities."""
        return (
            self.agent_development + 
            self.agent_operations + 
            self.data_platforms + 
            self.security + 
            self.governance
        ) / 5
    
    def to_dict(self) -> Dict[str, int]:
        """Convert to dictionary."""
        return {
            "agent_development": self.agent_development,
            "agent_operations": self.agent_operations,
            "data_platforms": self.data_platforms,
            "security": self.security,
            "governance": self.governance
        }


@dataclass
class Decision:
    """Represents a decision point in the game."""
    id: str
    title: str
    description: str
    category: DecisionCategory
    options: List['DecisionOption']
    week_available: int = 0
    completed: bool = False


@dataclass
class DecisionOption:
    """Represents an option for a decision."""
    id: str
    text: str
    cost: int
    time_weeks: int
    resources_required: int
    maturity_impact: Dict[str, int]
    immediate_impact: bool = True
    delayed_impact_weeks: int = 0
    consequences: str = ""


@dataclass
class GameEvent:
    """Represents an event that occurs during the game."""
    week: int
    title: str
    description: str
    impact: Dict[str, any]


@dataclass
class GameState:
    """Main game state."""
    budget: int
    time_remaining_weeks: int
    resources: int
    current_week: int
    maturity: MaturityMetrics
    decisions_made: List[Dict] = field(default_factory=list)
    events: List[GameEvent] = field(default_factory=list)
    is_production: bool = False
    production_week: Optional[int] = None
    production_issues: List[str] = field(default_factory=list)
    game_over: bool = False
    
    def to_dict(self) -> Dict:
        """Convert game state to dictionary."""
        return {
            "budget": self.budget,
            "time_remaining_weeks": self.time_remaining_weeks,
            "resources": self.resources,
            "current_week": self.current_week,
            "maturity": self.maturity.to_dict(),
            "decisions_made": self.decisions_made,
            "events": [
                {
                    "week": e.week,
                    "title": e.title,
                    "description": e.description,
                    "impact": e.impact
                } for e in self.events
            ],
            "is_production": self.is_production,
            "production_week": self.production_week,
            "production_issues": self.production_issues,
            "game_over": self.game_over
        }
