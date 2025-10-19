"""PDF Scenario Parser - Extracts game scenarios from PDF documents using AI."""
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig
import PyPDF2
import json
import config
from typing import List, Dict
import io


class PDFScenarioParser:
    """Parses PDF documents and extracts game scenarios using AI."""
    
    def __init__(self):
        """Initialize the PDF parser with Vertex AI."""
        if config.PROJECT_ID:
            vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)
        self.model = GenerativeModel(config.MODEL_NAME)
        self.generation_config = GenerationConfig(
            temperature=0.5,
            top_p=0.9,
            max_output_tokens=4096,
        )
    
    def extract_text_from_pdf(self, pdf_file) -> str:
        """Extract text content from PDF file."""
        try:
            # Read PDF from file object or bytes
            if isinstance(pdf_file, bytes):
                pdf_file = io.BytesIO(pdf_file)
            
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            
            # Extract text from all pages
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            
            return text.strip()
        except Exception as e:
            print(f"Error extracting PDF text: {e}")
            raise
    
    def generate_scenarios_from_text(self, pdf_text: str) -> List[Dict]:
        """Use AI to generate game scenarios from PDF text."""
        prompt = f"""You are an AI that extracts game scenarios from documents about enterprise multi-agent platform development.

Given the following document content, extract or generate realistic decision scenarios for a simulation game where players build an enterprise multi-agent platform.

Document Content:
{pdf_text[:10000]}  # Limit to first 10000 chars to avoid token limits

Generate 3-5 realistic decision scenarios based on the document content. Each scenario should:
1. Be relevant to enterprise multi-agent platform development
2. Have 2-3 options with different trade-offs (cost, time, maturity impact)
3. Include clear consequences for each option
4. Focus on one of these categories: development, operations, data, security, governance

Return your response as a JSON array with this EXACT structure:
[
  {{
    "id": "unique_scenario_id",
    "title": "Decision Title",
    "description": "Detailed description of the scenario",
    "category": "development|operations|data|security|governance",
    "week_available": 1,
    "options": [
      {{
        "id": "option1_id",
        "text": "Option description explaining what this choice involves",
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
        "consequences": "What happens if you choose this option"
      }},
      {{
        "id": "option2_id",
        "text": "Alternative option description",
        "cost": 100000,
        "time_weeks": 6,
        "resources_required": 3,
        "maturity_impact": {{
          "agent_development": 20,
          "agent_operations": 10,
          "data_platforms": 5,
          "security": 5,
          "governance": 5
        }},
        "immediate_impact": false,
        "delayed_impact_weeks": 3,
        "consequences": "What happens if you choose this alternative"
      }}
    ]
  }}
]

Rules:
- cost: Between 5,000 and 200,000 (realistic enterprise costs)
- time_weeks: Between 1 and 12 weeks
- resources_required: Between 1 and 6 team members
- maturity_impact: Values between -20 and +40 for each capability
- week_available: Between 1 and 30
- Make scenarios realistic and educational about multi-agent platforms

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
            
            scenarios = json.loads(response_text.strip())
            return scenarios
            
        except json.JSONDecodeError as e:
            print(f"Error parsing AI response as JSON: {e}")
            print(f"Response text: {response_text[:500]}")
            raise ValueError("Failed to parse AI response. The AI did not return valid JSON.")
        except Exception as e:
            print(f"Error generating scenarios from text: {e}")
            raise
    
    def parse_pdf_to_scenarios(self, pdf_file) -> List[Dict]:
        """
        Main method: Extract text from PDF and generate scenarios.
        
        Args:
            pdf_file: File object or bytes of the PDF
            
        Returns:
            List of scenario dictionaries
        """
        # Step 1: Extract text from PDF
        print("Extracting text from PDF...")
        pdf_text = self.extract_text_from_pdf(pdf_file)
        
        if not pdf_text or len(pdf_text) < 100:
            raise ValueError("PDF appears to be empty or contains insufficient text")
        
        # Step 2: Generate scenarios using AI
        print("Generating scenarios using AI...")
        scenarios = self.generate_scenarios_from_text(pdf_text)
        
        print(f"Successfully generated {len(scenarios)} scenarios from PDF")
        return scenarios
