# Usage Guide

## Prerequisites

Ensure that you have properly setup and configured Score My Text CLI following the [Development Setup](./development_setup.md) document.

## Using Score My Text CLI

To evaluate English proficiency in short stories, use the following command:

```bash
python evaluate_story.py examples/input.json
```

Replace `evaluate_story.py` with the actual name of your Python file (if different) and `input.json` with the JSON input file you want to use.

## Rating Structure

The output will contain proficiency level ratings (the higher, the better), based on the following constraints:

- **Level 1:** Basic comprehension; simple sentences; basic vocabulary. Focus on simple grammar and clarity.
- **Level 2:** Improved sentence structure; some variety in vocabulary. Consider basic storytelling elements.
- **Level 3:** Clear structure; good grammar; varied vocabulary. Evaluate coherence and the use of descriptive language.
- **Level 4:** Strong structure and grammar; diverse vocabulary. Assess narrative flow and complex language usage.
- **Level 5:** Advanced grammar; sophisticated vocabulary; complex sentences. Expect nuanced expression and advanced storytelling.

## Examples

```bash
$ python evaluate_story.py examples/input.json
{
  "Level 1": 7,
  "Level 2": 6,
  "Level 3": 5,
  "Level 4": 3,
  "Level 5": 1
}
```

```bash
$ python evaluate_story.py examples/input_good.json
{
  "Level 1": 8,
  "Level 2": 7,
  "Level 3": 6,
  "Level 4": 5,
  "Level 5": 4
}
```
