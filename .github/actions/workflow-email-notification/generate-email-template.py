import os
import json
import argparse
from jinja2 import Environment, FileSystemLoader

def parse_env_json(key):
    try:
        return json.loads(os.getenv(key, "[]"))
    except Exception:
        return []

def main():
    parser = argparse.ArgumentParser(description="Generates HTML file from Jinja2 template using environment variables.")
    parser.add_argument("--template", required=True, help="Path to Jinja2 template (.j2)")
    parser.add_argument("--output", default="output-email.html", help="Output HTML file path")
    args = parser.parse_args()

    # Build context from environment variables only
    context = {
        # GitHub workflow metadata from env
        "REPOSITORY": os.getenv("REPOSITORY", "unknown/repo"),
        "WORKFLOW_NAME": os.getenv("WORKFLOW_NAME", "Unnamed Workflow"),
        "BRANCH_TAG": os.getenv("BRANCH_TAG", "unknown"),
        "COMMIT_SHA": os.getenv("COMMIT_SHA", "abc123"),
        "TRIGGERED_BY": os.getenv("TRIGGERED_BY", "github-user"),
        "RUN_NUMBER": os.getenv("RUN_ID", "#0"),
        "RUN_URL": os.getenv("RUN_URL", "#unknown"),

        # Workflow status
        "WORKFLOW_SUCCESS": os.getenv("WORKFLOW_SUCCESS", "false").lower() == "true",

        # Changelog entries from env
        "WHATS_NEW": parse_env_json("WHATS_NEW"),
        "BUG_FIXES": parse_env_json("BUG_FIXES"),

        # Artifacts from env
        "ARTIFACTS": parse_env_json("ARTIFACTS")
    }

    # Load and render template
    env = Environment(loader=FileSystemLoader(os.path.dirname(args.template) or "."))
    template = env.get_template(os.path.basename(args.template))
    output = template.render(**context)

    # Write output HTML
    with open(args.output, "w") as f:
        f.write(output)

if __name__ == "__main__":
    main()
