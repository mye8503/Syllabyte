import logo from "./logo.svg";
import "./App.css";
import CourseAndUpload from "./components/CourseAndUpload";
import { TaskTable } from "./components/TaskTable";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
import { styled } from '@mui/material/styles';
import Navbar from "./components/Navbar";

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === "dark" ? "#1A2027" : "#fff",
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: "center",
  color: theme.palette.text.secondary,
}));

const course_info = {
  APS360: {
    priority: 1,
    Assignments: {
      Lab: {
        number: 4,
        percentage: 3,
        due: "2022-07-11",
        time_needed: 6,
        time_spent: 4,
        state: 1,
        rank: 0,
      },
      progress_report: {
        number: 1,
        percentage: 10,
        due: "2022-12-11",
        time_needed: 2,
        time_spent: 0,
        state: 1,
        rank: 0,
      },
    },
    Exams: {},
  },
  ECE344: {
    priority: 3,
    Assignments: {
      Lab: {
        number: 4,
        percentage: 6,
        due: "2022-08-11",
        time_needed: 10,
        time_spent: 2,
        state: 1,
        rank: 0,
      },
    },
    Exams: {
      Quiz: {
        number: 1,
        percentage: 12,
        due: "2022-13-11",
        time_needed: 14,
        time_spent: 1,
        state: 1,
        rank: 0,
      },
    },
  },
  ECE345: {
    priority: 3,
    Assignments: {
      Homework: {
        number: 2,
        percentage: 5,
        due: "2022-06-11",
        time_needed: 2,
        time_spent: 0,
        state: 1,
        rank: 0,
      },
    },
    Exams: {
      Midterm: {
        number: 1,
        percentage: 35,
        due: "2022-20-11",
        time_needed: 14,
        time_spent: 2,
        state: 1,
        rank: 0,
      },
    },
  },
};
function App() {
  return (

    <div className="App">
      
      <header className="App-header">
        <h1> syllabyte </h1>
        <CourseAndUpload style={{textAlign:"right", flexDirection:"row", justifyContent:"flex-end" }}/>
        <Grid container spacing={2}>
          <Grid item xs={4}>
          <h2>To Do</h2>
            <Item><TaskTable state={1} /></Item>
          </Grid>
          <Grid item xs={4}>
          <h2>Doing</h2>
            <Item><TaskTable state={2} /></Item>
          </Grid>
          <Grid item xs={4}>
            <h2>Completed</h2>
            <Item><TaskTable state={3} /></Item>
          </Grid>
        </Grid>
        
      </header>
    </div>
  );
}

export default App;
