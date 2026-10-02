def create_memory():
    """Create an empty conversation history."""
    return []

def add_message(
    history: list,
    role: str,
    content: str
    ):
    """Add one message to conversational history."""
    
    history.append({
        'role': role,
        'content': content
    })

def format_history(history: list) -> str:
    """Convert history into prompt-friendly text."""
    
    if not history:
        return "No previous conversation."
    
    lines = []
    for message in history:
        role = message['role'].capitalize()
        content = message['content']
        
        lines.append(
            f"{role}: {content}"
        )
        
        return "\n".join(lines)