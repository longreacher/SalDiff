name: Generate Animated Graph

on:
  workflow_dispatch: # Allows you to run this manually from the Actions tab

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y ffmpeg
          pip install pandas matplotlib

      - name: Run script to generate video
        run: python animate.py

      - name: Upload video artifact
        uses: actions/upload-artifact@v4
        with:
          name: animated-graph
          path: salary_difference.mp4
