#!/usr/bin/env python3
"""
Validate character files against the D&D 2024 Character JSON spec.

  python validate.py                 # validate every characters/*.json
  python validate.py path/to.json    # validate specific file(s)

Exit code is non-zero if any file fails, so it works in CI / Docker builds.
Requires: jsonschema  (pip install jsonschema)
"""
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("ERROR: jsonschema is not installed.  pip install jsonschema")
    sys.exit(2)


def main(workspace_dir=None):
    """
    Validates character JSON files against the D&D 2024 character schema.

    Args:
        workspace_dir (str or Path, optional): The root directory of the project 
            containing the 'characters/' folder. Defaults to the current 
            working directory if not provided.
    """
    if not workspace_dir:
        workspace_dir = Path.cwd()
    else:
        workspace_dir = Path(workspace_dir)

    # Where the library's internal files (like the schema) live
    library_dir = Path(__file__).parent.resolve()
    
    schema_path = library_dir / "spec" / "character.schema.json"
    if not schema_path.exists():
        print("ERROR: spec not found at {}".format(schema_path))
        sys.exit(2)
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    args = sys.argv[1:]
    if args:
        files = [Path(a) for a in args]
    else:
        # Fall back to looking in the user's workspace characters folder
        files = sorted((workspace_dir / "characters").glob("*.json"))

    if not files:
        print("No character files to validate.")
        return

    all_ok = True
    for f in files:
        try:
            doc = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            all_ok = False
            print("FAIL  {}  (not valid JSON: {})".format(f.name, e))
            continue
        errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))
        if errors:
            all_ok = False
            print("FAIL  {}".format(f.name))
            for e in errors:
                loc = "/".join(str(p) for p in e.path) or "(root)"
                print("        {}: {}".format(loc, e.message))
        else:
            ver = doc.get("spec_version", "?")
            print("OK    {}  (spec {})".format(f.name, ver))

    print("\n{}".format("All files valid." if all_ok else "Validation FAILED."))
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
