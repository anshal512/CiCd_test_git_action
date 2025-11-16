def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b

def main() -> None:
    """Main entry point for the application."""
    result = add(3, 5)
    print(f"Sum is: {result}")

if __name__ == "__main__":
    main()