def heading_hirarchy(text, current_path):
    with open("prompts_texts/heading_hierarchy", "r") as f: 
        system_prompt = f.read()
        return system_prompt