import urllib.request
import sys

def verify_book_content(book_id, expected_content):
    url = f"http://127.0.0.1:8000/books/{book_id}"
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            if expected_content in content:
                print(f"[PASS] Book {book_id}: Found expected content '{expected_content}'")
                return True
            else:
                print(f"[FAIL] Book {book_id}: Expected content '{expected_content}' NOT found")
                return False
    except Exception as e:
        print(f"[ERROR] Book {book_id}: Failed to fetch. {e}")
        return False

def verify_url_content(url, expected_content):
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            if expected_content in content:
                print(f"[PASS] {url}: Found expected content '{expected_content}'")
                return True
            else:
                print(f"[FAIL] {url}: Expected content '{expected_content}' NOT found")
                return False
    except Exception as e:
        print(f"[ERROR] {url}: Failed to fetch. {e}")
        return False

def main():
    print("Verifying application content...")
    results = [
        verify_url_content("http://127.0.0.1:8000/books/1", "The Big Bang"),
        verify_url_content("http://127.0.0.1:8000/books/2", "Wave-Particle Duality"),
        verify_url_content("http://127.0.0.1:8000/books/3", "The basic unit of life"),
        verify_url_content("http://127.0.0.1:8000/journals", "Scientific Journals"),
        verify_url_content("http://127.0.0.1:8000/tests", "Knowledge Checks"),
        verify_url_content("http://127.0.0.1:8000/planets", "Solar System Explorer")
    ]
    
    if all(results):
        print("\nAll checks passed!")
        sys.exit(0)
    else:
        print("\nSome checks failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
