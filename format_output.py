import json

def format_output(input_file, output_file):
    with open(input_file, 'r') as f:
        qa_pairs = json.load(f)
    
    final_pairs = []
    for pair in qa_pairs:
        if pair["valid"]:
            final_pairs.append({"question": pair["question"], "answer": pair["answer"]})
    
    with open(output_file, 'w') as f:
        json.dump(final_pairs, f, indent=4)

if __name__ == "__main__":
    format_output("qa_pairs.json", "final_qa_pairs.json")
