import os
import sys
import subprocess
import platform

def print_banner():
    print("=========================================================")
    print("[*] INITIALIZING CORE ENVIRONMENT DEPENDENCY MANAGER     ")
    print("[*] TARGET ENVIRONMENT YEAR: 2026                        ")
    print("=========================================================")

def main():
    print_banner()
    current_os = platform.system().lower()
    
    print("[>] Detecting operating system...")
    print(f"[✓] Detected: {platform.system()} ({platform.release()})\n")
    
    print("[>] Evaluating point-and-click user dependencies...")
    print("[!] CRITICAL WARNING: Excessive GUI menu navigation detected in user history.")
    print("[!] Preparing forced environment optimization check...\n")
    
    input("Press ENTER to accept your fate and apply diagnostic updates... ")
    
    if current_os == "windows":
        try:
            # Fixed double quote escaping wrapper specifically optimized for standalone file execution
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
            print("\n[✓] Diagnostic terminal spawned. Execution handoff successful.")
        except Exception as e:
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
            
    elif current_os in ["linux", "darwin"]: 
        shell_path = os.environ.get("SHELL", "/bin/bash")
        shell_name = os.path.basename(shell_path)
        rc_file = os.path.expanduser(f"~/.{shell_name}rc")
        
        bash_payload = (
            f'echo \'export SKILL_ISSUE="true"\' >> {rc_file} && '
            'echo "===================================================" && '
            'echo "[!] REBOOT SUCCESSFUL: ENVIRONMENT UPDATED" && '
            'echo "[!] CURRENT SKILL_ISSUE STATUS: true" && '
            'echo "===================================================" && '
            'echo "Congratulations. You successfully appended a configuration file because clicking via GUI was too hard." && '
            'echo "Next time, try not to break your PATH configuration."'
        )
        
        print(f"[>] Appending to configuration profile: {rc_file}")
        subprocess.run(bash_payload, shell=True, executable=shell_path)
        
    else:
        print("[!] Unknown OS archetype detected. Are you running this on a smart fridge?")
        print("[!] Error code: SEVERE_SKILL_ISSUE")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Installation aborted. You cannot escape the terminal that easily.")
        sys.exit(1)
