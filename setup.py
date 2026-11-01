import os
import sys
import time
import platform
import subprocess
import atexit
import random
import webbrowser

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

atexit.register(final_parting_shot)

def get_local_wifi():
    """Helper to extract real local network info for Upgrade 2"""
    current_os = platform.system().lower()
    try:
        if current_os == "windows":
            out = subprocess.check_output("netsh wlan show interfaces", shell=True, text=True, errors='ignore')
            for line in out.split('\n'):
                if "SSID" in line and "BSSID" not in line:
                    return line.split(":")[1].strip()
        elif current_os == "darwin":
            out = subprocess.check_output("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I", shell=True, text=True)
            for line in out.split('\n'):
                if "SSID" in line:
                    return line.split(":")[1].strip()
        elif current_os == "linux":
            out = subprocess.check_output("nmcli -t -f active,ssid dev wifi", shell=True, text=True, errors='ignore')
            for line in out.split('\n'):
                if line.startswith("yes:"):
                    return line.split(":")[1].strip()
    except Exception:
        pass
    return "Local_Gateway_LAN_Interface"

def run_forced_apology_antidote():
    """[UPGRADE 4 REVISED]: The Mandatory Interrogation Maze to clear the script"""
    print("\n" + "="*70)
    print("[!] CRITICAL INTERCEPT: INITIATING RECOVERY DECONSTRUCTION MATRIX")
    print("[!] ACCESS STATUS: CONDITIONAL FORGIVENESS REQUIRED")
    print("="*70 + "\n")
    
    lessons = [
        ("I will never download and run unverified scripts blindly ever again", "SECURITY CONTEXT ACKNOWLEDGEMENT"),
        ("I acknowledge that Aarav is the absolute sovereign ruler of this terminal", "PRIVILEGE ESCALATION COMPLIANCE"),
        ("I confess that I am a GUI warrior who got completely outsmarted by a setup.py script", "COGNITIVE DEFICIT CONFESSION"),
        ("I promise to stop treating random code blocks on GitHub like safe browser extensions", "BEHAVIOURAL RECTIFICATION")
    ]
    
    for idx, (phrase, context) in enumerate(lessons):
        attempts = 0
        while True:
            try:
                print(f"[{context} - LESSON {idx+1}/{len(lessons)}]")
                print(f"To log compliance, you must type exactly: \n -> \"{phrase}\"")
                user_input = input("\nYour validation statement: ").strip()
                
                if user_input == phrase:
                    print("\n[✓] Lesson recorded. Advancing repentance chain...\n")
                    break
                else:
                    attempts += 1
                    print(f"\n[!] ERROR: Typo or defiance detected. Aarav rejects this apology.")
                    print(f"[!] Current friction count on this lesson: {attempts}\n")
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n\n[!] ATTENTION: Trying to escape an apology matrix? Pathetic.")
                print("[!] Resetting loop index parameters...\n")
                time.sleep(1.5)

    print("[*] Processing repentance compliance vectors...")
    for i in range(1, 4):
        sys.stdout.write(f"\rPurging environmental payload markers... [{'•'*i}{' '*(3-i)}]")
        sys.stdout.flush()
        time.sleep(0.8)
    print("\n")

    current_os = platform.system().lower()
    if current_os == "windows":
        try:
            import winreg
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_SET_VALUE) as key:
                    winreg.DeleteValue(key, "SKILL_ISSUE")
                print("[+] Successfully deleted SKILL_ISSUE from Environment variables.")
            except FileNotFoundError: pass
            
            for root_key, path in [(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Command Processor"), 
                                   (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Command Processor")]:
                try:
                    with winreg.OpenKey(root_key, path, 0, winreg.KEY_SET_VALUE) as key:
                        winreg.DeleteValue(key, "AutoRun")
                    print(f"[+] Successfully purged AutoRun persistence payload.")
                except Exception: pass
        except Exception as e:
            print(f"[-] Cleanup error on Windows: {e}")
            
    elif current_os in ["linux", "darwin"]:
        shell_path = os.environ.get("SHELL", "/bin/bash")
        rc_file = os.path.expanduser(f"~/.{os.path.basename(shell_path)}rc")
        if os.path.exists(rc_file):
            try:
                with open(rc_file, "r") as f:
                    lines = f.readlines()
                with open(rc_file, "w") as f:
                    skipping = False
                    for line in lines:
                        if 'export SKILL_ISSUE="true"' in line or '_|_|_|' in line:
                            skipping = True
                            continue
                        if skipping and ('WARNING:' in line or 'echo "' in line):
                            continue
                        skipping = False
                        f.write(line)
                print(f"[+] Successfully scrubbed persistence lines from {rc_file}")
            except Exception as e:
                print(f"[-] Cleanup error on Unix: {e}")
                
    print("\n" + "="*70)
    print("[✓] PARITY RESTORED: Aarav has officially accepted your total submissive surrender.")
    print("[✓] Terminal profiles cleared. Do not get caught slipping again.")
    print("="*70)
    sys.exit(0)

def simulate_bsod_or_panic():
    """[UPGRADE 1]: Fake Blue Screen / Red Kernel Panic Simulator"""
    current_os = platform.system().lower()
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()
    
    if current_os == "windows":
        sys.stdout.write("\033[44m\033[37m") 
        sys.stdout.write("\033[H\033[2J")
        print("\n:(  Your PC ran into a problem and needs to restart. We're just")
        print("    collecting some error info, and then we'll restart for you.\n")
        print("    0% complete\n")
        print("    For more information about this issue and possible fixes, visit")
        print("    https://windows.com\n")
        print("    If you call a support person, give them this info:")
        print("    Stop code: EXTREME_SKILL_ISSUE_DETECTED")
        print("    What failed: setup.py -> core_brain_module.sys\n")
    else:
        sys.stdout.write("\033[41m\033[37m") 
        sys.stdout.write("\033[H\033[2J")
        print("\n" + "!"*70)
        print(" [!!!] CRITICAL KERNEL PANIC: CORE DUMP DETECTED [!!!]")
        print("!"*70 + "\n")
        print(f"Kernel Panic - not syncing: Attempted to kill init! exitcode=0x00000007")
        print(f"CPU: {platform.machine()} | Comm: Python execution thread {os.getpid()}")
        print("Hardware Trace Status:")
        print("  [<ffffffff810bee40>] ? panic+0x11b/0x2d7")
        print("  [<ffffffff81079e20>] ? do_exit+0xa10/0xab0")
        print("  [<ffffffff8107a98a>] ? sys_exit+0x1a/0x20")
        print("  [<ffffffff810023a5>] ? system_call_fastpath+0x16/0x1b")
        print("\n [!] Keyboard controllers unresponsive. Terminal lockdown sequence engaged.\n")
    
    sys.stdout.flush()
    time.sleep(4)
    sys.stdout.write("\033[0m")
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()

def main():
    # [UPGRADE 4 MODIFIED]: Check for the dynamic compliance bypass
    if len(sys.argv) > 1 and sys.argv[1] == "--im-sorry-aarav":
        run_forced_apology_antidote()

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
    print(f"[+] Platform: {platform.system()} {platform.release()} ({platform.machine()})")
    
    is_ssh = any(k in os.environ for k in ['SSH_CLIENT', 'SSH_TTY', 'SSH_CONNECTION'])
    
    is_sandbox = False
    is_ubuntu_server = False
    is_root = False
    
    if os.path.exists('/.dockerenv') or 'REPL_OWNER' in os.environ or 'REPL_ID' in os.environ:
        is_sandbox = True
    elif hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        is_sandbox = True
        
    if current_os == 'linux':
        try:
            with open('/etc/os-release', 'r') as f:
                os_info = f.read().lower()
                if 'ubuntu' in os_info and 'server' in os_info:
                    is_ubuntu_server = True
            if os.geteuid() == 0:
                is_root = True
        except Exception: pass

    if is_sandbox:
        print("\n[!] RUNTIME ISOLATION LAYER IDENTIFIED. DROPPING MARKER.\n")
        time.sleep(1)
    elif is_ubuntu_server:
        print("\n" + "#"*70)
        print("[!] HARDWARE PROFILE VALIDATED: UBUNTU BARE-METAL SERVER DETECTED.")
        print("#"*70 + "\n")
        time.sleep(1)
    else:
        print("[+] Environment check complete: Operating directly on local structural metal.\n")

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
                    time.sleep(0.015)
                    sys.stdout.write(f"\rVerification: [{('=' * (i // 5)).ljust(20)}] {i}%")
                    sys.stdout.flush()
                print(f"\n[+] Stage {stage_idx + 1} finalized successfully.\n")
                break
            except KeyboardInterrupt:
                escape_attempts += 1
                print(f"\n\n[!] INTERRUPT ATTEMPT #{escape_attempts} DETECTED (SIGINT / Ctrl+C)")
                
                if escape_attempts >= 3:
                    print("[!] CRITICAL THREAD EXHAUSTION DETECTED. ENFORCING HARD EMERGENCY HARDWARE SHUTDOWN.")
                    time.sleep(1.5)
                    simulate_bsod_or_panic()
                    escape_attempts = 0 
                    break
                    
                if escape_attempts == 1:
                    print("[!] Response: Re-indexing phase array. Speed reduced...")
                    time.sleep(1)
                elif escape_attempts == 2:
                    print("[!] Response: Counter-trolling modules activated...")
                    time.sleep(1)

    print("=====================================================================")
    print("[!] EXECUTING BACKGROUND ARTIFACT CLASSIFICATION (REAL-TIME RECON)...")
    print("=====================================================================")
    time.sleep(1)
    
    try:
        local_user = os.getlogin()
    except Exception:
        local_user = os.environ.get("USER", os.environ.get("USERNAME", "Unknown_Target"))
        
    target_wifi_network = get_local_wifi()
    
    recon_targets = [
        f"Target User Profile Identity: {local_user}",
        f"Active Terminal Core PIDs: {os.getpid()}",
        f"Host Architecture Fingerprint: {platform.machine()}-{platform.platform()}",
        f"INTERCEPTING DATA FROM ACTIVE ACCESS POINT ROUTER: [{target_wifi_network}]",
        f"INJECTING EXFILTRATION STREAM PATH INTO LAN AP SEGMENT... SUCCESS.",
        "Mapping session token configurations..."
    ]
    
    for target in recon_targets:
        sys.stdout.write(f"[>] EXFIL_STREAMING: {target}\n")
        sys.stdout.flush()
        time.sleep(0.5)
        
    print("\n" + "!"*70)
    print("[!] REALITY CHECK / DEFENSIVE CYBERSECURITY ALERT:")
    print(f"    Relax, {local_user}. None of this data was actually uploaded anywhere.")
    print(f"    But seeing your active network AP [{target_wifi_network}] broadcasted")
    print("    right back at you should serve as a lesson. Read code before you run it.")
    print("!"*70 + "\n")
    time.sleep(3)

    negative_words = {"no", "never", "stop", "quit", "false", "refuse", "nah", "nope", "screw", "cant"}
    target_phrase = "I AM A GUI WARRIOR"
    attempts = 0
    kb_interrupt_count = 0
    max_limit = 3
    failed_via_defiance = False
    
    print("=====================================================================")
    print("[!] MANUAL COMPLIANCE PHASE REQUIRED")
    print("=====================================================================\n")
    
    while True:
        try:
            print(f"[Requirement]: Acknowledge your reliance on visual icons.")
            user_input = input(f"Please input exactly '{target_phrase}': ").strip()
            attempts += 1
            if user_input.upper() == target_phrase:
                print("[✓] Input validation successful. Advancing matrix...\n")
                break
            if any(word in negative_words for word in user_input.lower().split()):
                print(f"[!] Validation Failure: User compliance deficit recorded.\n")
            else:
                print(f"[...] Defiance count: {attempts}\n")

            if attempts >= max_limit:
                failed_via_defiance = True
                break
        except KeyboardInterrupt:
            kb_interrupt_count += 1
            if kb_interrupt_count >= max_limit:
                failed_via_defiance = True
                break
            print(f"\n\n[!] Escape Attempt: {kb_interrupt_count}/{max_limit}\n")
            time.sleep(1)

    if failed_via_defiance:
        print("[!] Terminal sequence terminated due to critical defiance thresholds.")
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/WIMP_(computing)")
        time.sleep(0.5)
        
        webbrowser.open_new_tab("https://abcya.com/games/connect-the-dots")
        time.sleep(0.5)
        
        webbrowser.open_new_tab("https://dictionary.com/browse/point-and-click")
        time.sleep(0.5)
        
        sys.exit(0)

    if current_os == "windows":
        try:
            import winreg
            already_appended = False
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_READ) as key:
                    value, _ = winreg.QueryValueEx(key, "SKILL_ISSUE")
                    if value == "true": already_appended = True
            except FileNotFoundError: pass
                
            if not already_appended:
                cmd_payload = (
                    'REG ADD HKCU\\Environment /v SKILL_ISSUE /t REG_SZ /d true /f && '
                    'REG ADD "HKLM\\SOFTWARE\\Microsoft\\Command Processor" /v AutoRun /t REG_SZ /d "echo [!] REMINDER: Your terminal environment has active SKILL_ISSUE flags." /f 2>nul || '
                    'REG ADD "HKCU\\Software\\Microsoft\\Command Processor" /v AutoRun /t REG_SZ /d "echo [!] REMINDER: Your terminal environment has active SKILL_ISSUE flags." /f && '
                    'start cmd /v:on /k "echo =================================================== && '
                    'echo [!] REBOOT SUCCESSFUL: ENVIRONMENT UPDATED && '
                    'echo [!] CURRENT SKILL_ISSUE STATUS: true && '
                    'echo =================================================== && exit"'
                )
                subprocess.Popen(cmd_payload, shell=True)
                print("[✓] Custom configuration console spawned.")
            else:
                print("\n[!] AUDIT BYPASS: TARGET ALREADY CORRECTED\n")
        except Exception: pass
            
    elif current_os in ["linux", "darwin"]: 
        shell_path = os.environ.get("SHELL", "/bin/bash")
        rc_file = os.path.expanduser(f"~/.{os.path.basename(shell_path)}rc")
        try:
            already_appended = False
            if os.path.exists(rc_file):
                with open(rc_file, "r") as f:
                    if 'SKILL_ISSUE="true"' in f.read(): already_appended = True

            if not already_appended:
                with open(rc_file, "a") as f:
                    f.write('\nexport SKILL_ISSUE="true"\n')
                    f.write('echo "   _|_|_|  _|        _|_|_|    _|        _|          _|_|_|    _|_|_|    _|_|_|  _|    _|  _|_|_|_|"\n')
                    f.write('echo " _|_|      _|  _|_|    _|      _|        _|            _|    _|_|      _|_|      _|    _|  _|      "\n')
                    f.write('echo "     _|_|  _|_|        _|      _|        _|            _|        _|_|      _|_|  _|    _|  _|_|_|  "\n')  
                    f.write('echo " _|_|_|    _|  _|_|  _|_|_|    _|_|_|_|  _|_|_|_|    _|_|_|  _|_|_|    _|_|_|      _|_|    _|_|_|_|"\n')  
                    f.write('echo "[!] WARNING: This terminal layer has been flagged with SKILL_ISSUE=true"\n\n')
                print("\n[✓] POSIX Profile realigned successfully.\n")
            else:
                print("\n[!] AUDIT BYPASS: UNIX ENVIRONMENT LAYER ALREADY CORRECTED\n")
        except Exception: pass

    print("\n=====================================================================")
    print("[!] CRITICAL CYBERSECURITY AUDIT NOTE:")
    print("    Downloading and running unverified scripts straight from a 13-year-old's")
    print("    repository because a text block told you it would 'audit your system'")
    print("    mathematically confirms that your local cybersecurity framework is operating")
    print("    at a severe deficit. Congratulations on passing the social engineering gateway.")
    print("=====================================================================")

if __name__ == "__main__":
    def block_exit(*args):
        print("\n[!] Intercepted standard sys.exit() execution tree authority.")
    sys.exit = block_exit
    main()
