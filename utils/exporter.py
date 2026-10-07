import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def save_to_jsonl(data: list[dict], filename: str = "listings.jsonl") -> None:
    
    try:
        file_path = Path(filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            for item in data:
                json_line = json.dumps(item, ensure_ascii=False)
                f.write(json_line + "\n")
                
        logger.info(f"Successfully saved {len(data)} records to JSONL file: {file_path.absolute()}")

    except Exception as e:
        logger.error(f"Failed to save data to JSONL file: {e}")