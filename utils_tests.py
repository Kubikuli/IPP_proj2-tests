import subprocess

def run_test(input_path, source, expected_output):
    process = subprocess.run(
        ["php8.4", "interpret.php", f"--input={input_path}"],
        input=source,
        capture_output=True,
        text=True,
        timeout=3,
    )

    print(process.stdout)

    if process.returncode != 0 or process.stderr:
        print("STDERR:", process.stderr)

    assert process.returncode == 0, f"Expected return code 0, but got {process.returncode}"
    
    # assert len(process.stderr) == 0

    assert process.stdout.strip() == expected_output.strip(), f"Expected stdout:\n{expected_output}\nGot:\n{process.stdout}"


def run_sem_test(input_path, source, expected_codes):
    process = subprocess.run(
        ["php8.4", "interpret.php", f"--input={input_path}"],
        input=source,        
        capture_output=True,
        text=True,
        timeout=5
    )

    print(process.stdout)

    assert process.returncode in expected_codes, (f"Expected one of {expected_codes}, but got {process.returncode}")

    assert len(process.stderr) != 0
