import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from ACEest_Fitness import FitnessTrackerApp

class TestFitnessTrackerApp(unittest.TestCase):

    def setUp(self):
        # Create a root window but don't actually show it
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = FitnessTrackerApp(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch("tkinter.messagebox.showinfo")
    def test_add_valid_workout(self, mock_showinfo):
        self.app.workout_entry.insert(0, "Running")
        self.app.duration_entry.insert(0, "30")

        self.app.add_workout()

        self.assertEqual(len(self.app.workouts), 1)
        self.assertEqual(self.app.workouts[0]["workout"], "Running")
        self.assertEqual(self.app.workouts[0]["duration"], 30)
        mock_showinfo.assert_called_once_with("Success", "'Running' added successfully!")

    @patch("tkinter.messagebox.showerror")
    def test_add_workout_with_invalid_duration(self, mock_showerror):
        self.app.workout_entry.insert(0, "Cycling")
        self.app.duration_entry.insert(0, "abc")

        self.app.add_workout()

        self.assertEqual(len(self.app.workouts), 0)
        mock_showerror.assert_called_once_with("Error", "Duration must be a number.")

    @patch("tkinter.messagebox.showinfo")
    def test_view_workouts_no_entries(self, mock_showinfo):
        self.app.view_workouts()
        mock_showinfo.assert_called_once_with("Workouts", "No workouts logged yet.")

if __name__ == "__main__":
    unittest.main()

