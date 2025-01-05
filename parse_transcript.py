import json

def parse_transcript(input_file, output_file):
    with open(input_file, 'r') as f:
        transcript = f.read()
    
    turns = []
    lines = transcript.strip().split('\n')
    current_speaker = None
    current_text = []
    
    for line in lines:
        if line.startswith("User:") or line.startswith("Assistant:"):
            if current_speaker and current_text:
                turns.append({"speaker": current_speaker, "text": " ".join(current_text)})
            current_speaker = line.split(":")[0]
            current_text = [line.split(":", 1)[1].strip()]
        else:
            current_text.append(line.strip())
    
    if current_speaker and current_text:
        turns.append({"speaker": current_speaker, "text": " ".join(current_text)})
    
    with open(output_file, 'w') as f:
        json.dump(turns, f, indent=4)

if __name__ == "__main__":
    parse_transcript("transcript.txt", "turns.json")
