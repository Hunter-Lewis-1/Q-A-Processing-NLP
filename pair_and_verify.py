import json
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

def pair_and_verify(input_file, output_file):
    with open(input_file, 'r') as f:
        classified_turns = json.load(f)
    
    sbert_model = SentenceTransformer('all-MiniLM-L6-v2')
    qa_pairs = []
    
    for i in range(len(classified_turns) - 1):
        current_turn = classified_turns[i]
        next_turn = classified_turns[i + 1]
        if current_turn["speaker"] == "User" and current_turn["is_question"] and next_turn["speaker"] == "Assistant":
            question = current_turn["text"]
            answer = next_turn["text"]
            embedding_q = sbert_model.encode(question, convert_to_tensor=True)
            embedding_a = sbert_model.encode(answer, convert_to_tensor=True)
            similarity = cos_sim(embedding_q, embedding_a).item()
            valid = similarity > 0.5
            qa_pairs.append({"question": question, "answer": answer, "similarity": similarity, "valid": valid})
    
    with open(output_file, 'w') as f:
        json.dump(qa_pairs, f, indent=4)

if __name__ == "__main__":
    pair_and_verify("classified_turns.json", "qa_pairs.json")
