"""Tests for the Chaos Gremlin. Run with: python3 -m unittest discover -s tests -v"""

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "gremlin.py"


def run(*args: str) -> dict:
    out = subprocess.run(
        [sys.executable, str(SCRIPT), "--format", "json", *args],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)


class TestGremlin(unittest.TestCase):
    def test_decide_picks_one_of_the_options(self):
        result = run("--seed", "7", "decide", "tea", "coffee")
        self.assertIn(result["winner"], {"tea", "coffee"})

    def test_seeded_chaos_is_reproducible(self):
        args = [sys.executable, str(SCRIPT), "--seed", "42",
                "--format", "json", "fortune", "--mood", "chaotic"]
        first = subprocess.run(args, capture_output=True, text=True, check=True).stdout
        second = subprocess.run(args, capture_output=True, text=True, check=True).stdout
        self.assertEqual(first, second)

    def test_every_mode_returns_the_contract_fields(self):
        calls = [
            ("decide", "up", "down"),
            ("excuse", "--context", "work"),
            ("quest", "--minutes", "5"),
            ("compliment", "--name", "Sam", "--style", "pirate"),
            ("fortune", "--mood", "blessed"),
        ]
        for call in calls:
            with self.subTest(call=call):
                result = run(*call)
                for field in ("mode", "title", "winner", "body", "extra"):
                    self.assertTrue(result[field], f"{call} missing {field}")

    def test_decide_rejects_a_single_option(self):
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), "decide", "only-one"],
            capture_output=True, text=True,
        )
        self.assertNotEqual(proc.returncode, 0)


if __name__ == "__main__":
    unittest.main()
