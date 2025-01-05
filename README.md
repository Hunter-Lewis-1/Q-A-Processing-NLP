# Q&A Turn Parser for NLP Analysis

This repository contains a modular Python-based system to parse question-answer (Q&A) turns from conversation transcripts for natural language processing (NLP) analysis. It leverages advanced NLP techniques, including BERT for question detection and Sentence-BERT for semantic similarity, to accurately identify, pair, and verify Q&A turns. The output is a clean JSON file suitable for downstream NLP tasks.

## Overview

The system processes a conversation transcript (e.g., "User: How are you?\nAssistant: I'm fine.") through four discrete stages:
1. **Parsing**: Splits the transcript into individual turns.
2. **Question Classification**: Identifies user questions using a pre-trained BERT model.
3. **Pairing and Verification**: Pairs questions with answers and verifies them using semantic similarity.
4. **Formatting**: Stores valid Q&A pairs in a final JSON file.

Each stage is implemented as a separate script, with file-based inputs and outputs for modularity and ease of debugging.

## Features
- Uses [mrsinghania/asr-question-detection](https://huggingface.co/mrsinghania/asr-question-detection) for question detection.
- Employs [Sentence-BERT (`all-MiniLM-L6-v2`)](https://www.sbert.net/) for semantic similarity verification.
- Handles multi-line turns and simple turn-taking conversations.
- Outputs structured JSON for NLP analysis.

## Installation

### Prerequisites
- Python 3.8+
- Git (to clone the repository)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/qa-turn-parser.git
   cd qa-turn-parser
   ```
2. Install dependencies:
   ```bash
   pip install transformers sentence-transformers torch
   ```

## Usage

### Input
Prepare a `transcript.txt` file with your conversation data. Each line should start with `User:` or `Assistant:` followed by a colon and text. Example:
```
User: How are you?
Assistant: I'm fine.
User: What time is it?
Assistant: It's 3 PM.
```

### Running the Pipeline
Execute the scripts in sequence:
```bash
python parse_transcript.py
python classify_questions.py
python pair_and_verify.py
python format_output.py
```

### Output
The final output is `final_qa_pairs.json`, containing valid Q&A pairs. Example:
```json
[
    {"question": "How are you?", "answer": "I'm fine."},
    {"question": "What time is it?", "answer": "It's 3 PM."}
]
```

Intermediate files (`turns.json`, `classified_turns.json`, `qa_pairs.json`) are also generated for debugging or analysis.

### Example
An example `transcript.txt` is included. Run the pipeline with it to see the system in action:
```bash
python parse_transcript.py
python classify_questions.py
python pair_and_verify.py
python format_output.py
```
Check `final_qa_pairs.json` for the results.

## File Structure
```
qa-turn-parser/
│
├── parse_transcript.py      # Parses transcript into turns
├── classify_questions.py    # Classifies user turns as questions
├── pair_and_verify.py       # Pairs and verifies Q&A turns
├── format_output.py         # Formats valid pairs for output
├── transcript.txt           # Example input transcript
├── turns.json              # Output: Parsed turns (generated)
├── classified_turns.json   # Output: Classified turns (generated)
├── qa_pairs.json           # Output: Verified Q&A pairs (generated)
├── final_qa_pairs.json     # Output: Final valid Q&A pairs (generated)
└── README.md               # This file
```

## Architecture
The system follows a modular, file-based architecture:
```
transcript.txt → [parse_transcript.py] → turns.json → [classify_questions.py] → classified_turns.json → [pair_and_verify.py] → qa_pairs.json → [format_output.py] → final_qa_pairs.json
```
- **Parser**: Converts raw text to structured turns.
- **Classifier**: Uses BERT to detect questions.
- **Pairer/Verifier**: Pairs turns and checks similarity with Sentence-BERT.
- **Formatter**: Prepares the final output.

## Customization
- **Similarity Threshold**: Edit `pair_and_verify.py` to adjust the 0.5 threshold for validating pairs.
- **Model Choice**: Replace model names in `classify_questions.py` or `pair_and_verify.py` for different pre-trained models.
- **Input Format**: Modify `parse_transcript.py` if your transcript format differs (e.g., no colons).

## Limitations
- Assumes alternating User-Assistant turns; complex dialogues may require additional logic.
- Multi-line turns are supported, but nested or interrupted turns are not.
- Performance may vary with domain-specific transcripts; fine-tuning models could improve accuracy.

## Dependencies
- `transformers`: For BERT-based question detection.
- `sentence-transformers`: For Sentence-BERT similarity.
- `torch`: PyTorch backend for model inference.

## Contributing
Feel free to submit issues or pull requests for enhancements, such as:
- Support for complex conversation structures.
- Additional verification metrics.
- Command-line interface for easier execution.

## License
This project is licensed under the MIT License. 

## Acknowledgments
- Built with models from [Hugging Face](https://huggingface.co/).
- Inspired by research on Q&A pair detection in conversational data.
