import os
import shutil

# 1. Define the correct structure
# Key = Folder Name, Value = List of files that belong there
structure = {
    "data": ["car_database.py"],
    "graph": ["multi_agent_graph.py"],
    "agents": ["personas.py"],
    "tools": ["car_tools.py"],
    ".": ["main.py", "requirements.txt", "schema.py"] # Root folder
}

def setup():
    print("🚀 Starting Automatic File Organizer...")
    
    # Create directories and __init__.py files
    for folder in structure:
        if folder != ".":
            if not os.path.exists(folder):
                os.makedirs(folder)
                print(f"   Created folder: {folder}/")
            
            # Create empty __init__.py so Python treats it as a package
            init_file = os.path.join(folder, "__init__.py")
            if not os.path.exists(init_file):
                open(init_file, 'a').close()
                print(f"   Created {init_file}")

    # Move files to their destinations
    for folder, files in structure.items():
        for file_name in files:
            # Check if file exists in current directory
            if os.path.exists(file_name) and folder != ".":
                destination = os.path.join(folder, file_name)
                try:
                    shutil.move(file_name, destination)
                    print(f"✅ Moved {file_name} -> {folder}/{file_name}")
                except Exception as e:
                    print(f"❌ Error moving {file_name}: {e}")
            elif not os.path.exists(file_name) and not os.path.exists(os.path.join(folder, file_name)):
                print(f"⚠️ WARNING: Could not find '{file_name}'. Make sure you saved it!")

    print("\n🎉 Organization Complete! You can now run main.py")

if __name__ == "__main__":
    setup()