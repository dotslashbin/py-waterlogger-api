#!/usr/bin/python
from wtracker.app import app

def main():
  print("Running the webserver now...")
  app.run(debug=True, host='0.0.0.0')

if __name__ == "__main__":
  main()