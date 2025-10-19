# PDF Scenario Creation Guide 📄

## Quick Start (< 10 minutes)

This feature allows you to automatically create game scenarios from PDF documents using AI.

### How It Works

1. **Upload a PDF** - Any PDF document related to enterprise platforms, AI systems, or software development
2. **AI Extracts Content** - The system reads the PDF and extracts the text
3. **Generate Scenarios** - Gemini AI analyzes the content and creates realistic game scenarios
4. **Add to Game** - Scenarios are automatically added to the scenario manager

### Usage

#### Using cURL

```bash
# Upload a PDF to generate scenarios
curl -X POST http://localhost:5000/api/scenarios/add-from-pdf \
  -F "pdf_file=@/path/to/your/document.pdf"
```

#### Using Python

```python
import requests

# Upload PDF file
with open('your_document.pdf', 'rb') as f:
    files = {'pdf_file': f}
    response = requests.post(
        'http://localhost:5000/api/scenarios/add-from-pdf',
        files=files
    )
    
print(response.json())
```

#### Using Postman

1. Create a new POST request to: `http://localhost:5000/api/scenarios/add-from-pdf`
2. Go to the "Body" tab
3. Select "form-data"
4. Add a key named `pdf_file` with type "File"
5. Choose your PDF file
6. Click "Send"

### Expected Response

```json
{
  "success": true,
  "message": "Successfully added 4 scenarios from PDF",
  "scenarios_added": 4,
  "scenarios": [
    {
      "id": "scenario_1",
      "title": "Decision Title",
      "description": "Scenario description...",
      "category": "development",
      "week_available": 5,
      "options": [...]
    }
  ]
}
```

### What PDFs Work Best?

✅ **Good PDF Types:**
- Technical documentation about multi-agent systems
- Enterprise architecture guides
- Software development best practices
- AI/ML deployment guides
- Platform engineering documentation
- DevOps and operations guides

❌ **Not Ideal:**
- PDFs with mostly images (no extractable text)
- Encrypted or password-protected PDFs
- Very short documents (< 100 words)

### Troubleshooting

**Error: "PDF appears to be empty"**
- The PDF might be image-based. Try a text-based PDF instead.

**Error: "Failed to parse AI response"**
- The AI had trouble understanding the content. Try a PDF with clearer structure.

**Error: "No PDF file provided"**
- Make sure you're sending the file with the key name `pdf_file`

### Example Test

Create a test PDF about agent platforms and try it:

```bash
# Install dependencies if needed
pip install PyPDF2

# Upload a test PDF
curl -X POST http://localhost:5000/api/scenarios/add-from-pdf \
  -F "pdf_file=@test_document.pdf"
```

### Integration with Game

Once scenarios are added from a PDF:
1. They're saved to `scenarios.json`
2. They appear in the game based on `week_available` setting
3. Players can select them during gameplay
4. Each scenario has proper cost, time, and maturity impacts

### Time Estimate

- **Upload PDF**: < 1 minute
- **AI Processing**: 30 seconds - 2 minutes (depending on PDF size)
- **Total**: Usually under 3 minutes per PDF

---

**That's it!** You can now create scenarios from any PDF document in your organization. 🚀
