"""
Utility Functions Module
Provides helper functions for the application
"""

import os
import sys

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print application banner"""
    banner = """
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║         📚 SMART STUDY PLANNER 📚              ║
    ║                                                   ║
    ║        AI-Powered Learning Assistant              ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
    """
    print(banner)

def get_user_input(prompt):
    """Get user input with a prompt"""
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\n\nExiting...")
        sys.exit(0)

def format_duration(minutes):
    """Format duration in minutes to hours and minutes"""
    if minutes < 60:
        return f"{minutes} minutes"
    else:
        hours = minutes // 60
        mins = minutes % 60
        if mins == 0:
            return f"{hours} hour{'s' if hours > 1 else ''}"
        else:
            return f"{hours} hour{'s' if hours > 1 else ''} {mins} minutes"

def validate_date(date_string):
    """Validate date string in YYYY-MM-DD format"""
    if not date_string:
        return True
    
    try:
        from datetime import datetime
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def print_success(message):
    """Print success message"""
    print(f"\n✓ {message}")

def print_error(message):
    """Print error message"""
    print(f"\n✗ {message}")

def print_info(message):
    """Print info message"""
    print(f"\nℹ {message}")

def confirm_action(prompt):
    """Ask user to confirm an action"""
    response = get_user_input(f"{prompt} (y/n): ").lower()
    return response in ['y', 'yes']

def print_separator(char='-', length=50):
    """Print a separator line"""
    print(char * length)
