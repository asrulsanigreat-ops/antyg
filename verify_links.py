import urllib.request
import urllib.error
import sys

def verify_links():
    base_url = "http://127.0.0.1:8000"
    links_to_check = [
        "/",
        "/books",
        "/journals",
        "/tests",
        "/planets",
        "/books/1",
        "/books/2",
        "/journals/1",
        "/journals/4",
        "/journals/8",
    ]
    
    print("="*80)
    print("LINK VERIFICATION REPORT")
    print("="*80 + "\n")
    
    all_passed = True
    for link in links_to_check:
        url = f"{base_url}{link}"
        try:
            with urllib.request.urlopen(url) as response:
                status = response.getcode()
                if status == 200:
                    print(f"[PASS] {link} (200 OK)")
                else:
                    print(f"[FAIL] {link} (Status: {status})")
                    all_passed = False
        except urllib.error.HTTPError as e:
            print(f"[FAIL] {link} (HTTP Error: {e.code})")
            all_passed = False
        except Exception as e:
            print(f"[ERROR] {link}: {e}")
            all_passed = False
            
    print("\n" + "="*80)
    if all_passed:
        print("SUCCESS: All verified links are working correctly!")
    else:
        print("FAILURE: Some links are broken.")
    print("="*80)
    
    return all_passed

if __name__ == "__main__":
    success = verify_links()
    sys.exit(0 if success else 1)
