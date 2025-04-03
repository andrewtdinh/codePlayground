const { google } = require("googleapis");
const fs = require("fs");

// Load credentials from JSON key file
const credentials = JSON.parse(fs.readFileSync("credentials.json")); // Replace with your JSON key file

// Authenticate
const auth = new google.auth.GoogleAuth({
  credentials,
  scopes: ["https://www.googleapis.com/auth/documents.readonly"],
});

// Google Docs API client
const docs = google.docs({ version: "v1", auth });

async function extractTableData(documentId) {
  try {
    const res = await docs.documents.get({ documentId });
    const content = res.data.body.content;

    let tableData = [];

    // Loop through document elements
    content.forEach((element) => {
      if (element.table) {
        element.table.tableRows.forEach((row, rowIndex) => {
          row.tableCells.forEach((cell, colIndex) => {
            const text = cell.content
              .map((c) =>
                c.paragraph.elements
                  .map((e) => e.textRun?.content || "")
                  .join("")
              )
              .join("");
            tableData.push({ x: colIndex, y: rowIndex, char: text.trim() });
          });
        });
      }
    });

    console.log("Extracted Table Data:", tableData);
  } catch (error) {
    console.error("Error fetching table data:", error);
  }
}

// Replace with your Google Doc ID
const DOCUMENT_ID = "1yiZrWz0-1bqhvk4Rsrcj1TU5SjPn3_KKoYRNA40gJa4";
extractTableData(DOCUMENT_ID);
