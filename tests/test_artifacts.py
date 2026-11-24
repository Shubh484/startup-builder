
from pathlib import Path

ARTIFACTS = Path("artifacts")

REQUIRED_FILES = {
    "idea-brief.md": [
        "problem",
        "target",
    ],
    "market-report.md": [
        "competitor",
        "source",
    ],
    "product-requirements.md": [
        "user",
        "acceptance",
    ],
    "mvp-roadmap.md": [
        "task",
        "dependency",
        "testing",
    ],
}


def main():
    passed = 0
    failed = 0

    print("\nSTARTUP BUILDER - ARTIFACT EVALUATION\n")

    for filename, keywords in REQUIRED_FILES.items():
        path = ARTIFACTS / filename

        if not path.exists():
            print(f"FAIL: Missing {filename}")
            failed += 1
            continue

        content = path.read_text(
            encoding="utf-8"
        ).lower()

        missing = [
            word for word in keywords
            if word not in content
        ]

        if missing:
            print(
                f"FAIL: {filename} "
                f"missing concepts: {missing}"
            )
            failed += 1
        else:
            print(f"PASS: {filename}")
            passed += 1

    print("\n------------------------------")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print("------------------------------")

    if failed:
        raise SystemExit(1)

    print("\nAll basic artifact checks passed!")


if __name__ == "__main__":
    main()
