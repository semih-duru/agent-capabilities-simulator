#!/usr/bin/env python3
"""
Simple test script for PDF scenario upload feature.
Creates a sample PDF and uploads it to test the functionality.
"""
import requests
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io


def create_sample_pdf():
    """Create a sample PDF about multi-agent platforms for testing."""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # Add title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Enterprise Multi-Agent Platform Guide")
    
    # Add content
    c.setFont("Helvetica", 12)
    y_position = 700
    
    content = [
        "Key Decisions in Building Agent Platforms:",
        "",
        "1. Framework Selection",
        "   - Open-source frameworks provide quick start but limited features",
        "   - Enterprise frameworks offer security and scalability",
        "   - Custom frameworks provide maximum flexibility",
        "",
        "2. Observability Strategy",
        "   - Logging is essential for debugging agent behavior",
        "   - Metrics help track performance and resource usage",
        "   - Distributed tracing reveals inter-agent communication patterns",
        "",
        "3. Data Architecture",
        "   - Direct database access is fast but creates security risks",
        "   - API layers provide governed access to data",
        "   - Data mesh architecture enables scalable data management",
        "",
        "4. Security Considerations",
        "   - Authentication verifies agent identity",
        "   - Authorization controls what agents can access",
        "   - Encryption protects data in transit and at rest",
        "",
        "5. Governance Framework",
        "   - Policies define acceptable agent behavior",
        "   - Audit trails ensure compliance",
        "   - Risk management identifies potential issues",
    ]
    
    for line in content:
        c.drawString(100, y_position, line)
        y_position -= 20
    
    c.save()
    buffer.seek(0)
    return buffer


def test_pdf_upload(server_url="http://localhost:5000"):
    """Test the PDF upload endpoint."""
    print("🧪 Testing PDF Scenario Upload Feature\n")
    
    # Step 1: Create sample PDF
    print("📄 Creating sample PDF...")
    pdf_buffer = create_sample_pdf()
    print("✅ Sample PDF created\n")
    
    # Step 2: Upload PDF
    print(f"📤 Uploading PDF to {server_url}/api/scenarios/add-from-pdf...")
    
    try:
        files = {'pdf_file': ('test_document.pdf', pdf_buffer, 'application/pdf')}
        response = requests.post(
            f'{server_url}/api/scenarios/add-from-pdf',
            files=files,
            timeout=60
        )
        
        # Step 3: Check response
        if response.status_code == 200:
            data = response.json()
            print("✅ Upload successful!\n")
            print(f"📊 Results:")
            print(f"   - Scenarios added: {data.get('scenarios_added', 0)}")
            print(f"   - Message: {data.get('message', '')}")
            if 'pdf_saved_as' in data:
                print(f"   - PDF saved as: {data['pdf_saved_as']}")
            print()
            
            # Display scenarios
            scenarios = data.get('scenarios', [])
            if scenarios:
                print(f"🎮 Generated Scenarios:")
                for i, scenario in enumerate(scenarios, 1):
                    print(f"\n   {i}. {scenario.get('title', 'Untitled')}")
                    print(f"      Category: {scenario.get('category', 'N/A')}")
                    print(f"      Options: {len(scenario.get('options', []))}")
                    print(f"      Week: {scenario.get('week_available', 'N/A')}")
            
            print("\n✨ Test completed successfully!")
            return True
        else:
            print(f"❌ Upload failed with status {response.status_code}")
            print(f"   Error: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Is it running?")
        print(f"   Try: python app.py")
        return False
    except Exception as e:
        print(f"❌ Error during upload: {e}")
        return False


if __name__ == '__main__':
    # Get server URL from command line or use default
    server_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:5000"
    
    print("=" * 60)
    print("PDF Scenario Upload Test")
    print("=" * 60 + "\n")
    
    success = test_pdf_upload(server_url)
    sys.exit(0 if success else 1)
