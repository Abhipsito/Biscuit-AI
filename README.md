Biscuit: An Interactive AI Puppy Companion

Video Demo: https://youtu.be/BJYQ-uuP_nE?si=m2wZ4dPaI7CGRoeR

Project Description
Biscuit is a terminal-based AI companion designed to act like a real pet. Built as a 1-year-old Indian puppy who has a fluffy brown coat with white spots, he has an energetic and loyal personality to provide fun and emotional support. He responds to texts using dog logics, puppy emojis, barks and reactions like tail wagging.

This project connects a large language model with local file storage. By running an open-source AI model locally on a personal machine, Biscuit adapts his mood based on what you say. If you praise him, Biscuit gets happy and wags his tail. If you scold him, he expresses sadness and tries to be extra cute. This creates a highly responsive virtual pet experience inside the terminal window.

Key Features
Memory Tracking: Biscuit remembers the conversation by reading from and writing to a local storage file so he never loses context.

Mood Shifts: A custom system prompt allows Biscuit to dynamically react to positive or negative user sentiment.

Input Cleaning: Background utility functions clean, trim and normalize user inputs to keep the main chat loop from crashing.

Code Structure
The application relies on a modular architecture, breaking separate tasks into dedicated Python functions:

main(): The primary entry point. It handles user greeting sequences, asks for your name and starts the core loop.

core(user): Manages the chat environment. It tracks payload sizes to prevent token overflow by capping the memory at the most recent forty messages, calls the Ollama backend and appends replies.

load_mem() and save_mem(history): Handles native file system interactions. These functions verify the JSON data store, decode tracking logs, handle errors and save data to the disk.

ext(msg): A validation filter that checks user strings against exit phrases like bye, quit or exit. It returns a true or false flag to close the program loop.

neat(name): A string-processing function that cleans up nicknames by stripping trailing spaces and forcing capital casing.

clean(msg): An input utility that formats chat text to lowercase and removes white spaces so exit phrases match perfectly.

Tech Stack
This project uses Python 3 to script the logic flow and file processing. It uses the Ollama API wrapper to communicate between the Python script and the local machine intelligence engine. The Pytest framework verifies code execution safety across the string and boolean functions. Finally, the built-in JSON and OS libraries manage the conversation memory trees.

Setup Instructions
Download and install the core Ollama application engine from their official website.

Open a terminal shell and run the command ollama run llama3.2:3b to download the model.

Install the Python package requirements by running pip install -r requirements.txt.

Launch the application script to begin chatting by running python project.py.


Thank you to David J. Malan sir and the entire CS50 staff for providing such a fantastic course and learning experience. Building Biscuit has been an incredible way to finish this coding journey.
