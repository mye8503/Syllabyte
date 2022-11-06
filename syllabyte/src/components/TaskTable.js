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
    state: 1
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
  },
  {
    course: "ECE344",
    assignment: "Quiz 1",
    dueIn: "2 days",
    state: 2
  },
  {
    course: "ECE345",
    assignment: "Assignment 1",
    dueIn: "1 days",
    state: 2
  },
  {
    course: "APS360",
    assignment: "Lab 2",
    dueIn: "0 days",
    state: 3
  }
]);
  if (state != 3){
    return (
      <div>
        <Grid container rowSpacing={2}>
        {assignmentInfo && 
          assignmentInfo.filter((task) => task.state === state).map(info => (          
              
               <Grid item rowSpacing={3} xs={12}>
                <Item>
                {
                info? `${info.assignment} ${info.course} ${info.dueIn}` : ''} 
                </Item>
                
              </Grid>
           
        ))}
    
        </Grid>
          
  
      </div>
  
    )
  
  }
  else{
    return(
      <div>
      <Grid container rowSpacing={2}>
      {assignmentInfo && 
        assignmentInfo.filter((task) => task.state === 1).map(info => (          
            
             <Grid item rowSpacing={3} xs={12}>
              <Item>
              {
              info? `${info.assignment} ${info.course}` : ''} 
              </Item>
              
            </Grid>
         
      ))}
  
      </Grid>
        

    </div>

  )
    
  }
 
}

