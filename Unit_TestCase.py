import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from ACEest_Fitness import FitnessTrackerApp

class TestFitnessTrackerApp(unittest.TestCase):
    def setUp(self):
        # Mock Tkinter root
        self.root = MagicMock()
        # Mock Entry widgets to avoid real GUI
        with patch("tkinter.Entry", autospec=True) as MockEntry:
            self.mock_workout_entry = MagicMock()
            self.mock_duration_entry = MagicMock()
            MockEntry.side_effect = [self.mock_workout_entry, self.mock_duration_entry]
            self.app = FitnessTrackerApp(self.root)

    @patch("tkinter.messagebox.showinfo")
    def test_add_valid_workout(self, mock_showinfo):
        self.mock_workout_entry.get.return_value = "Running"
        self.mock_duration_entry.get.return_value = "30"

        self.app.add_workout()

        self.assertEqual(len(self.app.workouts), 1)
        self.assertEqual(self.app.workouts[0]["workout"], "Running")
        self.assertEqual(self.app.workouts[0]["duration"], 30)
        mock_showinfo.assert_called_once()

    @patch("tkinter.messagebox.showerror")
    def test_add_workout_with_invalid_duration(self, mock_showerror):
        self.mock_workout_entry.get.return_value = "Cycling"
        self.mock_duration_entry.get.return_value = "abc"

        self.app.add_workout()

        self.assertEqual(len(self.app.workouts), 0)
        mock_showerror.assert_called_once()

    @patch("tkinter.messagebox.showinfo")
    def test_view_workouts_no_entries(self, mock_showinfo):
        self.app.view_workouts()
        mock_showinfo.assert_called_once_with("Workouts", "No workouts logged yet.")

if __name__ == "__main__":
    unittest.main()
