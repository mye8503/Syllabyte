import React,{Component} from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";

export default function CourseAndUpload() {
  const [selectedFile, setSelectedFile] = useState();
 
  const changeHandler = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmission = () => {
    const formData = new FormData();
    
    // Update the formData object
    formData.append(
      "myFile",
      this.state.selectedFile,
      this.state.selectedFile.name
    );
    //post to backend
  };
  return (
    <div>
      <Box
        component="form"
        sx={{
          "& > :not(style)": { m: 1, width: "25ch" },
        }}
        noValidate
        autoComplete="off"
      >
        <TextField id="outlined-basic" label="Course Name" variant="outlined" />
        {/* <TextField id="filled-basic" label="Filled" variant="filled" />
      <TextField id="standard-basic" label="Standard" variant="standard" /> */}
      </Box>
      <div>
        <input type="file" name="file" onChange={changeHandler} />
       
        <div>
          <button onClick={handleSubmission}>Submit</button>
        </div>
      </div>
    </div>
  );
}
