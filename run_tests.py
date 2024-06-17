import subprocess
import multiprocessing
import time
import unittest


def run_flask_app():
    subprocess.run(["python", "app.py"])


if __name__ == '__main__':
    # Run unit tests
    print("Running unit tests...")
    result = unittest.TextTestRunner().run(unittest.defaultTestLoader.discover('.', pattern='test_app.py'))
    if not result.wasSuccessful():
        print("Unit tests failed")
        exit(1)

    # Start Flask server in a separate process
    print("Starting Flask server...")
    flask_process = multiprocessing.Process(target=run_flask_app)
    flask_process.start()

    # Wait a bit to ensure the server is running
    time.sleep(3)

    # Run end-to-end tests
    print("Running end-to-end tests...")
    e2e_result = subprocess.run(['python', '-m', 'unittest', 'test_e2e.py'], capture_output=True)
    print(e2e_result.stdout.decode())
    if e2e_result.returncode != 0:
        print("End-to-end tests failed")
        flask_process.terminate()
        exit(1)

    print("All tests passed. Terminating Flask server...")
    flask_process.terminate()
    flask_process.join()
