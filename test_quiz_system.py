import urllib.request
import sys

def test_quiz_system():
    """Test the complete quiz system functionality"""
    base_url = "http://127.0.0.1:8000"
    
    tests = [
        {
            "name": "Quiz Listing Page",
            "url": f"{base_url}/tests",
            "expected": ["Knowledge Checks", "Astronomy 101", "Quantum Physics", "Molecular Biology"]
        },
        {
            "name": "Quiz Taking Page - Astronomy",
            "url": f"{base_url}/tests/1",
            "expected": ["Which planet is known as the Red Planet?", "Start Quiz", "Submit Quiz"]
        },
        {
            "name": "Quiz Taking Page - Quantum Physics",
            "url": f"{base_url}/tests/2",
            "expected": ["wave-particle duality", "Submit Quiz"]
        },
        {
            "name": "Quiz Listing - Chemistry Basics",
            "url": f"{base_url}/tests",
            "expected": ["Chemistry Basics", "100 XP"]
        }
    ]
    
    print("="*80)
    print("QUIZ SYSTEM TEST REPORT")
    print("="*80 + "\n")
    
    all_passed = True
    for test in tests:
        try:
            with urllib.request.urlopen(test["url"]) as response:
                content = response.read().decode('utf-8')
                
                passed = all(expected in content for expected in test["expected"])
                status = "[PASS]" if passed else "[FAIL]"
                
                print(f"{status} {test['name']}")
                if not passed:
                    missing = [exp for exp in test["expected"] if exp not in content]
                    print(f"      Missing: {missing}")
                    all_passed = False
                    
        except Exception as e:
            print(f"[ERROR] {test['name']}: {e}")
            all_passed = False
    
    print("\n" + "="*80)
    if all_passed:
        print("SUCCESS: All quiz system tests passed!")
    else:
        print("FAILURE: Some tests failed.")
    print("="*80)
    
    return all_passed

if __name__ == "__main__":
    success = test_quiz_system()
    sys.exit(0 if success else 1)
