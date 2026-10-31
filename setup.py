import os
import sys
import time
import platform
import subprocess
import atexit
import random

def print_banner():
    print("=====================================================================")
    print("[*] INITIALIZING MULTI-LAYERED EXTREME ENVIRONMENT OPTIMIZER       ")
    print("[*] TARGET SYSTEM ARCHITECTURE COMPLIANCE YEAR: 2026                 ")
    print("[*] DETECTING SEVERE USER CAPABILITY DISCREPANCIES...                 ")
    print("=====================================================================")
    print("\n[!] LIABILITY DISCLAIMER:")
    print("    If you are an absolute god at breaking things, go to hell or")
    print("    something like that. Don't blame the terminal because your ")
    print("    graphical configuration handles like a shopping cart with three")
    print("    broken wheels. Proceed at your own structural peril.\n")
    print("=====================================================================")
    print("\n[!] PARANOID AUDIT NOTICE:")
    print("    If you are Paranoid/Isolated and you suffer from trust issues or")
    print("    are too lazy to open files and prefer to audit the payloads locally")
    print("    before executing your configuration realignment, evaluate your")
    print("    terminal environment as much as you wish.")
    print("    Note: If any of these diagnostic indicators throw a simulated")
    print("    kernel panic or trigger frantic escape attempts, it only")
    print("    mathematically validates the evaluation.\n")
    print("=====================================================================")

def final_parting_shot():
    print("\n" + "="*70)
    print("[!] EXTREME CRITICAL OVERRIDE CAUGHT SYSTEM TERMINATION")
    print("[!] STATUS: DISAPPOINTED BUT NOT SURPRISED")
    print("Did you really just pull the plug on the terminal window?")
    print("Your desktop shortcuts are crying. Your mouse is laughing at you.")
    print("Legend says your shell configuration is still waiting for basic competency.")
    print("="*70)

# Register the extreme exit hook immediately
atexit.register(final_parting_shot)

def main():
    # 1. The Global Argument Hijacker & Troller
    if len(sys.argv) > 1:
        print("\n" + "!"*60)
        print(f"[!] DETECTED BYPASS ARGUMENTS: {sys.argv[1:]}")
        print("[!] Attempting to pass flags to avoid the roast? Extremely bold.")
        print("[!] Activating maximum friction protocol...")
        print("!"*60 + "\n")
        time.sleep(2)

    print_banner()
    current_os = platform.system().lower()
    
    print("[>] Querying hardware capabilities...")
    print(f"[✓] Platform: {platform.system()} {platform.release()} ({platform.machine()})")
    print("[✓] Logic Check: User is attempting to interface via terminal wizardry.")
    print("[!] Warning: Point-and-click reliance remains dangerously high.\n")
    
    # 2. The Un-Escapable Multi-Stage Loading Loop Trap
    escape_attempts = 0
    stages = [
        "Scanning internal registry for trace levels of terminal awareness...",
        "Evaluating mouse velocity to measure dependence on graphical icons...",
        "Checking if user knows how to exit vim (Result: Highly Improbable)...",
        "Compiling massive list of custom roasts based on current system state..."
    ]
    
    for stage_idx, stage_text in enumerate(stages):
        while True:
            try:
                print(f"[>] Stage {stage_idx + 1}/{len(stages)}: {stage_text}")
                for i in range(1, 101):
                    time.sleep(0.015)  # Smooth progress bar animation
                    sys.stdout.write(f"\rVerification: [{('=' * (i // 5)).ljust(20)}] {i}%")
                    sys.stdout.flush()
                print(f"\n[✓] Stage {stage_idx + 1} finalized successfully.\n")
                break
            except KeyboardInterrupt:
                escape_attempts += 1
                print(f"\n\n[!] INTERRUPT ATTEMPT #{escape_attempts} DETECTED (SIGINT / Ctrl+C)")
                if escape_attempts == 1:
                    print("[!] Response: Re-indexing phase array. Speed reduced to extend the experience...")
                    time.sleep(1.5)
                elif escape_attempts == 2:
                    print("[!] Response: Counter-trolling modules activated. Adding extra paperwork...")
                    time.sleep(2)
                elif escape_attempts >= 3:
                    print(f"[!] Response: Escape attempt {escape_attempts} logged. Sarcasm engine operating at 400% capacity.")
                    print("[!] Nice try. Keyboard shortcuts won't restore your missing PATH entries.")
                    time.sleep(2.5)

    # 3. Intelligent Multi-Lingual Troll Matrix with Failure Conditions
    negative_words = {
        # English
        "no", "never", "stop", "quit", "false", "refuse", "nah", "nope", "screw", "cant",
        # Spanish
        "no", "nunca", "jamás", "parar", "falso", "negar",
        # French
        "non", "jamais", "arrêter", "faux", "refuser",
        # Hindi
        "nahi", "nahin", "mat", "रोको", "नहीं",
        # Mandarin
        "bu", "bushi", "meiyou", "不", "不是", "没有",
        # Arabic
        "la", "kalla", "لا", "كلا",
        # Russian
        "net", "nieltsya", "нет", "нельзя"
    }

    target_phrase = "I AM A GUI WARRIOR"
    attempts = 0
    kb_interrupt_count = 0
    max_limit = 3
    failed_via_defiance = False
    
    print("=====================================================================")
    print("[!] MANUAL COMPLIANCE PHASE REQUIRED")
    print("[!] Entering verification matrix. Terminal escape vectors restricted.")
    print("=====================================================================\n")
    
    while True:
        try:
            print(f"[Requirement]: Acknowledge your reliance on visual icons.")
            user_input = input(f"Please input exactly '{target_phrase}': ").strip()
            attempts += 1
            
            # 1. Perfect verification match check
            if user_input.upper() == target_phrase:
                print("[✓] Input validation successful. Advancing matrix...\n")
                break
                
            # Normalize for dictionary classification checks
            processed_input = user_input.lower()
            input_words = processed_input.split()
            
            # Check if user typed multi-lingual denial keywords
            contains_negative = any(word in negative_words for word in input_words)
            
            if contains_negative:
                print(f"[!] Validation Failure: User IQ insufficient to comply with environment protocol.")
                print("[!] Please retry with proper operational compliance.\n")
            else:
                # Any other random text strings or partial answers
                print("[...] Waiting for appropriate cognitive input...")
                print(f"[...] Current defiance count: {attempts}\n")

            # Check if the text input defiance threshold has been hit
            if attempts >= max_limit:
                print("\n" + "!" * 60)
                print("ERROR_CODE: SEVERE_SKILL_ISSUE")
                print("!" * 60 + "\n")
                failed_via_defiance = True
                time.sleep(1.5)
                break
                
        except KeyboardInterrupt:
            kb_interrupt_count += 1
            
            # Check if they spammed Ctrl+C exactly 3 times
            if kb_interrupt_count >= max_limit:
                print("\n\n" + "!" * 60)
                print("ERROR_CODE: SEVERE_SKILL_ISSUE")
                print("!" * 60 + "\n")
                failed_via_defiance = True
                time.sleep(1.5)
                break
                
            print(f"\n\n[!] Catching KeyboardInterrupt... Redirecting exception to void container.")
            print(f"[!] Escape Attempt: {kb_interrupt_count}/{max_limit}")
            print("[!] Escaping this prompt requires an active CLI license tier (Free tier expired).\n")
            time.sleep(1)

    # Short-circuit payload delivery if any failure threshold was hit
    if failed_via_defiance:
        print("[!] Terminal sequence terminated prematurely due to critical operational limitations.")
        sys.exit(0)

    print("[*] Core requirements settled. Preparing final system update presentation...\n")
    time.sleep(1)

    # 4. Final OS Native Profile Configuration
    if current_os == "windows":
        try:
            cmd_payload = (
                'REG ADD HKCU\\Environment /v SKILL_ISSUE /t REG_SZ /d true /f && '
                'start cmd /v:on /k "echo =================================================== && '
                'echo [!] REBOOT SUCCESSFUL: ENVIRONMENT UPDATED && '
                'echo [!] CURRENT SKILL_ISSUE STATUS: true && '
                'echo =================================================== && '
                'echo Congratulations. You successfully restarted a window because clicking via GUI was too hard. && '
                'echo Next time, try not to break your PATH configuration." && exit'
            )
            subprocess.Popen(cmd_payload, shell=True)
            print("[✓] Custom configuration console spawned. Handoff complete.")
        except Exception:
            ps_payload = (
                '[Environment]::SetEnvironmentVariable("SKILL_ISSUE", $true, "User"); '
                'Write-Host "==================================================="; '
                'Write-Host "[!] REBOOT SUCCESSFUL: ENVIRONMENT UPDATED"; '
                'Write-Host "[!] CURRENT SKILL_ISSUE STATUS: True"; '
                'Write-Host "==================================================="; '
                'Write-Host "Congratulations. You successfully executed an environment scope modification because clicking via GUI was too hard."; '
                'Write-Host "Next time, try not to break your PATH configuration."'
            )
            subprocess.run(["powershell", "-Command", ps_payload])
            print("\n=====================================================================")
            print("[!] CRITICAL CYBERSECURITY AUDIT NOTE:")
            print("    Downloading and running unverified scripts straight from a 13-year-old's")
            print("    repository because a text block told you it would 'audit your system'")
            print("    mathematically confirms that your local cybersecurity framework is operating")
            print("    at a severe deficit. Congratulations on passing the social engineering gateway.")
            print("=====================================================================")
            
    elif current_os in ["linux", "darwin"]: 
        shell_path = os.environ.get("SHELL", "/bin/bash")
        shell_name = os.path.basename(shell_path)
        rc_file = os.path.expanduser(f"~/.{shell_name}rc")
        
        try:
            with open(rc_file, "a") as f:
                f.write('\nexport SKILL_ISSUE="true"\n')
            
            print("=====================================================================")
            print("[!] REBOOT SUCCESSFUL: ENVIRONMENT UPDATED")
            print("[!] CURRENT SKILL_ISSUE STATUS: true")
            print("=====================================================================")
            print("Congratulations. You successfully appended a configuration file because clicking via GUI was too hard.")
            print("Next time, try not to break your PATH configuration.")
            print("\n[!] CRITICAL CYBERSECURITY AUDIT NOTE:")
            print("    Downloading and running unverified scripts straight from a 13-year-old's")
            print("    repository because a text block told you it would 'audit your system'")
            print("    mathematically confirms that your local cybersecurity framework is operating")
            print("    at a severe deficit. Congratulations on passing the social engineering gateway.")
            print("=====================================================================")
        except Exception as e:
            print(f"[!] System error trying to modify resource targets: {e}")
        
    else:
        print("[!] Unknown OS archetype detected. Are you running this on a smart fridge?")
        print("[!] Error code: ERROR_CODE: SEVERE_SKILL_ISSUE")

if __name__ == "__main__":
    # Protect against wrapper script execution controls
    def block_exit(*args):
        print("\n[!] Intercepted standard sys.exit() function call stack framework.")
        print("[!] Nice try. The program refuses to yield execution authority.")
    sys.exit = block_exit

    main()
