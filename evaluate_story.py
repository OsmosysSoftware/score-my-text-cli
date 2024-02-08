"""
Evaluate English proficiency in short stories using OpenAI's GPT-3
"""

import argparse
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
  api_key=openai_api_key,
)

def evaluate_story(story, words, word_count, scale):
  prompt = (
    f"Systematically evaluate the following story for English language "
    f"proficiency at each level from 1 to 5, using these strict criteria:\n"
    f"- Level 1: Basic comprehension; simple sentences; basic vocabulary. Focus"
    f" on simple grammar and clarity.\n- Level 2: Improved sentence structure; "
    f"some variety in vocabulary. Consider basic storytelling elements.\n- "
    f"Level 3: Clear structure; good grammar; varied vocabulary. Evaluate "
    f"coherence and the use of descriptive language.\n- Level 4: Strong "
    f"structure and grammar; diverse vocabulary. Assess narrative flow and "
    f"complex language usage.\n- Level 5: Advanced grammar; sophisticated "
    f"vocabulary; complex sentences. Expect nuanced expression and advanced "
    f"storytelling.\nProvide a score on a scale of {scale} for each level, "
    f"reflecting the specific criteria. Maintain strict consistency in scoring."
    f"\n\nStory (approximately {word_count} words, containing words: {words}):"
    f"\n{story}\n\nAfter scoring, verify each score to ensure it aligns with "
    f"the criteria for its respective level and fix if any discrepancy. Confirm"
    f" that the scoring is consistent and accurate for each level."
  )

  response = client.chat.completions.create(
    messages=[
      {"role": "user", "content": prompt},
      {
        "role": "user",
        "content": "Give the scores formatted as a JSON object.",
      },
    ],
    model="gpt-3.5-turbo",
    temperature=0,
  )
  return response.choices[0].message.content.strip()


def main():
  parser = argparse.ArgumentParser(
    description="Evaluate a story for English proficiency using ChatGPT.",
  )
  parser.add_argument("input_file", help="Path to the JSON input file")
  args = parser.parse_args()

  with open(args.input_file, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

  story = data.get("story")
  words = data.get("words")
  word_count = data.get("word_count")
  scale = data.get("scale")

  evaluation = evaluate_story(
    story,
    words,
    word_count,
    scale,
  )
  print(evaluation)

if __name__ == "__main__":
  main()
