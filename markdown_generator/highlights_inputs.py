import sys
from pathlib import Path
from typing import Any, Dict, List

import yaml


REQUIRED_TOP_LEVEL_KEYS = {"items"}
REQUIRED_ITEM_KEYS = {"id", "type"}
ALLOWED_TYPES = {"paper", "repo"}


class ValidationError(Exception):
    pass


def load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise ValidationError(f"Input file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data


def validate_schema(data: Dict[str, Any]) -> None:
    missing = REQUIRED_TOP_LEVEL_KEYS - set(data.keys())
    if missing:
        raise ValidationError(f"Missing top-level keys: {sorted(missing)}")

    items: List[Dict[str, Any]] = data.get("items", [])
    if not isinstance(items, list) or not items:
        raise ValidationError("'items' must be a non-empty list")

    seen_ids = set()
    for idx, item in enumerate(items):
        if not isinstance(item, dict):
            raise ValidationError(f"Item {idx} is not a mapping")

        missing_item = REQUIRED_ITEM_KEYS - set(item.keys())
        if missing_item:
            raise ValidationError(
                f"Item {idx} missing keys: {sorted(missing_item)} (has: {sorted(item.keys())})"
            )

        item_id = str(item["id"]).strip()
        if not item_id:
            raise ValidationError(f"Item {idx} has empty id")
        if item_id in seen_ids:
            raise ValidationError(f"Duplicate id: {item_id}")
        seen_ids.add(item_id)

        item_type = item["type"]
        if item_type not in ALLOWED_TYPES:
            raise ValidationError(
                f"Item {item_id} has invalid type '{item_type}'; expected one of {sorted(ALLOWED_TYPES)}"
            )

        if item_type == "paper":
            # At least one of arxiv/doi/pdf
            if not any(k in item for k in ("arxiv", "doi", "pdf")):
                raise ValidationError(
                    f"Paper {item_id} must specify at least one of 'arxiv', 'doi', or 'pdf'"
                )
        elif item_type == "repo":
            if "github" not in item:
                raise ValidationError(f"Repo {item_id} must specify 'github' URL")


def main(argv: List[str]) -> int:
    input_path = Path(argv[1]) if len(argv) > 1 else Path("markdown_generator/highlights.yml")
    try:
        data = load_yaml(input_path)
        validate_schema(data)
    except ValidationError as e:
        print(f"Validation failed: {e}")
        return 2
    except Exception as e:
        print(f"Error: {e}")
        return 1

    print(f"OK: {len(data['items'])} items validated from {input_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))


