# Sorting algorithms comparator

The purpose of this pproject is to compare the performance of different sorting algorithms.
The execution time and the carbon footprint are among the considered benchmarks.

## Prerequisites

- Install Python 3.11 or latest
- Navigate to the source folder (sortComp)
- Create a virtual environment: `python -m venv venv` or `python3 -m venv venv`
- Activate the environment:
  - On Windows: `venv\Scripts\activate`
  - On Linux: `source venv/bin/activate`
- Run `pip install -r requirements.txt`

## Usage

Once you went through the prerequisites section, you need to generate a file called __input.txt__ containing the array that will
be sorted. For this, you can run _input_generator.py_ using `python input_generator.py`.

Then, with the virtual environment active, you can run the following command:
`python --algo=<algo_name> main.py`, where _<algo_name>_ is one of the following:
- bubble
- qsort3
- pythonStd

## Output

After the run finishes, you should be able to see a new file called _emissions.csv_. With each run, a new entry with the run id is added to this csv file
so that you can compare the performance of the runs.
