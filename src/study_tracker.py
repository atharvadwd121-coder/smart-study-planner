"""
Study Tracker Module
Tracks study sessions and provides statistics
"""

import json
import os
from datetime import datetime
from collections import Counter

class StudyTracker:
    def __init__(self, data_file='data/study_sessions.json'):
        self.data_file = data_file
        self.sessions = []
        self._ensure_data_dir()
        self._load_sessions()
    
    def _ensure_data_dir(self):
        """Ensure data directory exists"""
        data_dir = os.path.dirname(self.data_file)
        if data_dir and not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def _load_sessions(self):
        """Load study sessions from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.sessions = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                self.sessions = []
        else:
            self.sessions = []
    
    def _save_sessions(self):
        """Save study sessions to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.sessions, f, indent=4)
    
    def start_session(self, subject, planned_duration):
        """Start a new study session"""
        session = {
            'subject': subject,
            'planned_duration': planned_duration,
            'actual_duration': planned_duration,  # In a real app, this would be tracked
            'start_time': datetime.now().isoformat(),
            'date': datetime.now().strftime('%Y-%m-%d'),
            'completed': True
        }
        self.sessions.append(session)
        self._save_sessions()
        return session
    
    def get_all_sessions(self):
        """Return all study sessions"""
        return self.sessions
    
    def get_sessions_by_subject(self, subject):
        """Get all sessions for a specific subject"""
        return [s for s in self.sessions if s['subject'].lower() == subject.lower()]
    
    def get_statistics(self):
        """Calculate and return study statistics"""
        if not self.sessions:
            return {
                'total_sessions': 0,
                'total_hours': 0,
                'avg_duration': 0,
                'most_studied_subject': 'None'
            }
        
        total_sessions = len(self.sessions)
        total_minutes = sum(s['actual_duration'] for s in self.sessions)
        total_hours = total_minutes / 60
        avg_duration = total_minutes / total_sessions if total_sessions > 0 else 0
        
        # Find most studied subject
        subjects = [s['subject'] for s in self.sessions]
        subject_counts = Counter(subjects)
        most_studied = subject_counts.most_common(1)[0][0] if subject_counts else 'None'
        
        return {
            'total_sessions': total_sessions,
            'total_hours': total_hours,
            'avg_duration': avg_duration,
            'most_studied_subject': most_studied
        }
    
    def get_recent_sessions(self, limit=5):
        """Get most recent study sessions"""
        return sorted(self.sessions, 
                     key=lambda x: x['start_time'], 
                     reverse=True)[:limit]
    
    def get_subject_breakdown(self):
        """Get breakdown of time spent on each subject"""
        subject_time = {}
        for session in self.sessions:
            subject = session['subject']
            duration = session['actual_duration']
            subject_time[subject] = subject_time.get(subject, 0) + duration
        
        return dict(sorted(subject_time.items(), 
                          key=lambda x: x[1], 
                          reverse=True))
