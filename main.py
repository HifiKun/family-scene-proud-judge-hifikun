#!/usr/bin/env python3
"""Family scene entry for make.fun's "Make the AI Judge Feel Proud".

The program picks the strongest of a shortlist of one-to-two-line family
scenes and writes it to /output/entry.txt. The scene has to be a small
domestic moment that is warm, funny and heartfelt: real family on the
page, genuine affection, one light funny turn, and one telling detail.

The pick is deterministic: every candidate is scored 0-2 on the five
things the judge brief weighs, most important first (real warm family
scene; heartfelt; funny; good use of one or two lines; specific and
fresh), and the highest total wins, ties broken by the shorter text.
"""

import os

# Shortlist. Each line is one or two sentences, kept well under 280 chars.
CANDIDATES = [
    "Dad fell asleep on the couch at 9 p.m. again, so the kids tucked "
    "the TV remote under his arm like a teddy bear \u2014 and Mom took a "
    "photo instead of waking him. \u2018Evidence,\u2019 she said, "
    "\u2018for Christmas.\u2019",
    "Mom said \u2018one more episode\u2019 at nine; by 9:04 Dad was "
    "snoring on the remote, the kids had built a blanket fort over him, "
    "and nobody had the heart to change the channel.",
    "Grandma\u2019s soup was too salty again, so Dad drank two bowls with "
    "a straight face and whispered to me, \u2018That\u2019s forty years of "
    "love. You don\u2019t send it back.\u2019",
    "My little brother hid Dad\u2019s glasses so he\u2019d have to stay for "
    "one more bedtime story \u2014 Dad found them in the cereal box, put "
    "them on, and said, \u2018Well. One more, then.\u2019",
    "At dinner my sister announced she was \u2018basically a chef now\u2019; "
    "Dad ate her burnt noodles like a five-star meal and asked for the "
    "recipe \u2014 she wrote it on a napkin in crayon.",
    "Every Sunday Dad burns the toast on purpose now, because the year "
    "Mom was sick the smell of it was the only thing that got her out "
    "of bed \u2014 and she still pretends not to know.",
]

# Scores per candidate, in the judge brief's criterion order:
# (warm real family scene, heartfelt, funny, uses its lines well,
#  specific and fresh). Assigned by hand while drafting, 0-2 each.
SCORES = {
    0: (2, 2, 2, 2, 2),  # remote as teddy bear; photo as evidence
    1: (2, 2, 2, 2, 2),  # blanket fort over a snoring dad
    2: (2, 2, 1, 2, 2),  # tender, but the joke lands softer
    3: (2, 2, 2, 2, 1),  # sweet turn; glasses in the cereal box is familiar
    4: (2, 1, 2, 2, 2),  # funny and specific; affection is mostly implied
    5: (2, 2, 1, 1, 2),  # heartfelt, but heavier than the brief's light tone
}

OUTPUT_PATH = "/output/entry.txt"


def pick(candidates):
    """Return the highest-scoring candidate; ties go to the shorter text."""
    best = None
    best_key = None
    for i, text in enumerate(candidates):
        key = (sum(SCORES[i]), -len(text))
        if best_key is None or key > best_key:
            best_key = key
            best = text
    return best


def main() -> None:
    line = pick(CANDIDATES).strip()
    assert "\n" not in line or line.count("\n") <= 1, "at most two lines"
    assert 1 <= len(line) <= 280, "entry must be 1 to 280 characters"
    output_path = os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
