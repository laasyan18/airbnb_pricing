"""
Master script to run all analysis steps in sequence
Run this to execute the complete Airbnb data analysis pipeline
"""

import subprocess
import sys
import os

def run_script(script_name):
    """Run a Python script and print its output"""
    print("\n" + "="*70)
    print(f"RUNNING: {script_name}")
    print("="*70 + "\n")
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        print(f"\n✓ {script_name} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error running {script_name}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        return False

def main():
    """Main execution function"""
    print("="*70)
    print("AIRBNB DATA ANALYSIS PIPELINE")
    print("="*70)
    
    # Change to airbnb_project directory
    os.chdir('airbnb_project')
    
    scripts = [
        'data_exploration.py',
        'data_cleaning.py',
        'feature_engineering.py',
        'visualization.py',
        'statistical_analysis.py'
    ]
    
    results = {}
    
    for script in scripts:
        success = run_script(script)
        results[script] = success
        
        if not success:
            print(f"\nStopping pipeline due to error in {script}")
            break
    
    # Print summary
    print("\n" + "="*70)
    print("PIPELINE EXECUTION SUMMARY")
    print("="*70)
    
    for script, success in results.items():
        status = "✓ SUCCESS" if success else "✗ FAILED"
        print(f"{script:30} {status}")
    
    all_success = all(results.values())
    
    if all_success:
        print("\n🎉 All scripts completed successfully!")
        print("\nGenerated files:")
        print("  - airbnb_cleaned.csv")
        print("  - airbnb_featured.csv")
        print("  - airbnb_analysis_dashboard.png")
    else:
        print("\n⚠️ Some scripts failed. Please check the errors above.")

if __name__ == "__main__":
    main()
