# IPP project 2 tests
## Usage:
Run all tests:
```
pytest
```
If it takes too long, try specifying the path:
```
pytest tests/
```
Run only specific test(s):
```
pytest tests/test_valid.py
pytest tests/test_valid.py::test_basic_output
```

## Before download:
**Remove remote** connection to ipp-core repo first or clone as **submodule**.
```
git remote remove origin
# (^^ in ipp-core dir)
```
## Download:
Download **into ipp-core**, **NOT** student/
```
git clone git@github.com:Kubikuli/IPP_proj2-tests.git tests
```
## Setup:
Create virtual environment (if you dont have one yet) and download dependencies
```
# in ipp-core dir
python -m venv .venv
source .venv/bin/activate
pip install -r tests/requirements.txt
```
## Update:
```
# in tests directory
git pull
```
## Notes:
Tag or DM me if you see any issues. (@Kubikuli)  
If you'd like to contribute to tests, create a pull request. Or send me SOL25 source code if you don't have working parser.  
You can find basic skeleton at the start of each test file that you can easily copy to create new tests.  
(100% of these tests was +- 90%+ of official tests)

#### Contributors
Special thanks to all the contributors who provided some extra tests and helped me correct all the mistakes:
- @alklk
- @ONdraid
- @fifixsandy
- @LeO (for sharing some of the official tests(I hope he doesn't mind I added them to this collection xd))
