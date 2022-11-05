import fs from 'fs'; 
import PDFParser from './node_modules/pdf2json/pdfparser.js';

const pdfParser = new PDFParser();

pdfParser.on("pdfParser_dataError", errData => console.error(errData.parserError) );
pdfParser.on("pdfParser_dataReady", pdfData => {
    fs.writeFile("./Syllabus.json", JSON.stringify(pdfData), function(err, result) {
        if(err) console.log('error', err);
      });
});

pdfParser.loadPDF("./Syllabus APS360 Fall 2022.pdf");