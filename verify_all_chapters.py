import urllib.request
import sys

def verify_all_cosmic_chapters():
    """Verify that all 12 chapters of Cosmic Origins are present in the HTML"""
    url = "http://127.0.0.1:8000/books/1"
    
    expected_chapters = [
        "The Big Bang",
        "Inflation and the Expansion of Space",
        "Formation of Fundamental Particles",
        "Birth of Light (Recombination)",
        "The Cosmic Dark Ages",
        "Formation of the First Stars",
        "Birth of the First Galaxies",
        "Supernovae and the Creation of Heavy Elements",
        "Formation of the Milky Way",
        "Birth of the Solar System",
        "Formation of Earth",
        "Earth's Early Environment and Readiness for Life"
    ]
    
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            
            print(f"Fetching: {url}")
            print(f"Response status: {response.status}")
            print("\n" + "="*80)
            print("CHAPTER VERIFICATION REPORT")
            print("="*80 + "\n")
            
            all_found = True
            for i, chapter in enumerate(expected_chapters, 1):
                if chapter in content:
                    print(f"[OK] Chapter {i:2d}: {chapter}")
                else:
                    print(f"[FAIL] Chapter {i:2d}: {chapter} [NOT FOUND]")
                    all_found = False
            
            print("\n" + "="*80)
            if all_found:
                print("SUCCESS: All 12 chapters found in the HTML output!")
                print("="*80)
                return True
            else:
                print("FAILURE: Some chapters are missing from the HTML output.")
                print("="*80)
                return False
                
    except Exception as e:
        print(f"ERROR: Failed to fetch book page. {e}")
        return False

if __name__ == "__main__":
    success = verify_all_cosmic_chapters()
    sys.exit(0 if success else 1)
