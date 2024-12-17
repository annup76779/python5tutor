function createPyramid(rows) {
    for (let i = 0; i < rows; i++) {
      let output = '';
  
      // Add the spaces
      for (let j = 0; j < rows - i - 1; j++) {
        output += ' ';
      }
      // Add the asterisks
      for (let k = 0; k <= i * 2; k++) {
        output += '*';
      }
      // New line after each row
      console.log(output);
    }
  }
  
createPyramid(10); // Call the function with the desired number of rows
  