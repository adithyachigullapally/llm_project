import os
import sys
import time
import pygame
import speech_recognition as sr
import numpy as np
import pyaudio
import uuid
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from graph.multi_agent_graph import get_multi_agent_app
from schema import ConversationState, Message

# Setup
load_dotenv(override=True)
client = OpenAI()
pygame.mixer.init()

# ==========================================
# SHARED: TEXT-TO-SPEECH (TTS)
# ==========================================
def speak_real_voice(text, enable_voice=True):
    """
    Plays audio using OpenAI Onyx voice.
    If enable_voice is False, it just prints the text.
    """
    print(f"\n🗣️  J.A.R.V.I.S: {text}")
    
    if not enable_voice:
        return # Exit if silent mode

    print("   (Speak LOUDLY to interrupt him...)")
    
    filename = f"response_{uuid.uuid4().hex[:8]}.mp3"
    speech_file_path = Path(__file__).parent / filename
    
    mic_stream = None
    p = None
    
    try:
        # Generate MP3
        response = client.audio.speech.create(
            model="tts-1",
            voice="onyx",
            input=text
        )
        response.stream_to_file(speech_file_path)
        
        # Play Audio
        chunk = 1024
        p = pyaudio.PyAudio()
        pygame.mixer.music.load(str(speech_file_path))
        pygame.mixer.music.play()
        
        # Interruption Logic
        mic_stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=chunk)
        start_time = time.time()
        
        while pygame.mixer.music.get_busy():
            # Grace period (prevents immediate self-interruption)
            if time.time() - start_time < 1.0:
                time.sleep(0.1)
                continue

            try:
                data = mic_stream.read(chunk, exception_on_overflow=False)
                audio_data = np.frombuffer(data, dtype=np.int16)
                volume = np.linalg.norm(audio_data)
                
                # === THRESHOLD SETTING ===
                # High threshold so background noise does not stop Jarvis.
                THRESHOLD = 160000 
                
                if volume > THRESHOLD:
                    print(f"\n🛑 Interrupted! (Vol: {int(volume)})")
                    pygame.mixer.music.stop()
                    break
            except:
                pass
            time.sleep(0.01)
            
    except Exception as e:
        print(f"Error in TTS: {e}")
    
    finally:
        if mic_stream: mic_stream.stop_stream(); mic_stream.close()
        if p: p.terminate()
        pygame.mixer.music.unload() 
        try:
            if os.path.exists(speech_file_path): os.remove(speech_file_path)
        except: pass

# ==========================================
# SHARED: SPEECH-TO-TEXT (STT)
# ==========================================
recognizer = sr.Recognizer()
def listen_mic():
    with sr.Microphone() as source:
        print("\n🎤 Listening... (Speak now)")
        # High threshold for your loud mic
        recognizer.energy_threshold = 4000 
        recognizer.dynamic_energy_threshold = False 
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("⏳ Processing...")
            text = recognizer.recognize_google(audio)
            print(f"👤 You: {text}")
            return text
        except:
            return None

# ==========================================
def process_and_respond(app, config, user_input, enable_voice):
    try:
        input_message = Message(role="user", content=user_input)
        
        # Send to LangGraph (Standard Invoke)
        # Note: If your graph still has 'interrupt_before=["booking_node"]', remove it in multi_agent_graph.py
        # Otherwise, this invoke will just pause silently if booking happens.
        # But since you asked to remove HITL logic here, we assume standard invoke.
        
        # Use stream to handle potentially multiple outputs (like parallel)
        final_response = ""
        for event in app.stream({"messages": [input_message]}, config=config):
            # We iterate through events until the end
            pass
            
        # Get Final State to read the answer
        snapshot = app.get_state(config)
        if snapshot.values['messages']:
            # Get the very last message
            last_msg = snapshot.values['messages'][-1]
            if last_msg.role == "assistant":
                ai_response = last_msg.content
                speak_real_voice(ai_response, enable_voice=enable_voice)
        
    except Exception as e:
        print(f"❌ Error: {e}")

# ==========================================
# MODES
# ==========================================
def run_voice_mode(app, config):
    print("\n🔹 STARTING VOICE MODE 🔹")
    speak_real_voice("Voice mode active. I am listening.", enable_voice=True)
    while True:
        user_input = listen_mic()
        if not user_input: continue
        if user_input.lower() in ["exit", "quit", "stop"]:
            speak_real_voice("Powering down, Sir.", enable_voice=True)
            break
        process_and_respond(app, config, user_input, enable_voice=True)

def run_text_mode(app, config):
    print("\n🔹 STARTING TEXT MODE 🔹")
    print("(Type 'quit' to exit)")
    while True:
        user_input = input("\n👤 You: ").strip()
        if not user_input: continue
        if user_input.lower() in ["exit", "quit", "stop"]:
            print("AI: Goodbye, Sir.")
            break
        process_and_respond(app, config, user_input, enable_voice=False)

def run_hybrid_mode(app, config):
    print("\n🔹 STARTING HYBRID MODE 🔹")
    print("(You Type -> Jarvis Speaks)")
    speak_real_voice("Hybrid mode initialized. Awaiting input.", enable_voice=True)
    while True:
        user_input = input("\n👤 You (Type): ").strip()
        if not user_input: continue
        if user_input.lower() in ["exit", "quit", "stop"]:
            speak_real_voice("Powering down.", enable_voice=True)
            break
        process_and_respond(app, config, user_input, enable_voice=True)

# ==========================================
# MAIN MENU
# ==========================================
if __name__ == "__main__":
    app = get_multi_agent_app()
    
    # Persistent Memory (Remembers you across restarts)
    # Uncomment the line below to enable long-term memory
    config = {"configurable": {"thread_id": "user_profile_001"}}
    
    while True:
        print("\n" + "="*50)
        print("🤖 J.A.R.V.I.S: SELECT PROTOCOL")
        print("="*50)
        print("1. 🗣️  Voice Mode   (Headphones Recommended)")
        print("2. ⌨️  Text Mode    (Silent Typing)")
        print("3. 🔀 Hybrid Mode  (You Type, AI Speaks)")
        print("4. ❌ Exit")
        
        choice = input("\nSelect Option (1-4): ").strip()
        
        if choice == "1":
            run_voice_mode(app, config)
        elif choice == "2":
            run_text_mode(app, config)
        elif choice == "3":
            run_hybrid_mode(app, config)
        elif choice == "4":
            print("System shutdown.")
            break
        else:
            print("Invalid protocol.")