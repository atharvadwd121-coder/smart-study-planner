#!/usr/bin/env python3
"""
Smart Study Planner - Main Entry Point
AI-powered study planner with task management and intelligent recommendations
"""

import sys
import os
from datetime import datetime
from src.task_manager import TaskManager
from src.study_tracker import StudyTracker
from src.recommender import StudyRecommender
from src.utils import clear_screen, print_banner, get_user_input

class SmartStudyPlanner:
    def __init__(self):
        self.task_manager = TaskManager()
        self.study_tracker = StudyTracker()
        self.recommender = StudyRecommender(self.study_tracker)
        self.running = True

    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("         SMART STUDY PLANNER")
        print("="*50)
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Complete Task")
        print("4. Start Study Session")
        print("5. View Study Statistics")
        print("6. Get AI Recommendations")
        print("7. View Priority Tasks")
        print("8. Delete Task")
        print("9. Exit")
        print("="*50)

    def add_task(self):
        """Add a new task"""
        clear_screen()
        print("\n--- Add New Task ---")
        title = get_user_input("Enter task title: ")
        description = get_user_input("Enter task description: ")
        
        print("\nPriority Levels:")
        print("1. High")
        print("2. Medium")
        print("3. Low")
        priority_choice = get_user_input("Select priority (1-3): ")
        
        priority_map = {"1": "High", "2": "Medium", "3": "Low"}
        priority = priority_map.get(priority_choice, "Medium")
        
        due_date = get_user_input("Enter due date (YYYY-MM-DD) or press Enter to skip: ")
        
        task_id = self.task_manager.add_task(title, description, priority, due_date)
        print(f"\n✓ Task added successfully! (ID: {task_id})")
        input("\nPress Enter to continue...")

    def view_tasks(self):
        """Display all tasks"""
        clear_screen()
        print("\n--- All Tasks ---")
        tasks = self.task_manager.get_all_tasks()
        
        if not tasks:
            print("No tasks found. Add some tasks to get started!")
        else:
            for task in tasks:
                status = "✓ Completed" if task['completed'] else "○ Pending"
                print(f"\nID: {task['id']}")
                print(f"Title: {task['title']}")
                print(f"Priority: {task['priority']}")
                print(f"Status: {status}")
                print(f"Due Date: {task['due_date'] or 'Not set'}")
                print("-" * 40)
        
        input("\nPress Enter to continue...")

    def complete_task(self):
        """Mark a task as completed"""
        clear_screen()
        print("\n--- Complete Task ---")
        self.view_tasks()
        
        task_id = get_user_input("\nEnter task ID to complete: ")
        if self.task_manager.complete_task(task_id):
            print("\n✓ Task marked as completed!")
        else:
            print("\n✗ Task not found!")
        
        input("\nPress Enter to continue...")

    def start_study_session(self):
        """Start a new study session"""
        clear_screen()
        print("\n--- Start Study Session ---")
        subject = get_user_input("Enter subject/topic: ")
        
        try:
            duration = int(get_user_input("Enter planned duration (minutes): "))
            
            print(f"\n✓ Study session started for {subject}!")
            print(f"Duration: {duration} minutes")
            print("\nGood luck with your studies!")
            
            self.study_tracker.start_session(subject, duration)
            
        except ValueError:
            print("\n✗ Invalid duration entered!")
        
        input("\nPress Enter to continue...")

    def view_statistics(self):
        """Display study statistics"""
        clear_screen()
        print("\n--- Study Statistics ---")
        stats = self.study_tracker.get_statistics()
        
        print(f"Total Study Sessions: {stats['total_sessions']}")
        print(f"Total Study Time: {stats['total_hours']:.2f} hours")
        print(f"Average Session Duration: {stats['avg_duration']:.2f} minutes")
        print(f"Most Studied Subject: {stats['most_studied_subject']}")
        
        input("\nPress Enter to continue...")

    def show_recommendations(self):
        """Show AI-powered study recommendations"""
        clear_screen()
        print("\n--- AI Study Recommendations ---")
        recommendations = self.recommender.get_recommendations()
        
        print("\nBased on your study patterns, here are some recommendations:\n")
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
        
        input("\nPress Enter to continue...")

    def view_priority_tasks(self):
        """Display high priority tasks"""
        clear_screen()
        print("\n--- High Priority Tasks ---")
        tasks = self.task_manager.get_priority_tasks()
        
        if not tasks:
            print("No high priority tasks found!")
        else:
            for task in tasks:
                status = "✓ Completed" if task['completed'] else "○ Pending"
                print(f"\nTitle: {task['title']}")
                print(f"Status: {status}")
                print(f"Due Date: {task['due_date'] or 'Not set'}")
                print("-" * 40)
        
        input("\nPress Enter to continue...")

    def delete_task(self):
        """Delete a task"""
        clear_screen()
        print("\n--- Delete Task ---")
        self.view_tasks()
        
        task_id = get_user_input("\nEnter task ID to delete: ")
        if self.task_manager.delete_task(task_id):
            print("\n✓ Task deleted successfully!")
        else:
            print("\n✗ Task not found!")
        
        input("\nPress Enter to continue...")

    def run(self):
        """Main application loop"""
        while self.running:
            clear_screen()
            print_banner()
            self.display_menu()
            
            choice = get_user_input("\nEnter your choice (1-9): ")
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.start_study_session()
            elif choice == "5":
                self.view_statistics()
            elif choice == "6":
                self.show_recommendations()
            elif choice == "7":
                self.view_priority_tasks()
            elif choice == "8":
                self.delete_task()
            elif choice == "9":
                print("\nThank you for using Smart Study Planner!")
                print("Keep studying smart! 📚")
                self.running = False
            else:
                print("\n✗ Invalid choice! Please try again.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    print("\nInitializing Smart Study Planner...")
    app = SmartStudyPlanner()
    app.run()
