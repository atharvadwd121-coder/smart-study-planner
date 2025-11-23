"""
Smart Study Planner Package
Makes the src directory a Python package
"""

from .task_manager import TaskManager
from .study_tracker import StudyTracker
from .recommender import StudyRecommender
from .utils import *

__version__ = '1.0.0'
__author__ = 'Smart Study Planner Team'
__all__ = ['TaskManager', 'StudyTracker', 'StudyRecommender']
