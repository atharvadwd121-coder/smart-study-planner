"""
Task Manager Module
Handles task creation, management, and storage
"""

import json
import os
from datetime import datetime
import uuid

class TaskManager:
    def __init__(self, data_file='data/tasks.json'):
        self.data_file = data_file
        self.tasks = []
        self._ensure_data_dir()
        self._load_tasks()
    
    def _ensure_data_dir(self):
        """Ensure data directory exists"""
        data_dir = os.path.dirname(self.data_file)
        if data_dir and not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def _load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.tasks = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                self.tasks = []
        else:
            self.tasks = []
    
    def _save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f, indent=4)
    
    def add_task(self, title, description, priority='Medium', due_date=None):
        """Add a new task"""
        task = {
            'id': str(uuid.uuid4())[:8],
            'title': title,
            'description': description,
            'priority': priority,
            'due_date': due_date if due_date else None,
            'created_at': datetime.now().isoformat(),
            'completed': False,
            'completed_at': None
        }
        self.tasks.append(task)
        self._save_tasks()
        return task['id']
    
    def get_all_tasks(self):
        """Return all tasks"""
        return sorted(self.tasks, key=lambda x: (
            x['completed'],
            {'High': 0, 'Medium': 1, 'Low': 2}.get(x['priority'], 3)
        ))
    
    def get_task_by_id(self, task_id):
        """Get a specific task by ID"""
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        task = self.get_task_by_id(task_id)
        if task:
            task['completed'] = True
            task['completed_at'] = datetime.now().isoformat()
            self._save_tasks()
            return True
        return False
    
    def delete_task(self, task_id):
        """Delete a task"""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self._save_tasks()
            return True
        return False
    
    def get_priority_tasks(self):
        """Get high priority tasks that are not completed"""
        return [task for task in self.tasks 
                if task['priority'] == 'High' and not task['completed']]
    
    def get_statistics(self):
        """Get task statistics"""
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t['completed']])
        pending = total - completed
        high_priority = len([t for t in self.tasks if t['priority'] == 'High'])
        
        return {
            'total': total,
            'completed': completed,
            'pending': pending,
            'high_priority': high_priority,
            'completion_rate': (completed / total * 100) if total > 0 else 0
        }
