#!/usr/bin/env python3
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="GitHub Activity CLI")
    parser.add_argument(
        "--config",
        type=str,
        default=os.path.join(os.path.expanduser("~"), ".github_activity"),
        help="Path to the configuration file",
    )
    parser.add_argument(
        "--token",
        type=str,
        help="GitHub personal access token",
    )
    parser.add_argument(
        "--username",
        type=str,
        help="GitHub username",
    )
    args = parser.parse_args()