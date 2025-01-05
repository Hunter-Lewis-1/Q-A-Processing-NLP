import json
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def classify_questions(input_file, output_file):
    with open(input_file, 'r') as f:
        turns = json.load(f)
    
    tokenizer = AutoTokenizer.from_pretrained("mrsinghania/asr-question-detection")
    model = AutoModelForSequenceClassification.from_pretrained("mrsinghania/asr-question-detection")
    
    classified_turns = []
    for turn in turns:
        if turn["speaker"] == "User":
            inputs = tokenizer(turn["text"], return_tensors="pt", truncation=True, max_length=512)
            with torch.no_grad():
                outputs = model(**inputs)
            score = torch.sigmoid(outputs.logits).item()
            turn["is_question"] = score > 0.5
        else:
            turn["is_question"] = False
        classified_turns.append(turn)
    
    with open(output_file, 'w') as f:
        json.dump(classified_turns, f, indent=4)

if __name__ == "__main__":
    classify_questions("turns.json", "classified_turns.json")
