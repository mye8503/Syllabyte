import logo from './logo.svg';
import './App.css';
import CourseAndUpload from './components/CourseAndUpload';
import { TaskTable } from './components/TaskTable';

const course_info = {
  'APS360': {
      'priority': 1,
      'Assignments': {
          'Lab': {
              'number': 4,
              'percentage': 3,
              'due': '2022-07-11',
              'time_needed': 6,
              'time_spent': 4,
              'state': 1,
              'rank': 0
          },
          'progress_report': {
              'number': 1,
              'percentage': 10,
              'due': '2022-12-11',
              'time_needed': 2,
              'time_spent': 0,
              'state': 1,
              'rank': 0
          }
      },
      'Exams': {}
  },
  'ECE344': {
      'priority': 3,
      'Assignments': {
          'Lab': {
              'number': 4,
              'percentage': 6,
              'due': '2022-08-11',
              'time_needed': 10,
              'time_spent': 2,
              'state': 1,
              'rank': 0
          }
      },
      'Exams': {
          'Quiz': {
              'number': 1,
              'percentage': 12,
              'due': '2022-13-11',
              'time_needed': 14,
              'time_spent': 1,
              'state': 1,
              'rank': 0
          }
      }
  },
  'ECE345': {
      'priority': 3,
      'Assignments': {
          'Homework': {
              'number': 2,
              'percentage': 5,
              'due': '2022-06-11',
              'time_needed': 2,
              'time_spent': 0,
              'state': 1,
              'rank': 0
          }
      },
      'Exams': {
          'Midterm': {
              'number': 1,
              'percentage': 35,
              'due': '2022-20-11',
              'time_needed': 14,
              'time_spent': 2,
              'state': 1,
              'rank': 0
          }
      }
  }
}
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1> syllabyte... </h1>
        <TaskTable state={1}/>
      </header>
    </div>
  );
}

export default App;
