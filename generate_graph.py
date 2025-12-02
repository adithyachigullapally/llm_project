from graph.multi_agent_graph import get_multi_agent_app

def generate_image():
    print("🎨 Generating Graph Image...")
    
    # 1. Load your new Hybrid Graph
    app = get_multi_agent_app()
    
    # 2. Draw it
    try:
        # This contacts Mermaid.ink to render the image
        png_data = app.get_graph().draw_mermaid_png()
        
        # 3. Save to file
        with open("hybrid_graph.png", "wb") as f:
            f.write(png_data)
            
        print("✅ Success! Image saved as 'hybrid_graph.png'")
        
    except Exception as e:
        print(f"❌ Could not draw graph: {e}")
        print("Note: You need an active internet connection for this.")

if __name__ == "__main__":
    generate_image()