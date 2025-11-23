"""
AI Study Recommender Module
Provides intelligent study recommendations based on patterns
"""

import random
from datetime import datetime, timedelta

class StudyRecommender:
    def __init__(self, study_tracker):
        self.study_tracker = study_tracker
    
    def get_recommendations(self):
        """Generate AI-powered study recommendations"""
        recommendations = []
        
        stats = self.study_tracker.get_statistics()
        sessions = self.study_tracker.get_all_sessions()
        
        # Recommendation 1: Study frequency
        if stats['total_sessions'] == 0:
            recommendations.append(
                "Start your learning journey! Add your first study session to track your progress."
            )
        elif stats['total_sessions'] < 5:
            recommendations.append(
                "Keep building momentum! Try to study consistently for better retention."
            )
        else:
            avg_duration = stats['avg_duration']
            if avg_duration < 30:
                recommendations.append(
                    "Consider longer study sessions (45-60 minutes) for deep focus and better learning."
                )
            elif avg_duration > 90:
                recommendations.append(
                    "Great dedication! Remember to take breaks every 50 minutes to maintain focus."
                )
            else:
                recommendations.append(
                    "Excellent session duration! You're in the optimal learning zone (30-90 minutes)."
                )
        
        # Recommendation 2: Subject diversity
        if sessions:
            subject_breakdown = self.study_tracker.get_subject_breakdown()
            if len(subject_breakdown) == 1:
                recommendations.append(
                    "Try diversifying your study topics to develop a well-rounded knowledge base."
                )
            elif len(subject_breakdown) >= 3:
                recommendations.append(
                    "Great subject diversity! Interleaving different topics enhances learning."
                )
        
        # Recommendation 3: Study consistency
        if len(sessions) >= 3:
            recent_sessions = self.study_tracker.get_recent_sessions(limit=7)
            unique_dates = set(s['date'] for s in recent_sessions)
            
            if len(unique_dates) >= 5:
                recommendations.append(
                    "Outstanding consistency! Daily practice is the key to mastery."
                )
            elif len(unique_dates) <= 2:
                recommendations.append(
                    "Try to study more frequently. Even 20-30 minutes daily is more effective than long, infrequent sessions."
                )
        
        # Recommendation 4: Pomodoro technique
        recommendations.append(
            "Pro tip: Use the Pomodoro Technique - 25 minutes of focused study followed by a 5-minute break."
        )
        
        # Recommendation 5: Best practices
        best_practices = [
            "Review your notes within 24 hours of learning for better retention.",
            "Practice active recall by testing yourself instead of just re-reading.",
            "Teach concepts to others (or explain out loud) to solidify understanding.",
            "Study in a distraction-free environment for maximum focus.",
            "Get adequate sleep (7-9 hours) - it's crucial for memory consolidation.",
            "Stay hydrated and take short breaks to maintain cognitive performance."
        ]
        
        if len(recommendations) < 5:
            recommendations.append(random.choice(best_practices))
        
        return recommendations[:5]  # Return top 5 recommendations
    
    def get_suggested_next_subject(self):
        """Suggest which subject to study next based on patterns"""
        subject_breakdown = self.study_tracker.get_subject_breakdown()
        
        if not subject_breakdown:
            return None
        
        # Suggest least studied subject
        least_studied = min(subject_breakdown.items(), key=lambda x: x[1])
        return least_studied[0]
    
    def get_optimal_study_time(self):
        """Suggest optimal study duration based on past performance"""
        stats = self.study_tracker.get_statistics()
        avg_duration = stats['avg_duration']
        
        if avg_duration == 0:
            return 45  # Default recommendation
        elif avg_duration < 30:
            return 40  # Gradually increase
        elif avg_duration > 90:
            return 60  # Recommend shorter, focused sessions
        else:
            return int(avg_duration)  # Maintain current duration
