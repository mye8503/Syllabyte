import React, { useState } from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));

export function TaskTable({state}) {
  const [assignmentInfo, setAssignmentInfo] = useState([{
    course: "Aps360",
    assignment: "Lab 4",
    dueIn: "7 days",
    state: '1'
  },
  {
    course: "Aps360",
    assignment: "Progress report 1",
    dueIn: "5 days",
    state: 1
  },
  {
    course: "Aps360",
    assignment: "Lab 3",
    dueIn: "1 days",
    state: 2
  },
  {
    course: "ECE344",
    assignment: "Lab 4",
    dueIn: "8 days",
    state: 1
  },
  {
    course: "ECE344",
    assignment: "Quiz 2",
    dueIn: "5 days",
    state: 1
  }]);

  return (
    
      assignmentInfo.filter(task => task.state === 1).map(info => (
        <React.Fragment>
          <Grid item xs={12}>
            <Item>info.assingment + " " + info.course + " " + info.dueIn</Item>
          </Grid>
        </React.Fragment>
      )
        
        
      )
    

  )}

