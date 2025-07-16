from croniter import croniter
from datetime import datetime, timedelta
import re

class TaskParser:
    def parse_natural_language(self, text: str) -> dict:
        """Parse natural language into structured task"""
        # Simple regex patterns for time extraction
        time_patterns = {
            r'at (\d{1,2}):?(\d{0,2})\s*(am|pm)?': 'time',
            r'tomorrow': 'tomorrow',
            r'next week': 'next_week',
            r'(\d{1,2})/(\d{1,2})': 'date'
        }
        
        task_data = {
            'title': text,
            'due_date': None,
            'description': text
        }
        
        # Extract time information
        for pattern, time_type in time_patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                if time_type == 'time':
                    hour = int(match.group(1))
                    minute = int(match.group(2)) if match.group(2) else 0
                    period = match.group(3)
                    
                    if period and period.lower() == 'pm' and hour != 12:
                        hour += 12
                    elif period and period.lower() == 'am' and hour == 12:
                        hour = 0
                    
                    today = datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
                    task_data['due_date'] = today
                    
                elif time_type == 'tomorrow':
                    task_data['due_date'] = datetime.now() + timedelta(days=1)
                    
                break
        
        return task_data