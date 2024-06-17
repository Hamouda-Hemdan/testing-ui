import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestCourseSchedulerE2E(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://127.0.0.1:5000/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.refresh()
        time.sleep(1)

    def test_valid_input(self):
        driver = self.driver
        driver.find_element(By.ID, "numCourses").send_keys("2")
        driver.find_element(By.ID, "prerequisites").send_keys("[[1, 0]]")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(1)
        result_text = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("True", result_text)

    def test_cycle_input(self):
        driver = self.driver
        driver.find_element(By.ID, "numCourses").send_keys("2")
        driver.find_element(By.ID, "prerequisites").send_keys("[[1, 0], [0, 1]]")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(1)
        result_text = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("False", result_text)

    def test_no_prerequisites(self):
        driver = self.driver
        driver.find_element(By.ID, "numCourses").send_keys("3")
        driver.find_element(By.ID, "prerequisites").send_keys("[]")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(1)
        result_text = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("True", result_text)

    def test_single_course_with_self_dependency(self):
        driver = self.driver
        driver.find_element(By.ID, "numCourses").send_keys("1")
        driver.find_element(By.ID, "prerequisites").send_keys("[[0, 0]]")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(1)
        result_text = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("False", result_text)

    def test_disconnected_graph(self):
        driver = self.driver
        driver.find_element(By.ID, "numCourses").send_keys("5")
        driver.find_element(By.ID, "prerequisites").send_keys("[[1, 0], [3, 2]]")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(1)
        result_text = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("True", result_text)

    def test_multiple_courses_with_no_circular_dependency(self):
        driver = self.driver
        driver.find_element(By.ID, "numCourses").send_keys("4")
        driver.find_element(By.ID, "prerequisites").send_keys("[[1, 0], [2, 1], [3, 2]]")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(1)
        result_text = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("True", result_text)

    def test_all_courses_interdependent(self):
        driver = self.driver
        driver.find_element(By.ID, "numCourses").send_keys("3")
        driver.find_element(By.ID, "prerequisites").send_keys("[[0, 1], [1, 2], [2, 0], [0, 2]]")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(1)
        result_text = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("False", result_text)

    def test_single_chain(self):
        driver = self.driver
        driver.find_element(By.ID, "numCourses").send_keys("5")
        driver.find_element(By.ID, "prerequisites").send_keys("[[1, 0], [2, 1], [3, 2], [4, 3]]")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(1)
        result_text = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("True", result_text)

    def test_empty_course_list(self):
        driver = self.driver
        driver.find_element(By.ID, "numCourses").send_keys("0")
        driver.find_element(By.ID, "prerequisites").send_keys("[]")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(1)
        result_text = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("True", result_text)

    def test_large_input(self):
        driver = self.driver
        driver.find_element(By.ID, "numCourses").send_keys("500")
        driver.find_element(By.ID, "prerequisites").send_keys(str([[i, i + 1] for i in range(499)]))
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(2)
        result_text = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("True", result_text)
if __name__ == '__main__':
    unittest.main()
